from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from queriWin import Mysql

class UserWin(QWidget):
    def __init__(self,user_win):
        super().__init__()
        self.w_win = user_win
        self.resize(400,500)
        self.setStyleSheet("font-size:20px")

        self.country_uq = Mysql()
        self.countr_data = Mysql()

        self.v_main_lyt = QVBoxLayout()
        self.h_btn_lyt = QHBoxLayout()
        self.h_dan_lyt = QHBoxLayout()
        self.h_ga_lyt = QHBoxLayout()
        self.h_ncht_lyt = QHBoxLayout()
        self.ltsu = QListWidget()

        self.lbl_dan = QLabel("dan")
        self.lbl_dan.setStyleSheet("color:blue")
        self.lbl_ga = QLabel("ga")
        self.lbl_ga.setStyleSheet("color:blue")

        self.lbl_qld = QLabel()
        self.lbl_qld.setStyleSheet("font-size:16px")
        self.lbl_qld.setStyleSheet("color:blue")
        self.hide()

        self.cb_edit = QLineEdit()
        self.cb_edit.setPlaceholderText("Nechta bilet olishni xohlaysiz...")
        self.cb_edit.setFixedSize(100,30)

        self.cmb_dan = QComboBox()
        self.cmb_dan.addItems(self.country_uq.uch_dv())
        self.cmb_ga = QComboBox()
        self.cmb_ga.addItems(self.country_uq.qon_dv())
        self.cmb_ga.currentIndexChanged.connect(self.show_data)

        self.submit_btn = QPushButton("Buy",clicked = self.buy)
        self.submit_btn.setFixedSize(100,40)
        self.submit_btn.setStyleSheet("background:skyblue")
        self.back_btn = QPushButton("Back",clicked = self.back)
        self.back_btn.setFixedSize(100,40)
        self.back_btn.setStyleSheet("background:skyblue")

        self.h_btn_lyt.addWidget(self.submit_btn)
        self.h_btn_lyt.addWidget(self.back_btn)

        self.h_dan_lyt.addWidget(self.cmb_dan)
        self.h_dan_lyt.addWidget(self.lbl_dan)

        self.h_ga_lyt.addWidget(self.cmb_ga)
        self.h_ga_lyt.addWidget(self.lbl_ga)

        self.h_ncht_lyt.addWidget(self.cb_edit)
        self.h_ncht_lyt.addWidget(self.lbl_qld)

        self.v_main_lyt.addLayout(self.h_dan_lyt)
        self.v_main_lyt.addLayout(self.h_ga_lyt)
       
        self.v_main_lyt.addWidget(self.ltsu)
        self.v_main_lyt.addLayout(self.h_ncht_lyt)
        self.v_main_lyt.addLayout(self.h_btn_lyt)

        self.setLayout(self.v_main_lyt)
    def show_data(self):
        self.lbl_qld.clear()
        self.cb_edit.clear()
        self.ltsu.clear()
        self.temps = self.countr_data.celect_data(self.cmb_dan.currentText(),self.cmb_ga.currentText())
        for i in self.temps:
            self.ltsu.addItem(f"Soni: {i[0]}\nNarxi: {i[1]}\nUchish vaqti: {i[2]}\nQo'nish vaqti: {i[3]}")

    def buy(self):
        
        self.qolgan_b = self.countr_data.buy_select(self.cb_edit.text(),self.cmb_dan.currentText(),self.cmb_ga.currentText())
        self.lbl_qld.show()
        self.son = self.countr_data.soni()
        if self.son < int(self.cb_edit.text()):
            self.cb_edit.clear()
            self.lbl_qld.setStyleSheet("color:red")
            self.lbl_qld.setText(f"Bu yo'nalishda faqat\n{self.qolgan_b} ta bilet qolgan")
        elif self.qolgan_b:
            self.lbl_qld.setStyleSheet("color:blue")
            self.ltsu.clear()
            self.ltstime= []
            for i in self.countr_data.times_data(self.cmb_dan.currentText(),self.cmb_ga.currentText()):
                self.ltstime.append(i[0])
                self.ltstime.append(i[1])
            self.ltsu.addItem(f"""{self.cmb_dan.currentText()} -> {self.cmb_ga.currentText()} Yo'nalishida 
{self.cb_edit.text()} ta bilet sotib oldingiz
Uchish vaqti {self.ltstime[0]}
Qo'nish vaqti {self.ltstime[1]}""")
            self.lbl_qld.setText(f"{self.cmb_dan.currentText()} -> {self.cmb_ga.currentText()}\nYo'nalishida  {self.qolgan_b} ta bilet qoldi")
    def back(self):
        self.hide()
        self.w_win.show()