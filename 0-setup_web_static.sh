#!/usr/bin/env bash
# Script that sets up my servers for deployment

sudo apt-get -y install nginx
sudo mkdir -p '/data/web_static/releases/test'
sudo mkdir -p /data/web_static/shared
sudo ln -sf '/data/web_static/releases/test/' /data/web_static/current
sudo touch /data/web_static/releases/test/index.html

sudo chown -R ubuntu:ubuntu /data/

new_string="server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}"
sudo sed -i "s/server_name _;/$new_string/" /etc/nginx/sites-enabled/default

echo -e "<html>\n  <head>\n  </head>\n    <body>\n      Hello World!\n    </body>\n</html>" | sudo tee '/data/web_static/releases/test/index.html'

sudo service nginx restart


