money = input("Summa:")

# imena izmeneny na translit

per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}

money = float(money)

deposit = [int(money * per_cent['TKB']*0.01), int(money * per_cent['SKB']*0.01), int(money * per_cent['VTB']*0.01), int(money * per_cent['SBER']*0.01)]

print(deposit)

print("Максимальная сумма, которую вы можете заработать -", max(deposit))