import sys
import os
import subprocess
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QGroupBox, QPlainTextEdit, QToolButton, QFrame, QDesktopWidget, 
                             QCheckBox, QMessageBox, QFileDialog, QComboBox, QLineEdit)
from PyQt5.QtCore import Qt, QPoint, QRect, QDateTime, QTimer, QDate, QProcess
from PyQt5.QtGui import QFont, QCursor, QIntValidator
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(779, 485)
        Form.setStyleSheet("background-color: rgb(230, 0, 35);")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.btnMinimize = QtWidgets.QPushButton(Form)
        self.btnMinimize.setGeometry(QtCore.QRect(710, 20, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(12)
        font.setWeight(50)
        
        self.btnLogs = QtWidgets.QPushButton(Form)
        self.btnLogs.setGeometry(630, 20, 21, 21)
        self.btnLogs.setFont(font)
        self.btnLogs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogs.setStyleSheet("color: rgb(255, 255, 255); font: 12pt 'MS PGothic'; background-color: rgb(230, 0, 35);")
        self.btnLogs.clicked.connect(self.showLogs)

        self.btnInfo = QtWidgets.QPushButton(Form)
        self.btnInfo.setGeometry(670, 20, 21, 21)
        self.btnInfo.setFont(font)
        self.btnInfo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnInfo.setStyleSheet("color: rgb(255, 255, 255); font: 12pt 'MS PGothic'; background-color: rgb(230, 0, 35);")
        self.btnInfo.clicked.connect(self.showInfo)

        self.btnMinimize.setFont(font)
        self.btnMinimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMinimize.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(230, 0, 35);\n"
                                       "font: 12pt \"MS PGothic\";")
        self.btnMinimize.setObjectName("btnMinimize")
        self.btnMinimize.clicked.connect(self.showMinimized)

        self.btnClose = QtWidgets.QPushButton(Form)
        self.btnClose.setGeometry(QtCore.QRect(750, 20, 21, 21))
        self.btnClose.setFont(font)
        self.btnClose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClose.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(230, 0, 35);\n"
                                    "font: 12pt \"MS PGothic\";")
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.confirmClose)

        self.lbTitle = QtWidgets.QLabel(Form)
        self.lbTitle.setGeometry(QtCore.QRect(10, 0, 291, 61))
        self.lbTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbTitle.setStyleSheet("font: 18pt \"Khmer OS Muol Light\"; color: rgb(255, 255, 255);")
        self.lbTitle.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbTitle.setObjectName("lbTitle")

        self.gbMain = QtWidgets.QGroupBox(Form)
        self.gbMain.setGeometry(QtCore.QRect(10, 60, 761, 381))
        font.setPointSize(10)
        self.gbMain.setFont(font)
        self.gbMain.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gbMain.setStyleSheet("color: rgb(255, 255, 255);")
        self.gbMain.setTitle("")
        self.gbMain.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gbMain.setObjectName("gbMain")

        self.lbKeyDown = QtWidgets.QLabel(self.gbMain)
        self.lbKeyDown.setGeometry(QtCore.QRect(10, 10, 181, 20))
        font.setPointSize(10)
        self.lbKeyDown.setFont(font)
        self.lbKeyDown.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbKeyDown.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbKeyDown.setObjectName("lbKeyDown")

        self.txtLinkKeywordDownload = QtWidgets.QPlainTextEdit(self.gbMain)
        self.txtLinkKeywordDownload.setGeometry(QtCore.QRect(10, 30, 741, 181))
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.txtLinkKeywordDownload.setFont(font)
        self.txtLinkKeywordDownload.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txtLinkKeywordDownload.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "color: rgb(0, 0, 0);")
        self.txtLinkKeywordDownload.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.txtLinkKeywordDownload.setObjectName("txtLinkKeywordDownload")
        self.txtLinkKeywordDownload.setPlaceholderText("Ex. https://www.pinterest.com/pin/1900024837771047/")

        self.gbDownload = QtWidgets.QGroupBox(self.gbMain)
        self.gbDownload.setGeometry(QtCore.QRect(10, 220, 741, 151))
        font.setPointSize(10)
        self.gbDownload.setFont(font)
        self.gbDownload.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gbDownload.setStyleSheet("color: rgb(255, 255, 255);")
        self.gbDownload.setTitle("Option | Phekdey | V.1")
        self.gbDownload.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gbDownload.setObjectName("gbDownload")

        self.lbPath = QtWidgets.QLabel(self.gbDownload)
        self.lbPath.setGeometry(QtCore.QRect(10, 20, 61, 31))
        self.lbPath.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbPath.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbPath.setObjectName("lbPath")

        self.txtPathSave = QtWidgets.QPlainTextEdit(self.gbDownload)
        self.txtPathSave.setGeometry(QtCore.QRect(80, 21, 481, 71))
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.txtPathSave.setFont(font)
        self.txtPathSave.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txtPathSave.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.txtPathSave.setObjectName("txtPathSave")
        self.txtPathSave.textChanged.connect(self.check_path)

        self.btnBrowsePath = QtWidgets.QToolButton(self.gbDownload)
        self.btnBrowsePath.setGeometry(QtCore.QRect(10, 50, 61, 31))
        self.btnBrowsePath.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBrowsePath.setObjectName("btnBrowsePath")
        self.btnBrowsePath.clicked.connect(self.browse_directory)

        self.lineSave = QtWidgets.QFrame(self.gbDownload)
        self.lineSave.setGeometry(QtCore.QRect(80, 90, 651, 20))
        self.lineSave.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSave.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSave.setObjectName("lineSave")

        self.btnDownload = QtWidgets.QToolButton(self.gbDownload)
        self.btnDownload.setGeometry(QtCore.QRect(630, 110, 101, 31))
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btnDownload.setFont(font)
        self.btnDownload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDownload.setStyleSheet("color: rgb(255, 255, 255);")
        self.btnDownload.setObjectName("btnDownload")

        self.btnStop = QtWidgets.QToolButton(self.gbDownload)
        self.btnStop.setGeometry(QtCore.QRect(520, 110, 101, 31))
        self.btnStop.setFont(font)
        self.btnStop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStop.setStyleSheet("color: rgb(255, 255, 0);")
        self.btnStop.setObjectName("btnStop")

        self.btnClear = QtWidgets.QToolButton(self.gbDownload)
        self.btnClear.setGeometry(QtCore.QRect(80, 110, 101, 31))
        self.btnClear.setFont(font)
        self.btnClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClear.setStyleSheet("color: rgb(170, 255, 0);")
        self.btnClear.setObjectName("btnClear")
        self.btnClear.clicked.connect(self.clear_code)

        self.lbAmount = QtWidgets.QLabel(self.gbDownload)
        self.lbAmount.setGeometry(QtCore.QRect(590, 20, 61, 31))
        self.lbAmount.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbAmount.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbAmount.setObjectName("lbAmount")

        self.txtAmountNum = QLineEdit(self.gbDownload)
        self.txtAmountNum.setGeometry(650, 20, 81, 31)
        self.txtAmountNum.setFont(QFont("Roboto", 9))
        self.txtAmountNum.setCursor(Qt.IBeamCursor)
        self.txtAmountNum.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.txtAmountNum.setValidator(QIntValidator(0, 9999, self.txtAmountNum))
        self.txtAmountNum.textChanged.connect(self.validate_amount)

        self.lbDelay = QtWidgets.QLabel(self.gbDownload)
        self.lbDelay.setGeometry(QtCore.QRect(590, 60, 61, 31))
        self.lbDelay.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbDelay.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbDelay.setObjectName("lbDelay")

        self.txtDelayNum = QtWidgets.QComboBox(self.gbDownload)
        self.txtDelayNum.setGeometry(QtCore.QRect(650, 60, 81, 31))
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.txtDelayNum.setFont(font)
        self.txtDelayNum.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.txtDelayNum.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(0, 0, 0);")
        self.txtDelayNum.setObjectName("txtDelayNum")
        self.txtDelayNum.addItems(["5", "10", "15", "20", "25", "30"])
        self.txtDelayNum.setCurrentIndex(2)

        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 450, 761, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.oldPos = self.pos()
        self.process = None

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnLogs.setText(_translate("Form", "O"))
        self.btnInfo.setText(_translate("Form", "?"))
        self.btnMinimize.setText(_translate("Form", "-"))
        self.btnClose.setText(_translate("Form", "X"))
        self.lbTitle.setText(_translate("Form", "កម្មវិធីទាញយក Pinterest"))
        self.lbKeyDown.setText(_translate("Form", "Link Download"))
        self.gbDownload.setTitle(_translate("Form", " Option | Phekdey | V.3 "))
        self.lbPath.setText(_translate("Form", "Path Save:"))
        self.btnBrowsePath.setText(_translate("Form", "..."))
        self.btnDownload.setText(_translate("Form", "Download"))
        self.btnStop.setText(_translate("Form", "Stop"))
        self.btnClear.setText(_translate("Form", "Clear"))
        self.lbAmount.setText(_translate("Form", "Amount:"))
        self.lbDelay.setText(_translate("Form", "Delay:"))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def confirmClose(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setIcon(QtWidgets.QMessageBox.Question)
        message_box.setWindowTitle('បញ្ជាក់ការបិទ')
        message_box.setText('តើអ្នកពិតជាចង់បិទចោលកម្មវិធីមែនឬទេ?')

        yes_button = message_box.addButton('យល់ព្រម', QtWidgets.QMessageBox.YesRole)
        yes_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        no_button = message_box.addButton('បដិសេដ', QtWidgets.QMessageBox.NoRole)
        no_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        message_box.setDefaultButton(no_button)

        reply = message_box.exec_()

        if message_box.clickedButton() == yes_button:
            QtCore.QCoreApplication.instance().quit()

    def showMinimized(seft):
        seft.showMinimized()

    def showInfo(self):
        info_text = """
        <html>
            <body style='font-size: 10pt; color: white; background-color: gray;'>
                <h1>Owner Info</h1>
                <hr>
                <p>កម្មវិធីឈ្មោះ: Pinterest Downloader</p>
                <p>សរសេរដោយ: Phekdey PHORN | ផន ភក្ដី</p>
                <p>ទំនាក់ទំនង: 089 755 770</p>
                <p>ភាសាកូដៈ Python</p>
                <p>បង្កើតថ្ងៃៈ 12-June-2024</p>
                <p>បច្ចុប្បន្នភាពចុងក្រោយៈ 07-Auguest-2024</p>
                <p>ការប្រើប្រាស់ៈ Free</p>
                <p>កំណែទម្រង់ៈ 3.0</p>
                <br>
                <h1>User Info</h1>
                <hr>
                <p>Machine ID: {current}</p>
                <p>License Key: {current}</p>
                <p>Create Key: {current}</p>
                <p>Expiry Key: {current}</p>
            </body>
        </html>
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Info")
        msg_box.setText(info_text)
        msg_box.setStyleSheet("QLabel{min-width: 600px;}")
        return_button = msg_box.addButton("ត្រលប់", QMessageBox.AcceptRole)
        return_button.setStyleSheet("color: white;")
        return_button.setCursor(Qt.PointingHandCursor)
        msg_box.exec_()
        return_button.clicked.connect(msg_box.close)


    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "ជ្រើសរើសទីតាំង")
        if directory:
            self.txtPathSave.setPlainText(directory)
    

    def check_path(self):
        path = self.txtPathSave.toPlainText().strip()
        if path and not os.path.isdir(path):
            warning_box = QMessageBox(self)
            warning_box.setWindowTitle('ទីតាំងមិនត្រឹមត្រូវ')
            warning_box.setText('សូមជ្រើសរើសទីតាំងដែលមានសុពលភាព ឬ ត្រឹមត្រូវ !')
            warning_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            warning_box.setStandardButtons(QMessageBox.Ok)
            warning_box.button(QMessageBox.Ok).setText('យល់ព្រម')
            warning_box.button(QMessageBox.Ok).setCursor(Qt.PointingHandCursor)
            warning_box.exec_()
            self.txtPathSave.clear()

    def validate_amount(self):
        text = self.txtAmountNum.text()
        if text and not text.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
            self.txtAmountNum.clear()

    def clear_code(self):
        linkKeywordDownload = self.txtLinkKeywordDownload.toPlainText().strip()
        pathSave = self.txtPathSave.toPlainText().strip()
        amountNum = self.txtAmountNum.text().strip()
        
        if not linkKeywordDownload and not pathSave and not amountNum:
            warning_box = QMessageBox(self)
            warning_box.setWindowTitle('ការព្រមាន')
            warning_box.setText('មិនមានទិន្នន័យទេ!')
            warning_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            warning_box.setStandardButtons(QMessageBox.Ok)
            warning_box.button(QMessageBox.Ok).setText('យល់ព្រម')
            warning_box.button(QMessageBox.Ok).setCursor(Qt.PointingHandCursor)
            warning_box.exec_()
        elif linkKeywordDownload or pathSave or amountNum:
            confirmation_box = QMessageBox(self)
            confirmation_box.setWindowTitle('បញ្ជាក់ការសម្អាត')
            confirmation_box.setText('តើអ្នកពិតជាចង់សម្អាតទម្រង់វាចោលមែនទេ?')
            confirmation_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirmation_box.button(QMessageBox.Yes).setText('យល់ព្រម')
            confirmation_box.button(QMessageBox.Yes).setCursor(Qt.PointingHandCursor)
            confirmation_box.button(QMessageBox.No).setText('បដិសេដ')
            confirmation_box.button(QMessageBox.No).setCursor(Qt.PointingHandCursor)
            
            reply = confirmation_box.exec_()
            if reply == QMessageBox.Yes:
                self.txtLinkKeywordDownload.clear()
                self.txtPathSave.clear()
                self.txtAmountNum.clear()
                self.txtDelayNum.setCurrentIndex(1)

    def showLogs(self):
        confirmation_box = QMessageBox(self)
        confirmation_box.setWindowTitle('បញ្ជាក់ការបើកមើល log')
        confirmation_box.setText('តើអ្នកពិតជាចង់មើល log មែនទេ?')
        confirmation_box.setStyleSheet("""
            QLabel { color: white; }
            QPushButton { color: white; background-color: rgb(50, 50, 50); }
        """)
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmation_box.button(QMessageBox.Yes).setText('យល់ព្រម')
        confirmation_box.button(QMessageBox.Yes).setCursor(Qt.PointingHandCursor)
        confirmation_box.button(QMessageBox.No).setText('បដិសេដ')
        confirmation_box.button(QMessageBox.No).setCursor(Qt.PointingHandCursor)
        reply = confirmation_box.exec_()

        if reply == QMessageBox.Yes:
            log_dir = r"C:\Tools Data\Pinterest DL Logs"
            if os.path.exists(log_dir):
                try:
                    # Open the directory in file explorer
                    if os.name == 'nt':  # For Windows
                        os.startfile(log_dir)
                    elif os.name == 'posix':  # For Unix-like OS
                        subprocess.call(['xdg-open', log_dir])
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Unable to open log directory: {e}")
            else:
                QMessageBox.warning(self, "Path Not Found", "Log directory does not exist.")









class CustomForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = CustomForm()
    form.show()
    sys.exit(app.exec_())

