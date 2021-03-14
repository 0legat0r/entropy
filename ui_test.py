# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testptNwhD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(809, 526)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.uploadNetwork = QPushButton(self.centralwidget)
        self.uploadNetwork.setObjectName(u"uploadNetwork")
        self.uploadNetwork.setGeometry(QRect(10, 130, 221, 41))
        self.formatNet = QListWidget(self.centralwidget)
        QListWidgetItem(self.formatNet)
        QListWidgetItem(self.formatNet)
        self.formatNet.setObjectName(u"formatNet")
        self.formatNet.setGeometry(QRect(10, 10, 221, 111))
        self.fileName = QLineEdit(self.centralwidget)
        self.fileName.setObjectName(u"fileName")
        self.fileName.setGeometry(QRect(10, 180, 211, 22))
        self.fileName.setReadOnly(True)
        self.visualNetwork = QPushButton(self.centralwidget)
        self.visualNetwork.setObjectName(u"visualNetwork")
        self.visualNetwork.setEnabled(False)
        self.visualNetwork.setGeometry(QRect(10, 410, 161, 28))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 10, 121, 81))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 110, 131, 101))
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.infoNetwork = QTextBrowser(self.centralwidget)
        self.infoNetwork.setObjectName(u"infoNetwork")
        self.infoNetwork.setGeometry(QRect(10, 210, 231, 181))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(480, 30, 241, 51))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(480, 140, 211, 41))
        self.label_4.setFont(font1)
        self.entropy_shortest = QTextBrowser(self.centralwidget)
        self.entropy_shortest.setObjectName(u"entropy_shortest")
        self.entropy_shortest.setGeometry(QRect(280, 230, 241, 191))
        self.entropy_closed = QTextBrowser(self.centralwidget)
        self.entropy_closed.setObjectName(u"entropy_closed")
        self.entropy_closed.setGeometry(QRect(530, 230, 256, 192))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 809, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.formatNet.setCurrentRow(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.uploadNetwork.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b", None))

        __sortingEnabled = self.formatNet.isSortingEnabled()
        self.formatNet.setSortingEnabled(False)
        ___qlistwidgetitem = self.formatNet.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442 SIF (.sif)", None));
        ___qlistwidgetitem1 = self.formatNet.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0435\u0431\u0435\u0440  (.txt)", None));
        self.formatNet.setSortingEnabled(__sortingEnabled)

        self.fileName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u0441\u0435\u0442\u0438 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 SIF", None))
        self.visualNetwork.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0441\u0435\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043d\u0442\u0440\u043e\u043f\u0438\u044f \u0441 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435\u043c \u043a\u0440\u0430\u0442\u0447\u0430\u0439\u0448\u0438\u0445 \u043f\u0443\u0442\u0435\u0439", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043d\u0442\u0440\u043e\u043f\u0438\u044f \u0441 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435\u043c \u0437\u0430\u043c\u043a\u043d\u0443\u0442\u044b\u0445 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432", None))
        self.infoNetwork.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u0435\u0442\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ENTROPY_1.png", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ENTROPY_2.png", None))
    # retranslateUi

