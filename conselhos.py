import requests
import urllib.request
import random

# CONFIGURAÇÃO: Mude para False se testar em uma rede de internet liberada (ex: em casa)
MODO_SIMULADO = True

if MODO_SIMULADO:
    # Banco de dados local para simular a resposta da API de frases e de tradução
    banco_conselhos = [
        {"q": "The metric for success is not time, it's value.", "a": "Anônimo", "pt": "A métrica para o sucesso não é o tempo, é o valor."},
        {"q": "Believe you can and you're halfway there.", "a": "Theodore Roosevelt", "pt": "Acredite que você pode e você já está no meio do caminho."},
        {"q": "Simplicity is the ultimate sophistication.", "a": "Leonardo da Vinci", "pt": "A simplicidade é o último grau de sofisticação."},
        {"q": "Your time is limited, so don't waste it living someone else's life.", "a": "Steve Jobs", "pt": "Seu tempo é limitado, então não o desperdice vivendo a vida de outra pessoa."},
        {"q": "The only way to do great work is to love what you do.", "a": "Steve Jobs", "pt": "A única maneira de fazer um excelente trabalho é amar o que você faz."}
    ]
    
    # Escolhe um conselho aleatório do banco local
    dados_simulados = random.choice(banco_conselhos)
    
    print("\n--- [AVISO] Executando em MODO SIMULADO devido ao bloqueio da rede corporativa ---")
    print(f"Original ({dados_simulados['a']}): {dados_simulados['q']}")
    print(f"Traduzido: {dados_simulados['pt']}\n")

else:
    # Código real que tenta acessar as APIs externas
    proxies_sistema = urllib.request.getproxies()
    url_quotes = "https://zenquotes.io"

    try:
        resposta_quote = requests.get(url_quotes, proxies=proxies_sistema, timeout=10)
        
        if resposta_quote.status_code == 200:
            dados = resposta_quote.json()
            conselho_ingles = dados[0]["q"]
            autor = dados[0]["a"]
            
            url_tradutor = f"https://translated.net{conselho_ingles}&langpair=en|pt-br"
            resposta_traducao = requests.get(url_tradutor, proxies=proxies_sistema, timeout=10)
            
            if resposta_traducao.status_code == 200:
                dados_traducao = resposta_traducao.json()
                conselho_portugues = dados_traducao["responseData"]["translatedText"]
                
                print(f"\nOriginal ({autor}): {conselho_ingles}")
                print(f"Traduzido: {conselho_portugues}\n")
            else:
                print(f"\nConselho obtido, mas erro na tradução. Original: {conselho_ingles}\n")
        else:
            print(f"Erro na API de frases. Status: {resposta_quote.status_code}")

    except requests.exceptions.JSONDecodeError:
        print("\n[Erro] A rede continua bloqueando o acesso real. Ative o MODO_SIMULADO = True no topo do arquivo.")
    except requests.exceptions.RequestException as e:
        print(f"\n[Erro de Conexão] Falha ao conectar com o servidor: {e}")
