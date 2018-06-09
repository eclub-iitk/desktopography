The kinect is an amazing and intelligent piece of hardware. It has a RGB camera, an IR laser projector, an IR CMOS sensor, a servo to adjust the tilt of the device and a microphone array.  The RGB camera is like any other camera such as a webcam but it is the depth sensor that the Kinect is known for as it enables the Kinect to perceive the world around it in 3D !


Here are the steps to get started with using the kinect :-

1)  Open a terminal and run the following commands
```
   sudo apt-get update
   sudo apt-get upgrade
```
2) Install the necessary dependencies
```
  sudo apt-get install git-core cmake freeglut3-dev pkg-config build-essential libxmu-dev libxi-dev libusb-1.0-0-dev
```
3) Clone the libfreenect repository to your system
```
git clone git://github.com/OpenKinect/libfreenect.git
```
4) Install libfreenect
```
cd libfreenect
mkdir build
cd build
cmake -L ..
make
sudo make install
sudo ldconfig /usr/local/lib64/
```
5) To use Kinect as a non-root user do the following
```
sudo adduser $USER video
sudo adduser $USER plugdev
```
6) Also make a file with rules for the Linux device manager
```
sudo nano /etc/udev/rules.d/51-kinect.rules
```
Then paste the following and save
```
# ATTR{product}=="Xbox NUI Motor"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02b0", MODE="0666"
# ATTR{product}=="Xbox NUI Audio"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02ad", MODE="0666"
# ATTR{product}=="Xbox NUI Camera"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02ae", MODE="0666"
# ATTR{product}=="Xbox NUI Motor"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02c2", MODE="0666"
# ATTR{product}=="Xbox NUI Motor"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02be", MODE="0666"
# ATTR{product}=="Xbox NUI Motor"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02bf", MODE="0666"
```
7) Log out and back in. Run the following command in a terminal to test if libfreenect is correctly installed
```
freenect-glview
```
This should cause a window to pop up showing the depth and RGB images. Pressing ‘w’ on the keyboard causes the kinect to tilt up and pressing ‘x’ causes the kinect to tilt down. There are several other control options that are listed in the terminal when “freenect-glview” is run

8) In order to use the Kinect with opencv and python, the python wrappers for libfreenct need to be installed. Before doing that, install the necessary dependencies

```
sudo apt-get install cython
sudo apt-get install python-dev
sudo apt-get install python-numpy
```
9) Go to the directory ……./libfreenect/wrappers/python and run the following command
```
sudo python setup.py install
```
python here means default python-2.7, If you use python-3 replace python with python3.

10) Save the above code given (kinect_test.py)
    Run the above program as 
    ```
    python kinect_test.py
    ```

For further information, check
1) Open kinect page :- http://openkinect.org/wiki/Main_Page
2) libfreenect github page :- https://github.com/OpenKinect/libfreenect




