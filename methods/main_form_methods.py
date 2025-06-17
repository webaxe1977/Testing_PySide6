#!/usr/bin/env python3

from PySide6.QtWidgets import QMessageBox, QApplication
from datetime import datetime


def start_app():
    """Correctly start the application with logging"""

    # logging
    current_datetime = datetime.now().strftime("%H:%M:%S %d_%m_%Y")
    with open("start_stop_app.txt", "a", encoding="utf-8") as file:
        file.write(f"{current_datetime}: App started by user\n{'=' * 50}\n\n")

    print("DEBUG: app started!")


def close_app(window):
    """Correctly close the application with logging"""
    QMessageBox.information(
        window, "Information", "Application now closed.\nBye, see you!"
    )

    # logging
    current_datetime = datetime.now().strftime("%H:%M:%S %d_%m_%Y")
    with open("start_stop_app.txt", "a", encoding="utf-8") as file:
        file.write(f"{current_datetime}: App closed by user\n{'=' * 50}\n\n")

    QApplication.quit()

def test_messagebox(window):
    """Test QMessageBox"""
    QMessageBox.information(window, 'Information', 'Simple test QMessageBox!\nTest! Test!\nLOL!')

def test_statusbar(main_window):
    '''Test statusbar'''
    if not main_window.le_send.text().strip():
        QMessageBox.warning(main_window, 'Warning!', 'Enter any phrase!')
        return

    text = main_window.le_send.text()
    main_window.statusbar.showMessage(f"Processed: {text.upper()}", 3000)