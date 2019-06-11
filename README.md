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
Na parte de conexão com thingspeak só necessario passar para variáveis o servidor do thingspeak, a ID do canal e a chave de escrita do mesmo.



