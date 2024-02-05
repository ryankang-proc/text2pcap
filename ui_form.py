# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1001, 599)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inputlabel = QLabel(Widget)
        self.inputlabel.setObjectName(u"inputlabel")

        self.verticalLayout.addWidget(self.inputlabel)

        self.plainTextEdit = QPlainTextEdit(Widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formatButton = QPushButton(Widget)
        self.formatButton.setObjectName(u"formatButton")

        self.horizontalLayout_2.addWidget(self.formatButton)

        self.commitButton = QPushButton(Widget)
        self.commitButton.setObjectName(u"commitButton")

        self.horizontalLayout_2.addWidget(self.commitButton)

        self.clearButton = QPushButton(Widget)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout_2.addWidget(self.clearButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pcapfilepath = QLabel(Widget)
        self.pcapfilepath.setObjectName(u"pcapfilepath")

        self.horizontalLayout.addWidget(self.pcapfilepath)

        self.textBrowser = QTextBrowser(Widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.openButton = QPushButton(Widget)
        self.openButton.setObjectName(u"openButton")
        self.openButton.setIconSize(QSize(10, 10))
#if QT_CONFIG(shortcut)
        self.openButton.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.openButton.setAutoRepeatDelay(100)

        self.verticalLayout_2.addWidget(self.openButton)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"text2pcap", None))
        self.inputlabel.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">\u8f93\u5165\u6587\u672c</p></body></html>", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"\u8bf7\u8f93\u5165\u6587\u672c", None))
        self.formatButton.setText(QCoreApplication.translate("Widget", u"\u683c\u5f0f\u5316\u6587\u672c", None))
        self.commitButton.setText(QCoreApplication.translate("Widget", u"\u751f\u6210pcap", None))
        self.clearButton.setText(QCoreApplication.translate("Widget", u"\u6e05\u9664\u6587\u672c", None))
        self.pcapfilepath.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u683c\u5f0f\u5316\u6587\u672c: </span></p></body></html>", None))
        self.openButton.setText(QCoreApplication.translate("Widget", u"\u6253\u5f00pcap\u6587\u4ef6", None))
    # retranslateUi

