# Använd en liten Python-bild för att minska bildens storlek
FROM python:3.12-slim

# Ställ in arbetskatalog
WORKDIR /app

# Kopiera och installera beroenden
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera över resten av appfilerna
COPY . .

# Exponera port 80 för containern
EXPOSE 80

# Ställ in miljövariabler
ENV STREAMLIT_SERVER_PORT 80
ENV OPENWEATHER_API_KEY=${OPENWEATHER_API_KEY}

# Starta Streamlit-applikationen på port 80
CMD ["streamlit", "run", "app.py", "--server.port=80", "--server.address=0.0.0.0"]
