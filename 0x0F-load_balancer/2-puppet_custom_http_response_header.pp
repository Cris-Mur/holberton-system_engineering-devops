# using scripts in puppet
exec {'./0-custom_http_response-header':
  command => "/usr/bin/bash -c '0-custom_http_response-header'"
}
