## Инструкция по развертыванию

#### Обновить список пакетов
```shell
apt update
```

#### Установить Docker
```shell
curl https://get.docker.com | sh
```

#### Установить Git
```shell
apt install git -y
```

#### Склонировать Git
```shell
git clone <GIT_REPO_URL> ./bot
```

#### Получить самоподписываемый сертификат на Ip адрес (раз скорей всего домена нет)
```shell
cd bot
mkdir certs && cd certs 
openssl genpkey -algorithm RSA -out private_key.pem
```
```shell
# Заменить "<IP_АДРЕСС>" на актуальный
openssl req -new -key private_key.pem -out certificate.csr \
  -subj "/C=RU/ST=Moscow/L=City/O=Organization/CN=<IP_АДРЕСС>" \
  -reqexts SAN \
  -config <(echo "[req]"; echo "req_extensions = SAN"; echo "[SAN]"; echo "subjectAltName = IP:<IP_АДРЕСС>")
```
```shell
openssl x509 -req -in certificate.csr -signkey private_key.pem -out certificate.crt
```

#### Догрузить .env файл на сервер (заменить на свой ip)
```shell
# Заменить "<IP_АДРЕСС>" на актуальный
WEBHOOK_TELEGRAM_URL="https://<IP_АДРЕСС>:8443"
```

#### Собрать контейнер
```shell
docker compose build
```

#### Запустить контейнер
```shell
docker compose up -d
```
