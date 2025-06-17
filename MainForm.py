#!/usr/bin/env python3

import sys
from datetime import datetime
import traceback
import Ui_MainForm
import SecondForm
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from methods.main_form_methods import (
    start_app,
    close_app,
    test_messagebox,
    test_statusbar,
)


class MainForm(QMainWindow, Ui_MainForm.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # logging start app
        start_app()

        # connection to signals and slots
        self.pb_quit.clicked.connect(self.close_app)
        self.pb_test_messagebox.clicked.connect(self.test_qmessagebox)
        self.pb_send.clicked.connect(self.test_statusbar)
        self.pb_open_new_form.clicked.connect(self.open_second_form)

    def close_app(self):
        """calling method from methods folder"""
        close_app(self)

    def test_qmessagebox(self):
        """calling method from methods folder"""
        test_messagebox(self)

    def test_statusbar(self):
        # from methods.main_form_methods import test_statusbar
        test_statusbar(self)

    def open_second_form(self):
        try:
            self.show_second_form = SecondForm.SecondForm(self.le_send.text())
            self.show_second_form.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Can not open a new window: {e}")
            return


if __name__ == "__main__":
    """handled exception in start app and save posible errors in errors_log.txt"""
    try:
        app = QApplication(sys.argv)
        MainWin = MainForm()
        MainWin.show()
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
                f"MainForm launch error: \n{current_datetime}\n{error_trace}\n{e}\n{'=' * 90}\n\n"
            )
        print(error_trace)
        sys.exit(1)
