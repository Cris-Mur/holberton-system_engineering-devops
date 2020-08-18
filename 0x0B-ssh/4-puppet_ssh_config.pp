# manifest modify the file ssh_config
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => 'HB_config
  IdentityFile ~/.ssh/holberton
  PasswordAuthentication no'
}
