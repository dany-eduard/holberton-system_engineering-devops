# Client configuration file (w/ Puppet)
# using Puppet to make changes to our configuration file
file {'~/.ssh/config':
  ensure  => present,
  replace => 'yes',
  path    => '~/.ssh/config',
  content => 'Host *
     HostName 35.196.52.46
     User ubuntu
     IdentityFile ~/.ssh/holberton',
  mode    => '7000',
}
