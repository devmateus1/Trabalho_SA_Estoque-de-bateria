import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do e-mail
remetente = 'gustavowendt14@gmail.com'
senha = 'lnji dajd dyfy bhfx'
destinatario = 'pipocay01@gmail.com'

# Criar o corpo do e-mail
mensagem = MIMEMultipart()
mensagem['From'] = remetente
mensagem['To'] = destinatario
mensagem['Subject'] = 'Assunto do Email'

corpo = 'Olá! Este é um e-mail enviado pelo meu software em Python! Testteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
mensagem.attach(MIMEText(corpo, 'plain'))

# Enviar o e-mail
try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatario, mensagem.as_string())
    servidor.quit()
    print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar e-mail: {e}')
