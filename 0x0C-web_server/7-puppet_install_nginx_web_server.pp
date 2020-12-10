#Install and Setup NGINX server via puppet.
exec { 'Update system':
  command => '/usr/bin/env apt-get -y update',
}

exec { 'Install NGINX.':
  command => '/usr/bin/env apt-get -y install nginx',
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

exec {'/usr/bin/env sed -i "/server_name _;/ a\\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default': }

exec {'/usr/bin/env sed -i "/server_name _;/ a\\\terror_page 404 /custom_404.html;" /etc/nginx/sites-available/default': }

file { '/var/www/html/custom_404.html':
  content => 'Ceci n\'est pas une page',
}

exec { 'Starting NGINX':
  command => '/usr/bin/env service nginx start',
}
