import sys
from selenium import webdriver
from PyQt5.QtWidgets import QApplication
from fbs_runtime.application_context import ApplicationContext
from gui import Menu
from archive import get_all_memes

ALL_MEMES = []
ALL_MEMES_FILE = '/home/whatever/Desktop/dankest_memes.txt'  # MEME FILE
IMAGE_FILE = '/home/whatever/PythonStuff/9gag_machine/src/main/icons/logo.png'  # GUI LOGO
CHROMEDRIVER = '/usr/bin/chromedriver'  # driver for selenium (chrome)
DRIVER = webdriver.Chrome(CHROMEDRIVER)
CREDENTIALS = []  # list with 9gag credentials [0] -> email && [1] -> password
with open('/home/whatever/PythonStuff/9gag_machine/credentials.txt', 'r') as f:
    for line in f:
        CREDENTIALS.append(line.strip())


class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):                              # 2. Implement run()
        get_all_memes(ALL_MEMES_FILE, ALL_MEMES)
        app = QApplication(sys.argv)
        ex = Menu(ALL_MEMES, IMAGE_FILE, DRIVER, CREDENTIALS)
        return self.app.exec_()                 # 3. End run() with this line


if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit([exit_code, DRIVER.quit()])
