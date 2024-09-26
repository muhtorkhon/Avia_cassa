from PyQt5.QtWidgets import *
from work_windov import WorkingWin

app = QApplication([])
win = WorkingWin()
win.show()
app.exec_()