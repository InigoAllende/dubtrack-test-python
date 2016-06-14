import requests
import json
from flask import Flask
app = Flask(__name__)

roomId = ""

@app.route('/')
def get_roomId():
    global roomId
    roomInfo =  json.loads(requests.get("https://api.dubtrack.fm/room/nightblue3").content.decode('utf-8'))
    roomId = roomInfo['data']['_id']
    return roomId

@app.route('/history')
def get_history():
    history = requests.get("https://api.dubtrack.fm/room/"+roomId+"/playlist/history").content
    return history