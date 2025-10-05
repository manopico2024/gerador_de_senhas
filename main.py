from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
import random
import string

from telaPrincipal import Ui_telaPrincipal


class Gerador(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaPrincipal()
        self.ui.setupUi(self)

        # Conectar o botão à função
        self.ui.BTN_SENHA.clicked.connect(self.gerar_senha)

    def gerar_senha(self):
        length = 15
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.ui.TXT_SENHA.setText(password)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Gerador()
    window.show()
    sys.exit(app.exec_())
