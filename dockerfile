FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 80
ENV STREAMLIT_SERVER_PORT 80
CMD ["python", "app.py"] 
