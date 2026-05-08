def numeros_primos(n):
    if n < 2:
        return False
        # Verifica divisores de 2 até a raiz quadrada de n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def filtrar_numeros(numeros):
    return[num for num in numeros if numeros_primos(num)]

# numeros usados para saber qual é primo
lista_numeros = [2,3,4,6,8,44,62,32,636,14,32,34,37]
lista_primos = filtrar_numeros(lista_numeros)

print(f"lista:  {lista_numeros}")
print(f"lista primos:  {lista_primos}")

