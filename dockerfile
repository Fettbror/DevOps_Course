# 1. Använd en Python-bild som bas
FROM python:3.12-slim

# 2. Sätt arbetskatalog
WORKDIR /app

# 3. Kopiera beroenden och installera dem
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kopiera applikationskoden
COPY . .

# 5. Exponera port 80
EXPOSE 80

# 6. Startkommando för applikationen
# Byt "app.py" till den fil där din Flask eller FastAPI-app initieras, eller ett annat kommando om du använder något som gunicorn
CMD ["python", "app.py"]
