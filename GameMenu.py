import HangedGame
import DivinationGame

def escolhe_jogo():
    print("*******Escolha o seu jogo!*******")
    print("🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮")

    Jogo = int(input("Qual jogo deseja jogar? (1) Hanged (2) Divination"))

    if(Jogo == 1):
        print("Jogando forca")
        HangedGame.jogar()
    elif(Jogo == 2):
        print("Jogando adivinhação")
        DivinationGame.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
