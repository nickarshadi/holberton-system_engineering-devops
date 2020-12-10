Install and Setup NGINX server via puppet.
exec { 'Update system':
  command => '/usr/bin/env apt-get -y update',
}

exec { 'Install NGINX.':
  command => '/usr/bin/env apt-get -y install nginx',
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

file_line { 'Sed append 301':
  ensure   => 'present',
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => '	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  multiple => true,
}

file_line { 'Sed append 404':
  ensure   => 'present',
  path     => '/etc/nginx/sites-available/default',
  after    => '	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  line     => '	error_page 404 /custom_404.html;',
  multiple => true,
}


file { '/var/www/html/custom_404.html':
  content => 'Ceci n\'est pas une page',
}

exec { 'Starting NGINX':
  command => '/usr/bin/env service nginx start',
}
