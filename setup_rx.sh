# FOR THE FIRST RUN
#
#if [! -d "venv" ]; then
#	python3 -m venv venv
#fi
#
#source ./venv/bin/activate
#
#pip3 install RPi.GPIO
#pip3 install picamera
#pip3 install Pillow

make -C ./lora-comm/dragino_lora_app/

cd ./lora-comm/dragino_lora_app 
./dragino_lora_app rec
