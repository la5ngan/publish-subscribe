# import paho mqtt
import paho.mqtt.client as mqtt
# import time untuk sleep()
import time
# import random dari library numpy
from numpy import random
# buat callback on_publish untuk publish data
########################################
def on_publish(client, userdata, mid):
    print("on_publish, mid {}".format(mid))
########################################
# definisikan nama broker yang akan digunakan
broker_address="localhost"
# buat client baru bernama P2
print("creating new instance")
client = mqtt.Client("P2")
# kaitkan callback on_publish ke client
client.on_publish=on_publish
# koneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=3333)
# mulai loop client
client.loop_start()
# lakukan 20x publish topik "topik_2"
for i in range (20):
    # sleep 1 detik
    time.sleep(1)
    # munculkan angka random
    rand = random.random()
    # publish angka yang muncul dengan topik "topik_2" (SESUAIKAN DENGAN FORMAT DI SOAL)
    print("Publishing message to topic","topik_2")
    client.publish("topik_2",rand)
#stop loop

