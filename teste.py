from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from datetime import datetime
from num2words import num2words

def extenso(valor):
    t = num2words(int(valor), lang="pt_BR")
    return t

pdf = canvas.Canvas('contrato.pdf', pagesize=A4, verbosity=0)
styles = getSampleStyleSheet()
x = 40
y = 800


texto = "1Bola 2Balo 3mesa 4Mesa"
texto_split = texto.split()

multa = "O(A) CONTRATANTE declara-se fiel depositário(a) dos bens locados e assume integral responsabilidade pela sua conservação durante todo o período da locação. Em caso de avaria, perda, roubo, destruição parcial ou total dos itens, o(a) CONTRATANTE compromete-se a indenizar a CONTRATADA no valor de reposição de cada material danificado. Para a devida preservação do acervo, o(a) CONTRATANTE compromete-se a:"

responsabilidades = [
    "Zelar pela integridade dos itens recebidos;",
    "Não molhar, sujar excessivamente ou expor as peças ao sol e intempéries;",
    "Não alterar, personalizar ou modificar a estrutura da decoração;",
    "Restituir todos os itens no término do evento nas mesmas condições em que foram"
]

paragrafo = ParagraphStyle(
    'EstiloCorpo', parent=styles['Normal'], fontSize=12, leading=18, alignment=TA_LEFT
)

titulo = ParagraphStyle(
    'EstiloTitulo', parent=styles['Title'], fontSize=14, leading=18, alignment=TA_LEFT
)

bullet = ParagraphStyle(
    'EstiloBullet', parent=styles['Normal'], fontSize=12, leading=18, alignment=TA_LEFT, bulletText='•'
)

dic_s = {
    '1': paragrafo,
    '2': titulo,
    '3': bullet
}

dic_c = {
   '1': 'CLÁUSULA 1ª – DO OBJETO',
   '2': 'CLÁUSULA 2ª – DATA E PRAZO',
   '3': 'CLÁUSULA 3ª – VALOR E PAGAMENTO',
   '4': 'CLÁUSULA 4ª – DAS RESPONSABILIDADES E INDENIZAÇÕES',
   '5': 'CLÁUSULA 6ª – CANCELAMENTO',
   '6': 'CLÁUSULA 7ª – FORO'
}



def novo_paragrafo(texto, style):
  global y
  p = Paragraph(texto, style)

  x_max = 515
  y_max = 800

  _, y_restante = p.wrapOn(pdf, x_max, y_max)

  y -= y_restante + 14

  p.drawOn(pdf, x, y)

def c1(titulo, items):
    novo_paragrafo(titulo, dic_s['2'])

    if items:
        for i in items:
            novo_paragrafo(i, dic_s['3'])
    else:
       return None

def c2(titulo, data, hora,local):
    if not data or not hora or not local:
       return None
    else:
        novo_paragrafo(titulo, dic_s['2'])
        novo_paragrafo(f"O evento ocorrerá em {data}, às {hora}, no {local}, incluindo a montagem do cenário.",dic_s['1'])

def c3(titulo, valor, forma_de_pagamento, estado):
   if not valor or not forma_de_pagamento or not estado:
      return None
   else:
      novo_paragrafo(titulo, dic_s['2'])
      novo_paragrafo(f"O valor total do contrato é de R${valor} ({extenso(valor)}), pago via {forma_de_pagamento} {estado}.",dic_s['1'])

def c4(titulo, responsabilidade):
   novo_paragrafo(titulo,dic_s['2'])
   novo_paragrafo(multa, dic_s['1'])
   if responsabilidade:
      for r in responsabilidade:
         novo_paragrafo(r,dic_s['3'])
   else:
      return None
   
def gerar_contrato():
  novo_paragrafo(
    'Pelo presente instrumento particular, de um lado Vemfestejarjp,'
    ' inscrita no CNPJ nº 34.126.562/0001-06, com sede na Av. Henrique'
    ' Ruffo, nº 223, Jardim Treze de Maio, João Pessoa/PB, doravante'
    ' denominada CONTRATADA,'
    ' e, de outro lado, o CONTRATANTE, doravante denominado CONTRATANTE,'
    ' celebram o presente contrato de prestação de serviços tecnológicos,'
    ' que se regerá pelas cláusulas e condições seguintes.',
      dic_s['1'],
  )

  c1(
      dic_c['1'],
      texto_split
    )

  c2(
     dic_c['2'],
     '10/12/2026',
     '16:00',
     'Rua Lucas Borges da Silva, 431'
  )

  c3(
     dic_c['3'],
     '540',
     'Pix',
     'Quitado'
  )

  c4(
     dic_c['4'],
     responsabilidades
  )




gerar_contrato()

pdf.showPage()
pdf.save()