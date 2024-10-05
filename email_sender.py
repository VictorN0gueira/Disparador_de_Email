# email_sender.py
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class EmailSenderApp(QtWidgets.QMainWindow):
    def __init__(self, server, email, password, on_logoff, dark_mode=False):
        super().__init__()
        self.server = server
        self.email = email
        self.password = password
        self.on_logoff = on_logoff  # Função para redirecionar para o login
        self.dark_mode = dark_mode  # Recebe o modo
        self.attachments = []  # Lista para armazenar arquivos anexados
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Disparador de E-mails - Contador de Padarias')
        self.setGeometry(100, 100, 600, 600)
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)

        # Status e logo
        self.status_label = QtWidgets.QLabel('', self)
        layout.addWidget(self.status_label)
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        image_path = os.path.join(os.getcwd(), 'images', 'logo.jpg')
        self.load_logo(image_path)
        layout.addWidget(self.logo_label)

        # Campo para destinatários com ícone
        recipients_layout = QtWidgets.QHBoxLayout()
        self.recipients_label = QtWidgets.QLabel('<b>Destinatários (separados por vírgula):</b>', self)
        self.recipients_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        recipients_layout.addWidget(self.recipients_label)
        self.recipients_text = QtWidgets.QLineEdit(self)
        self.recipients_text.setStyleSheet("""
            font-size: 14px;
            border-radius: 10px;
            padding: 6px;
            border: 1px solid gray;
        """)
        recipients_layout.addWidget(self.recipients_text)
        layout.addLayout(recipients_layout)

        # Assunto do e-mail com ícone
        subject_layout = QtWidgets.QHBoxLayout()
        self.subject_label = QtWidgets.QLabel('<b>Assunto:</b>', self)
        self.subject_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        subject_layout.addWidget(self.subject_label)
        self.subject_text = QtWidgets.QLineEdit(self)
        self.subject_text.setStyleSheet("""
            font-size: 14px;
            border-radius: 10px;
            padding: 6px;
            border: 1px solid gray;
        """)
        subject_layout.addWidget(self.subject_text)
        layout.addLayout(subject_layout)

        # Corpo do e-mail
        body_layout = QtWidgets.QVBoxLayout()
        self.body_label = QtWidgets.QLabel('<b>Corpo do E-mail:</b>', self)
        self.body_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        body_layout.addWidget(self.body_label)
        self.body_text = QtWidgets.QTextEdit(self)
        self.body_text.setStyleSheet("""
            font-size: 14px;
            border-radius: 10px;
            padding: 6px;
            border: 1px solid gray;
        """)
        body_layout.addWidget(self.body_text)
        layout.addLayout(body_layout)

        # Botão para anexar arquivos com sombra
        self.attach_button = QtWidgets.QPushButton('📎 Anexar Arquivo', self)
        self.add_shadow(self.attach_button)  # Adiciona sombra ao botão
        self.attach_button.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                font-size: 14px;
                border-radius: 10px;
                padding: 8px;
                background-color: #0078D7;
                color: white;
            }
            QPushButton:hover {
                background-color: #005BBB;
            }
        """)
        self.attach_button.clicked.connect(self.attach_file)
        layout.addWidget(self.attach_button)

        # Botão para enviar o e-mail com sombra
        self.send_email_button = QtWidgets.QPushButton('Enviar E-mails', self)
        self.add_shadow(self.send_email_button)  # Adiciona sombra ao botão
        self.send_email_button.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                font-size: 14px;
                border-radius: 10px;
                padding: 8px;
                background-color: #0078D7;
                color: white;
            }
            QPushButton:hover {
                background-color: #005BBB;
            }
        """)
        self.send_email_button.clicked.connect(self.send_emails)
        layout.addWidget(self.send_email_button)

        # Botão de Logoff com sombra
        self.logoff_button = QtWidgets.QPushButton('Sair', self)
        self.add_shadow(self.logoff_button)  # Adiciona sombra ao botão
        self.logoff_button.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                font-size: 14px;
                border-radius: 10px;
                padding: 8px;
                background-color: #0078D7;
                color: white;
            }
            QPushButton:hover {
                background-color: #005BBB;
            }
        """)
        self.logoff_button.clicked.connect(self.logoff)
        layout.addWidget(self.logoff_button)

        # Botão de Modo Claro/Escuro com sombra
        self.theme_button = QtWidgets.QPushButton('☼', self)
        self.theme_button.setFixedSize(40, 40)
        self.add_shadow(self.theme_button)  # Adiciona sombra ao botão
        self.theme_button.setStyleSheet("""
            QPushButton {
                border-radius: 20px;
                background-color: #0078D7;
                color: white;
            }
            QPushButton:hover {
                background-color: #005BBB;
            }
        """)
        self.theme_button.clicked.connect(self.toggle_theme)
        layout.addWidget(self.theme_button)

        # Centralizando o botão de tema abaixo de "Sair"
        layout.setAlignment(self.theme_button, QtCore.Qt.AlignHCenter)

        # Aplica o tema
        self.apply_theme()

    def load_logo(self, image_path):
        if os.path.exists(image_path):
            pixmap = QtGui.QPixmap(image_path)
            if not pixmap.isNull():
                self.logo_label.setPixmap(pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio))
            else:
                self.status_label.setText("Erro ao carregar a imagem. Formato inválido.")
        else:
            self.status_label.setText(f"Erro: Caminho da imagem '{image_path}' não encontrado.")

    # Função para anexar arquivos
    def attach_file(self):
        options = QtWidgets.QFileDialog.Options()
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Selecionar Arquivo", "", "Todos os Arquivos (*);;Arquivos de Texto (*.txt);;Imagens (*.png *.jpg *.jpeg)", options=options)
        if files:
            self.attachments.extend(files)  # Adiciona os arquivos selecionados à lista de anexos
            self.status_label.setText(f"Arquivos anexados: {', '.join(os.path.basename(f) for f in self.attachments)}")

    def send_emails(self):
        subject = self.subject_text.text()
        body = self.body_text.toPlainText()
        recipients = self.recipients_text.text().split(',')  # Dividir os destinatários por vírgulas

        if subject and body and recipients:
            try:
                for recipient in recipients:
                    recipient = recipient.strip()  # Remove espaços desnecessários
                    self.send_email(recipient, subject, body)
                self.status_label.setText(f"✅ E-mails enviados com sucesso!")
            except Exception as e:
                self.status_label.setText(f"❌ Erro no envio: {str(e)}")
        else:
            self.status_label.setText("❌ Erro: Por favor, complete os campos de Destinatários, Assunto e Corpo do E-mail.")

    def send_email(self, to_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Anexa arquivos se houver
        for file in self.attachments:
            attachment = open(file, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(file)}")
            msg.attach(part)

        if self.server:
            self.server.sendmail(self.email, to_email, msg.as_string())

    def logoff(self):
        self.close()
        self.on_logoff(self.dark_mode)  # Passa o modo escuro ao fazer logoff

    def toggle_theme(self):
        """Alterna entre modo claro e escuro"""
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        """Aplica o tema claro ou escuro na interface"""
        if self.dark_mode:
            self.setStyleSheet("""
                QWidget { background-color: #2b2b2b; color: white; }
                QLineEdit, QComboBox, QPushButton { background-color: white; color: black; border-radius: 10px; }
            """)
            self.theme_button.setStyleSheet("border-radius: 20px; color: white; background-color: #2b2b2b;")
            self.theme_button.setText("☼")  # Ícone branco no modo escuro
        else:
            self.setStyleSheet("""
                QWidget { background-color: white; color: black; }
                QLineEdit, QComboBox, QPushButton { background-color: #f0f0f0; color: black; border-radius: 10px; }
            """)
            self.theme_button.setStyleSheet("border-radius: 20px; color: black; background-color: white;")
            self.theme_button.setText("☼")  # Ícone preto no modo claro

    def add_shadow(self, widget):
        """Adiciona sombra a um widget (como botões)"""
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(3, 3)
        widget.setGraphicsEffect(shadow)
