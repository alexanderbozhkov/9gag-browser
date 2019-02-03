import sys
from selenium import webdriver
from PyQt5.QtWidgets import QApplication
Menu = __import__('9gui').Menu
get_all_memes = __import__('9archive').get_all_memes

ALL_MEMES = []
ALL_MEMES_FILE = '/home/whatever/Desktop/dankest_memes.txt'  # MEME FILE
IMAGE_FILE = '/home/whatever/PythonStuff/9gag_machine/logo.png'  # GUI LOGO
CHROMEDRIVER = '/usr/bin/chromedriver'  # driver for selenium (chrome)
DRIVER = webdriver.Chrome(CHROMEDRIVER)
CREDENTIALS = []  # list with 9gag credentials [0] -> email && [1] -> password
with open('credentials.txt', 'r') as f:
    for line in f:
        CREDENTIALS.append(line.strip())

if __name__ == '__main__':
    get_all_memes(ALL_MEMES_FILE, ALL_MEMES)
    app = QApplication(sys.argv)
    ex = Menu(ALL_MEMES, IMAGE_FILE, DRIVER, CREDENTIALS)
    sys.exit([app.exec_(), DRIVER.quit()])
