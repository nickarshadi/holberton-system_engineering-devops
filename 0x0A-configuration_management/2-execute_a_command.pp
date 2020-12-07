#Kill a process.
exec { 'Kill a process':
  command  =>  '/usr/bin/env pkill -9 killmenow',
}
