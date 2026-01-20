def filtrar_pares(numeros: list[int]) -> list[int]:
    """
    Recebe uma lista de números e retorna apenas os números pares.
    """
    pares = []

    for n in numeros:
        if n % 2 == 0:
            pares.append(n)

    return pares


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    resultado = filtrar_pares(lista)

    print("Lista original:", lista)
    print("Números pares:", resultado)
