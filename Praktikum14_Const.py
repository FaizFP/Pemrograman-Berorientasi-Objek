#Faiz FIrdaus Priyanto
#064002300005
#GUI

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QMessageBox
from PySide6.QtGui import QFont

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Masukkan detail Anda:")
        self.label.setFont(QFont('Arial'))

        self.name_textbox = QLineEdit()
        self.name_textbox.setFont(QFont('Arial'))
        self.name_textbox.setPlaceholderText("Nama")

        self.nim_textbox = QLineEdit()
        self.nim_textbox.setFont(QFont('Arial'))
        self.nim_textbox.setPlaceholderText("NIM")

        self.hobby_textbox = QLineEdit()
        self.hobby_textbox.setFont(QFont('Arial'))
        self.hobby_textbox.setPlaceholderText("Hobi")

        self.button_send = QPushButton("Kirim")
        self.button_send.setFont(QFont('Arial'))

        self.button_reset = QPushButton("Reset")
        self.button_reset.setFont(QFont('Arial'))

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.name_textbox)
        self.layout.addWidget(self.nim_textbox)
        self.layout.addWidget(self.hobby_textbox)
        self.layout.addWidget(self.button_send)
        self.layout.addWidget(self.button_reset)
        self.setStyleSheet("background-color: #FFFFFF;")
        self.button_send.setStyleSheet("background-color: #82E0AA ;")
        self.button_reset.setStyleSheet("background-color: #E9F5AA ;")
        
        self.button_send.clicked.connect(self.greet)
        self.button_reset.clicked.connect(self.reset)

    def greet(self):
        name = self.name_textbox.text().strip()
        nim = self.nim_textbox.text().strip()
        hobby = self.hobby_textbox.text().strip()

        if name == "" and nim == "" and hobby == "":
            QMessageBox.warning(self, "Peringatan", "Mohon isi semua kolom yang tersedia.")
        elif not nim.isdigit():
            QMessageBox.warning(self, "Peringatan", "NIM harus berupa angka.")
        
        elif not nim :
            QMessageBox.warning(self, "Peringatan", "NIM harus diisi.")
        
        elif not hobby:
            QMessageBox.warning(self, "Peringatan", "Hobby harus disi.")

        elif not name:
            QMessageBox.warning(self, "Peringatan", "nama harus diisi.")

        else:
            self.label.setText(f"Halo, {name}!\nNIM Anda adalah {nim}\ndan hobi Anda adalah {hobby}.")

    def reset(self):
        self.name_textbox.clear()
        self.nim_textbox.clear()
        self.hobby_textbox.clear()
        self.label.setText("Masukkan detail Anda:")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Input Detail")
        
        self.widget = CustomWidget()
        self.setCentralWidget(self.widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
