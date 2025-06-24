import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do remetente
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_remetente = 'seu_email@gmail.com'
senha = 'sua_senha_do_app'  # Use senha de app se for Gmail

# Lista de destinatários
destinatarios = ['cliente1@email.com', 'cliente2@email.com']

# Criando o corpo do e-mail (HTML)
html = """
<html>
  <body>
    <h2>🔥 Oferta Especial!</h2>
    <p>Aproveite 30% de desconto nos nossos produtos. Só até amanhã!</p>
    <a href="https://seusite.com/oferta">Clique aqui para ver a promoção</a>
  </body>
</html>
"""

# Criando o servidor SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(email_remetente, senha)

# Enviando e-mail para cada destinatário
for destinatario in destinatarios:
    msg = MIMEMultipart('alternative')
    msg['From'] = email_remetente
    msg['To'] = destinatario
    msg['Subject'] = '🎯 Promoção Exclusiva Só Para Você!'

    # Anexa o HTML ao corpo da mensagem
    msg.attach(MIMEText(html, 'html'))

    # Envia o e-mail
    server.sendmail(email_remetente, destinatario, msg.as_string())
    print(f'E-mail enviado para {destinatario}')

# Finaliza a conexão
server.quit()
