# coding=utf-8
import numpy as np
import paho.mqtt.client as mqtt
import time

broker = "broker.emqx.io"
port = 1883
topic = "/python/mqtt_simu"
t = []
x = []
y = []
vx = []
vy = []


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)
    client.subscribe(topic, qos=2)


def on_message(client, userdata, msg):
    print("Receiving data")
    data = str(msg.payload)[2: -1].split('#')
    t.append(eval(data[0]))
    x.append(eval(data[1]))
    y.append(eval(data[2]))
    vx.append(eval(data[3]))
    vy.append(eval(data[4]))
    save_res()


def mqtt_sub():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port, 10)
    client.loop_forever()


def save_res():
    f = open('simulation_data.txt', 'w')
    f.write(f't: {t}\n')
    f.write(f'x: {x}\n')
    f.write(f'y: {y}\n')
    f.write(f'vx: {vx}\n')
    f.write(f'vy: {vy}\n')
    f.close()


if __name__ == '__main__':
    mqtt_sub()

