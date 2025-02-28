#!/bin/bash

echo "Deteniendo NGINX y NGROK..."
sudo systemctl stop nginx
pkill ngrok

echo "Actualizando el repositorio..."
sudo git pull origin main

echo "Iniciando NGINX..."
sudo systemctl start nginx

echo "Iniciando NGROK..."
nohup ngrok http 80 > /dev/null 2>&1 &

sleep 3

NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')

if [[ -z "$NGROK_URL" ]]; then
    echo "No se pudo obtener la URL de NGROK. Verifica si NGROK está corriendo."
else
    echo "La URL de NGROK es: $NGROK_URL"
fi