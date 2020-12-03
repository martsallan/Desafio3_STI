#Criação do DataFrame
from src.createDF import *
# Classe Aluno
from src.aluno import Aluno
# Classe Curso
from src.curso import Curso

#Classe responsável com funções para tratar do cálculo de CR do aluno
class CalCR:
    #Cria o conjunto de alunos
    def conjuntoAluno(self,alunos,mat,ini,qtde):
        totalCargaHoraria = 0
        nota = 0
        aluno = Aluno()
        for i in range(ini,tamTotal):
            matricula = doc['MATRICULA'][i]
            if(mat == 0):
                mat = matricula
            if(matricula == mat):
                carga = doc['CARGA_HORARIA'][i]
                nota += (doc['NOTA'][i]*carga)
                totalCargaHoraria += carga
                aluno.inserirNovo(i)
            elif(matricula!=mat or i==tamTotal):
                alunos = aluno.insereAluno(aluno,alunos, mat, nota, totalCargaHoraria)
                qtde+=1
                return self.conjuntoAluno(alunos, matricula,i,qtde)
        qtde+=1
        alunos = aluno.insereAluno(aluno,alunos, mat, nota, totalCargaHoraria)
        return [qtde,alunos]

    #Responsável pela função principal de chamada
    def cr_aluno(self):
        alunos = []
        valor = self.conjuntoAluno(alunos,0,0,0)
        qtde = valor[0]
        alunosTotal = valor[1]
        #print("Qtde: %d" % qtde)

        print("------- O CR dos alunos é: --------")
        for aluno in alunosTotal:
            print("Matricula: %d  -  CR: %.1f"% (aluno.getMatricula(),aluno.getCR()))

#Classe responsável com funções para tratar do cálculo de CR médio do curso
class CalCR_curso:
    #Verifica se o curso já está na lista de Cursos
    def verificaCodCurso(self,cursos, codigo):
        for i in cursos:
            if(i.getCodCurso()==codigo):
                return True
        return False

    #Insere Documento ao curso que o contem
    def insereDocumento(self,cursos,codigo, num):
        for i in cursos:
            if(i.getCodCurso()==codigo):
                i.setDocumento(i.getDocumento().append(doc.loc[num]))
                return

    #Faz uma lista de Cursos para melhor contabilidade
    def organiza(self,cursos):
        qtde = 0
        for i in range(tamTotal):
            codCurso = doc['COD_CURSO'][i]
            valida = self.verificaCodCurso(cursos,codCurso)
            if(valida==False):
                curso = Curso()
                curso.setCodCurso(codCurso)
                curso.setDocumento(curso.getDocumento().append(doc.loc[i]))
                qtde += 1
                cursos.append(curso)
            else:
                self.insereDocumento(cursos,codCurso,i)

        return [qtde,cursos]

    #Chama as funções para realizar objetivos
    def cr_curso(self):
        cursar = []
        valor = self.organiza(cursar)
        qtde  = valor[0]
        cursos = valor[1]
        #print("Qtde: %d" % qtde)

        print("-----------------------------------")
        print("----- Média de CR dos cursos ------")        

        for i in cursos:
            indicesNovos = i.getDocumento().reset_index(drop=True)
            i.setDocumento(indicesNovos)
            media  = i.verificarMedia()

            print("%d  -  %.1f "% (i.getCodCurso(),media))
        print("-----------------------------------")
