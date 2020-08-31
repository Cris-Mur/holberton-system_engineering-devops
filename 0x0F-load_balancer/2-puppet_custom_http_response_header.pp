# using scripts in puppet
exec {'./0-custom_http_response-header':
  command => '/usr/bin/bash ./0-custom_http_response-header'
}

exec {'1-install_load_balancer':
  command => '/usr/bin/bash ./1-install_load_balancer'
}
