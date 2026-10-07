from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_CENTER

pdf = canvas.Canvas("contrato.pdf", pagesize=A4, verbosity=0)

x = 20
y = 800



styles = getSampleStyleSheet()

paragrafo = styles["Normal"].alligment = TA_CENTER
titulo = styles["Title"].alignment = TA_CENTER
dic_t = {
   '1': paragrafo,
   '2': titulo,
}


def novo_paragrafo(texto, style):
    global y 
    p = Paragraph(texto, style)

    x_max = 495
    y_max = 800

    _, y_restante = p.wrapOn(pdf, x_max, y_max)

    y -= y_restante + 10

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
