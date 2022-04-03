import openpyxl
import GerarQrcode

def CarregaDados(CaminhoArquivo):
# Abre o Arquivo
    Arquivo = CaminhoArquivo
    book = openpyxl.load_workbook(Arquivo)

    # Seleciona Página
    Pagina = book.active #book.worksheets[0]   #book['Plan1']
    UltimaLinha = 100

    #for linhas in Pagina.iter_rows(min_row=2,max_row=UltimaLinha):
    for linhas in Pagina:
        if linhas[0] != "" and linhas[1] != "":
            GerarQrcode.gerar(linhas[0].value, linhas[1].value)