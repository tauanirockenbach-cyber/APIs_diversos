import requests

#Pede para o usuário informar oq deseja buscar
nome = input("Digite um país (em inglês): ")
ano = input("Digite um ano: ")
print("\n")

# Faz a requisição GET
response = requests.get(
    f"https://api.api-ninjas.com/v1/gdp?country={nome}&year={ano}",
    headers={'X-Api-Key': 'te07gI373afhSRB8I8IdbBErZkYmdzefwwHjCedn'},
    timeout=30,
)
# Verifica se a requisição deu certo
response.raise_for_status()

dados = response.json()
if dados:

    #pega o primeiro dado fornecido pela API
    pais = dados[0]

    # Exibe os resultados formatados
    print(f"País: {pais['country']}")
    print(f"Ano: {pais['year']}")
    print(f"PIB: {pais['gdp_growth']}")
else:
    print("Nenhum dado encontrado")
