from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

pdf = canvas.Canvas("contrato.pdf", pagesize=A4, verbosity=0)

styles = getSampleStyleSheet()
estilo_corpo = styles['Normal']

x = 20
y = 800

def novo_paragrafo(texto):
    global y 
    p = Paragraph(texto, estilo_corpo)

    largura_util = 495
    altura_disponivel = 800

    _, altura_ocupada = p.wrapOn(pdf, largura_util, altura_disponivel)

    y -= altura_ocupada + 10

    p.drawOn(pdf, x, y)
    
def gerar_contrato():
  novo_paragrafo(
      "Pelo presente instrumento particular, de um lado Vemfestejarjp,"
      " inscrita no CNPJ nº 34.126.562/0001-06, com sede em Av: Henrique"
      " Ruffo, 223 jardim treze de maio, João Pessoa PB, doravante"
      " denominada contratada."
  )
  
  novo_paragrafo(
      "E de outro lado o contratante, doravante denominado contratante,"
      " celebram o presente contrato de prestação de serviços tecnológicos,"
      " que se regirá pelas cláusulas e condições seguintes."
  )


gerar_contrato()

pdf.showPage()
pdf.save()
