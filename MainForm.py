#!/usr/bin/env python3

import sys
from datetime import datetime
import traceback
import Ui_mainForm
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from methods.main_form_methods import start_app, close_app, test_messagebox, test_statusbar



class MainForm(QMainWindow, Ui_mainForm.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # logging start app
        start_app()



        # connection to signals and slots
        self.pb_quit.clicked.connect(self.close_app)
        self.pb_test_messagebox.clicked.connect(self.test_qmessagebox)
        self.pb_send.clicked.connect(self.test_statusbar)


    def close_app(self):
        '''calling method from methods folder'''
        close_app(self)

    def test_qmessagebox(self):
        '''calling method from methods folder'''
        test_messagebox(self)

    def test_statusbar(self):
        if not self.le_send.text().strip():
            QMessageBox.warning(self, 'Warning!', 'Enter any phrase!')
            return
        self.statusbar.showMessage(test_statusbar(self.le_send.text()))


if __name__ == "__main__":
    '''handled exception in start app and save posible errors in errors_log.txt'''
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
            file.write(f"{current_datetime}\n{error_trace}\n{e}\n{'=' * 90}\n\n")
        print(error_trace)
        sys.exit(1)
