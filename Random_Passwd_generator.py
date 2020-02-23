import random as r
import string as s
import sys
from PyQt5.QtWidgets import *
def random_generate():
    l_password=[]
    len_passwd,dailog_box = QInputDialog.getInt(window,"Dailog","Enter the  length of the Password ")
    if len_passwd<=0:
        mbox_1 = QMessageBox()
        mbox_1.setText("Your Password Is")
        mbox_1.resize(150,150)
        mbox_1.move(250,200)
        mbox_1.setStyleSheet("background-color:#B34AFE;")
        mbox_1.setDetailedText("Invalid Length")
        mbox_1.exec()
    else:
        for i in range(len_passwd):
            l_password.append(r.choice(s.digits+s.ascii_letters))
        mbox = QMessageBox()
        mbox.setText("Your Password Is")
        mbox.resize(150,150)
        mbox.move(250,200)
        mbox.setStyleSheet("background-color:#B34AFE;")
        mbox.setDetailedText("".join(l_password))
        mbox.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= QWidget()
    window.resize(500,500)
    window.setWindowTitle('Password Generator')
    window.setStyleSheet("background-color:#B34AFE;")

    label=QLabel(window)
    label.setStyleSheet("color:black")
    label.setText('Click Here To Generate!')
    label.move(180,210)
    label.show()
		

    btn=QPushButton(window)
    btn.setText('Generate')
    btn.move(206,240)
    btn.show()
    btn.resize(100,35)
    btn.setStyleSheet("background-color:black;color:#FFFFFF")
    btn.clicked.connect(random_generate)

    window.show()
    sys.exit(app.exec_())




