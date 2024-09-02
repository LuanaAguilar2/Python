#Mini Akinator
import random

#Personagens
personagens = ["Law",
               "Kento Nanami",
               "Shanks",
               "Megumi Fushiguro",
               "Miss Fortune",
               "Teemo",
               "Master Yi",
               "Max",
               "Lucas",
               "Velma",
               "Mabel",
               "Rammus",
               "Yuumi"]

# Características
caracteristicas = {
    "Law": {"irmaos": False, "anime": True, "netflix": False, "espada": True, "desenho": False, "jogo": False,
            "poder": True, "one_piece": True, "jujutsu": False, "ruivo": False, "loiro": False,
            "animal": False,"espinhos":False,"conecta":False,"invisivel":False},

    "Kento Nanami": {"irmaos": False, "anime": True, "netflix": False, "espada": False, "desenho": False, "jogo": False,
                     "poder": True, "one_piece": False, "jujutsu": True, "ruivo": False, "loiro": True,
                     "animal": False,"espinhos":False,"conecta":False,"invisivel":False},

    "Shanks": {"irmaos": False, "anime": True, "netflix": False, "espada": True, "desenho": False, "jogo": False,
               "poder": True, "one_piece": True, "jujutsu": False, "ruivo": True, "loiro": False,
               "animal": False,"espinhos":False,"conecta":False,"invisivel":False},

    "Megumi Fushiguro": {"irmaos": False, "anime": True, "netflix": False, "espada": False, "desenho": False, "jogo": False,
                         "poder": True, "one_piece": False, "jujutsu": True, "ruivo": False, "loiro":False,
                         "animal": False,"espinhos":False,"conecta":False,"invisivel":False},

    "Miss Fortune": {"irmaos": False, "anime": False, "netflix": False, "espada": False, "desenho": False, "jogo": True,
                     "poder": False, "one_piece": False, "jujutsu": False, "ruivo": True, "loiro": False,
                     "animal": False,"espinhos":False,"conecta":False,"invisivel":False},

    "Teemo": {"irmaos": False, "anime": False, "netflix": False, "espada": False, "desenho": False, "jogo": True,
              "poder": True, "one_piece": False, "jujutsu": False, "ruivo": False, "loiro": False,
              "animal": True,"espinhos":False,"conecta":False,"invisivel":True},

    "Master Yi": {"irmaos": False, "anime": False, "netflix": False, "espada": True, "desenho": False, "jogo": True,
                  "poder": False, "one_piece": False, "jujutsu": False, "ruivo": False, "loiro": False,
                  "animal": False,"espinhos":False,"conecta":False,"invisivel":False},

    "Rammus":{"irmaos": False, "anime": False, "netflix": False, "espada": False, "desenho": False, "jogo": True,
              "poder": True, "one_piece": False, "jujutsu": False, "ruivo": False, "loiro": False,
              "animal": True, "espinhos":True,"conecta":False,"invisivel":False},

    "Yuumi": {"irmaos": False, "anime": False, "netflix": False, "espada": False, "desenho": False, "jogo": True,
              "poder": True, "one_piece": False, "jujutsu": False, "ruivo": False, "loiro": False,
              "animal": True,"espinhos":False,"conecta":True,"invisivel":False},

    "Max": {"irmaos": True, "anime": False, "netflix": True, "espada": False, "desenho": False, "jogo": False,
            "poder": False, "one_piece": False, "jujutsu": False, "ruivo": True, "loiro": False,
            "animal": False,"espinhos":False,"conecta":False,"invisivel":False},

    "Lucas": {"irmaos": True, "anime": False, "netflix": True, "espada": False, "desenho": False, "jogo": False,
              "poder": False, "one_piece": False, "jujutsu": False, "ruivo": False, "loiro": False,
              "animal": False,"espinhos":False,"conecta":False,"invisivel":False},

    "Velma": {"irmaos": False, "anime": False, "netflix": False, "espada": False, "desenho": True, "jogo": False,
              "poder": False, "one_piece": False, "jujutsu": False, "ruivo": False, "loiro": False,
              "animal": False,"espinhos":False,"conecta":False,"invisivel":False},

    "Mabel": {"irmaos": True, "anime": False, "netflix": True, "espada": False, "desenho": True, "jogo": False,
              "poder": False, "one_piece": False, "jujutsu": False, "ruivo": False, "loiro": False,
              "animal": False,"espinhos":False,"conecta":False,"invisivel":False}
}

# Definindo as caracteristicas para as perguntas
perguntas = {
    "Seu personagem tem irmão ou irmã?": "irmaos",
    "Seu personagem é de anime?": "anime",
    "Seu personagem é da Netflix?": "netflix",
    "Seu personagem usa espada?": "espada",
    "Seu personagem é de desenho animado?": "desenho",
    "Seu personagem é de jogo?": "jogo",
    "Seu personagem tem poder?": "poder",
    "Seu personagem é de One Piece?": "one_piece",
    "Seu personagem é de Jujutsu?": "jujutsu",
    "Seu personagem é ruivo?": "ruivo",
    "Seu personagem é loiro?": "loiro",
    "Seu personagem é um animal?": "animal",
    "Seu personagem tem espinhos": "espinhos",
    "Seu personagem se conecta com outros personagens?:": "conecta",
    "Seu personagem pode ficar invisível por alguns segundos?": "invisivel"
}

# Exibir personagens
def exibir_personagens(personagens):
   print("Escolha um personagem")
   for i, personagem in enumerate(personagens, 1):
        print(f"{i}. {personagem}")

# Não repetir perguntas
def filtrar_perguntas_validas(personagens, perguntas, caracteristicas):
    perguntas_validas = []
    for pergunta, caract in perguntas.items():
        valores = {caracteristicas[p][caract] for p in personagens}
        if len(valores) > 1:
            perguntas_validas.append(pergunta)
    return perguntas_validas

while personagens:
    exibir_personagens(personagens)

    # Perguntas para os personagens restantes
    perguntas_validas = filtrar_perguntas_validas(personagens, perguntas, caracteristicas)

    # Sorteio de perguntas
    pergunta = random.choice(perguntas_validas)

    resposta = input(f"\n{pergunta} (digite: 1 para sim/2 para não): ").strip().lower()

    if resposta == '1':
        personagens = [p for p in personagens if caracteristicas[p][perguntas[pergunta]]]
    elif resposta == '2':
        personagens = [p for p in personagens if not caracteristicas[p][perguntas[pergunta]]]
    else:
        print("Resposta inválida, por favor responda com 's' ou 'n'.")
        continue

    if len(personagens) == 1:
        print(f"\nO personagem que você escolheu é: {personagens[0]}!")
        break
