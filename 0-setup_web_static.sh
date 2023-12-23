#!/usr/bin/env bash
#This is a bash script that sets up my web servers fro deployment

#Update package and intall nginx
sudo apt-get update
sudo apt-get -y install nginx

#create the driectories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html &> /dev/null

# Remove the existing symbolic link if it exists
sudo rm -rf /data/web_static/current

#Create a symbolic link /data/web_static/current linked to what 
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

#update nginx content to server hbnb_static
content="server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}"

sudo sh -c "echo \"$content\" > /etc/nginx/sites-available/default"
# Restart Nginx
sudo service nginx restart

