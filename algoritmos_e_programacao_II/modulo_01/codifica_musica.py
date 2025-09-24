substituicoes = {
    'a': '!',
    'e': '@',
    'i': '#',
    'o': '$',
    'u': '%',
    'A': '!', 
    'E': '@',
    'I': '#',
    'O': '$',
    'U': '%'
}

with open("musica.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

texto_codificado = ""
for caractere in conteudo:
    if caractere in substituicoes:
        texto_codificado += substituicoes[caractere]
    else:
        texto_codificado += caractere

nome_arquivo_saida = input("Digite o nome do novo arquivo de saída (ex: musica_codificada.txt): ")

with open(nome_arquivo_saida, "w", encoding="utf-8") as novo_arquivo:
    novo_arquivo.write(texto_codificado)

print("Conversão concluída com sucesso!")