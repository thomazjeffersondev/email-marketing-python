import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Carrega as credenciais
with open("crendenciais.json") as cred_file:
    credenciais = json.load(cred_file)

email_remetente = credenciais['email_remetente']
senha = credenciais['senha']
smtp_host = credenciais['smtp_host']
smtp_port = credenciais['smtp_port']

# Lista de destinatários
destinatarios = [
    'cliente1@email.com',
    'cliente2@email.com'
]

# Corpo do e-mail (HTML)
html = """
<html>
  <body>
    <h2>🔥 Oferta Especial!</h2>
    <p>Aproveite 30% de desconto nos nossos produtos. Só até amanhã!</p>
    <a href="https://seusite.com/oferta">Clique aqui para ver a promoção</a>
  </body>
</html>
"""

# Enviando e-mails
try:
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(email_remetente, senha)
    print("✅ Login bem-sucedido!")

    for destinatario in destinatarios:
        msg = MIMEMultipart('alternative')
        msg['From'] = email_remetente
        msg['To'] = destinatario
        msg['Subject'] = '🎯 Promoção Exclusiva Só Para Você!'

        msg.attach(MIMEText(html, 'html'))

        server.sendmail(email_remetente, destinatario, msg.as_string())
        print(f'📤 E-mail enviado para {destinatario}')

    server.quit()
    print("✅ Todos os e-mails foram enviados com sucesso!")

except Exception as e:
    print(f'❌ Erro ao enviar e-mail: {e}')
