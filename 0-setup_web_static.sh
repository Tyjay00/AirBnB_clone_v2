#!/usr/bin/env bash
# This script sets up a web server for deployment of web_static.

# Update the package lists for upgrades and new package installations
apt-get update

# Install nginx web server
apt-get install -y nginx

# Create directories for web deployment
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a test index.html file
echo "Holberton School" > /data/web_static/releases/test/index.html

# Create a symbolic link to the current release
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change the owner and group of the /data/ directory to ubuntu
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Configure the default Nginx server block
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    # Serve static files from this location
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    # Redirect requests to this location
    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    # Custom error page
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# Restart the nginx service to apply the changes
service nginx restart
