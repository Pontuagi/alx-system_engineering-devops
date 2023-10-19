# Puppet script to enable login with the holberton user and open a file

user { 'holberton':
  ensure  => 'present',    # Ensure the user exists
  managehome => true,      # Create the user's home directory
  home    => '/home/holberton',  # Specify the home directory path
  shell   => '/bin/bash',  # Specify the user's default shell
}
