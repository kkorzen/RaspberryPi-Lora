# RaspberryPi LoRa Communication README
---
## Introduction
Project was under development during the second semester of Master studies in Embedded Systems field on **Warsaw Univeristy of Technology**. Project was a part of a total of three mini-projects as part of the **Internet of Things** (pol. *Internet Rzeczy*) classes.

The main goal of the project was to establish a connection between **two Raspberry Pi 3 SBCs** (ang. Single Board Computers) using a LoRa protocol. Every Raspbbery Pi had its own Dragino LoRa/GPS hat which enables setting up a communiaction. As mentioned, the hat is equipped with a GPS module, although it wasn't tested and used in this project. For data sent we chose an avarge RGB value of the picture taken by PiCamera.

## Before moving on into README
The recommended OS for this project is **Raspbian OS 32-bit** as the WiringPi library works best on this software. Make sure you've installed the right OS as our program may not work on the 64-bit version.

## Important links & files

Below are the two most important links which content was heavily "explored" during development of this project. The first one is referencing the main page of the WiringPi library home page. The second one is referencing specifically the *News* section of the library, where you can find more examples than shown below in the **Quick Setup** section.

[WiringPi library docs](http://wiringpi.com/)\
[WiringPi news](http://wiringpi.com/news/)

Look also into the PDF file in PDF-DocFiles directory for a specific step-by-step installation. In the project, **chapter 4** titled <u>Example3: Two RPI use LoRa to transmit to each other</u>, was used.

## Quick setup
Quick setup is recommended to test the functionality of the LoRa librarry. Although all of the code below can be find in the links given above and in the mentioned PDF file, we decide to also write it here, because we value your time. :)

1. Installation of WiringPi.h library for Raspberry Pi 3 - written in C.
```
cd /tmp

wget https://unicorn.drogon.net/wiringpi-2.46-1.deb

sudo dpkg -i wiringpi-2.46-1.deb
```

2. Downloading the lora transceiver source files:
```
wget https://codeload.github.com/dragino/rpi-lora-tranceiver/zip/master

unzip master
```

3. Run a make file.
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


## Project files description
Project is mainly divided into two parts: one responsible for handling the LoRa communication and the second one handling the PiCamera and image analysis. 

Directory "PDF-DocFiles" contains all the files (.pdf format) which where considered worth putting in for the future developers. At the moment there is only one file, which is the LoRa hat datasheet.

Directory "cameraAnalysis" contains two files:
- camera.py -- there is only one function responsible for taking a shot using PiCamera and storing it in the main directory.
- ImageAnalyzer.py -- class written to make code clearer and easy-expandable. The main goal of this class is to calculate average RGB of an image but many other functionalities can by easily implemented.

Directory "lora-comm" contains all the files used in the process of communication between two Raspberry Pis. 

---
---

**IMPORTANT:**\
Files for LoRa communication used in this project are located in the "dragino_lora_app" directory. The other two directories are included into the package delivered by the manufacturer of the LoRa module.

---
---

The most important file is the *main.c* file including all the code needed for the LoRa protocol. File *Makefile* contains rules for the **make program**. Two more files:
- main.o -- object file being the effect of comipilation
- dragin_lora_app -- executable file ready to be run

Located in the main directory file **app.py** is responsible for taking a shot using PiCamera, calculate its average RGB and finally writing results into text file. Its also responsible for generating "RPi-camphoto.jpg" file in the main directory.

## Starting the application

### Introducion
Runing the application can be done simply by runing **setup_tx.sh** and **setup_rx.sh** files. But please take it into account that those scripts already run the application for you. So **DO NOT** run both scripts at once.

Run the **setup_tx.sh** on your tranceiver device (the one with camera).

Run the **setup_rx.sh** on your receiver device.

Tip: it is better to run these scripts through the terminal using the ```sudo bash setup_name_file.sh``` command.

### First run
If it's the first time your Raspberry runs our program, please make sure that you uncomment code written between the '='-lines in both files: **setup_tx.sh** and **setup_rx.sh**.

### Second and every next run
If it's not the first time your Raspberry runs our program, just run **setup_tx.sh** and **setup_rx.sh** respectively on the tranceiver and receiver device. If you edited these files before, make sure you commented sections mentioned above.

## Conclusion & future development
We highly recommend to experiment and modify both hardware and software. Maybe clear the code by writing your own libraries or change PiCamera to a different sensor. Feel free to do with this project whatever you want. :)

Probably this project will no longer be supported by us but as we give it to another engineering team it's highly plausible that they would upgrade already existing solutions or add something new. We would try to link their GitHub repos down below: ........
