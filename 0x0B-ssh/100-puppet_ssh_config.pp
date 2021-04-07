# Client configuration file (w/ Puppet)
# using Puppet to make changes to our configuration file

file_line { 'assword no auth':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}

file_line { 'file_identity':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/holberton',
}
