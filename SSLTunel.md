## Ubuntu

### Update & Upgrade Ubuntu
apt-get update
apt-get upgrade

### Install stunnel
apt-get install stunnel4 -y

### Configure stunnel
nano /etc/stunnel/stunnel.conf
cert = /etc/stunnel/stunnel.pem

### Create ssl certificates
openssl genrsa -out key.pem 2048
openssl req -new -x509 -key key.pem -out cert.pem -day 1095
cat kep.pem cert.pem >> /etc/stunnel/stunnel.pem
