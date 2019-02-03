from random import choice
from PyQt5.QtWidgets import QLabel, QMainWindow, QWidget, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap
from login import log_in_9gag


class Menu(QMainWindow):

    def __init__(self, meme_list: list, image_file, webdriver, credentials):
        super().__init__()
        self.previous_meme = None
        self.meme_list = meme_list
        self.next_meme = self.meme_generator(self.meme_list)
        self.image_file = image_file
        self.webdriver = webdriver
        self.credentials = credentials
        self.setWindowTitle("MEMES")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        lay = QVBoxLayout(self.central_widget)

        label = QLabel(self)
        pixmap = QPixmap(self.image_file).scaledToWidth(200)
        label.setPixmap(pixmap)

        lay.addWidget(label)
        next_button = QPushButton('NEXT')
        rand_button = QPushButton('RANDOM MEME')
        lay.addWidget(next_button)
        lay.addWidget(rand_button)

        next_button.clicked.connect(self.on_next_button_clicked)
        rand_button.clicked.connect(self.on_random_button_clicked)

        next_button.show()
        rand_button.show()
        self.show()

    @staticmethod
    def meme_generator(meme_list):
        for meme in meme_list:
            yield meme

    def on_next_button_clicked(self):
        try:
            next_meme_url = next(self.next_meme)
            if not self.previous_meme:
                username = self.credentials[0]
                password = self.credentials[1]
                self.webdriver.get(next_meme_url)
                self.webdriver.maximize_window()
                log_in_9gag(self.webdriver, username, password, QMessageBox)
                self.previous_meme = next_meme_url
            else:
                self.previous_meme = next_meme_url
                self.webdriver.get(next_meme_url)
                self.webdriver.maximize_window()
        except StopIteration:
            alert = QMessageBox()
            alert.setText('No more meymeys :(')
            alert.exec_()

    def on_random_button_clicked(self):
        random_meme_url = choice(self.meme_list)
        self.webdriver.get(random_meme_url)
        self.webdriver.maximize_window()
