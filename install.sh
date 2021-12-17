sudo apt-get install -qq xterm  && echo Installing dependencies....
sleep 1
sudo xterm -e sudo wget https://raw.githubusercontent.com/K4L1T00lz/KAL1T00lz-gui/main/KAL1T00lz-gui.py -P /opt && sudo xterm -e sudo wget https://raw.githubusercontent.com/K4L1T00lz/KAL1T00lz-gui/main/KAL1T00lz-gui.sh -O /usr/bin/kalitoolz-gui && sudo chmod +x /usr/bin/kalitoolz && sudo xterm -e sudo apt-get install -y python3 build-essential autoconf automake libtool pkg-config libnl-3-dev libnl-genl-3-dev libssl-dev ethtool shtool rfkill zlib1g-dev libpcap-dev libsqlite3-dev libpcre3-dev libhwloc-dev libcmocka-dev hostapd wpasupplicant tcpdump screen iw usbutils git ruby default-jdk python3-pip python3-venv alien devscripts && echo Installed dependencies
sleep 1
echo "Installed successfully. Run the script by typing kalitoolz-gui"


