# Install NginX with puppet
# set default page
# set redirection "301 Moved Permanently"

package { 'nginx':
  ensure => 'installed'
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => 'Holberton School'
}

exec { 'sed':
  command => "/bin/sed -i 's/server_name _;/server_name _;\n\trewrite ^\/redirect_me http:\/\/cris-mur.tech permanent;/' /etc/nginx/sites-available/default"
}

exec { 'restart_nginx':
  command => "/etc/init.d/nginx restart"
}
