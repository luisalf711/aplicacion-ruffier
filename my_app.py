from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QPushButton, QVBoxLayout)
from instr import *
from second_win import * # TestWindow

class MainWindow(QWidget):
    def __init__(self, title=TXT_TITLE):
        self.title = title
        super().__init__()

    def setui(self)
        self.welcome_label = Qlabel(TXT_HELLO)
        self.instructions_label = QLabel(TXT_INSTRUCTION)
        self.btn_next = QPushButton(TXT_NEXT, self)
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.welcome_label, aligment=Qt.alignleft)
        self.main_layout.addWidget(self.instructions_label, aligment=Qt.alignleft)
        self.main_layout.addWidget(self.btn_next, aligment=Qt.aligncenter)
        self.setLayout(self.main_layout)
