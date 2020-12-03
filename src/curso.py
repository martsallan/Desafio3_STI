from src.createDF import *

class Curso:
    #Inicialização de cada curso
    def __init__(self):
        #Cada curso tem seu código e do seu documento tipo DataFrame
        self.cod = None
        self.documento = criarDataFrame()

    #Os gets e sets da classe Curso
    def setCodCurso(self, codCurso):
        self.cod = codCurso

    def getCodCurso(self):
        return self.cod

    def getDocumento(self):
        return self.documento

    def setDocumento(self,doc):
        self.documento = doc

    def getTamanho(self,document):
        #Tamanho Total do Documento
        return int(document.size/document.columns.size)

    #Verificar Média do curso estudado
    def verificarMedia(self):
        document = self.getDocumento()
        nota = 0
        totalCargaHoraria = 0
        tamTotal = self.getTamanho(document)
        for i in range(tamTotal):
            carga = document['CARGA_HORARIA'][i]
            nota += (document['NOTA'][i]*carga)
            totalCargaHoraria += carga

        media = nota/totalCargaHoraria
        return media