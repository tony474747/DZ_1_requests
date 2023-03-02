import requests


def max_intelect(superheroe_list):
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    resp = response.json()
    dict_intel_heroes = {}
    for i in resp:
        if i['name'] in superheroe_list:
            dict_intel_heroes.update({i['name']: i['powerstats']['intelligence']})
    return max(dict_intel_heroes)


super_heroes = ['Hulk', 'Captain America', 'Thanos']

print(f'Самый умный супергерой - {max_intelect(super_heroes)}!')
