#!/usr/bin/env python
import paho.mqtt.client as mqtt
import time
import random

host = "67.205.170.247"
port = 1883
topic = "iot/cmd/variables/fmt/json/PARAGUAY/POC/ATM1"
topic1 = "iot/evt/result/fmt/json/PARAGUAY/POC/ATM1"
username = "banco"
password = "demostracion"
rele = True
i = 0

#def publicado(client, userdata, result):
#    print("Publicado...")
#    pass
#
#def conectado(client, userdata, result):
#    print("Conectado..")
#    pass

def onSubscribe(topic, payload):
    client1.publish(topic, payload)
    
    pass


client1 = mqtt.Client()                                               #constructor
client1.username_pw_set(username, password)
#client1.on_publish = publicado
# client1.on_connect = conectado
client1.connect(host, port)


for n in range(1, 11):
    intrele = int(rele == True)
    #payload = '{"d":{"variable":"rele","paso":' + str(n) + ',"valor":' + str(intrele) +' }}'
    payload = '{"d":{"variables":"rele","valor":' + str(intrele) +', "paso":' + str(n) + ' }}'
    payload1 = '{"d":{"result": 200, "variable":' "rele"', "valor":' + str(intrele) + ' }}'
    rele = not rele
    ret = client1.publish(topic, payload)
    i += 1
    print(i)
    client1.on_subscribe = onSubscribe(topic1, payload1)

    x = random.uniform(0.1, 10.0)
    time.sleep(x) 

print("Terminado......")