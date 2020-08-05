# manifest modify the file ssh_config

file_line { 'no_password':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'private_key':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentifyFile ~/.ssh/holberton',
  replace => true,
}
