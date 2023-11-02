# RaspberryPi_LoRa_Communication
---
## Introduction
Project was being developed during the second semester of Master studies in Embedded System Field on **Warsaw Univeristy of Technology**. Project was a part of a total of three mini-projects as part of the **Internet of Things** (pol. *Internet Rzeczy*) classes.

The main goal of the project was to establish a connection between **two Raspberry Pi 3 SBCs** (ang. Single Board Computers) using a LoRa protocol. Every Raspbbery Pi had its own Dragino LoRa/GPS hat which enables setting up a communiaction. As mentioned, the hat is equipped with a GPS module, although it wasn't tested and used in this project.

## Important links & files

[WiringPi library docs](http://wiringpi.com/)\
[WiringPi news](http://wiringpi.com/news/)

Look also into the PDF file in PDF-DocFiles directory for a specific step-by-step installation. In the project **chapter 4**, titled <u>Example3: Two RPI use LoRa to transmit to each other</u>, was used.

## Quick setup
For quick setup run the following commands

1. Installation of wiringPi.h library written in C:
```
cd /tmp

wget https://unicorn.drogon.net/wiringpi-2.46-1.deb

sudo dpkg -i wiringpi-2.46-1.deb
```

2. Downloading the lora transmit code:
```
wget https://codeload.github.com/dragino/rpi-lora-tranceiver/zip/master

unzip master
```

3. Run a make:
```
cd rpi-lora-tranceiver-master/dragino_lora_app

make
```

4. Run the app (sender or rec (receiver))
```
./dragino_lora_app sender
./dragino_lora_app rec
```

Remember that every change in the main.c source file requiers performing steps 3. and 4. once again.
<<<<<<< HEAD






=======
>>>>>>> lora-comm
