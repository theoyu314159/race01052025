import paho.mqtt.client as mqtt
import os
from time import sleep

while True:
    msg = None

    def on_message(client, userdata, message):
        global msg
        msg = message.payload.decode()
        print(msg)

    client = mqtt.Client()
    client.on_message = on_message
    client.connect("broker.MQTTGO.io", 1883, 60)
    client.subscribe("park01")
    client.loop_start()
    sleep(0.1)
    client.loop_stop()
    client.disconnect()
    if msg:
        print("in")
        msg_array = msg.split()
        try:
            money_str = ""
            with open(f"cars/{msg_array[0]}.txt", "r", encoding="utf-8") as f:
                money_str = f.read()
            money_int = int(money_str)
            money_int += int(msg_array[1])
            with open(f"cars/{msg_array[0]}.txt", "w", encoding="utf-8") as f:
                f.write(str(money_int))
            print(str(money_int), "edit file", msg_array[0])
        except:
            with open(f"cars/{msg_array[0]}.txt", "w", encoding="utf-8") as f:
                f.write(msg_array[1])
            print(msg_array[0], "open file", msg_array[1])
