#-*- coding:utf-8 -*-
import websocket
import gzip
import time
ws = websocket.WebSocket()
ws.connect("wss://api.huobipro.com/ws",http_proxy_host ="127.0.0.1",http_proxy_port =1080 )
print(ws.recv())
# 订阅 KLine 数据
tradeStr="""{"sub": "market.ethusdt.kline.1min","id": "id10"}"""
# 请求 KLine 数据
# tradeStr="""{"req": "market.ethusdt.kline.1min","id": "id10", "from": 1513391453, "to": 1513392453}"""
#订阅 Market Depth 数据
# tradeStr="""{"sub": "market.ethusdt.depth.step5", "id": "id10"}"""
#请求 Market Depth 数据
# tradeStr="""{"req": "market.ethusdt.depth.step5", "id": "id10"}"""
#订阅 Trade Detail 数据
# tradeStr="""{"sub": "market.ethusdt.trade.detail", "id": "id10"}"""
#请求 Trade Detail 数据
# tradeStr="""{"req": "market.ethusdt.trade.detail", "id": "id10"}"""
#请求 Market Detail 数据
# tradeStr="""{"req": "market.ethusdt.detail", "id": "id12"}"""
ws.send(tradeStr)
while True:
    compressData=ws.recv()
    result=gzip.decompress(compressData).decode('utf-8')
    if result[:7] == '{"ping"':
        ts=result[8:21]
        pong='{"pong":'+ts+'}'
        ws.send(pong)
        ws.send(tradeStr)
    else:
        print(result)
