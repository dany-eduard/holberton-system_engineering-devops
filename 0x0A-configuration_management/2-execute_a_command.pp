exec { 'pkill killmenow':
  provider => 'shell',
  command  => 'pkill -x killmenow'
}
