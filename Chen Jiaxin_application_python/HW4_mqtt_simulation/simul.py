# coding=utf-8
import numpy as np
import paho.mqtt.client as mqtt
import time

G = 9.8
broker = "broker.emqx.io"

port = 1883
topic = "/python/mqtt_simu"


def simu_mov(vx0, vy0):
    t0 = int(2 * vx0 / G)
    t = np.linspace(0, t0, t0 + 1)
    x = vx0 * t - 0.5 * G * t ** 2
    y = vy0 * t
    vx = vx0 - G * t
    vy = vy0 + t * 0
    return t, x, y, vx, vy


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


def on_publish(client, userdata, mid):
    print('Sending data')


def mqtt_pub(vx0, vy0):
    t, x, y, vx, vy = simu_mov(vx0, vy0)
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(broker, port, 60)
    client.loop_start()
    for i in range(len(t)):
        data = str(t[i]) + '#' + str(format(x[i], '.1f')) + '#' + str(format(y[i], '.1f')) + '#' + str(format(vx[i], '.1f')) + '#' + str(vy[i])
        client.publish(topic=topic, payload=data, qos=2, retain=False)
        time.sleep(2)


if __name__ == '__main__':
    init_vx = eval(input('Please input initial vertical speed:'))
    init_vy = eval(input('Please input initial horizontal speed:'))
    mqtt_pub(init_vx, init_vy)
