file {'/root/.ssh/config':
  ensure => file,
  owner => 'ubuntu',
  group => 'ubuntu',
  mode => '0600',
  content => "Host 18.208.120.220\n IdentityFile ~/.ssh/school\n
  PasswordAuthentication no\n",
}
