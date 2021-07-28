# Usage:
    setup -n mysql -w /opt/mysql -s 10G -p passw0rd

This will create a luks volume file inside /opt/mysql dir and generate skeleton docker-compose that will use the encrypted volume. The compose file has a simple webapp service that will pass password from user to cryptsetup and decrypt the luks volume first time.

Unfortunately I did not find a proper way to run the compose services at reboot with help of docker restart policy, so you will need to use crontab or systemd to start the compose services :

    @reboot sleep 60s && /usr/local/bin/docker-compose -f /opt/mysql/docker-compose.yml up -d

#

Contributions to work this properly are welcomed :)