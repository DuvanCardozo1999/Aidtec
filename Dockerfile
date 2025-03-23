# Imagen base de Python
FROM python:3.11

# Configurar la carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requerimientos y el código fuente
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto donde correrá la app
EXPOSE 8000

# Comando para correr la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
