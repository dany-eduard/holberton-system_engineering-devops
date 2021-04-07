# Using Puppet, create a manifest
# that kills a process named killmenow.

exec { 'pkill killmenow':
  provider => 'shell',
  command  => 'pkill -x killmenow'
}
