#!/usr/bin/env bash
# Configures a brand new ubuntu with a custom HTTP header response

# Ensure Nginx is installed
class { 'nginx':
  ensure => 'installed',
}

# Define a custom Nginx location block
nginx::resource::location { 'custom_header':
  location => '~ ^/(.*)$',
  vhost    => 'default',
  content  => "add_header X-Served-By $hostname;",
}

# Ensure Nginx is running
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Nginx::Resource::Location['custom_header'],
}
