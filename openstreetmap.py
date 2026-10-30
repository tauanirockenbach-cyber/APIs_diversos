from geopy.geocoders import ArcGIS

geolocator = ArcGIS()

try:
    print("Buscando locais... Por favor, aguarde.\n")
    
    locais = geolocator.geocode("restaurantes em Schroeder", exactly_one=False)
    
    if not locais:
        print("Nenhum local encontrado para esta busca.")
    else:
        # Limitamos os resultados exibidos usando uma fatia do Python [:10]
        resultados = locais[:10]
        
        print(f"--- Exibindo {len(resultados)} locais encontrados --- \n")
        for lugar in resultados:
            print(f"📍 {lugar.address}")
            print(f"   Coordenadas: Lat {lugar.latitude}, Lon {lugar.longitude}")
            print("-" * 50)

except Exception as e:
    print(f"Ocorreu um erro ao buscar os dados: {e}")
