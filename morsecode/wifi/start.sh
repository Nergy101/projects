#!/bin/bash
#install apps

#sudo apt-get update
#sudo apt install hostapd isc-dhcp-server -y
#sudo apt install iptables-persistent -y

#configure dhcp
echo "configure dhcp"
cp -p /etc/dhcp/dhcp.conf /etc/dhcp/dhcp.conf.bak
cp  -f dhcp.conf /etc/dhcp/dhcp.conf

cp -p /etc/default/isc-dhcp-server /etc/default/isc-dhcp-server.bak
cp -f isc-dhcp-server /etc/default/isc-dhcp-server

# create static ip for wlan0
sudo ip addr flush dev wlan0
ifdown wlan0
echo "changing to static ip"

cp -p /etc/network/interfaces /etc/network/interfaces.bak
cp -f interfaces /etc/network/interfaces


ifconfig wlan0 192.168.42.1

ifup wlan0

# configure access point
echo "configurating access point"
cp hostapd1.conf /etc/hostapd/hostapd.conf
cp hostapd2 /etc/default/hostapd


echo "restarting services"
systemctl start isc-dhcp-server; systemctl start hostapd


sudo /usr/sbin/hostapd  /etc/hostapd/hostapd.conf &
