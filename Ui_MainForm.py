# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designersqcOGZ.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(330, 227)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_send = QLineEdit(self.centralwidget)
        self.le_send.setObjectName(u"le_send")

        self.gridLayout.addWidget(self.le_send, 0, 0, 1, 1)

        self.pb_send = QPushButton(self.centralwidget)
        self.pb_send.setObjectName(u"pb_send")

        self.gridLayout.addWidget(self.pb_send, 0, 1, 1, 1)

        self.pb_test_messagebox = QPushButton(self.centralwidget)
        self.pb_test_messagebox.setObjectName(u"pb_test_messagebox")

        self.gridLayout.addWidget(self.pb_test_messagebox, 1, 0, 1, 2)

        self.pb_open_new_form = QPushButton(self.centralwidget)
        self.pb_open_new_form.setObjectName(u"pb_open_new_form")

        self.gridLayout.addWidget(self.pb_open_new_form, 2, 0, 1, 2)

        self.pb_quit = QPushButton(self.centralwidget)
        self.pb_quit.setObjectName(u"pb_quit")

        self.gridLayout.addWidget(self.pb_quit, 3, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test PySide6", None))
        self.pb_send.setText(QCoreApplication.translate("MainWindow", u"Test statusbar", None))
        self.pb_test_messagebox.setText(QCoreApplication.translate("MainWindow", u"Test messagebox", None))
        self.pb_open_new_form.setText(QCoreApplication.translate("MainWindow", u"New Form", None))
        self.pb_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

