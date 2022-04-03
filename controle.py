from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox #Caixa de mensagem

import GerarQrcode
import Excel

def exibir_mensagem():
    QMessageBox.about(janela,"Concluido","Arquivos Gerados com Sucesso!")

def ComPlanilha(caminho):
    caminho = janela.txtPlanilha.text()
    Excel.CarregaDados(caminho)

def GerarCodigo():
    if janela.rbDigitado.isChecked() == True:
        conteudo = janela.txtConteudo.text()
        arquivo = janela.txtNomeArquivo.text()
        
        GerarQrcode.gerar(conteudo, arquivo)

        exibir_mensagem()

    elif janela.rbPlanilha.isChecked() == True:
        caminho = janela.txtPlanilha.text()        
        ComPlanilha(caminho)

        exibir_mensagem()

#Carrega a Janela criada no PyQT
NomeDaJanela = 'Janela.ui'
app=QtWidgets.QApplication([])
janela=uic.loadUi(NomeDaJanela)


#Dispara função do botão
janela.btoGerar.clicked.connect(GerarCodigo)

janela.show()
app.exec()