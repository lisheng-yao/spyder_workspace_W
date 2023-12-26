# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 11:03:46 2023

@author: w
"""

import json
import websocket

def on_message(ws, message):
    message = json.loads(message)
    price = message['p']
    print(f"比特幣即時價格（BTC/USDT）: {price}")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### connection closed ###")

def on_open(ws):
    print("Connected to Binance WebSocket API...")

if __name__ == "__main__":
    socket = "wss://stream.binance.com:9443/ws/btcusdt@trade"
    ws = websocket.WebSocketApp(socket, 
                                on_message=on_message, 
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()