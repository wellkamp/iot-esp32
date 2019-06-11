# Monitoramento na IoT
# Atividade da Disciplina de Sistemas Operacionais II

* Embarcado utilizado: [Esp32](https://www.espressif.com/en/products/hardware/esp32/overview)

* Linguagem de Programação: [MicroPython](https://micropython.org/)

* Ambiente de Desenvolvimento: [uPyCraft](http://docs.dfrobot.com/upycraft/)

* Plataforma de Nuvem na IoT utilizada: [ThingSpeak](https://thingspeak.com/)

## Tutoriais utilizados:
   
   [Primeiro tutorial](https://randomnerdtutorials.com/esp32-esp8266-dht11-dht22-micropython-temperature-humidity-sensor/)
   
   [Segundo tutorial](https://mjrobot.org/2018/06/13/iot-feito-facil-esp-micropython-mqtt-thingspeak/)
   
## Resumo das Funcionalidades:

### Funcionalidades no embarcado:
Neste projeto o embarcado possui a função de monitorar a temperatura e umidade do ar enviando os dados para a plataforma de Nuvem Thingspeak.

#### Componentes utilizados:
[Esp32](https://www.espressif.com/en/products/hardware/esp32/overview)

![esp32](https://user-images.githubusercontent.com/37946947/59139488-9a9c0b80-8969-11e9-99b7-4068a2560d80.jpg)

Sensor DHT11
![Dht11](https://user-images.githubusercontent.com/37946947/59138527-01b6c180-8964-11e9-9311-4a5b48f5fc2a.jpg)
Resistor de 4.7k ilustrado no esquemático abaixo.

![dht_esp32_bb-1](https://user-images.githubusercontent.com/37946947/59139262-53f9e180-8968-11e9-9cf6-65029f9d5bc8.png)




### Funcionalidades na Plataforma de Nuvem na IoT
A plataforma utilizada foi o [thingspeak](https://thingspeak.com/) que teve a função de receber os dados e realizar o gerenciamento dos resultados obtidos pelo sensor DHT11.

### Comentários sobre os Códigos
Ao utilizar o ambiente de desenvolvimento do upycraft é possivel manipular várias das suas bibliotecas. Vou comentar um pouco sobre as mesmas. 

```
import wifi
import network
import dht
from machine import Pin
from time import sleep
from umqtt.simple import MQTTClient
```

Biblioteca "network": Possui as funções que auxiliam no gerenciamento da rede.<p>
Biblioteca "wifi": Função criada para conectar a rede wifi.<p>
Biblioteca "dht": Possui as funções de medir a temperatura e umidade.<p>
Biblioteca "machine": Possui as funções que controlam os pinos da esp.<p>
Biblioteca "time": Possui as função de temporizador.<p>
Biblioteca "umqtt": Possui as funções para conexão utilizando o protocolo MQTT.<p>

Ao utilizar essas bibliotecas o código se torna mais simples de entender. 
Na parte de conexão com thingspeak só é necessario passar para as variáveis o servidor do thingspeak, a ID do canal e a chave de escrita do mesmo. Inicializa então uma váriavel "client" onde é implementado o protocolo MQTT e uma váriavel "topic" onde a mesma é uma URL para conseguir postar os dados no servidor thingspeak.
```
SERVER = "mqtt.thingspeak.com"
CHANNEL_ID = "ID DO CANAL Thingspeak"
WRITE_API_KEY = "Chave Do Canal Thingspeak"
client = MQTTClient("umqtt_client", SERVER)
topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY
```

Na linha 22 é criado um loop que de 30 em 30 minutos monitora a temperatura e atualiza o thingspeak com os valores. Essa função de temporizador se da pela função "sleep(1800)". Na linha 23 é feita a medição do sensor e na linha 24 e 25 é passado para variáveis o valor dessa medição.
Na linha 28 os valores medidos são transformados em string e passados para uma váriavel "payload".
Na linha 29, 30 e 31 respectivamente se faz a conexão com o servidor do thingspeak, publica no canal e logo após desconecta. 
```
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
  ```



