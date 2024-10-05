
# 🚀 Disparador de E-mails - Contador de Padarias

Este é um projeto simples e funcional que permite o envio de e-mails personalizados para múltiplos destinatários usando diferentes provedores (Gmail, Outlook, Yahoo, etc.) através de uma interface gráfica criada com **PyQt5**. O objetivo é facilitar o envio de e-mails diretamente de uma aplicação sem a necessidade de acessar plataformas externas.

## 🎯 Funcionalidades
- 💼 Interface gráfica interativa e responsiva.
- 💌 Envio de e-mails para múltiplos destinatários, com suporte a separação por vírgulas.
- 📎 Anexar arquivos diretamente pela interface.
- 🔐 Suporte a autenticação SMTP via Gmail, Outlook, Titan, UOL Host, entre outros.
- 🌗 Alternância entre modo claro e modo escuro.
- ✨ Animações suaves para melhor experiência de usuário.
- 🔑 Suporte a senhas de aplicativos para provedores com autenticação em dois fatores.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **PyQt5**: Biblioteca para criar a interface gráfica.
- **smtplib**: Biblioteca para envio de e-mails via protocolo SMTP.
- **email.mime**: Para formatação e envio de e-mails em formato MIME (com anexos e corpo formatado).

## 📋 Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o Python 3.x instalado. Você pode verificar se o Python está instalado executando:

```bash
python --version
```

Se o Python não estiver instalado, você pode baixá-lo [aqui](https://www.python.org/downloads/).

## 🚀 Instalação

1. **Clone o repositório**:
   
   ```bash
   git clone https://github.com/seu-usuario/disparador-emails.git
   cd disparador-emails
   ```

2. **Instale as dependências**:

   Instale as bibliotecas necessárias com o comando:

   ```bash
   pip install -r requirements.txt
   ```

   Ou, se você preferir instalar manualmente:

   ```bash
   pip install PyQt5
   ```

## 🔑 Autenticação via Senha de Aplicativos

Para enviar e-mails com provedores como Gmail ou Outlook, é necessário o uso de **senhas de aplicativos** caso você tenha a verificação em dois fatores ativada.

### 🚨 Como gerar uma senha de aplicativo:

- **Gmail**:
  1. Acesse as [configurações de segurança](https://myaccount.google.com/security) da sua conta Google.
  2. Habilite a **verificação em duas etapas**.
  3. Na seção "Senhas de Aplicativos", gere uma senha específica para o seu aplicativo.

- **Outlook**:
  1. Acesse o portal de segurança da [Microsoft](https://account.live.com/proofs/manage).
  2. Habilite a **verificação em duas etapas**.
  3. Gere uma senha de aplicativo.

Utilize essa senha no campo de senha do programa para autenticação.

## 📂 Estrutura de Arquivos

```bash
📦Disparador E-mails
 ┣ 📂images
 ┃ ┗ 📜logo.jpg
 ┣ 📜main.py
 ┣ 📜login.py
 ┣ 📜email_sender.py
 ┗ 📜README.md
```

- **`main.py`**: Arquivo principal para rodar a aplicação.
- **`login.py`**: Interface de login com autenticação via SMTP.
- **`email_sender.py`**: Interface para envio de e-mails com suporte a anexos e múltiplos destinatários.
- **`images/logo.jpg`**: Imagem da logo da aplicação.

## 🏃‍♂️ Como Usar

1. **Execute o arquivo principal**:

   ```bash
   python main.py
   ```

2. **Login**:

   - Insira seu **e-mail**, **senha de aplicativo**, e selecione o provedor (Gmail, Outlook, etc.).
   - Após o login bem-sucedido, você será redirecionado para a tela de envio de e-mails.

3. **Envio de E-mails**:

   - Digite os **destinatários** (separados por vírgula).
   - Preencha o **assunto** e o **corpo** do e-mail.
   - Se quiser anexar arquivos, clique no botão **📎 Anexar Arquivo**.
   - Clique em **Enviar E-mails** para finalizar o envio.

4. **Logoff**:

   - Para sair da aplicação, clique em **Sair**.

## ⚙️ Configurações SMTP

Por padrão, o aplicativo suporta os seguintes provedores de e-mail:

- **Gmail**:
  - SMTP: `smtp.gmail.com`
  - Porta: `587`
- **Outlook**:
  - SMTP: `smtp-mail.outlook.com`
  - Porta: `587`
- **Titan**:
  - SMTP: `smtp.titan.email`
  - Porta: `587`
- **UOL Host**:
  - SMTP: `smtp.uol.com.br`
  - Porta: `587`

## 🌟 Funcionalidades Futuras

- 🔄 Agendamento de envio de e-mails.
- 📊 Relatórios de e-mails enviados.
- 🔗 Integração com APIs de terceiros.

## 🤝 Contribuição

Se você quiser contribuir para o projeto:

1. Faça um **fork** do projeto.
2. Crie uma **branch** para suas alterações (`git checkout -b minha-feature`).
3. **Commit** suas alterações (`git commit -m 'Adiciona minha-feature'`).
4. **Push** para a branch (`git push origin minha-feature`).
5. Abra um **Pull Request**.

## 🛡️ Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📝 Agradecimentos

Agradecemos à comunidade Python por todas as ferramentas incríveis que tornam projetos como este possíveis!
