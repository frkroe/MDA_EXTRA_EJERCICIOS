FROM 3.7.15-alpine3.17

# crear carpeta 'app' y establecerla como directorio de trabajo
RUN mkdir /app
WORKDIR /app

# copiar archivo 'main.py' en la carpeta 'app'
COPY main.py main.py

# ejecutar 'main.py'
CMD ["python", "main.py"]
