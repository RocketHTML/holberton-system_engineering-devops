# create a file with puppet
file { 'holberton':
    ensure  => file,
    path    => '/tmp/holberton',
    owner   => www-data,
    group   => www-data,
    content => 'I love Puppet'
}
