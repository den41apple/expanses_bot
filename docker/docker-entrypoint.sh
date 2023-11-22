cd app

echo "CREATE DATABASE"
python create_db.py

echo "RUN APP"
python loader.py