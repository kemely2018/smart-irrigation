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


