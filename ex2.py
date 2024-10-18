def contar_letra(string):
    contagem = string.lower().count('a')

    if contagem > 0:
        return f"A letra 'a' aparece {contagem} vez(es) na frase."
    else:
        return "A letra 'a' não aparece na frase."


texto = input("Informe uma frase: ")
print(contar_letra(texto))
