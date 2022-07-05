from riotwatcher import LolWatcher, ApiError
import pandas as pd
import mysql.connector
from mysql.connector import Error
import json


# golbal variables
api_key = 'RGAPI-b0fa0c6b-e9f9-4eb5-8910-62c2cf239f18'
watcher = LolWatcher(api_key)
my_region = 'na1'
summoner_name = 'What She 0rder'
host_name = '192.168.1.21'
user_name = 'root'
user_password = '981273465aA!'
port = '49153'

def create_server_connection(host_name, user_name, user_password, port):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            port=port
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
connection = create_server_connection(host_name, user_name, user_password, port)
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

me = watcher.summoner.by_name(my_region, summoner_name)
my_matches = watcher.match.matchlist_by_puuid(my_region, me['puuid'],0,100,400)

for x in my_matches:
    game = watcher.match.by_id(my_region,x)
    info = game['info']
    teams = info['teams']
    participants = info['participants']
    team1 = teams[0]
    bans1 = team1['bans']
    obj1 = team1['objectives']
    team2 = teams[1]
    bans2 = team2['bans']
    obj2 = team2['objectives']
    #with open('json_data.json', 'a') as outfile:
   #     outfile.write(json.dumps(game))
    continue