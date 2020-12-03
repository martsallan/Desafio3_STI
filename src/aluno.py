from src.createDF import *

class Aluno:
    # Inicialização dos objetos necessários para um Aluno
    def __init__(self):
        self.mat = None
        self.cr = None
        self.documento = criarDataFrame()

    # Gets e sets da classe Aluno
    def setMatricula(self, matricula):
        self.mat = matricula

    def getMatricula(self):
        return self.mat

    def setCR(self, cr):
        self.cr = cr

    def getCR(self):
        return self.cr

    def setDocumento(self, doc):
        self.documento = doc

    def getDocumento(self):
        return self.documento

    # Função que calcula CR do aluno
    def calculaCR(self, nota, totalCargaHoraria):
        cr = 0
        cr = nota/totalCargaHoraria
        return cr

    # Insere novo dado do aluno
    def inserirNovo(self, i):
        self.setDocumento(self.getDocumento().append(doc.loc[i]))

    # Insere informações do aluno à lista
    def insereAluno(self, aluno, alunos, mat, nota, totalCargaHoraria):
        aluno.setMatricula(mat)
        cr = aluno.calculaCR(nota, totalCargaHoraria)
        aluno.setCR(cr)
        alunos.append(aluno)
        return alunos