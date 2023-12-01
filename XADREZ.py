import chess
import chess.svg
import random

def escolher_jogada_aleatoria(tabuleiro):
    jogadas_possiveis = list(tabuleiro.legal_moves)
    jogada_aleatoria = random.choice(jogadas_possiveis)
    return jogada_aleatoria.uci()

def calcular_jogada(tabuleiro):
    print("Calculando jogada...")
    jogada = escolher_jogada_aleatoria(tabuleiro)
    print(f"Jogada calculada: {jogada}")
    return jogada

def uci_loop():
    while True:
        comando = input()
        if comando == "uci":
            print("id name Xadrez aleatório")
            print("id authors João Cruz, Wendril, Cristovam")
            print("uciok")
        elif comando == "isready":
            print("readyok")
        elif comando.startswith("position"):
            partes = comando.split()
            if "startpos" in partes:
                tabuleiro = chess.Board()
            else:
                fen = " ".join(partes[2:])
                tabuleiro = chess.Board(fen)
        elif comando.startswith("go"):
            jogada = calcular_jogada(tabuleiro)
            print(f"bestmove {jogada}")
        elif comando == "quit":
            break

if __name__ == "__main__":
    uci_loop()
