# kill a process via puppet
exec {'killmenow':
    command => 'pkill -f killmenow',
    path    => '/usr/bin/',
    returns => [0, 1]
}
