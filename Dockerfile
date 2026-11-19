# Python ka halka image
FROM python:3.11-slim

# kaam ka folder container ke andar
WORKDIR /app

# pehle sirf requirements copy karke install karo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# phir poora project copy karo
COPY . .

# Streamlit ka port
EXPOSE 8501

# app chalao (0.0.0.0 taake container ke bahar se khule)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]