#!/usr/bin/env python3

from PySide6.QtWidgets import QMessageBox

def test_messagebox(window):
    """Test QMessageBox"""
    QMessageBox.information(window, 'Information', 'Simple test QMessageBox on second window!\nTest! Test!\nLOL!')

def close_second_window(window):
    QMessageBox.information(window, 'Information', 'Close current window')
    window.close()

def clear_label(second_form):
    if not second_form.label_recieve.text():
        QMessageBox.information(second_form, 'Information', 'Nothing to clean')
        return
    second_form.label_recieve.clear()
    QMessageBox.information(second_form, 'Information', 'Label was cleared')