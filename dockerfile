# 1. Använd en lättvikts-Python-bild som grund
FROM python:3.12-slim

# 2. Ange arbetskatalogen i containern
WORKDIR /app

# 3. Kopiera beroenden från din `requirements.txt` till containern
COPY requirements.txt .

# 4. Installera Python-beroenden
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopiera all kod från ditt projekt till arbetskatalogen i containern
COPY . .

# 6. Ange kommandot för att köra applikationen
CMD ["python", "app.py"]
