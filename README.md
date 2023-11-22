## ���������� �� �������������

#### �������� ������ �������
```shell
apt update
```

#### ���������� Docker
```shell
curl https://get.docker.com | sh
```

#### ���������� Git
```shell
apt install git -y
```

#### ������������ Git
```shell
git clone <GIT_REPO_URL> ./bot
```

#### �������� ����������������� ���������� �� Ip ����� (��� ������ ����� ������ ���)
```shell
cd bot
mkdir certs && cd certs 
openssl genpkey -algorithm RSA -out private_key.pem
```
```shell
# �������� "<IP_������>" �� ����������
openssl req -new -key private_key.pem -out certificate.csr \
  -subj "/C=RU/ST=Moscow/L=City/O=Organization/CN=<IP_������>" \
  -reqexts SAN \
  -config <(echo "[req]"; echo "req_extensions = SAN"; echo "[SAN]"; echo "subjectAltName = IP:<IP_������>")
```
```shell
openssl x509 -req -in certificate.csr -signkey private_key.pem -out certificate.crt
```

#### ��������� .env ���� �� ������ (�������� �� ���� ip)
```shell
# �������� "<IP_������>" �� ����������
WEBHOOK_TELEGRAM_URL="https://<IP_������>:8443"
```

#### ������� ���������
```shell
docker compose build
```

#### ��������� ���������
```shell
docker compose up -d
```
