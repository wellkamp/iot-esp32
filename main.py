#Bibliotecas
import wifi
import dht
from machine import Pin
from time import sleep
from umqtt.simple import MQTTClient

#Pino Utilizado
sensor = dht.DHT11(Pin(14))

#Chamando a função para conectar-se ao Wifi
wifi.connect()

#Passando os dados do Thingspeak para variáveis
SERVER = "mqtt.thingspeak.com"
CHANNEL_ID = "ID DO CANAL Thingspeak"
WRITE_API_KEY = "Chave Do Canal Thingspeak"
client = MQTTClient("umqtt_client", SERVER)
topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY

#Código que faz a publicação
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



