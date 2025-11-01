# 💱 Conversor de Divisas Serverless

**Aplicación web que utiliza AWS Lambda y API Gateway para convertir divisas en tiempo real**

[![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?style=flat&logo=amazon-aws)](https://aws.amazon.com/lambda/)
[![API Gateway](https://img.shields.io/badge/AWS-API_Gateway-FF9900?style=flat&logo=amazon-aws)](https://aws.amazon.com/api-gateway/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)](https://www.python.org/)

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Arquitectura](#-arquitectura)
- [Tecnologías](#-tecnologías)
- [Cloud Functions](#-cloud-functions)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [APIs Utilizadas](#-apis-utilizadas)
- [Costos](#-costos)
- [Ventajas Serverless](#-ventajas-serverless)
- [Limitaciones](#-limitaciones)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Autor](#-autor)

---

## 🎯 Descripción

Este proyecto es una aplicación web serverless que permite convertir entre diferentes monedas en tiempo real. Utiliza **AWS Lambda** para las funciones backend, **API Gateway** para exponer endpoints REST, y una interfaz web moderna construida con HTML, CSS y JavaScript vanilla.

### ¿Qué es Serverless?

**Serverless** (FaaS - Function as a Service) es un modelo de computación en la nube donde:
- ❌ **No gestionas servidores**: AWS maneja toda la infraestructura
- ⚡ **Escalado automático**: De 0 a miles de ejecuciones instantáneamente
- 💰 **Pago por uso**: Solo pagas cuando tu código se ejecuta
- 🚀 **Despliegue rápido**: Enfoque en el código, no en la infraestructura

---

## ✨ Características

✅ **Conversión en tiempo real** entre 8+ monedas  
✅ **Arquitectura 100% serverless** (sin servidores que mantener)  
✅ **Escalado automático** según la demanda  
✅ **Interfaz responsive** y moderna  
✅ **Manejo robusto de errores**  
✅ **Validación de datos** en frontend y backend  
✅ **CORS configurado** correctamente  
✅ **Logs en CloudWatch** para monitoreo  

### Monedas Soportadas

🇺🇸 USD | 🇪🇺 EUR | 🇨🇴 COP | 🇬🇧 GBP | 🇯🇵 JPY | 🇲🇽 MXN | 🇧🇷 BRL | 🇨🇦 CAD

---

## 🏗️ Arquitectura

```
┌─────────────────┐
│  Usuario Web    │
└────────┬────────┘
         │ HTTP Request
         ▼
┌─────────────────┐
│   Frontend      │ (HTML/CSS/JS)
│   index.html    │
└────────┬────────┘
         │ fetch()
         ▼
┌─────────────────┐
│  API Gateway    │ (REST API)
│   /convert      │ POST
│   /rates        │ GET
└────────┬────────┘
         │ invoke
         ▼
┌─────────────────┐
│  AWS Lambda     │
│  ┌───────────┐  │
│  │ convert-  │  │
│  │ currency  │  │
│  └───────────┘  │
│  ┌───────────┐  │
│  │ get-      │  │
│  │ exchange- │  │
│  │ rates     │  │
│  └───────────┘  │
└────────┬────────┘
         │ HTTP GET
         ▼
┌─────────────────┐
│ ExchangeRate    │ (API Externa)
│ API             │
└─────────────────┘
```

### Flujo de Datos

1. **Usuario** ingresa cantidad y selecciona monedas
2. **Frontend** valida y envía petición a API Gateway
3. **API Gateway** enruta la petición a la Lambda correcta
4. **Lambda Function** consulta tasas de cambio actuales
5. **API Externa** (ExchangeRate-API) devuelve tasas
6. **Lambda** procesa y calcula conversión
7. **API Gateway** devuelve respuesta JSON
8. **Frontend** muestra resultado al usuario

---

## 🛠️ Tecnologías

### Frontend
- **HTML5**: Estructura semántica
- **CSS3**: Estilos modernos con gradientes y animaciones
- **JavaScript (Vanilla)**: Lógica de la aplicación, fetch API

### Backend (Serverless)
- **AWS Lambda**: Funciones serverless en Python 3.11
- **API Gateway**: REST API para exponer funciones
- **CloudWatch**: Logs y monitoreo

### APIs Externas
- **ExchangeRate-API**: Tasas de cambio en tiempo real (gratis)

### Herramientas
- **AWS CLI**: Despliegue desde línea de comandos
- **Visual Studio Code**: Editor de código
- **Git**: Control de versiones

---

## ☁️ Cloud Functions

### 1. `convert-currency`

**Propósito**: Convertir una cantidad entre dos monedas

**Método**: `POST /convert`

**Request Body**:
```json
{
  "from_currency": "USD",
  "to_currency": "COP",
  "amount": 100
}
```

**Response**:
```json
{
  "success": true,
  "from_currency": "USD",
  "to_currency": "COP",
  "amount": 100,
  "rate": 4000.0,
  "converted_amount": 400000.00,
  "formatted": "100.00 USD = 400,000.00 COP"
}
```

**Validaciones**:
- ✅ Monedas no vacías
- ✅ Monto mayor a 0
- ✅ Formato de datos correcto
- ✅ Moneda destino soportada

---

### 2. `get-exchange-rates`

**Propósito**: Obtener tasas de cambio actuales para una moneda base

**Método**: `GET /rates?base=USD`

**Query Parameters**:
- `base` (opcional): Moneda base (default: USD)

**Response**:
```json
{
  "success": true,
  "base": "USD",
  "rates": {
    "EUR": 0.85,
    "COP": 4000.0,
    "GBP": 0.73,
    "JPY": 110.0
  },
  "timestamp": "2025-10-31"
}
```

---

## 📦 Instalación

### Prerrequisitos

- ✅ Cuenta AWS (Free Tier)
- ✅ AWS CLI instalado y configurado
- ✅ Python 3.11+
- ✅ Navegador web moderno

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/currency-converter-serverless.git
cd currency-converter-serverless
```

### Paso 2: Configurar AWS CLI

```bash
aws configure
# Ingresa:
# - AWS Access Key ID
# - AWS Secret Access Key
# - Default region: us-east-2
# - Output format: json
```

### Paso 3: Crear rol IAM para Lambda

```bash
# Crear rol
aws iam create-role \
  --role-name lambda-execution-role \
  --assume-role-policy-document file://trust-policy.json

# Adjuntar política
aws iam attach-role-policy \
  --role-name lambda-execution-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

### Paso 4: Desplegar funciones Lambda

```bash
# Función 1: convert-currency
cd lambda-functions/convert-currency
zip function.zip lambda_function.py

aws lambda create-function \
  --function-name convert-currency \
  --runtime python3.11 \
  --role arn:aws:iam::TU_ACCOUNT_ID:role/lambda-execution-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip \
  --timeout 10 \
  --memory-size 128 \
  --region us-east-2

# Función 2: get-exchange-rates
cd ../get-exchange-rates
zip function.zip lambda_function.py

aws lambda create-function \
  --function-name get-exchange-rates \
  --runtime python3.11 \
  --role arn:aws:iam::TU_ACCOUNT_ID:role/lambda-execution-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip \
  --timeout 10 \
  --memory-size 128 \
  --region us-east-2
```

### Paso 5: Configurar API Gateway

1. Ir a [API Gateway Console](https://console.aws.amazon.com/apigateway)
2. Create API → REST API → Build
3. API name: `currency-converter-api`
4. Crear recursos `/convert` y `/rates`
5. Configurar métodos POST y GET
6. Integrar con funciones Lambda
7. Habilitar CORS
8. Deploy a stage `prod`

### Paso 6: Actualizar frontend

En `frontend/index.html`, línea ~217:

```javascript
const API_BASE_URL = 'https://TU_API_ID.execute-api.us-east-2.amazonaws.com/prod';
```

Reemplazar con tu URL de API Gateway.

### Paso 7: Probar

Abrir `frontend/index.html` en navegador.

---

## 🚀 Uso

### Desde la Aplicación Web

1. **Abrir** `frontend/index.html` en navegador
2. **Ingresar** cantidad a convertir
3. **Seleccionar** moneda origen
4. **Seleccionar** moneda destino
5. **Click** en "🔄 Convertir Ahora"
6. **Ver** resultado con tasa de cambio

### Desde la API (cURL)

**Convertir moneda:**
```bash
curl -X POST https://xn6lxsf1e2.execute-api.us-east-2.amazonaws.com/prod/convert \
  -H "Content-Type: application/json" \
  -d '{"from_currency":"USD","to_currency":"COP","amount":100}'
```

**Obtener tasas:**
```bash
curl https://xn6lxsf1e2.execute-api.us-east-2.amazonaws.com/prod/rates?base=USD
```

### Desde JavaScript

```javascript
// Convertir
const response = await fetch('https://API_URL/prod/convert', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    from_currency: 'USD',
    to_currency: 'COP',
    amount: 100
  })
});
const data = await response.json();
console.log(data.converted_amount);
```

---

## 🌐 APIs Utilizadas

### ExchangeRate-API

**URL**: https://api.exchangerate-api.com  
**Plan**: Gratis (1,500 requests/mes)  
**Documentación**: https://www.exchangerate-api.com/docs  

**Características**:
- ✅ Sin API key requerida
- ✅ Actualización diaria
- ✅ 160+ monedas soportadas
- ✅ Alta disponibilidad
- ✅ Respuesta rápida (<100ms)

**Ejemplo de request**:
```
GET https://api.exchangerate-api.com/v4/latest/USD
```

**Ejemplo de respuesta**:
```json
{
  "base": "USD",
  "rates": {
    "EUR": 0.85,
    "COP": 4000.0
  },
  "time_last_updated": 1698710400
}
```

---

## 💰 Costos

### AWS Free Tier (12 meses)

| Servicio | Límite Gratis | Después del Free Tier |
|----------|---------------|----------------------|
| **Lambda** | 1M invocaciones/mes | $0.20 por 1M invocaciones |
| **API Gateway** | 1M llamadas/mes | $3.50 por 1M llamadas |
| **CloudWatch** | 5GB logs | $0.50 por GB |

### Estimación de Costos

**Escenario 1: Tráfico Bajo** (1,000 conversiones/mes)
- Lambda: $0.00 (dentro del Free Tier)
- API Gateway: $0.00 (dentro del Free Tier)
- **Total: $0.00/mes** ✅

**Escenario 2: Tráfico Medio** (100,000 conversiones/mes)
- Lambda: $0.00 (dentro del Free Tier)
- API Gateway: $0.00 (dentro del Free Tier)
- **Total: $0.00/mes** ✅

**Escenario 3: Tráfico Alto** (2M conversiones/mes - después del Free Tier)
- Lambda: $0.40 (2M × $0.20/1M)
- API Gateway: $7.00 (2M × $3.50/1M)
- **Total: $7.40/mes** 💵

### Comparación con Servidor Tradicional

| Aspecto | Serverless | EC2 t3.micro |
|---------|-----------|--------------|
| **Costo base** | $0 (sin uso) | ~$8/mes (siempre) |
| **Mantenimiento** | $0 | Tiempo de admin |
| **Escalado** | Automático | Manual |
| **Alta disponibilidad** | Incluida | Extra (~$20/mes) |

**💡 Conclusión**: Serverless es más económico para tráfico bajo-medio.

---

## ✨ Ventajas del Modelo Serverless

### Observadas en este Proyecto

#### 1. **Sin Gestión de Servidores** 🚫🖥️
- No necesitas provisionar EC2
- No instalas ni actualizas dependencias del OS
- AWS maneja toda la infraestructura
- **Ahorro**: ~8 horas/mes de administración

#### 2. **Escalado Automático** 📈
- De 0 a 1,000 ejecuciones concurrentes
- Sin configuración adicional
- Sin preocupaciones por límites
- **Probado**: La app maneja picos de tráfico sin cambios

#### 3. **Pago por Uso Real** 💰
- Solo pagas cuando el código se ejecuta
- Granularidad: por milisegundo
- $0 cuando no hay tráfico
- **Ahorro**: ~$8/mes vs servidor dedicado

#### 4. **Desarrollo Rápido** ⚡
- Deploy en minutos, no días
- Foco en código, no infraestructura
- Iteración rápida
- **Tiempo de desarrollo**: 2-3 horas vs 1-2 días

#### 5. **Alta Disponibilidad** 🌍
- Multi-AZ por defecto
- 99.99% uptime SLA
- Sin configuración adicional
- **Beneficio**: Robustez empresarial sin esfuerzo

#### 6. **Mantenimiento Mínimo** 🔧
- No parches de seguridad
- No actualizaciones de OS
- AWS maneja todo
- **Ahorro**: 100% tiempo de mantenimiento

### Casos de Uso Ideales

✅ **APIs con tráfico variable**  
✅ **Webhooks y eventos**  
✅ **Procesamiento de datos en batch**  
✅ **Microservicios**  
✅ **Backends móviles**  
✅ **Tareas programadas (cron jobs)**  

---

## ⚠️ Limitaciones

### Encontradas Durante el Desarrollo

#### 1. **Cold Starts** ❄️
- **Problema**: Primera invocación tarda 1-2 segundos
- **Causa**: AWS debe inicializar el contenedor
- **Impacto**: Latencia inicial en peticiones
- **Mitigación**: Mantener funciones "calientes" con pings periódicos

#### 2. **Timeout Máximo** ⏱️
- **Límite**: 15 minutos por ejecución
- **Impacto**: No apto para procesos muy largos
- **Solución**: Dividir en funciones más pequeñas

#### 3. **Tamaño de Paquete** 📦
- **Límite**: 50 MB comprimido (sin capas), 250 MB descomprimido
- **Impacto**: No se pueden usar librerías muy pesadas
- **Solución**: Usar Lambda Layers para dependencias

#### 4. **Stateless** 💾
- **Característica**: Sin estado entre ejecuciones
- **Impacto**: No se puede guardar info en memoria
- **Solución**: Usar DynamoDB, S3, o ElastiCache

#### 5. **Vendor Lock-in** 🔒
- **Riesgo**: Dependencia de AWS
- **Mitigación**: Usar frameworks como Serverless Framework
- **Portabilidad**: Código Python es portable, configuración no

#### 6. **Debugging Complejo** 🐛
- **Desafío**: No hay acceso directo al servidor
- **Solución**: CloudWatch Logs exhaustivos
- **Herramienta**: AWS X-Ray para tracing

### Cuándo NO Usar Serverless

❌ **Aplicaciones con tráfico constante 24/7** (más caro que servidor dedicado)  
❌ **Procesos de larga duración** (>15 minutos)  
❌ **Aplicaciones con estado** (sin soluciones externas)  
❌ **Workloads con latencia crítica** (<100ms) debido a cold starts  

---

## 📸 Capturas de Pantalla

### Interfaz Principal
![Interfaz del Conversor](docs/screenshots/main-interface.png)
*Vista principal con formulario de conversión*

### Conversión Exitosa
![Resultado de Conversión](docs/screenshots/conversion-result.png)
*Resultado mostrando 100 USD = 400,000 COP*

### AWS Lambda Console
![Lambda Functions](docs/screenshots/lambda-console.png)
*Funciones Lambda desplegadas en AWS*

### API Gateway
![API Gateway](docs/screenshots/api-gateway.png)
*Configuración de endpoints REST*

### CloudWatch Logs
![CloudWatch](docs/screenshots/cloudwatch-logs.png)
*Logs de ejecución en tiempo real*

---

## 📚 Conceptos Aprendidos

### Serverless (FaaS)
- ✅ Function as a Service
- ✅ Event-driven architecture
- ✅ Stateless execution model
- ✅ Auto-scaling mechanisms

### AWS Services
- ✅ Lambda function creation and deployment
- ✅ API Gateway REST API configuration
- ✅ IAM roles and permissions
- ✅ CloudWatch monitoring

### Best Practices
- ✅ CORS configuration
- ✅ Error handling strategies
- ✅ Input validation
- ✅ Environment variables
- ✅ Minimal dependencies

---

## 🔄 Serverless vs Modelos Tradicionales

| Aspecto | Serverless (Lambda) | IaaS (EC2) | PaaS (Elastic Beanstalk) |
|---------|-------------------|-----------|------------------------|
| **Setup Inicial** | Minutos | Horas/Días | Horas |
| **Escalado** | Automático | Manual | Semi-automático |
| **Costo Base** | $0 (sin uso) | ~$8/mes | ~$15/mes |
| **Mantenimiento** | Mínimo | Alto | Medio |
| **Control** | Bajo | Total | Medio |
| **Cold Start** | Sí (~1s) | No | No |
| **Límite Tiempo** | 15 min | Ilimitado | Ilimitado |
| **Estado** | Stateless | Stateful | Stateful |

**Conclusión**: Cada modelo tiene su lugar. Serverless brilla en:
- 🎯 Microservicios y APIs
- 🎯 Carga variable o impredecible
- 🎯 Proyectos con presupuesto limitado
- 🎯 Desarrollo rápido y ágil

---

## 🚀 Mejoras Futuras

### Funcionalidades
- [ ] Autenticación con AWS Cognito
- [ ] Histórico de conversiones con DynamoDB
- [ ] Gráficos de tendencias de tasas
- [ ] Alertas de cambios significativos
- [ ] Soporte para más monedas
- [ ] Conversión inversa automática

### Técnicas
- [ ] Cache con ElastiCache
- [ ] API Gateway con API Keys
- [ ] Rate limiting
- [ ] Versionado de API
- [ ] Tests unitarios
- [ ] CI/CD con GitHub Actions
- [ ] Monitoreo con AWS X-Ray

### Performance
- [ ] Reducir cold starts con Provisioned Concurrency
- [ ] Optimizar tamaño de paquetes
- [ ] Lambda Layers para dependencias compartidas
- [ ] CloudFront CDN para frontend

---

## 🧪 Testing

### Probar Funciones Lambda Localmente

```bash
# Crear evento de prueba
echo '{
  "httpMethod": "POST",
  "body": "{\"from_currency\":\"USD\",\"to_currency\":\"COP\",\"amount\":100}"
}' > test-event.json

# Invocar función
aws lambda invoke \
  --function-name convert-currency \
  --payload file://test-event.json \
  --region us-east-2 \
  output.json

# Ver resultado
cat output.json
```

### Probar API Gateway

```bash
# Probar GET /rates
curl https://xn6lxsf1e2.execute-api.us-east-2.amazonaws.com/prod/rates?base=USD

# Probar POST /convert
curl -X POST https://xn6lxsf1e2.execute-api.us-east-2.amazonaws.com/prod/convert \
  -H "Content-Type: application/json" \
  -d '{"from_currency":"USD","to_currency":"EUR","amount":100}'
```

### Casos de Prueba

| Test | Input | Expected Output | Status |
|------|-------|----------------|--------|
| Conversión USD→COP | 100 USD | ~400,000 COP | ✅ Pass |
| Conversión EUR→USD | 100 EUR | ~118 USD | ✅ Pass |
| Misma moneda | USD→USD | Error | ✅ Pass |
| Monto negativo | -50 USD | Error | ✅ Pass |
| Moneda inválida | XXX→USD | Error | ✅ Pass |

---

## 🔒 Seguridad

### Implementado
- ✅ HTTPS/TLS en todas las comunicaciones
- ✅ CORS configurado correctamente
- ✅ Validación de inputs en backend
- ✅ IAM roles con permisos mínimos necesarios
- ✅ Logs en CloudWatch para auditoría

### Recomendado para Producción
- 🔐 Autenticación con AWS Cognito
- 🔐 API Keys en API Gateway
- 🔐 Rate limiting
- 🔐 WAF (Web Application Firewall)
- 🔐 Secrets Manager para credenciales
- 🔐 VPC para Lambda functions sensibles

---

## 📖 Referencias

### Documentación Oficial
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [API Gateway Documentation](https://docs.aws.amazon.com/apigateway/)
- [CloudWatch Logs](https://docs.aws.amazon.com/cloudwatch/)

### Tutoriales
- [Getting Started with Lambda](https://aws.amazon.com/lambda/getting-started/)
- [Serverless Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [API Gateway Tutorial](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html)

### Herramientas
- [AWS CLI](https://aws.amazon.com/cli/)
- [Serverless Framework](https://www.serverless.com/)
- [ExchangeRate-API Docs](https://www.exchangerate-api.com/docs)

### Artículos
- [What is Serverless?](https://aws.amazon.com/serverless/)
- [Lambda Cold Starts](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/)
- [Serverless Patterns](https://serverlessland.com/patterns)



---

## 📊 Estadísticas del Proyecto

- 📅 **Fecha de Inicio**: Octubre 2025
- ⏱️ **Tiempo de Desarrollo**: ~4 horas
- 🐍 **Líneas de Código**: ~300 (Python + JavaScript)
- ☁️ **Funciones Lambda**: 2
- 🌐 **Endpoints API**: 2
- 💰 **Costo Mensual**: $0 (Free Tier)

---

## 🎓 Proyecto Académico

**Curso**: Computación en la Nube - Actividad 6  
**Período**: Octubre 2025  
**Tema**: Aplicación Web con Computación Serverless (Cloud Functions)  

### Objetivos Cumplidos

✅ Implementar funciones serverless usando AWS Lambda  
✅ Crear aplicación web frontend que consuma las funciones  
✅ Configurar APIs REST usando API Gateway  
✅ Demostrar ventajas del modelo serverless  
✅ Documentar proceso completo de desarrollo y despliegue  

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub ⭐**

Hecho con ❤️ y ☕ usando AWS Lambda

</div>