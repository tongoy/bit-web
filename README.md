The script is used to get [BIT](https://www.bit.edu.cn/) [network connection](http://10.0.0.55/) when the desktop environment is unavailable.



## 1. Installation

### Ubuntu OS
1. Download Chrome from [here](https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb).
2. Install Chrome with
   + `apt-get update`
   + `dpkg -i google-chrome-stable_current_amd64.deb`
   + `apt-get install -f`
3. Install WebDriver
   + Check Chrome version with `google-chrome --version`
   + Download corresponding WebDriver for Chrome from [here](https://chromedriver.chromium.org/downloads)
   + `unzip chromedriver-linux64.zip`
   + `mv chromedriver-linux64/chromedriver /usr/bin/`
4. Install Selenium with `pip install selenium`.
5. Install requirements `pip install requests`.

### Windows OS
1. Download Chrome from [here](https://www.google.com/chrome/) and install it.
2. Install WebDriver
   + Check Chrome version with `chrome://version`
   + Download corresponding WebDriver for Chrome from [here](https://chromedriver.chromium.org/downloads)
   + Unzip it and put `chromedriver.exe` and the script in the same directory
3. Install Selenium with `pip install selenium`.
4. Install requirements `pip install requests`.



## 2. Usage

### Login
Run `python3 client2.py -u stu_id -p password -a login`.

### Logout
Run `python3 client2.py -u stu_id -p password -a logout`.


