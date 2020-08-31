### Docker
```bash
sudo -E docker run --name myadmin -d \
-e PMA_HOST=127.0.0.1 \
-e PMA_PORT=3306 \
-e PMA_USER=user \
-e PMA_PASSWORD=pass \
-p 80:80 phpmyadmin/phpmyadmin
