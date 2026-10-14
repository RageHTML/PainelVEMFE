from datetime import datetime
from num2words import num2words
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


def converter_numero_extenso(valor):
  t = num2words(int(valor), lang='pt_BR')
  return t

def data_extenso():
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

pdf_x = 40
pdf_y = 800

texto = '1Bola 2Balo 3mesa 4Mesa'
texto_split = texto.split()


paragrafo = ParagraphStyle(
    'EstiloCorpo', parent=styles['Normal'], fontSize=12, leading=18, alignment=TA_LEFT
)

titulo = ParagraphStyle(
    'EstiloTitulo', parent=styles['Title'], fontSize=14, leading=18, alignment=TA_LEFT
)

bullet = ParagraphStyle(
    'EstiloBullet', parent=styles['Normal'], fontSize=12, leading=18, alignment=TA_LEFT, bulletText='•'
)

tipo_texto = {'1': paragrafo, '2': titulo, '3': bullet}

titulos_clasulas = {
    '1': 'CLÁUSULA 1ª – DO OBJETO',
    '2': 'CLÁUSULA 2ª – DATA E PRAZO',
    '3': 'CLÁUSULA 3ª – VALOR E PAGAMENTO',
    '4': 'CLÁUSULA 4ª – DAS RESPONSABILIDADES E INDENIZAÇÕES',
    '5': 'CLÁUSULA 5ª – CANCELAMENTO',
    '6': 'CLÁUSULA 6ª – FORO',
}

def texto_clasulas(cliente=None, codigo=None, endereco=None, data=None, hora=None, local=None, valor=None, forma_de_pagamento=None, estado=None, tempo=None, porcentagem=None, data_contrato=None):
  dict_textos = {
      'preambulo': (
          f"Pelo presente instrumento particular, de um lado, <b>VEM FESTEJAR "
          f"JP</b>, inscrita no CNPJ sob o nº 34.126.562/0001-06, com sede na "
          f"Av. Henrique Ruffo, nº 223, Jardim Treze de Maio, João Pessoa/PB, "
          f"doravante denominada <b>CONTRATADA</b>, e, de outro lado, "
          f"<b>{cliente}</b>, inscrito(a) no CPF/CNPJ sob o nº "
          f"<b>{codigo}</b>, residente e domiciliado(a) na "
          f"<b>{endereco}</b>, doravante denominado(a) <b>CONTRATANTE</b>, "
          f"têm entre si justo e contratado o presente instrumento de "
          f"prestação de serviços e locação de bens móveis, que se regerá "
          f"pelas cláusulas e condições a seguir expostas."
      ),
      'objetos': (
          "O presente contrato tem como objeto a locação dos bens e materiais "
          "decorativos descritos a seguir, que serão disponibilizados para "
          "o evento:"
      ),
      'data_prazo': (
        f"O evento objeto deste contrato será realizado na data de "
        f"<b>{data}</b>, às <b>{hora}</b>, no endereço <b>{local}</b>, "
        f"englobando a montagem do cenário e a prestação dos serviços."
      ),
      'valor_pagemento': (
        f"O valor total ajustado para o presente contrato é de <b>R${valor} "
        f"({converter_numero_extenso(valor) if valor else ''})</b>, a ser adimplido através de "
        f"<b>{forma_de_pagamento}</b>, constando atualmente como "
        f"<b>{estado}</b>."
      ),
      'declaracao_responsabilidade': (
          "O(A) <b>CONTRATANTE</b> declara-se fiel depositário(a) dos bens "
          "locados e assume integral responsabilidade pela sua conservação "
          "durante todo o período da locação. Em caso de avaria, perda, roubo, "
          "destruição parcial ou total dos itens, o(a) <b>CONTRATANTE</b> "
          "compromete-se a indenizar a <b>CONTRATADA</b> no valor de reposição "
          "de cada material danificado. Para a devida preservação do acervo, "
          "o(a) <b>CONTRATANTE</b> compromete-se a:"
      ),
      'responsabilidades': [
          "Zelar pela integridade dos itens recebidos;",
          (
              "Não molhar, sujar excessivamente ou expor as peças ao sol e "
              "intempéries;"
          ),
          "Não alterar, personalizar ou modificar a estrutura da decoração;",
          (
              "Restituir todos os itens no término do evento nas mesmas "
              "condições em que foram"
          ),
      ],
      'multa': (
        f"Em caso de solicitação de cancelamento pelo(a) <b>CONTRATANTE</b> "
        f"informada com antecedência mínima de <b>{tempo} ({converter_numero_extenso(tempo) if tempo else ''}) "
        f"dias</b> da data do evento, haverá a restituição de "
        f"<b>{porcentagem}% ({converter_numero_extenso(porcentagem) if porcentagem else ''} por cento)</b> do valor pago. "
        f"Decorrido este prazo, o contrato será considerado rescindido sem "
        f"direito a reembolso de qualquer quantia."
      ),
      'forum': [
        (
          "Fica eleito o Foro da Comarca de <b>João Pessoa/PB</b>, com renúncia "
          "expressa de qualquer outro, por mais privilegiado que seja, para "
          "dirimir quaisquer dúvidas, controvérsias ou litígios oriundos do "
          "presente contrato."
        ),
        (
          "E, por estarem assim justos e contratados, assinam o presente "
          "instrumento em 02 (duas) vias de igual teor e forma, para um só "
          "efeito legal."
        ),
        (
          f"<b>João Pessoa/PB, {data_contrato}.</b>"
        ),
      ],
  }

  return dict_textos

def criar_texto(texto, style):
  global pdf_y
  paragrafo = Paragraph(texto, style)

  x_max = 515
  y_max = 800

  _, y_restante = paragrafo.wrapOn(pdf, x_max, y_max)

  if pdf_y - y_restante < 80:
    pdf.showPage()  
    pdf_y = 800 

  pdf_y -= y_restante + 14
  paragrafo.drawOn(pdf, pdf_x, pdf_y)

def contrato_preambulo(cliente, codigo, endereco):
  t = texto_clasulas(cliente=cliente, codigo=codigo, endereco=endereco)
  criar_texto(t['preambulo'], tipo_texto["1"])

def contrato_objeto(items):
  t = texto_clasulas()
  criar_texto(f"<b>{titulos_clasulas['1']}</b>", tipo_texto["2"])
  criar_texto(t['objetos'], tipo_texto["1"])

  if items:
    for i in items:
      criar_texto(i, tipo_texto["3"])
  else:
    return None

def contrato_data_prazo(data, hora, local):
  if not data or not hora or not local:
    return None
  else:
    t = texto_clasulas(data=data, hora=hora, local=local)
    criar_texto(f"<b>{titulos_clasulas['2']}</b>", tipo_texto["2"])
    criar_texto(t['data_prazo'], tipo_texto["1"])

def contrato_valor_pagamento(valor, forma_de_pagamento, estado):
  if not valor or not forma_de_pagamento or not estado:
    return None
  else:
    t = texto_clasulas(valor=valor, forma_de_pagamento=forma_de_pagamento, estado=estado)
    criar_texto(f"<b>{titulos_clasulas['3']}</b>", tipo_texto["2"])
    criar_texto(t['valor_pagemento'], tipo_texto["1"])

def contrato_responsabilidade():
  t = texto_clasulas()
  criar_texto(f"<b>{titulos_clasulas['4']}</b>", tipo_texto["2"])
  criar_texto(t['declaracao_responsabilidade'], tipo_texto["1"])
  for r in t['responsabilidades']:
    criar_texto(r, tipo_texto["3"])

def contrato_multa(tempo, porcentagem):
  t = texto_clasulas(tempo=tempo, porcentagem=porcentagem)
  criar_texto(f"<b>{titulos_clasulas['5']}</b>", tipo_texto["2"])
  criar_texto(t['multa'], tipo_texto["1"])

def contrato_forum():
  data_contrato = data_extenso()
  t = texto_clasulas(data_contrato=data_contrato)
  criar_texto(f"<b>{titulos_clasulas['6']}</b>", tipo_texto["2"])
  for f in t['forum']:
    criar_texto(f, tipo_texto['1'])
   
def gerar_contrato():
  contrato_preambulo("Maria Lucia da Silva", "833.740.478-74", "Rua Francisca Pereira Nóbrega, 664")
  contrato_objeto(texto_split)
  contrato_data_prazo("10/12/2026", "16:00", "Rua Lucas Borges da Silva, 431")
  contrato_valor_pagamento("540", "Pix", "Quitado")
  contrato_responsabilidade()
  contrato_multa("07", "30")
  contrato_forum()

gerar_contrato()
pdf.showPage()
pdf.save()