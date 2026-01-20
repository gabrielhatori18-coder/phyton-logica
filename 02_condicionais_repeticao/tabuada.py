def tabuada(numero: int, ate: int = 10) -> None:
    """
    Exibe a tabuada de um número até o valor informado.
    """
    if numero <= 0:
        print("Digite um número maior que zero.")
        return

    print(f"Tabuada do {numero}")
    print("-" * 20)

    for i in range(1, ate + 1):
        print(f"{numero} x {i} = {numero * i}")


if __name__ == "__main__":
    try:
        n = int(input("Digite um número para ver a tabuada: "))
        tabuada(n)
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
