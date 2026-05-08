import json

caminho = r"C:\Users\lenno\OneDrive\Área de Trabalho\nomes.txt"
caminho_json = r"C:\Users\lenno\OneDrive\Área de Trabalho\nomes.json"

with open(caminho,'r',encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    #valor = linhas
    #print(arquivo.read())
    #print(valor[0])

#a = json.dumps(linhas)
#z = " ".join(linhas)

with open(caminho_json, 'w', encoding='utf-8') as arquivo_json:
    json.dump(linhas, arquivo_json, ensure_ascii=False, indent=4)



#for x in a:
#    print(x + z)
#    break
