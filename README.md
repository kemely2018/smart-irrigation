# Smart Irrigation System (Fog + Serverless + IaC)

## Descripción

Este proyecto implementa un sistema de **riego automático inteligente** utilizando **Fog Computing**, **Serverless Computing** y **Infrastructure as Code (IaC)**. El sistema simula un nodo Fog que toma decisiones locales sobre el riego basado en la humedad, y envía eventos a la nube donde una función AWS Lambda los procesa y los almacena en DynamoDB.

Este enfoque demuestra una arquitectura distribuida y escalable, ideal para proyectos de IoT y automatización de hogares o cultivos.

## Tecnologías utilizadas

* **AWS Lambda**: procesamiento serverless de los eventos de riego.
* **AWS DynamoDB**: base de datos NoSQL para almacenar los registros de riego.
* **Terraform**: IaC para desplegar toda la infraestructura en AWS.
* **Python 3.12**: lenguaje para el nodo Fog y Lambda.
* **boto3**: SDK de AWS para comunicación entre el nodo Fog y Lambda.
* **WSL2 + Ubuntu**: entorno de desarrollo en Windows.

## Estructura del proyecto

```
smart-irrigation/
├── iac/                   # Código Terraform (IaC)
│   ├── provider.tf
│   ├── iam.tf
│   ├── dynamodb.tf
│   └── lambda.tf
|   ├── lambda_code/        # Código de la función Lambda
│       └── handler.py
├── fog_node/              # Nodo Fog simulado
│   ├── fog_node.py
└── README.md
```

## Configuración y despliegue

### 1. Configurar AWS CLI

```bash
aws configure
```

Ingresa tus credenciales de AWS y región (por ejemplo: `us-east-1`).

### 2. Inicializar Terraform

```bash
cd smart-irrigation/iac
terraform init
```

### 3. Verificar el plan

```bash
terraform plan
```

### 4. Aplicar infraestructura

```bash
terraform apply
```

Responde `yes` cuando se solicite.

### 5. Preparar nodo Fog

```bash
cd ../fog_node
python3 -m venv venv
source venv/bin/activate
pip install boto3
```

### 6. Ejecutar nodo Fog

```bash
python fog_node.py
```

Esto simula la lectura de humedad, decide si regar o no y envía el evento a Lambda.

## Funcionalidades

* Decisión local de riego en el nodo Fog.
* Registro en tiempo real de eventos de riego y humedad en DynamoDB.
* Infraestructura reproducible mediante Terraform.
* Sistema 100% funcional sin necesidad de hardware físico (simulación).

## Capturas y validación

* AWS Lambda activo.
* DynamoDB con registros generados.
* Nodo Fog simulado enviando eventos exitosamente.

---

# 🔌 Integración con Arduino ESP32 (Hardware real)

Este proyecto no se limita a una simulación: también fue integrado con un **ESP32 con WiFi**, convirtiéndolo en un sistema **IoT real** de riego inteligente.

El ESP32 funciona como el **dispositivo Edge**, enviando mediciones de humedad al **nodo Fog**, que actúa como intermediario entre el hardware y la nube **Serverless**.

---

### Arquitectura con hardware

```
ESP32 (Sensor de humedad)
        │  WiFi
        ▼
Fog Node (Flask en WSL)
        │  HTTP
        ▼
AWS API Gateway
        │
AWS Lambda
        │
DynamoDB
```

---

### Flujo de funcionamiento

1. El **ESP32** mide (o simula) la humedad del suelo.  
2. Envía los datos vía **WiFi** al **Fog Node**.  
3. El **Fog Node** valida y reenvía los datos a la nube.  
4. **AWS Lambda** ejecuta la lógica de riego (ON / OFF).  
5. El evento se guarda en **DynamoDB**.  
6. La respuesta regresa al Fog y puede ser usada para activar actuadores físicos (bomba, relé, etc).

---

### Código del ESP32 (Edge Node)

```cpp
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "TU_WIFI";
const char* password = "TU_PASSWORD";
const char* fogURL = "http://<IP_FOG_NODE>:5000/sensor";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void loop() {
  float humidity = random(20, 90);  // Simulación de sensor

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(fogURL);
    http.addHeader("Content-Type", "application/json");

    String json = "{\"humidity\":" + String(humidity) + "}";
    http.POST(json);
    http.end();
  }

  delay(5000);
}
```

---

### Importancia académica

Esta integración demuestra una arquitectura **completa de IoT distribuido**:

| Capa | Implementación |
|------|----------------|
| Edge | ESP32 |
| Fog | Flask (WSL) |
| Cloud | AWS Lambda |
| Serverless | API Gateway + Lambda |
| Data | DynamoDB |
| IaC | Terraform |

El ESP32 **no se conecta directamente a la nube**, sino que utiliza el **Fog Node**, lo que refleja una arquitectura usada en sistemas industriales y de agricultura inteligente.



