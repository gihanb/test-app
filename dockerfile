FROM python:3.11.4-slim-bullseye

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY sampleapp.py /app

EXPOSE 9090

CMD ["python", "sampleapp.py"]


