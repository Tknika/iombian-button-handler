FROM python:3.9.2-alpine
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY src .
EXPOSE 5556
CMD ["python", "/app/src/main.py"]
# De momento sin variables de entorno ni nada como primera prueba
