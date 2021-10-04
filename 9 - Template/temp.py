from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r', encoding="utf-8") as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Pedro Lisboa', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Pedro Henrique Lisboa'
msg['to'] = meu_email  # cliente
msg['subject'] = 'Atenção: esse é um e-mail de testes.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# ENVIO DE IMAGEM EM ANEXO
with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

# ENVIO DE E-MAIL
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)  # e-mail que esta enviando
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado')
        print('Error: ', e)
