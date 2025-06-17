#!/usr/bin/env python3

import sys
from datetime import datetime
import traceback
import Ui_mainForm
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget


class MainForm(QMainWindow, Ui_mainForm.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        # connection to signals and slots
        self.pb_quit.clicked.connect(self.close_app)







    def close_app(self):
        '''correct close application'''
        QMessageBox.information(self, 'Information', 'Application now closed.\nBay, see you!')
        QApplication.quit()


if __name__ == "__main__":
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
