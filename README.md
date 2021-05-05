# publish-subscribe

* Akan dibuat program menggunakan metode indirect communication (publish dan subscribe). 
Broker yang digunakan adalah mqtt mosquito. Sebuah publisher akan mempublish 20 data 
dengan topik bernama “waktu”. Data yang dipublish berupa tanggal dan waktu di server (tahun, 
bulan, hari, jam, menit, detik). Sebuah subscriber akan subscribe topik “waktu” dan menampilkan 
hasilnya

* Akan dibuat program menggunakan metode indirect communication (publish dan subscribe). Broker yang digunakan adalah mqtt mosquito. Sebuah publisher akan mempublish 20 data 
dengan topik bernama “topik_1”. Data berupa waktu (seperti soal no.1) pada komputer A. Format 
data: AAA tahun, bulan, hari, jam, menit, detik. Publisher no. 2 akan mempublish 20 data dengan 
topik bernama “topik_2”. Data berupa random integer pada komputer B. Format data: BBB angka. 
Sebuah subscriber akan mensubscribe pada dua topik yaitu: topik_1 dan topik_2. Subscriber akan 
menampikan semua pesan yang diterimanya.

