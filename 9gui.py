from PyQt5.QtWidgets import QLabel, QMainWindow, QWidget, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap
log_in_9gag = __import__('9login').log_in_9gag


class Menu(QMainWindow):

    def __init__(self, meme_list: list, image_file, webdriver, credentials):
        super().__init__()
        self.previous_meme = None
        self.next_meme = self.meme_generator(meme_list)
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
        button = QPushButton('NEXT')
        lay.addWidget(button)

        button.clicked.connect(self.on_button_clicked)
        button.show()
        self.show()

    @staticmethod
    def meme_generator(meme_list):
        for meme in meme_list:
            yield meme

    def on_button_clicked(self):
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
