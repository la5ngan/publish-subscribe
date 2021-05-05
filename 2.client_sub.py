# import paho mqtt
import paho.mqtt.client as mqtt
# import time for sleep()
import time
# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
     print("message received " , str(message.payload.decode("utf-8")))
########################################
# buat definisi nama broker yang akan digunakan
broker_address="localhost"
# buat client baru bernama P1
print("creating new instance")
client = mqtt.Client("P1")
# kaitkan callback on_message ke client
client.on_message=on_message
# buat koneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=3333)
# jalankan loop client
client.loop_start()
# print topik yang disubscribe (dalam konteks ini, "topik_1" dan "topik_2")
print("Subscribing to topic","topik_1","topik_2")
# loop forever
while True:
    # berikan waktu tunggu 1 detik
    time.sleep(1)
    # client melakukan subscribe ke topik 1 dan topik 2   
    client.subscribe("topik_1")
    client.subscribe("topik_2")
#stop loop
client.loop_stop()