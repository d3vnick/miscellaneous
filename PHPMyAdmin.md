### Docker
```
sudo -E docker run --name myadmin -d \
-e PMA_HOST=localhost \
-e PMA_PORT=3306 \
-e PMA_USER=user \
-e PMA_PASSWORD=pass \
-p 80:80 phpmyadmin/phpmyadmin
