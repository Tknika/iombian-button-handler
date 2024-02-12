FROM python:3.9.2-slim
WORKDIR /app
COPY requirements.txt ./
RUN apt-get update && apt-get install build-essential -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY src ./
EXPOSE 5556
CMD ["python", "/app/main.py"]
# De momento sin variables de entorno ni nada como primera prueba
