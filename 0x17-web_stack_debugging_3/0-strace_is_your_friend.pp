# fix typo in wp-settings file
exec { 'fix typo in php config':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
