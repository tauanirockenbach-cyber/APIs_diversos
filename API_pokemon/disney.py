import requests

nome = input("Digite o nome do seu personagem: ")

# Endpoint correto da API REST da Disney para filtragem por nome
url = f"https://api.disneyapi.dev/character?name={nome}"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    resultados = dados.get("data", [])
    
    # Verifica se a lista de resultados não está vazia
    if isinstance(resultados, list) and len(resultados) > 0:
        princesa = resultados[0]  # Pega a primeira correspondência
        print(f"Personagem encontrada: {princesa['name']}")
        
        # Obtém e exibe os filmes do personagem
        filmes = princesa.get("films", [])
        if filmes:
            print(f"Filmes: {', '.join(filmes)}")
        else:
            print("Filmes: Nenhum filme de animação listado.")
            
    elif isinstance(resultados, dict) and "name" in resultados:
        print(f"Personagem: {resultados['name']}")
        
        # Obtém e exibe os filmes caso o retorno venha como dicionário único
        filmes = resultados.get("films", [])
        if filmes:
            print(f"Filmes: {', '.join(filmes)}")
        else:
            print("Filmes: Nenhum filme de animação listado.")
    else:
        print("Não foi possível reconhecer este personagem.")
else:
    print(f"Erro na requisição. Código HTTP: {resposta.status_code}")
