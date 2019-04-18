import random


def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar VR": "Ir jogar um pouco de Realidade Virtual",
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },    
        "andar VR": {
            "titulo": "Andar da distração",
            "descricao": "Andar para jogar video game em vez de fazer o trabalho",
            "opcoes": { 
                "inicio": "Tomar o elevador para o saguao de entrada",
                "jogar vr": "Ligar o console e joga por horas",
            }
        },
        "jogar vr": {
            "titulo": "jogo infinito",
            "descricao" : "nuca ira sair dessa sala, somente se ganhar.",
            "opcoes": {
                "tentar tirar o oculos": "chute um numero de 0 a 10",
                "desistir": "desista"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    
    vida = 3
    
    coins = 0
    
    
    while not game_over:
        vr = 5
        
        cenario_atual = cenarios[nome_cenario_atual]
        titulo_cenario_atual = cenario_atual['titulo']
        descricao_cenario_atual = cenario_atual['descricao']
        
        
        print(titulo_cenario_atual)
        print("-" * len(titulo_cenario_atual))
        print(descricao_cenario_atual)

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True

        else:
            for e in opcoes:
                print('- ' + e)
            
            escolha = input("O que vai fazer? ")
            
            if escolha == "tentar tirar o oculos":
                chuteVR = int(input("Chute numero de 0 a 10 "))
                while vida > 0 and chuteVR != vr:
                    chuteVR = int(input("Chute numero de 0 a 10 "))
                    if chuteVR != vr:
                        vida -= 1
                        print('Vida: {0}'.format(vida))
                    else:
                        coins += 500
                        print("Escapou e ganhou 500 coins. Agora voce tem {0} coins".format(coins))
                        escolha = "inicio"
                        nome_cenario_atual = "inicio"
                       
                    if vida == 0:
                        game_over = True
        
                
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
