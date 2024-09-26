from PyQt5.QtWidgets import *
from admin_Win import AdminWin
from user_Win import UserWin

class WorkingWin(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,500)
        self.setStyleSheet("font-size:20px")

        self.v_main_lyt = QVBoxLayout()
        self.h_plic_lyt = QHBoxLayout()

        self.admin_btn = QPushButton("Admin",clicked = self.admin)
        self.admin_btn.setFixedSize(140,50)
        self.user_btn = QPushButton("User",clicked = self.user)
        self.user_btn.setFixedSize(140,50)
        self.exit_btn = QPushButton("Exit",clicked = exit)
        self.exit_btn.setFixedSize(140,50)

        self.v_main_lyt.addWidget(self.admin_btn)
        self.v_main_lyt.addWidget(self.user_btn)
        self.v_main_lyt.addWidget(self.exit_btn)
        self.h_plic_lyt.addStretch()
        self.h_plic_lyt.addLayout(self.v_main_lyt)
        self.h_plic_lyt.addStretch()
        self.setLayout(self.h_plic_lyt)

    def admin(self):
        self.admin_w = AdminWin(self)
        self.admin_w.show()
        self.hide()
    def user(self):
        self.user_w = UserWin(self)
        self.user_w.show()
        self.hide()
        
    
