import json
import requests
import datetime

nick = ''
token = 'RGAPI-706f9dd9-da82-45c0-a94d-ea8cb637c6ef'
# requisição status do LoL
r_status = requests.get('https://br1.api.riotgames.com/lol/status/v4/platform-data?api_key='+token)
r_summoner = requests.get('https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nick+'?api_key='+token)

result_status = json.loads(r_status.content)

# Requisição status do Invocador
nick = str(input('Qual o seu nick no jogo para sabermos o seu lvl? '))


def dadosInvocador(nome):
    r_summoner = requests.get('https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nick+'?api_key='+token)
    result_summoner = json.loads(r_summoner.content)
    print(result_summoner)
    print('Seu LVL é: '+ str(result_summoner['summonerLevel']))

dadosInvocador(nick)




