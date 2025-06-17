# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerqvzssq.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    Qt,
)
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(309, 128)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_message = QPushButton(Form)
        self.pb_message.setObjectName("pb_message")

        self.verticalLayout.addWidget(self.pb_message)

        self.pb_clear = QPushButton(Form)
        self.pb_clear.setObjectName("pb_clear")

        self.verticalLayout.addWidget(self.pb_clear)

        self.pb_close = QPushButton(Form)
        self.pb_close.setObjectName("pb_close")

        self.verticalLayout.addWidget(self.pb_close)

        self.label_recieve = QLabel(Form)
        self.label_recieve.setObjectName("label_recieve")
        self.label_recieve.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_recieve)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate("Form", "Second Form PySide6", None)
        )
        self.pb_message.setText(
            QCoreApplication.translate("Form", "Test QMessageBox", None)
        )
        self.pb_clear.setText(QCoreApplication.translate("Form", "Clear label", None))
        self.pb_close.setText(QCoreApplication.translate("Form", "Close", None))
        self.label_recieve.setText(
            QCoreApplication.translate("Form", "TextLabel", None)
        )

    # retranslateUi
