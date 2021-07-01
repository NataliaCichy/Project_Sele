# Project_Sele
Automation testing using Selenium Webdriver - Registration of a new user (foreigner) using invalid phone number

I. Installation and configuration (for Debian-based Linux systems)

1. In order to install Selenium package you should use the pip stack manager
# to check what version of pip is installed in the system, type in the terminal:
$ pip3 --version

# install the pip manager (in its absence) as superuser:
$ sudo apt install python3-pip

# installing selenium with a pip is very easy:
$ pip3 install selenium

2. Selenium package also needs drivers to work with the browser
# links to selected drivers:
# Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
# Firefox: https://github.com/mozilla/geckodriver/releases
# the driver version must match the browser version

# Firefox uses a driver called geckodriver. After downloading the archive adapted to the architecture of our processor and operating system, unpack it:
$ tar -xvf geckodriver-v0.26.0-linux64.tar.gz
# Then move the unpacked file to the /usr/local/bin directory:
$ mv geckodriver /usr/local/bin

# Chrome needs a driver called chromedriver. After downloading the archive adapted to the operating system, unpack it:
$ unzip chromedriver_linux64.zip
# Then move the unpacked file to the /usr/local/bin directory:
$ sudo mv chromedriver /usr/local/bin

II. Running Project_Sele.py
# In the terminal:
$ python3 Procekt_Sele.py




