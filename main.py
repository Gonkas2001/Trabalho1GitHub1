print("Olá, espero que estejas bem!")


def pedir_nome():

    nome = input("Como te chamas? ")

    print(f"Espero que aprender a usar GitHub seja fácil para ti, {nome}")


def perguntar():

    while True:

        resposta = input("Tens dúvidas com o GitHub? (s/n) ").lower()

        if resposta in ["s", "sim"]:
            print("Ooops!")

        elif resposta in ["n", "nao", "não"]:
            print("Boa!")

        else:
            print("Resposta inválida.")

        continuar = input("Queres continuar? (s/n) ").lower()

        if continuar not in ["s", "sim"]:
            print("Adeus!")
            break

pedir_nome()
perguntar()