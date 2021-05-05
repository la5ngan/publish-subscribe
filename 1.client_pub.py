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
# lakukan koneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=3333)
# mulai loop client
client.loop_start()
# lakukan 20x publish waktu dengan topik "waktu"
for i in range (20):
    # sleep 1 detik
    time.sleep(1)
    # client melakukan publish data dengan topik "waktu"
    print("Publishing message to topic","waktu")
    client.publish('waktu', payload=datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S"))
#stop loop
client.loop_stop()

