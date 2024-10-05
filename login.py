# login.py
import os
import smtplib
from PyQt5 import QtWidgets, QtGui, QtCore

class LoginApp(QtWidgets.QWidget):
    def __init__(self, on_login_success, dark_mode=False):
        super().__init__()
        self.on_login_success = on_login_success
        self.dark_mode = dark_mode  # Define o modo (claro ou escuro)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login - Disparador de E-mails')
        self.setGeometry(100, 100, 400, 500)
        layout = QtWidgets.QVBoxLayout(self)

        # Adicionar a logo centralizada
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        image_path = os.path.join(os.getcwd(), 'images', 'logo.jpg')
        self.load_logo(image_path)
        layout.addWidget(self.logo_label)

        # Campo de texto para o e-mail com ícone
        self.email_label = QtWidgets.QLabel('E-mail:')
        self.email_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.email_input = QtWidgets.QLineEdit()
        self.email_input.setPlaceholderText("Digite seu e-mail")
        self.email_input.setStyleSheet("""
            font-size: 14px;
            border-radius: 10px;
            padding: 6px;
            border: 1px solid gray;
        """)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        # Campo de texto para a senha com ícone
        self.password_label = QtWidgets.QLabel('Senha (Use senha de aplicativo):')
        self.password_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setPlaceholderText("Digite sua senha")
        self.password_input.setStyleSheet("""
            font-size: 14px;
            border-radius: 10px;
            padding: 6px;
            border: 1px solid gray;
        """)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        # Dropdown para selecionar o provedor de e-mail com ícone
        self.provider_label = QtWidgets.QLabel('Provedor:')
        self.provider_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.provider_dropdown = QtWidgets.QComboBox(self)
        self.provider_dropdown.setStyleSheet("""
            font-size: 14px;
            border-radius: 10px;
            padding: 6px;
            border: 1px solid gray;
        """)
        self.provider_dropdown.addItems(['Gmail', 'Outlook', 'Titan', 'UOL Host'])
        layout.addWidget(self.provider_label)
        layout.addWidget(self.provider_dropdown)

        # Botão de login com sombra
        self.login_button = QtWidgets.QPushButton('Login')
        self.add_shadow(self.login_button)  # Adiciona sombra ao botão
        self.login_button.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                font-size: 16px;
                border-radius: 10px;
                padding: 8px;
                background-color: #0078D7;
                color: white;
            }
            QPushButton:hover {
                background-color: #005BBB;
            }
        """)
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        # Botão de Ajuda com sombra
        self.help_button = QtWidgets.QPushButton('Ajuda❓')
        self.add_shadow(self.help_button)  # Adiciona sombra ao botão
        self.help_button.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                font-size: 16px;
                border-radius: 10px;
                padding: 8px;
                background-color: #0078D7;
                color: white;
            }
            QPushButton:hover {
                background-color: #005BBB;
            }
        """)
        self.help_button.clicked.connect(self.show_help)
        layout.addWidget(self.help_button)

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

        # Centralizando o botão de tema
        layout.setAlignment(self.theme_button, QtCore.Qt.AlignHCenter)

        # Espaçamento para o botão de tema abaixo do "Ajuda"
        layout.addSpacing(30)

        # Campo para exibir o status do login (sucesso ou falha)
        self.status_label = QtWidgets.QLabel('')
        layout.addWidget(self.status_label)

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

    def handle_login(self):
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()

        # Simulação de conta de exemplo
        if email == "exemplo.com.br" and password == "123":
            self.status_label.setText('✅ Login com a conta de exemplo bem-sucedido!')
            self.status_label.setStyleSheet('color: green;')
            # Simulação de login bem-sucedido sem conexão ao SMTP
            self.on_login_success(None, email, password, self.dark_mode)
            return

        # Verificar se os campos de e-mail e senha estão vazios
        if not email or not password:
            self.status_label.setText("❌ Erro: Os campos de E-mail e Senha são obrigatórios.")
            self.status_label.setStyleSheet("color: red;")
            return

        provider = self.provider_dropdown.currentText()
        smtp_servers = {
            'Gmail': 'smtp.gmail.com',
            'Outlook': 'smtp-mail.outlook.com',
            'Titan': 'smtp.titan.email',
            'UOL Host': 'smtp.uol.com.br'
        }
        smtp_server = smtp_servers.get(provider)

        try:
            server = smtplib.SMTP(smtp_server, 587)
            server.starttls()
            server.login(email, password)
            self.status_label.setText('✅ Login bem-sucedido!')
            self.status_label.setStyleSheet('color: green;')
            self.on_login_success(server, email, password, self.dark_mode)
        except smtplib.SMTPAuthenticationError:
            self.status_label.setText('❌ Usuário ou senha inválidos. Verifique suas credenciais.')
            self.status_label.setStyleSheet('color: red;')
        except Exception as e:
            self.status_label.setText(f'❌ Erro: {str(e)}')
            self.status_label.setStyleSheet('color: red;')

    def show_help(self):
        help_text = (
            "Para acessar esta plataforma, siga estas instruções:\n\n"
            "1. Gmail: Acesse sua conta Google e gere uma 'Senha de Aplicativo'.\n"
            "2. Outlook: Gere uma 'Senha de Aplicativo'.\n"
            "3. Titan e UOL Host: Use seu e-mail e senha normais ou consulte o provedor.\n"
            "⚠️ Use senhas de aplicativos em vez de senhas normais."
        )
        QtWidgets.QMessageBox.information(self, 'Ajuda❓', help_text)

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
