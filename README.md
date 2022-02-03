# Usage:
    setup -n mysql -w /opt/mysql -s 10G -p passw0rd

This will create a luks volume file inside /opt/mysql dir and generate skeleton docker-compose that will use the encrypted volume. The compose file has a simple webapp service that will pass password from user to cryptsetup and decrypt the luks volume first time.

Unfortunately I did not find a proper way to run the compose services at reboot in specific order with help of docker restart policy, so you will need to use crontab or systemd to run the startup.sh shell script file, the shell script will make sure the app services run only after decryption stage finish successfully :

    @reboot root /opt/mysql/startup.sh

# Demo:


https://user-images.githubusercontent.com/31401744/127346723-94db0eda-43da-4219-8926-db241b1b55f1.mp4



Contributions to work this properly are welcomed :)
