# main.py
import sys
from PyQt5 import QtWidgets
from login import LoginApp
from email_sender import EmailSenderApp

class MainApp:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.show_login()

    def show_login(self, dark_mode=False):
        self.login_window = LoginApp(self.on_login_success, dark_mode)
        self.login_window.show()

    def on_login_success(self, server, email, password, dark_mode):
        self.login_window.close()  # Fecha a janela de login
        self.email_sender_window = EmailSenderApp(server, email, password, self.show_login, dark_mode)
        self.email_sender_window.show()

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    main_app = MainApp()
    main_app.run()
