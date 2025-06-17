#!/usr/bin/env python3

import sys
import traceback
import Ui_SecondForm
from datetime import datetime
from methods.second_form_methods import (
    test_messagebox,
    close_second_window,
    clear_label,
)
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication


class SecondForm(QWidget, Ui_SecondForm.Ui_Form):
    def __init__(self, some_string=""):
        self.some_string = some_string
        super().__init__()
        self.setupUi(self)
        self.label_recieve.setText(some_string)

        self.pb_close.clicked.connect(self.close_window)
        self.pb_message.clicked.connect(self.test_message)
        self.pb_clear.clicked.connect(self.cls_label)

    def close_window(self):
        close_second_window(self)

    def test_message(self):
        test_messagebox(self)

    def cls_label(self):
        clear_label(self)


if __name__ == "__main__":
    """handled exception in start app and save posible errors in errors_log.txt"""
    try:
        app = QApplication(sys.argv)
        SecondWin = SecondForm()
        SecondWin.show()
        sys.exit(app.exec())
    except Exception as e:
        widget = QWidget()
        current_datetime = datetime.now().strftime("%H:%M:%S %d_%m_%Y")
        error_trace = traceback.format_exc()
        QMessageBox.critical(
            widget,
            "Critical error!",
            f"{current_datetime}\n{error_trace}\n{e}\n",
        )
        with open("errors_log.txt", "a", encoding="utf-8") as file:
            file.write(
                f"SeconfForm launch error:\n{current_datetime}\n{error_trace}\n{e}\n{'=' * 90}\n\n"
            )
        print(error_trace)
