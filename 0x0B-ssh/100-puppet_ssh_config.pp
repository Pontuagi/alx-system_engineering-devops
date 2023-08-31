# configure ssh
file { 'SSH configuration':
  ensure  => present
  path    => '/etc/ssh/ssh_config',
  content => "
    IdentityFile ~/.ssh/school
    PasswordAuthentication no\n",
  return  => [0,1]
}
