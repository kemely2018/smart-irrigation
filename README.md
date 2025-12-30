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

# 🔌 Integración con Hardware Real (Arduino Nano + Fog Computing)

Además de la simulación por software, el proyecto **SmartPlant-IoT** fue extendido para trabajar con **hardware real**, utilizando un **Arduino Nano**, sensores físicos y actuadores, integrados mediante un **Fog Node**.

Debido a que el Arduino Nano no posee conectividad WiFi, la comunicación con la nube se realiza a través de un **nodo Fog**, que actúa como intermediario inteligente entre el hardware y los servicios **Serverless en AWS**.

## 🏗️ Arquitectura con Hardware Real

Arduino Nano  
(Sensor de humedad + Relé)  
│  USB / Serial  
▼  
Fog Node (Python + Flask + PySerial en WSL)  
│  HTTP  
▼  
AWS API Gateway  
│  
AWS Lambda  
│  
DynamoDB  

## 🔄 Flujo de Funcionamiento

1. El **Arduino Nano** mide la humedad del suelo mediante un sensor de humedad.
2. El valor leído se envía por **comunicación serial (USB)** al Fog Node.
3. El **Fog Node** interpreta los datos del sensor, aplica validaciones y control local, y reenvía la información a la nube mediante **HTTP**.
4. **AWS API Gateway** recibe la solicitud.
5. **AWS Lambda** ejecuta la lógica de riego (**ON / OFF**).
6. El evento se almacena en **DynamoDB**.
7. La respuesta puede ser utilizada por el Fog Node para activar la bomba de agua mediante el relé o mostrar el estado del sistema en una interfaz web.

## 🌱 Rol del Arduino Nano (Edge Device)

El **Arduino Nano** funciona como el dispositivo **Edge**, encargado exclusivamente de la lectura del sensor de humedad del suelo, la activación del relé (bomba de agua) y el envío de datos crudos al Fog Node vía **Serial**.  
El Arduino **no se conecta directamente a la nube**, lo que reduce la complejidad, el consumo energético y las dependencias externas.

## 🌫️ Rol del Fog Node

El **Fog Node** es el componente clave de la arquitectura. Se ejecuta en **WSL + Ubuntu**, lee datos del Arduino mediante **PySerial**, ejecuta lógica intermedia y validaciones, expone una **API local** usando **Flask** y se comunica con **AWS Lambda** mediante **HTTP**.  
Este enfoque refleja arquitecturas reales utilizadas en **agricultura inteligente**, **IoT industrial** y **sistemas distribuidos**.

## 🎓 Importancia Académica de esta Integración

Esta implementación demuestra conceptos fundamentales de **Cloud Computing** e **IoT moderno**:

Capa: Edge  
Implementación: Arduino Nano  
Herramientas: Sensor de humedad, relé  

Capa: Fog  
Implementación: Nodo intermedio  
Herramientas: Python, Flask, PySerial  

Capa: Cloud  
Implementación: Serverless  
Herramientas: AWS Lambda  

Capa: Comunicación  
Implementación: HTTP / Serial  
Herramientas: API Gateway  

Capa: Persistencia  
Implementación: NoSQL  
Herramientas: DynamoDB  

Capa: IaC  
Implementación: Infraestructura  
Herramientas: Terraform  

## ✅ Beneficios del Enfoque Fog + Serverless

- **Escalable**: Se pueden añadir múltiples Arduino Nano conectados a uno o más Fog Nodes.
- **Replicable**: Toda la infraestructura cloud se despliega automáticamente con **Terraform**.
- **Resiliente**: El Fog Node puede operar incluso si la nube no está disponible temporalmente.
- **Eficiente**: Reduce latencia y consumo de red al no enviar datos crudos directamente a la nube.
- **Académicamente sólido**: Aplica conceptos reales de arquitecturas distribuidas.

## 🏁 Conclusión

La integración del **Arduino Nano** con un **Fog Node** y servicios **Serverless en AWS**, desplegados mediante **Infrastructure as Code**, convierte a **SmartPlant-IoT** en un proyecto **completo, realista y alineado con arquitecturas modernas de Cloud Computing**, ideal para fines **académicos y demostrativos**.

