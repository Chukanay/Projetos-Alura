import random

def jogar():
    print("Você está começando o jogo 'Divination'!")
    print('🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮')
    print('')

    nível = int(input ('Digite seu nível de dificuldade: (1) Fácil; (2) Médio; (3) Dificil:'))
    Número_Secreto = random.randrange(1, 51)
    Pontos = 1000

    if nível == 1:
        Tentativa = 10
        Tentativas_Totais = 10
    elif nível == 2:
        Tentativa = 7
        Tentativas_Totais = 7
    else:
        Tentativa = 5
        Tentativas_Totais = 5


    while Tentativa > 0:
        print("Tentativa {} de {}". format(Tentativa, Tentativas_Totais))
        Resposta = input('Digite um número entre 1 e 50: ')
        Resposta_int = int(Resposta)
        Acertou = Número_Secreto == Resposta_int
        Abaixo = Número_Secreto < Resposta_int
        Acima = Número_Secreto > Resposta_int

        if Resposta_int < 1 or Resposta_int > 50:
            print('Você inseriu um valor não aceitável, tente novamente.')
            continue

        print("Você escolheu:", Resposta)
        if Acertou:
            print('PARABÉNS! VOCÊ ACERTOU!')
            print('🎇🌟🎇🌟🏆🏆🏆🌟🎇🌟🎇')
            break
        else:
            if Abaixo:
                print('Infelizmente essa não é a resposta. O seu palpite foi acima do resultado.')
            elif Acima:
                print('Infelizmente essa não é a resposta. O seu palpite foi abaixo do resultado.')
        Tentativa = Tentativa - 1
        Pontos_perdidos = abs(Número_Secreto - Resposta_int)
        Pontos = Pontos - Pontos_perdidos

    print('')
    print("Fim de Jogo!")

if (__name__ == "__main__"):
    jogar()
