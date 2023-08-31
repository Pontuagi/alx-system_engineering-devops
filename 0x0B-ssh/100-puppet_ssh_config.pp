# configure ssh
exec {'echo':
  path => 'usr/bin:/bin',
  command => 'echo " IdentityFile ~/.ssh/school\n PasswordAuthentication no\n" >> /etc/ssh/ssh_config',
  return => [0, 1],
}
