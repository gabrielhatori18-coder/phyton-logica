def eh_primo(n: int) -> bool:
    """
    Verifica se um número é primo.
    Retorna True se for primo, False caso contrário.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 9, 11, 25, 29]
    for x in numeros:
        print(f"{x} -> {eh_primo(x)}")
