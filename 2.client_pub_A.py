# import paho mqtt
import paho.mqtt.client as mqtt
# import time untuk sleep()
import time
# import datetime untuk mendapatkan waktu dan tanggal
import datetime
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
# lakukan 20x publish topik "topik_1"
for i in range (20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang dengan topik "topik_1" (SESUAIKAN DENGAN FORMAT DI SOAL)
    print("Publishing message to topic","topik_1")
    client.publish('topik_1', payload=datetime.datetime.now().strftime("AAA %Y, %m, %d, %H, %M, %S"))
#stop loop
client.loop_stop()

