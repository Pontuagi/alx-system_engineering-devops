#!/usr/bin/env bash
# Configures a brand new ubuntu with a custom HTTP header response

class nginx_custom_header {
  nginx::resource::location { 'custom_header':
    location => '~ ^/(.*)$',
    vhost    => 'default',
    content  => "add_header X-Served-By $hostname;",
  }
}

# Ensure Nginx is installed
class { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx is running
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Nginx::Resource::Location['custom_header'],
}
