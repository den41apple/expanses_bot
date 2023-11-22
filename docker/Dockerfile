FROM python:3.10

COPY requirements.txt .

RUN pip install --upgrade pip -r requirements.txt --no-cache-dir


ENV PYTYHONBUFFERED=1
ENTRYPOINT ["bash", "app/docker/docker-entrypoint.sh"]
