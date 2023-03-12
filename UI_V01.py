# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pokemon_Info_UI_V01cRZniF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Pokemon_Info(object):
    def setupUi(self, Pokemon_Info):
        if not Pokemon_Info.objectName():
            Pokemon_Info.setObjectName(u"Pokemon_Info")
        Pokemon_Info.resize(967, 544)
        self.label_1 = QLabel(Pokemon_Info)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(20, 50, 341, 31))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setTextFormat(Qt.PlainText)
        self.label_1.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Pokemon_ComboBox = QComboBox(Pokemon_Info)
        self.Pokemon_ComboBox.addItem("")
        self.Pokemon_ComboBox.setObjectName(u"Pokemon_ComboBox")
        self.Pokemon_ComboBox.setGeometry(QRect(20, 100, 301, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        self.Pokemon_ComboBox.setFont(font1)
        self.Search_Button = QPushButton(Pokemon_Info)
        self.Search_Button.setObjectName(u"Search_Button")
        self.Search_Button.setEnabled(True)
        self.Search_Button.setGeometry(QRect(350, 300, 181, 41))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.Search_Button.setFont(font2)
        self.Download_Button = QPushButton(Pokemon_Info)
        self.Download_Button.setObjectName(u"Download_Button")
        self.Download_Button.setEnabled(False)
        self.Download_Button.setGeometry(QRect(350, 370, 181, 41))
        self.Download_Button.setFont(font2)
        self.Refresh_Button = QPushButton(Pokemon_Info)
        self.Refresh_Button.setObjectName(u"Refresh_Button")
        self.Refresh_Button.setEnabled(True)
        self.Refresh_Button.setGeometry(QRect(350, 440, 181, 41))
        self.Refresh_Button.setFont(font2)
        self.KeyIn_Text = QLineEdit(Pokemon_Info)
        self.KeyIn_Text.setObjectName(u"KeyIn_Text")
        self.KeyIn_Text.setGeometry(QRect(490, 100, 431, 41))
        self.KeyIn_Text.setFont(font1)
        self.KeyIn_Text.setEchoMode(QLineEdit.Password)
        self.label_6 = QLabel(Pokemon_Info)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 500, 411, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setWeight(75)
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_4 = QLabel(Pokemon_Info)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(730, 40, 211, 41))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_4.setFont(font4)
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.Info_TextEdit = QTextEdit(Pokemon_Info)
        self.Info_TextEdit.setObjectName(u"Info_TextEdit")
        self.Info_TextEdit.setGeometry(QRect(590, 220, 321, 271))
        self.Info_TextEdit.setFont(font1)
        self.Info_TextEdit.setReadOnly(True)
        self.label_2 = QLabel(Pokemon_Info)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(590, 180, 341, 31))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.KeyIn_Text_2 = QLineEdit(Pokemon_Info)
        self.KeyIn_Text_2.setObjectName(u"KeyIn_Text_2")
        self.KeyIn_Text_2.setGeometry(QRect(110, 170, 431, 41))
        self.KeyIn_Text_2.setFont(font1)
        self.KeyIn_Text_2.setEchoMode(QLineEdit.Normal)

        self.retranslateUi(Pokemon_Info)

        QMetaObject.connectSlotsByName(Pokemon_Info)
    # setupUi

    def retranslateUi(self, Pokemon_Info):
        Pokemon_Info.setWindowTitle(QCoreApplication.translate("Pokemon_Info", u"Pokemon_Info", None))
        self.label_1.setText(QCoreApplication.translate("Pokemon_Info", u"Pokemon Name: ", None))
        self.Pokemon_ComboBox.setItemText(0, QCoreApplication.translate("Pokemon_Info", u"Choose Pokemon", None))

        self.Pokemon_ComboBox.setCurrentText(QCoreApplication.translate("Pokemon_Info", u"Choose Pokemon", None))
        self.Search_Button.setText(QCoreApplication.translate("Pokemon_Info", u"Search", None))
        self.Download_Button.setText(QCoreApplication.translate("Pokemon_Info", u"Download", None))
        self.Refresh_Button.setText(QCoreApplication.translate("Pokemon_Info", u"Refresh Data", None))
        self.label_6.setText(QCoreApplication.translate("Pokemon_Info", u"Developed by WillyF", None))
        self.label_4.setText(QCoreApplication.translate("Pokemon_Info", u"Pokemon Type:", None))
        self.label_2.setText(QCoreApplication.translate("Pokemon_Info", u"Pokemon Info: ", None))
    # retranslateUi

