#!/bin/bash
#restore dhcp
echo "restoring dhcp.conf.."
cp /etc/dhcp/dhcp.conf.bak /etc/dhcp/dhcp.conf

echo "restoring isc-dhcp-server.."
cp /etc/default/isc-dhcp-server.bak /etc/default/isc-dhcp-server


# create static ip for wlan0
sudo ip addr flush dev wlan0
echo "restoring interfaces.."
cp /etc/network/interfaces.bak /etc/network/interfaces
echo "done."

echo "reassigning static ip"

ifconfig wlan0 192.168.178.30
ifdown wlan0
ifup wlan0

echo "restarting services"
systemctl stop isc-dhcp-server
service hostapd stop
echo "finished, welcome back"

###possible to try
#sudo update-rc.d hostapd defaults
#sudo update-rc.d hostapd disable

