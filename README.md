# 📧 Automação de Email Marketing com Python

Automação para envio de e-mail marketing utilizando Python e SMTP, com configuração segura via arquivo JSON. Ideal para campanhas promocionais, newsletters e comunicação com clientes.

---

## 🚀 Funcionalidades

- Envio de e-mails em massa com conteúdo HTML personalizado  
- Configuração externa de credenciais e servidor SMTP via arquivo JSON  
- Fácil adaptação para múltiplos destinatários  
- Uso da biblioteca padrão Python (`smtplib` e `email`)  

---

## 🧰 Tecnologias Utilizadas

- Python 3.8+  
- Biblioteca nativa `smtplib`  
- Biblioteca nativa `email.mime`  

---

## 📦 Instalação e Uso

### 1. Clone o repositório

```bash
git clone https://github.com/thomazcabral/email-marketing-python.git
cd email-marketing-python
2. Crie o arquivo credentials.json na raiz do projeto
json
Copiar
Editar
{
  "email_remetente": "curso.python.dev@gmail.com",
  "senha": "SUA_SENHA_DO_APP",
  "smtp_host": "smtp.gmail.com",
  "smtp_port": 587
}
Importante:

Use senha de app para Gmail: Gerar aqui

Nunca compartilhe este arquivo. Adicione ao .gitignore.

3. Edite a lista de destinatários no arquivo main.py
python
Copiar
Editar
destinatarios = [
    'cliente1@email.com',
    'cliente2@email.com'
]
4. Execute o script
bash
Copiar
Editar
python main.py
📄 Estrutura do Projeto
bash
Copiar
Editar
email-marketing-python/
│
├── credentials.json      # Configurações sensíveis (não versionar)
├── main.py               # Script principal para envio dos e-mails
├── README.md             # Documentação do projeto
└── .gitignore            # Arquivos ignorados pelo Git
⚙️ Personalização
Você pode modificar o conteúdo do e-mail HTML diretamente no main.py:

python
Copiar
Editar
html = """
<html>
  <body>
    <h2>🔥 Oferta Especial!</h2>
    <p>Aproveite 30% de desconto nos nossos produtos. Só até amanhã!</p>
    <a href="https://seusite.com/oferta">Clique aqui para ver a promoção</a>
  </body>
</html>
"""
🤝 Contribuindo
Contribuições são bem-vindas!
Abra issues ou pull requests para sugerir melhorias.

📬 Contato
Thomaz Jefferson Marins Cabral
📧 marinscabralster@gmail.com
🔗 LinkedIn