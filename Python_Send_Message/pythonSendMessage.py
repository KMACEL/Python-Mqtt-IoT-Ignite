#!/usr/bin/env python
#-*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import os
import time
import ssl



def sendMessage_on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish(topic=topic.format(gateway_id=gateway_id,
    								  nodeName=node_name,
    								  sensorName=sensor_name),
			payload=message_code,
			qos=2)


def sendMessage_on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))
    client.disconnect()




gateway_id="python@test@mqtt"
user_name="pythontest"
password="12345678"

node_name="PythonNode1"
sensor_name="PySens"

topic="{gateway_id}/publish/DeviceProfile/{nodeName}/{sensorName}"

client=mqtt.Client(gateway_id,mqtt.MQTTv311)
client.username_pw_set(user_name,password)
client.tls_set(os.getcwd()+"/GlobalSign_Root_CA.pem", tls_version=ssl.PROTOCOL_TLSv1)

client.on_connect =sendMessage_on_connect
client.on_message =sendMessage_on_message



message_code="""
			{
				data:
				{
					sensorData:
					[
						{
							date: %s,
							values:[%s]
						}
					],
				formatVersion:2
			}
		}""" %(str(time.time())[:10]+"000","150")	


client.connect("mqtt.ardich.com", "8883", keepalive=60)



client.loop_forever()
