from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def effectivechart(lis):
    effectivelis = []
    immunelis = []
    notveryeffectivelis = []
    
    index = {
        "normal": 1, "fighting": 2, "flying": 3, "poison": 4, "ground": 5,
        "rock": 6, "bug": 7, "ghost": 8, "steel": 9, "fire": 10,
        "water": 11, "grass": 12, "electric": 13, "psychic": 14,
        "ice": 15, "dragon": 16, "dark": 17, "fairy": 18,
        "stellar": 19, "unknown": 10001
    }
    
    for typ in lis:
        if typ in index:
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

def multiply(effectivelis, immunelis, noteffectivelis):
    supereffective = 1.6
    noteffective = 0.625
    immune = 0.39
    
    types = [
        "normal","fighting","flying","poison","ground","rock","bug","ghost",
        "steel","fire","water","grass","electric","psychic","ice","dragon",
        "dark","fairy","stellar","unknown"
    ]
    
    board = {t: 1.0 for t in types}
    
    for i in range(len(effectivelis)):
        for atk in effectivelis[i]:
            if atk in board: board[atk] *= supereffective
        for atk in noteffectivelis[i]:
            if atk in board: board[atk] *= noteffective
        for atk in immunelis[i]:
            if atk in board: board[atk] *= immune
            
    return board

@app.route('/', methods=['GET', 'POST'])
def index():
    pokemon_data = {}
    top_threats = []
    error = None
    image_url = None

    if request.method == 'POST':
        n = request.form.get('pokemon_name', '').lower().strip()
        
        if n:
            url = f"https://pokeapi.co/api/v2/pokemon/{n}"
            send = requests.get(url)
            
            if send.status_code == 200:
                receive = send.json()
                
                types_list = [t['type']['name'] for t in receive['types']]
                pokemon_data = {
                    'name': receive['name'],
                    'types': types_list
                }
                
                image_url = receive['sprites']['front_default']
                
                effective, immune, notveryeffective = effectivechart(types_list)
                
                result = multiply(effective, immune, notveryeffective)
                
                last = []
                for i in result:
                    if result[i] > 1.0:
                        last.append((i, round(result[i], 2)))
                
                last.sort(key=lambda x: x[1], reverse=True)
                
                top_threats = last[:5]
                
            else:
                error = "Pokemon not found!"
        else:
            error = "Please enter a name."

    return render_template('index.html', 
                           pokemon_name=pokemon_data.get('name'),
                           types=pokemon_data.get('types'),
                           top_threats=top_threats,
                           image_url=image_url,
                           error=error)

if __name__ == '__main__':
    app.run(debug=True)