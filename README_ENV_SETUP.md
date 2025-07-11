# Configuración de Variables de Entorno

## Configuración de API Key de OpenAI

Para usar el agente MCP con OpenAI, necesitas configurar tu API key como variable de entorno.

### Opción 1: Archivo .env (Recomendado)

1. Crea un archivo `.env` en la raíz del proyecto:

```bash
# En Windows
copy config.env.example .env

# En Linux/Mac
cp config.env.example .env
```

2. Edita el archivo `.env` y reemplaza `tu_api_key_aqui` con tu API key real:

```bash
OPENAI_API_KEY=sk-tu_api_key_real_aqui
```

### Opción 2: Variable de Entorno del Sistema

#### Windows (PowerShell)

```powershell
$env:OPENAI_API_KEY="sk-tu_api_key_real_aqui"
```

#### Windows (Command Prompt)

```cmd
set OPENAI_API_KEY=sk-tu_api_key_real_aqui
```

#### Linux/Mac

```bash
export OPENAI_API_KEY="sk-tu_api_key_real_aqui"
```

### Verificación

Para verificar que la variable está configurada correctamente, puedes ejecutar:

```python
import os
print(os.getenv("OPENAI_API_KEY"))
```

### Seguridad

- **Nunca** commits el archivo `.env` con tu API key real
- El archivo `.env` ya está incluido en `.gitignore`
- Usa siempre variables de entorno para credenciales sensibles

### Obtener API Key de OpenAI

1. Ve a [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Crea una nueva API key
3. Copia la key (comienza con `sk-`)
4. Configúrala en tu archivo `.env` o variable de entorno
