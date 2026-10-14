from datetime import datetime
from num2words import num2words
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


def extenso(valor):
  t = num2words(int(valor), lang='pt_BR')
  return t

from datetime import datetime

def data_por_extenso(dt=None):
    if dt is None:
        dt = datetime.now()
        
    meses = {
        1: "janeiro", 
        2: "fevereiro", 
        3: "março", 
        4: "abril",
        5: "maio", 
        6: "junho", 
        7: "julho", 
        8: "agosto",
        9: "setembro", 
        10: "outubro", 
        11: "novembro", 
        12: "dezembro"
    }
    
    dia = str(dt.day).zfill(2)
    mes = meses[dt.month]
    ano = dt.year
    
    return f"{dia} de {mes} de {ano}"


pdf = canvas.Canvas('contrato.pdf', pagesize=A4, verbosity=0)
styles = getSampleStyleSheet()
x = 40
y = 800


items_intro = (
    'O presente contrato tem como objeto a locação dos bens e materiais'
    ' decorativos descritos a seguir, que serão disponibilizados para o evento:'
)
texto = '1Bola 2Balo 3mesa 4Mesa'
texto_split = texto.split()

multa = (
    'O(A) <b>CONTRATANTE</b> declara-se fiel depositário(a) dos bens locados e'
    ' assume integral responsabilidade pela sua conservação durante todo o'
    ' período da locação. Em caso de avaria, perda, roubo, destruição parcial'
    ' ou total dos itens, o(a) <b>CONTRATANTE</b> compromete-se a indenizar a'
    ' <b>CONTRATADA</b> no valor de reposição de cada material danificado. Para'
    ' a devida preservação do acervo, o(a) <b>CONTRATANTE</b> compromete-se a:'
)

responsabilidades = [
    'Zelar pela integridade dos itens recebidos;',
    'Não molhar, sujar excessivamente ou expor as peças ao sol e intempéries;',
    'Não alterar, personalizar ou modificar a estrutura da decoração;',
    (
        'Restituir todos os itens no término do evento nas mesmas condições em'
        ' que foram'
    ),
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

dic_s = {'1': paragrafo, '2': titulo, '3': bullet}

dic_c = {
    '1': 'CLÁUSULA 1ª – DO OBJETO',
    '2': 'CLÁUSULA 2ª – DATA E PRAZO',
    '3': 'CLÁUSULA 3ª – VALOR E PAGAMENTO',
    '4': 'CLÁUSULA 4ª – DAS RESPONSABILIDADES E INDENIZAÇÕES',
    '5': 'CLÁUSULA 5ª – CANCELAMENTO',
    '6': 'CLÁUSULA 6ª – FORO',
}


def novo_paragrafo(texto, style):
  global y
  p = Paragraph(texto, style)

  x_max = 515
  y_max = 800

  _, y_restante = p.wrapOn(pdf, x_max, y_max)

  if y - y_restante < 80:
    pdf.showPage()  
    y = 800 

  y -= y_restante + 14
  p.drawOn(pdf, x, y)


def intro(cliente, codigo, endereco):
  novo_paragrafo(
      f"Pelo presente instrumento particular, de um lado, <b>VEM FESTEJAR"
      f" JP</b>, inscrita no CNPJ sob o nº 34.126.562/0001-06, com sede na Av."
      f" Henrique Ruffo, nº 223, Jardim Treze de Maio, João Pessoa/PB, doravante"
      f" denominada <b>CONTRATADA</b>, e, de outro lado, <b>{cliente}</b>,"
      f" inscrito(a) no CPF/CNPJ sob o nº <b>{codigo}</b>, residente e"
      f" domiciliado(a) na <b>{endereco}</b>, doravante denominado(a)"
      f" <b>CONTRATANTE</b>, têm entre si justo e contratado o presente"
      f" instrumento de prestação de serviços e locação de bens móveis, que se"
      f" regerá pelas cláusulas e condições a seguir expostas.",
      dic_s["1"],
  )


def c1(titulo, items):
  novo_paragrafo(f"<b>{titulo}</b>", dic_s["2"])

  novo_paragrafo(items_intro, dic_s["1"])

  if items:
    for i in items:
      novo_paragrafo(i, dic_s["3"])
  else:
    return None


def c2(titulo, data, hora, local):
  if not data or not hora or not local:
    return None
  else:
    novo_paragrafo(f"<b>{titulo}</b>", dic_s["2"])
    novo_paragrafo(
        f"O evento objeto deste contrato será realizado na data de"
        f" <b>{data}</b>, às <b>{hora}</b>, no endereço <b>{local}</b>,"
        f" englobando a montagem do cenário e a prestação dos serviços.",
        dic_s["1"],
    )


def c3(titulo, valor, forma_de_pagamento, estado):
  if not valor or not forma_de_pagamento or not estado:
    return None
  else:
    novo_paragrafo(f"<b>{titulo}</b>", dic_s["2"])
    novo_paragrafo(
        f"O valor total ajustado para o presente contrato é de <b>R${valor}"
        f" ({extenso(valor)})</b>, a ser adimplido através de"
        f" <b>{forma_de_pagamento}</b>, constando atualmente como"
        f" <b>{estado}</b>.",
        dic_s["1"],
    )


def c4(titulo, responsabilidade):
  novo_paragrafo(f"<b>{titulo}</b>", dic_s["2"])
  novo_paragrafo(multa, dic_s["1"])
  if responsabilidade:
    for r in responsabilidade:
      novo_paragrafo(r, dic_s["3"])
  else:
    return None

def c5(titulo, tempo, porcentagem):
  novo_paragrafo(f"<b>{titulo}</b>", dic_s["2"])
  novo_paragrafo(
      f"Em caso de solicitação de cancelamento pelo(a) <b>CONTRATANTE</b>"
      f" informada com antecedência mínima de <b>{tempo} ({extenso(tempo)})"
      f" dias</b> da data do evento, haverá a restituição de"
      f" <b>{porcentagem}% ({extenso(porcentagem)} por cento)</b> do valor pago."
      f" Decorrido este prazo, o contrato será considerado rescindido sem"
      f" direito a reembolso de qualquer quantia.",
      dic_s["1"],
  )

def c6(titulo):
  data_contrato = data_por_extenso()
  novo_paragrafo(f"<b>{titulo}</b>", dic_s["2"])
  novo_paragrafo(
      "Fica eleito o Foro da Comarca de <b>João Pessoa/PB</b>, com renúncia"
      " expressa de qualquer outro, por mais privilegiado que seja, para"
      " dirimir quaisquer dúvidas, controvérsias ou litígios oriundos do"
      " presente contrato.",
      dic_s["1"],
  )
  novo_paragrafo(
      "E, por estarem assim justos e contratados, assinam o presente"
      " instrumento em 02 (duas) vias de igual teor e forma, para um só"
      " efeito legal.",
      dic_s["1"],
  )
  novo_paragrafo(f"<b>João Pessoa/PB, {data_contrato}.</b>", dic_s["1"])
   


def gerar_contrato():
  intro(
      "Maria Lucia da Silva",
      "833.740.478-74",
      "Rua Francisca Pereira Nóbrega, 664",
  )

  c1(dic_c["1"], texto_split)

  c2(dic_c["2"], "10/12/2026", "16:00", "Rua Lucas Borges da Silva, 431")

  c3(dic_c["3"], "540", "Pix", "Quitado")

  c4(dic_c["4"], responsabilidades)

  c5(dic_c["5"], "07","30")

  c6(dic_c["6"])


gerar_contrato()

pdf.showPage()
pdf.save()