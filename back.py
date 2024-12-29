import paho.mqtt.client as mqtt
from time import sleep

while True:
    msg = None

    def on_message(client, userdata, message):
        msg = message.payload.decode()

    client = mqtt.Client()
    client.on_message = on_message
    client.connect("broker.mqttgo.io", 1883, 60)
    client.subscribe("race01")
    client.loop_start()
    while msg is None:
        sleep(0.1)
    client.loop_stop()
    client.disconnect()
    print("msg on")
    msg_array = msg.split()
    try:
        money_str = ""
        with open(f"{msg_array[0]}.txt", "r", encoding="utf-8") as f:
            money_str = f.read()
        money_int = int(money_str)
        money_int += int(msg_array[1])
        with open(f"{msg_array[0]}.txt", "w", encoding="utf-8") as f:
            f.write(money_int)
        print(str(money_int), " ", msg_array[0])
    except:
        with open(f"{msg_array[0]}.txt", "w", encoding="utf-8") as f:
            f.write(msg_arr[1])
        print(msg_arr[0], " ", msg_arr[1])
