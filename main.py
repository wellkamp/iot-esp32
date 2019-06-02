#Bibliotecas
import wifi
import dht
from machine import Pin
from time import sleep
from umqtt.simple import MQTTClient

sensor = dht.DHT11(Pin(14))

wifi.connect()

SERVER = "mqtt.thingspeak.com"
CHANNEL_ID = "785472"
WRITE_API_KEY = "OCZTDDDZ6VQZSTJH"

client = MQTTClient("umqtt_client", SERVER)

topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY

while True:
  sensor.measure()
  valorTemp = sensor.temperature()
  valorHum = sensor.humidity()
  print('Temperatura: %3.1f C' %valorTemp)
  print('umidade: %3.1f %%' %valorHum)
  payload = "field1="+str(valorTemp)+"&field2="+str(valorHum)

  client.connect()
  client.publish(topic, payload)
  client.disconnect()
  sleep(1800)



