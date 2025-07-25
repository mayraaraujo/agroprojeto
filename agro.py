custo_tomate = {
"arrendamento": 5.0,
"mudas": 100,
"insumos": 30,
"mao_obra": 60,
"energia": 500,
}

bruto_tomate = {
"valorKg": 3.0,
"kgHec": 500,
}

custo_abacaxi= {
"arrendamento": 6.00,
"mudas": 100,
"insumos": 60,
"mao_obra": 60,
"energia": 500,
}

bruto_abacaxi = {
"valorKg": 3.0,
"kgHec": 900,
}

custo_banana= {
"arrendamento": 5.0,
"mudas": 100,
"insumos": 20,
"mao_obra": 60,
"energia": 500,
}

bruto_banana = {
"valorKg": 3.0,
"kgHec": 700,
}

custo_morango = {
"arrendamento": 4.0,
"mudas": 100,
"insumos": 30,
"mao_obra": 60,
"energia": 500,
}

bruto_morango = {
"valorKg": 3.0,
"kgHec": 600,
}

custo_laranja = {
"arrendamento": 5.0,
"mudas": 100,
"insumos": 30,
"mao_obra": 60,
"energia": 400,
}

bruto_laranja = {
"valorKg": 3.0,
"kgHec": 800,
}

quantidade_hec = int(input("digite o numero de hectare: "))
produto = input("digite 1 para tomate, 2 para abacaxi, 3 para banana, 4 para morango e 5 para laranja: ")

if produto == "1":
    soma = custo_tomate['arrendamento'] + custo_tomate['mudas'] + custo_tomate['insumos'] + custo_tomate['mao_obra'] + custo_tomate['energia'] 
    valor = soma * quantidade_hec
    lucro_total = bruto_tomate['valorKg'] * bruto_tomate['kgHec'] * quantidade_hec
    lucro_liquido = lucro_total -  valor
    print(f"o seu lucro será: {lucro_liquido}")


elif produto == "2":
    soma = custo_abacaxi['arrendamento'] + custo_abacaxi['mudas'] + custo_abacaxi['insumos'] + custo_abacaxi['mao_obra'] + custo_abacaxi['energia'] 
    valor = soma * quantidade_hec
    lucro_total = bruto_abacaxi['valorKg'] * bruto_abacaxi['kgHec'] * quantidade_hec
    lucro_liquido = lucro_total -  valor
    print(f"o seu lucro será: {lucro_liquido}")

elif produto == "3":
    soma = custo_banana['arrendamento'] + custo_banana['mudas'] + custo_banana['insumos'] + custo_banana['mao_obra'] + custo_banana['energia'] 
    valor = soma * quantidade_hec
    lucro_total = bruto_banana['valorKg'] * bruto_banana['kgHec'] * quantidade_hec
    lucro_liquido = lucro_total -  valor
    print(f"o seu lucro será: {lucro_liquido}")

elif produto == "4":
    soma = custo_morango['arrendamento'] + custo_morango['mudas'] + custo_morango['insumos'] + custo_morango['mao_obra'] + custo_morango['energia'] 
    valor = soma * quantidade_hec
    lucro_total = bruto_morango['valorKg'] * bruto_morango['kgHec'] * quantidade_hec
    lucro_liquido = lucro_total -  valor
    print(f"o seu lucro será: {lucro_liquido}")

elif produto == "5":
    soma = custo_laranja['arrendamento'] + custo_laranja['mudas'] + custo_laranja['insumos'] + custo_laranja['mao_obra'] + custo_laranja['energia'] 
    valor = soma * quantidade_hec
    lucro_total = bruto_laranja['valorKg'] * bruto_laranja['kgHec'] * quantidade_hec
    lucro_liquido = lucro_total -  valor
    print(f"o seu lucro será: {lucro_liquido}")