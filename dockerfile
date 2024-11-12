FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 80
ENV STREAMLIT_SERVER_PORT 80
ENV OPENWEATHER_API_KEY=${OPENWEATHER_API_KEY}
CMD ["streamlit", "run", "app.py", "--server.port=80", "--server.address=0.0.0.0"]
