import requests

def effectivechart(lis):
    effectivelis = []
    immunelis = []
    notveryeffectivelis = []
    index = {
        "normal": 1,
        "fighting": 2,
        "flying": 3,
        "poison": 4,
        "ground": 5,
        "rock": 6,
        "bug": 7,
        "ghost": 8,
        "steel": 9,
        "fire": 10,
        "water": 11,
        "grass": 12,
        "electric": 13,
        "psychic": 14,
        "ice": 15,
        "dragon": 16,
        "dark": 17,
        "fairy": 18,
        "stellar": 19,
        "unknown": 10001
    }
    for typ in lis:
        url = "https://pokeapi.co/api/v2/type/" + str(index[typ])
        send = requests.get(url)
        effectivelis.append([])
        immunelis.append([])
        notveryeffectivelis.append([])
        if send.status_code == 200:
            receive = send.json()
            for i in receive['damage_relations']['double_damage_from']:
                effectivelis[-1].append(i['name'])
            for j in receive['damage_relations']['no_damage_from']:
                immunelis[-1].append(j['name'])
            for z in receive['damage_relations']['half_damage_from']:
                notveryeffectivelis[-1].append(z['name'])
    return effectivelis, immunelis, notveryeffectivelis

def pokemontype(name):
    url = f"https://pokeapi.co/api/v2/pokemon/" + name.lower()
    send = requests.get(url)
    lis = []
    if send.status_code == 404:
        return "Pokemon not found"
    elif send.status_code == 200:
        receive = send.json()
        for i in receive['types']:
            temp = i['type']['name']
            lis.append(temp)
    return lis


def multiply(effectivelis, immunelis, noteffectivelis):
    supereffective = 1.6
    noteffective = 0.625
    immune = 0.39
    types = [
        "normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy","stellar","unknown"
    ]
    board = {t: 1.0 for t in types}
    for i in range(len(effectivelis)):
        for atk in effectivelis[i]:
            board[atk] *= supereffective
        for atk in noteffectivelis[i]:
            board[atk] *= noteffective
        for atk in immunelis[i]:
            board[atk] *= immune
    return board


n = ''
while True:
    n = input()
    if n == 'exit':
        break
    types = pokemontype(n)
    effective, immune, notveryeffective = effectivechart(types)
    result = multiply(effective, immune, notveryeffective)
    last = []
    leng = 0
    for i in result:
        if result[i] > 1:
            last.append([i, round(result[i],2)])
            leng += 1
    last.sort(key=lambda x: x[1], reverse=True)
    if leng <= 5:
        print(last)
    else:
        print(last[:5])