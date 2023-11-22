FROM python:3.10

COPY requirements.txt .

ENV PYTYHONBUFFERED=1

RUN pip install --upgrade pip -r requirements.txt --no-cache-dir

ENTRYPOINT ["bash", "app/docker/docker-entrypoint.sh"]
