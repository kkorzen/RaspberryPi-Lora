#=================================
# FOR THE FIRST RUN
#
#if [ $(uname -m) == aarch32 ];then 
#	echo "You have 32bit architecture, which means it matches for this program"
#	cd /tmp
#	wget https://unicorn.drogon.net/wiringpi-2.46-1.deb
#	sudo dpkg -i wiringpi-2.46-1.deb
#else
#	echo "You have 64bit architecture, which is not match for this program"
#	echo "Please install 32bit OS architecture."
#	exit 0
#fi
#
#cd source
#
#if [ ! -d "$venv" ]; then
#	python3 -m venv venv
#fi
#
#source ./venv/bin/activate
#
#pip3 install RPi.GPIO
#pip3 install picamera
#pip3 install Pillow
#
#deactivate
#=================================


make -C ./lora-comm/dragino_lora_app/

cd ./lora-comm/dragino_lora_app 
./dragino_lora_app rec
