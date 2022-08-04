import adivinhacao
import forca

def escolha_jogo():
    print("*********************************")
    print("******Escolha o seu jogo!********")
    print("*********************************")

    print("(1) Forca (2)Adivinhação")


    jogo = int(input("qual jogo?"))

    if (jogo ==1):
        print("jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("jogando adivinhação")
        adivinhacao.jogar()
if(__name__ == "__main__"):
    escolha_jogo()