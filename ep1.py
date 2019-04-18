# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Luis Filipe Carrete, luisfsc@insper.edu.br
# - aluno B: Luís Filipe Loureiro, luisfml@insper.edu.br

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar VR": "Ir jogar um pouco de Realidade Virtual",
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "fumódramo": "ir tomar um ar poluído no fumódramo"
            }
        },
            
        "andar VR": {
            "titulo": "Andar da distração",
            "descricao": "Você sabe que está escolhendo jogar video-game em vez de estudar né estudante",
            "opcoes": { 
                "inicio": "Tomar o elevador para o saguao de entrada",
                "jogar vr": "Ligar o console e joga por horas",
            }
        },
        "jogar vr": {
            "titulo": "jogo infinito",
            "descricao" : "nuca ira sair dessa sala, somente se ganhar.",
            "opcoes": {
                "bater no chefao": "chute um numero de 0 a 10",
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
                "inicio": "Voltar para o saguao de entrada",
                
            }
        },
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
    while not game_over:
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

            print ("\nVocê terá que fazer uma escolha: \n")
            for choice in opcoes:
                print()
                print("{0}: {1}".format(choice,opcoes[choice]))
                print()
            escolha = input("Eai? O que você decidiu fazer? ")

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
