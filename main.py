#É feito a importação das funções utilizadas do arquivo functions
from src.functions import CalCR, CalCR_curso

def main():
    cr_aluno = CalCR()
    cr_aluno.cr_aluno()

    cr_curso = CalCR_curso()
    cr_curso.cr_curso()

main()