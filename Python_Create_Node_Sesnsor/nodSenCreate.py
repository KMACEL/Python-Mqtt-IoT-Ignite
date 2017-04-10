#!/usr/bin/env python
#-*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import os
import time
import ssl



def nodsen_on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish(topic=topic.format(clnt_id=gateway_id),
			payload=message_code,
			qos=2)


def nodsen_on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))
    client.disconnect()




gateway_id="python@test@mqtt"
user_name="pythontest"
password="12345678"
topic="{clnt_id}/publish/DeviceProfile/Status/DeviceNodeInventory"

client=mqtt.Client(gateway_id,mqtt.MQTTv311)
client.username_pw_set(user_name,password)
client.tls_set(os.getcwd()+"/GlobalSign_Root_CA.pem", tls_version=ssl.PROTOCOL_TLSv1)

client.on_connect =nodsen_on_connect
client.on_message =nodsen_on_message

client.connect("mqtt.ardich.com", "8883", keepalive=60)


message_code=open(os.getcwd()+"/message.txt")  
message_code=message_code.read()


client.loop_forever()
