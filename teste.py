from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from datetime import datetime

pdf = canvas.Canvas('contrato.pdf', pagesize=A4, verbosity=0)

x = 40
y = 800

styles = getSampleStyleSheet()

paragrafo = ParagraphStyle(
    'EstiloCorpo', parent=styles['Normal'], fontSize=12, alignment=TA_LEFT
)

titulo = ParagraphStyle(
    'EstiloTitulo', parent=styles['Title'], fontSize=14, alignment=TA_LEFT
)

bullet = ParagraphStyle(
    'EstiloBullet', parent=styles['Normal'], fontSize=12, alignment=TA_LEFT, bulletText='•'
)

dic_s = {
    '1': paragrafo,
    '2': titulo,
    '3': bullet
}

dic_c = {
   '1': 'CLÁUSULA 1ª – DO OBJETO',
   '2': 'CLÁUSULA 2ª – DATA E PRAZO'
}

texto = "1Bola 2Balo 3mesa 4Mesa"
texto_split = texto.split()


def novo_paragrafo(texto, style):
  global y
  p = Paragraph(texto, style)

  x_max = 495
  y_max = 800

  _, y_restante = p.wrapOn(pdf, x_max, y_max)

  y -= y_restante + 10

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



gerar_contrato()

pdf.showPage()
pdf.save()