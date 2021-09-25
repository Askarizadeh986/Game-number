import os
import random as r
import sqlite3
from datetime import datetime, timedelta
from pandas import DataFrame
import pandas as pd
from io import StringIO
from PyQt5 import QtCore, QtGui, QtWidgets
from turtle import *


os.system('cls' or 'clear')
starttime_str = str(datetime.today()).replace("-", ":")
arr = starttime_str.split(':')
starttime = datetime(int(arr[0]), int(arr[1]), int(arr[2].split(' ')[0]), int(arr[2].split(' ')[1]), int(arr[3]), int(float(arr[4])))
datecom=str(starttime)
chancee_input=int(input('Enter your level (1/2/3)\t'))
if chancee_input==1:
    chancee=7
    x=10
    y=99
elif chancee_input==2:
    chancee=7
    x=10
    y=500
elif chancee_input==3:
    chancee=7
    x=10
    y=1000
else:
    print("error")
    input("prees key to exit\t")
    exit()
num=r.randint(x, y)


class Ui_Game_Number(object):
    def setupUi(self, Game_Number):
        Game_Number.setObjectName("Game_Number")
        Game_Number.resize(720, 513)
        Game_Number.setMinimumSize(QtCore.QSize(720, 513))
        Game_Number.setMaximumSize(QtCore.QSize(720, 513))
        font = QtGui.QFont()
        font.setFamily("B Kamran")
        font.setPointSize(15)
        Game_Number.setFont(font)
        Game_Number.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.centralwidget = QtWidgets.QWidget(Game_Number)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 261, 51))
        font = QtGui.QFont()
        font.setFamily("B Kamran")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 50, 661, 461))
        self.tabWidget.setMinimumSize(QtCore.QSize(661, 461))
        self.tabWidget.setMaximumSize(QtCore.QSize(661, 461))
        font = QtGui.QFont()
        font.setFamily("B Kamran")
        font.setPointSize(30)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.261364 rgba(230, 255, 0, 255), stop:0.443182 rgba(0, 234, 255, 255), stop:0.8125 rgba(21, 0, 255, 255), stop:1 rgba(0, 0, 0, 255));")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Select = QtWidgets.QPushButton(self.tab)
        self.Select.setGeometry(QtCore.QRect(340, 10, 131, 61))
        font = QtGui.QFont()
        font.setFamily("B Kamran")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Select.setFont(font)
        self.Select.setStyleSheet("\n"
"background-color: rgb(0, 255, 255);\n"
"font: 15pt \"B Kamran\";")
        self.Select.setObjectName("Select")
        self.Status = QtWidgets.QTextBrowser(self.tab)
        self.Status.setGeometry(QtCore.QRect(0, 100, 641, 170))
        font = QtGui.QFont()
        font.setFamily("B Kamran")
        font.setPointSize(15)
        self.Status.setFont(font)
        self.Status.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.Status.setObjectName("Status")
        self.Number = QtWidgets.QTextEdit(self.tab)
        self.Number.setGeometry(QtCore.QRect(510, 10, 104, 71))
        font = QtGui.QFont()
        font.setFamily("B Kamran")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Number.setFont(font)
        self.Number.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"B Kamran\";")
        self.Number.setObjectName("Number")
        self.exitb = QtWidgets.QPushButton(self.tab)
        self.exitb.setGeometry(QtCore.QRect(40, 20, 121, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitb.sizePolicy().hasHeightForWidth())
        self.exitb.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.exitb.setFont(font)
        self.exitb.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.exitb.setObjectName("exitb")
        self.Player = QtWidgets.QTextEdit(self.tab)
        self.Player.setGeometry(QtCore.QRect(210, 10, 104, 71))
        font = QtGui.QFont()
        font.setFamily("B Kamran")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Player.setFont(font)
        self.Player.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"B Kamran\";")
        self.Player.setObjectName("Player")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 90, 641, 231))
        font = QtGui.QFont()
        font.setFamily("B Kamran")
        font.setPointSize(20)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(234, 255, 0);")
        self.textBrowser.setPlaceholderText("")
        self.textBrowser.setObjectName("textBrowser")
        self.ShowHistory = QtWidgets.QPushButton(self.tab_2)
        self.ShowHistory.setGeometry(QtCore.QRect(390, 50, 201, 41))
        font = QtGui.QFont()
        font.setFamily("B Kamran")
        font.setPointSize(20)
        self.ShowHistory.setFont(font)
        self.ShowHistory.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.ShowHistory.setObjectName("ShowHistory")
        self.tabWidget.addTab(self.tab_2, "")
        Game_Number.setCentralWidget(self.centralwidget)
        self.Status.append(' شما '+str(chancee)+' شانس دارید ')
        self.Select.clicked.connect(self.gamenumber)
        self.retranslateUi(Game_Number)
        self.exitb.hide()
        self.exitb.clicked.connect(Game_Number.close)
        self.ShowHistory.clicked.connect(self.ShowPoans)
        self.retranslateUi(Game_Number)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Game_Number)

    def retranslateUi(self, Game_Number):
        _translate = QtCore.QCoreApplication.translate
        Game_Number.setWindowTitle(_translate("Game_Number", "حدس عدد"))
        self.label.setText(_translate("Game_Number", "از عدد "+str(x)+"تا "+str(y)+" یک عددحدس بزنید "))
        self.Select.setText(_translate("Game_Number", "وارد کردن عدد"))
        self.Number.setPlaceholderText(_translate("Game_Number", "عدد را وارد کنید"))
        self.exitb.setText(_translate("Game_Number", "Exit"))
        self.Player.setPlaceholderText(_translate("Game_Number", "بازیکن را وارد کنید"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Game_Number", "بازی"))
        self.textBrowser.setHtml(_translate("Game_Number", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'B Kamran\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ShowHistory.setText(_translate("Game_Number", "نشان دادن تاریخچه ی امتیاز"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Game_Number", "تاریخچه"))

    def gamenumber(self):
        try:
                global chancee
                mynumber=int(self.Number.toPlainText())
                if chancee==0:
                    self.Select.setEnabled(False)
                    self.Number.setEnabled(False)
                    self.Status.append("باختی عدد:\t"+str(num)+'\n امتیاز شما : 0')
                    Game_Number.setStyleSheet("background-color: rgb(255, 0, 4);")
                    self.exitb.show()
                    self.database()
                if mynumber==num:
                    self.Status.clear()
                    self.database()
                    self.Status.append("آفرین صد آفرین هزار و سیصد آفرین یواش برو نخوری زمین"+"\n"+"امتياز شما:"+str(chancee+1))
                    self.Select.setEnabled(False)
                    Game_Number.setStyleSheet('background-color: rgb(0, 255, 0);')
                    speed=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000**10
                    colors=['red','blue','green','orange']
                    for i in range(400):
                        pencolor(colors[i % 4])
                        forward(i)
                        left(91)

                    self.exitb.show()
                elif mynumber<num:
                    chancee-=1
                    self.Status.append("عددی که من ( کامپیوتر ) ذهنمه از این بزرگتره\t\t شما "+str(chancee)+" شانس دارید ")
                    if chancee==0:
                        self.Select.setEnabled(False)
                        self.Number.setEnabled(False)
                        self.Status.append("باختی عدد:\t"+str(num)+'\n امتیاز شما : 0')
                        Game_Number.setStyleSheet("background-color: rgb(255, 0, 4);")
                        self.exitb.show()
                        self.database()
                elif mynumber>num:
                    chancee-=1
                    self.Status.append("عددی که من ( کامپیوتر ) ذهنمه از این کوچکتره\t\t شما "+str(chancee)+" شانس دارید ")
                    if chancee==0:
                        self.Select.setEnabled(False)
                        self.Number.setEnabled(False)
                        self.Status.append("باختی، عدد:\t"+str(num)+'\n امتیاز شما : 0')
                        Game_Number.setStyleSheet("background-color: rgb(255, 0, 4);")
                        self.exitb.show()
                        self.database()

                        

        except ValueError:
                self.Status.append('Error')
    def ShowPoans(self):
        conn=sqlite3.connect("Trainig.db")
        c=conn.cursor()
        self.textBrowser.append("امتیاز  عدد \t\t زمان \t بازیکن")
        for row in c.execute("SELECT * FROM apptable;"):
                self.textBrowser.append(str(row).strip("(").strip(")"))
        self.textBrowser.append("\n")

    def database(self):
        playergame=str(self.Player.toPlainText())
        poann=chancee+chancee_input
        if chancee==0:
                poann=0
        conn=sqlite3.connect("Trainig.db")
        c=conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS apptable(player string,'+'datetime string,'+'Numbercomputer interger,'+'poan integer)')
        conn.commit()
        c.execute("INSERT INTO apptable(player,Numbercomputer, poan, datetime) VALUES(""\'%s\',\'%s\', \'%s\', \'%s\');" % (playergame,num,poann,datecom))
        conn.commit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Game_Number = QtWidgets.QMainWindow()
    ui = Ui_Game_Number()
    ui.setupUi(Game_Number)
    Game_Number.show()
    sys.exit(app.exec_())
