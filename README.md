# Runit-control

A simple python script that makes it easier to enable, disable, start and stop runit services (Still in development)

# How to use

the only dependencies for this application are `python` and `runit`

**N/B:** you can use python(2) instead of python3 but I recommend you use python3

The script has to be run as root, so to run it, you can do `python3 runit-sysc.py {command_here}` or `python runit-sysc.py {command_here}` for python2 

**Example: **`sudo python3 runit-sysc.py start dbus`

See next section for the commands that can be ran

# Start a service

To start a service, simply do `start {service_name}` and it will start the service if it's available in `/etc/sv/`. If not it throws an error

# Stop a service
To stop a service, simply do 'stop {service_name}` and it will stop the service if it's available in `/etc/sv`. If not it throws an error

# Enable a service
To enable a service, simply do `enable {service_name}` and it will create a symlink from `/etc/sv` to `/var/service`. If the service isn't available in 
`/etc/sv`, it throws an error and if it's already avialable in `/var/service`, it prompts the user if they want to really write another symbolic link

# Disable a service
To disable a service, simply do `disable {service_name}` and it will remove the symlink from `/var/service`. If the service isn't available in `/var/service`
it throws an error
