# proj4_back

## START UP
new directory tab: 
source ~/ga-env/bin/activate

## web socket
redis-server
daphne proj4_back.asgi:application
### postman
ws://127.0.0.1:8000/ws/api
python -m pip install Django

# notes for local test
wss://connect4back.herokuapp.com/ws/api
ws://127.0.0.1:8000/ws/api
{"type": "subscribe",
"id": 1337,
"model": "connect4.Connect4",
"action": "list"}