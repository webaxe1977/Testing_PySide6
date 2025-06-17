# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerqvzssq.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(309, 128)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_message = QPushButton(Form)
        self.pb_message.setObjectName(u"pb_message")

        self.verticalLayout.addWidget(self.pb_message)

        self.pb_clear = QPushButton(Form)
        self.pb_clear.setObjectName(u"pb_clear")

        self.verticalLayout.addWidget(self.pb_clear)

        self.pb_close = QPushButton(Form)
        self.pb_close.setObjectName(u"pb_close")

        self.verticalLayout.addWidget(self.pb_close)

        self.label_recieve = QLabel(Form)
        self.label_recieve.setObjectName(u"label_recieve")
        self.label_recieve.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_recieve)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Second Form PySide6", None))
        self.pb_message.setText(QCoreApplication.translate("Form", u"Test QMessageBox", None))
        self.pb_clear.setText(QCoreApplication.translate("Form", u"Clear label", None))
        self.pb_close.setText(QCoreApplication.translate("Form", u"Close", None))
        self.label_recieve.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

