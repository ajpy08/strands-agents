# Configuración de Variables de Entorno

## Configuración de Modelos de IA

El agente MCP puede usar diferentes modelos de IA configurados a través de variables de entorno.

### Tipos de Modelos Disponibles

- **OpenAI**: Modelos de OpenAI (GPT-3.5, GPT-4, etc.)
- **Ollama**: Modelos locales ejecutados con Ollama
- **AWS Bedrock**: Modelos de AWS Bedrock (default)

### Configuración General

1. Crea un archivo `.env` en la raíz del proyecto:

```bash
# En Windows
copy config.env.example .env

# En Linux/Mac
cp config.env.example .env
```

2. Edita el archivo `.env` y configura las variables según el modelo que quieras usar:

```bash
# Tipo de modelo (opciones: openai, ollama, bedrock)
MODEL_TYPE=bedrock
```

### Configuración por Modelo

#### OpenAI

```bash
MODEL_TYPE=openai
OPENAI_API_KEY=sk-tu_api_key_real_aqui
OPENAI_MODEL_ID=gpt-3.5-turbo
OPENAI_MAX_TOKENS=1000
OPENAI_TEMPERATURE=0.7
```

#### Ollama

```bash
MODEL_TYPE=ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL_ID=qwen3:1.7b
OLLAMA_TEMPERATURE=0.2
OLLAMA_KEEP_ALIVE=10m
OLLAMA_STOP_SEQUENCES=###,END
OLLAMA_TOP_K=40
```

#### AWS Bedrock (Default)

```bash
MODEL_TYPE=bedrock
```

### Configuración de Credenciales AWS

Para AWS Bedrock, las credenciales se configuran automáticamente desde:

#### Opción 1: Variables de Entorno

```bash
export AWS_ACCESS_KEY_ID="tu_access_key"
export AWS_SECRET_ACCESS_KEY="tu_secret_key"
export AWS_REGION="us-east-1"
```

#### Opción 2: Archivo de Credenciales

Crea el archivo `~/.aws/credentials`:

```ini
[default]
aws_access_key_id = tu_access_key
aws_secret_access_key = tu_secret_key
```

#### Opción 3: IAM Roles

Si ejecutas en EC2, ECS, o Lambda, las credenciales se configuran automáticamente.

### Verificación

Para verificar que las variables están configuradas correctamente:

```python
import os
from dotenv import load_dotenv

load_dotenv()
print(f"Modelo: {os.getenv('MODEL_TYPE', 'bedrock')}")
print(f"API Key OpenAI: {os.getenv('OPENAI_API_KEY', 'No configurada')}")
print(f"Región AWS: {os.getenv('AWS_REGION', 'us-east-1')}")
```

### Seguridad

- **Nunca** commits el archivo `.env` con credenciales reales
- El archivo `.env` ya está incluido en `.gitignore`
- Usa siempre variables de entorno para credenciales sensibles
- Para AWS, considera usar IAM roles en lugar de credenciales hardcodeadas

### Obtener Credenciales

#### Desde OpenAI

1. Ve a [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Crea una nueva API key
3. Copia la key (comienza con `sk-`)

#### Desde AWS

1. Ve a [AWS IAM Console](https://console.aws.amazon.com/iam/)
2. Crea un usuario con permisos para Bedrock
3. Genera credenciales de acceso
4. Configura las credenciales según las opciones anteriores
