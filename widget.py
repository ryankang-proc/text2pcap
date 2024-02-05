# This Python file uses the following encoding: utf-8
import sys, time, struct, re, os

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Pcap:
    def __init__(self, filename, ethtype = 1):
        self.pcapfile = open(filename, "wb")
        self.pcapfile.write(struct.pack('@ I H H i I I I', 0xa1b2c3d4, 2, 4, 0, 0, 65535, ethtype))

    def write(self, data):
        ts_sec, ts_usec = map(int, str(time.time()).split('.'))
        datalen = len(data)
        self.pcapfile.write(struct.pack('@ I I I I', ts_sec, ts_usec, datalen, datalen))
        self.pcapfile.write(data)

    def close(self):
        self.pcapfile.close()

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.formatButton.clicked.connect(self.formatText)
        self.ui.commitButton.clicked.connect(self.text2pcap)
        self.ui.clearButton.clicked.connect(self.clearText)
        self.ui.openButton.clicked.connect(self.opencmd)

    def clearText(self):
        self.ui.plainTextEdit.clear()
        self.ui.textBrowser.clear()
    def formatText(self, Qstring=None):
        textinfo = self.ui.plainTextEdit.toPlainText()
        if (len(textinfo) == 0):
            QMessageBox.information(None, "通知", "文本输入为空!")
            return

        count = textinfo.count(' ')
        if count == 0:
            for line in textinfo.splitlines(','):
                pattern = re.compile('.{2}')
                s = ' '.join(pattern.findall(line))
                self.ui.textBrowser.append(s)
        else:
            self.ui.textBrowser.append(textinfo.replace("\n", " "))

        QMessageBox.information(None, "通知", "格式文本成功!")

    def text2pcap(self):
        formattedText = self.ui.textBrowser.toPlainText()
        if (len(formattedText) == 0):
            QMessageBox.information(None, "通知", "文本输入为空!")
            return
        self.pcapfile = Pcap("output.pcap")
        for line in formattedText.splitlines():
            textbytearr = bytearray()
            splitstr = line.split()
            for si in splitstr:
                print(si)
                strint = int(si, 16)
                textbytearr.append(strint)
            self.pcapfile.write(textbytearr)
        self.pcapfile.close()
        QMessageBox.information(None, "通知", "生成文件output.pcap!")

    def opencmd(self):
        os.startfile(r".\output.pcap")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

