import websocket
import json
import importlib  
limits = importlib.import_module("limits")

live_price_data = []

def on_message(ws, message):
    data = json.loads(message)
    if 'type' in data and data['type'] == 'ticker':
        price = float(data['price'])
        print(f"Live Price: {price}")
        limits.main(price)

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("WebSocket connection closed")

def on_open(ws):
    subscription_message = {
        "type": "subscribe",
        "channels": [{"name": "ticker", "product_ids": ["BTC-USD"]}]
    }
    ws.send(json.dumps(subscription_message))

websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://ws-feed.pro.coinbase.com",
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)
ws.on_open = on_open
