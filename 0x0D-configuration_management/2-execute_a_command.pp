# kill a process via puppet
exec {'killmenow':
    command => 'pkill killmeknow',
    path    => '/usr/bin/',
    returns => [0, 1]
}
