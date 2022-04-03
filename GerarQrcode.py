import qrcode
def gerar(conteudo, arquivo):
    img = qrcode.make(conteudo)
    type(img)
    img.save(arquivo + ".png")