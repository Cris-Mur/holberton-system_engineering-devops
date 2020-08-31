# using scripts in puppet
exec {'./0-custom_http_response-header':
  command => "/usr/bin/bash -c 'apt-get -y update; apt-get -y install nginx; echo "Holberton School" >  /var/www/html/index.nginx-debian.html; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me google.com permanent;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-enabled/default; service nginx start'"
}
