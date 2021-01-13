# Boson OpenCV Sample Application

## About

This is a sample application, showing an OpenCV frame and triggering an FFC over I2C, for GMSL Boson on the Nvidia AGX Xavier platform with a D3 SerDes GMSL2 adapter board.

## Installation
Clone this repo and change to this directory
From the command line, enter:
```sh
git clone git@github.com:FLIR/Xavier_OpenCV_Sample.git
cd Xavier_OpenCV_Sample
```
### Installing Python
```sh
sudo apt-get update
sudo apt-get install python3 python3-pip
```
### Installing Dependencies
```sh
sudo apt-get install python-opencv
pip3 install -r requirements.txt

# Update pip to get lastest dependency fixes
pip3 install --upgrade pip
```
Ensure that the dependencies installed properly
```sh
python3
```
```python
>> import cv
>> import numpy
```
If you did not get errors, the packages were installed properly. Note: while numpy is not explicitly used in the script it is a requirement for `python-opencv`.
### Grant Executes Permission
```sh
chmod +x boson_video.py
chmod +x boson_i2c.py
```

## Usage

Both .py files are entry points. boson_video.py shows streaming video. boson_i2c.py triggers an FFC.
```sh
./boson_video.py
```
or 
```sh
./boson_i2c.py
```

Every time you connect a new camera, you must restart the computer - the Boson driver cannot detect when a new camera has been connected.

## Troubleshooting/Questions

This is a first release, so I have no troubleshooting guidelines yet. If you run into issues, please contact me (Anil Dhurjaty - adhurjaty@novacoast.com).

