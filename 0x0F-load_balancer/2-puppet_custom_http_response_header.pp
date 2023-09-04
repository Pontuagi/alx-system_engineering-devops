#!/usr/bin/env bash
# Configures a brand new ubuntu with a custom HTTP header response


# Ensure Nginx is installed
class { 'nginx':
  ensure => 'installed',
}
# Define the custom header content
$custom_header_content = 'add_header X-Served-By $hostname;'

# Define the Nginx configuration file path
$nginx_config_file = '/etc/nginx/sites-enabled/default'

# Manage the Nginx configuration file
file { $nginx_config_file:
  ensure => file,
  content => $custom_header_content,
  notify => Exec['configure_custom_header'],
}

# Run the command to configure the custom header
exec { 'configure_custom_header':
  command     => "sed -i '/server {/a \\ \\ \\ \\ ${custom_header_content}' $nginx_config_file && service nginx restart",
  path        => '/usr/bin',
  refreshonly => true,
}

# Notify the exec resource to trigger the custom header configuration
File[$nginx_config_file] ~> Exec['configure_custom_header']
