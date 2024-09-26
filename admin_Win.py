from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from queriWin import Mysql

class AdminWin(QWidget):
    def __init__(self,work_win):
        super().__init__()
        self.w_win = work_win
        self.resize(400,500)
        self.setStyleSheet("font-size:20px")

        self.v_main_lyt = QVBoxLayout()
        self.h_btn_lyt = QHBoxLayout()
        self.lts = QListWidget()

        self.country1_edit = QLineEdit()
        self.country1_edit.setPlaceholderText("Qayerdan...")
        self.country2_edit = QLineEdit()
        self.country2_edit.setPlaceholderText("Qayerga...")
        self.count_edit = QLineEdit()
        self.count_edit.setPlaceholderText("Bilet soni...")
        self.price_edit = QLineEdit()
        self.price_edit.setPlaceholderText("Narxi...")
        self.flighttime_edit = QLineEdit()
        self.flighttime_edit.setPlaceholderText("Uchish vaqti...")
        self.landingtime_edit = QLineEdit()
        self.landingtime_edit.setPlaceholderText("Qo'nish vaqti...")

        self.lts_edit = [self.country1_edit,
                         self.country2_edit,
                         self.count_edit,
                         self.price_edit,
                         self.flighttime_edit,
                         self.landingtime_edit]
        
        for i in self.lts_edit:
            self.lts_widg = QListWidgetItem()
            self.lts_widg.setSizeHint(QSize(370,40))
            self.lts.addItem(self.lts_widg)
            i.setFixedSize(360,40)
            self.lts.setItemWidget(self.lts_widg,i)

        self.submit_btn = QPushButton("Submit",clicked = self.submit)
        self.submit_btn.setFixedSize(100,40)
        self.submit_btn.setStyleSheet("background:skyblue")
        self.back_btn = QPushButton("Back",clicked = self.back)
        self.back_btn.setFixedSize(100,40)
        self.back_btn.setStyleSheet("background:skyblue")

        self.h_btn_lyt.addWidget(self.submit_btn)
        self.h_btn_lyt.addWidget(self.back_btn)

        self.v_main_lyt.addWidget(self.lts)
        self.v_main_lyt.addLayout(self.h_btn_lyt)
        self.setLayout(self.v_main_lyt)

    def submit(self):
        self.addData = Mysql()
        self.addData.insertTb(self.country1_edit.text(),
                         self.country2_edit.text(),
                         self.count_edit.text(),
                         self.price_edit.text(),
                         self.flighttime_edit.text(),
                         self.landingtime_edit.text())
        for i in self.lts_edit:
            i.clear()
    def back(self):
        self.hide()
        self.w_win.show()



