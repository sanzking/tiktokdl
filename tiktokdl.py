import requests as req
import json
import os
import time

os.system('clear')
x = '\x1b'
y = '['
z = ';'
abu = x + y + '90m'
merah = x + y + '91m'
hijau = x + y + '92m'
kuning = x + y + '93m'
biru = x + y + '94m'
ungu = x + y + '95m'
birumud = x + y + '96m'
putih = x + y + '37m'
kotak = x + y + '47' + z + '30m'
bersih = x + y + 'm'

try:
	print(f"{kotak} TiktokDownloader | sanzking {bersih}")
	url   = input(f"\n{putih}enter url : ")
	file = input(f"{birumud}masukan nama output : {bersih}")
	print()
	print(end=f"\r{putih}Downloading █▒▒▒▒▒▒▒▒▒▒▒▒▒ 0%")
	time.sleep(1)
	print(end=f"\r{putih}Downloading ███▒▒▒▒▒▒▒▒▒▒▒ 20%")
	time.sleep(1)
	print(end=f"\r{putih}Downloading █████▒▒▒▒▒▒▒▒▒ 30%")
	time.sleep(1)
	print(end=f"\r{putih}Downloading ███████▒▒▒▒▒▒▒ 50%")
	try:
		raw = req.get(f"https://fzn-gaz.herokuapp.com/api/tiktok?url={url}", timeout=5).text
		js = json.loads(raw)
		ah = js['result']
		r = req.get(ah, allow_redirects=True)
		print(end=f"\r{putih}Downloading ██████████▒▒▒▒ 70%")
		time.sleep(1)
		print(end=f"\r{putih}Downloading ██████████████ 100%\n")
		time.sleep(1)
		print(end=f"\r{putih}File berhasil disimpan dengan nama {file}.mp4\n")
		open(f'/sdcard/{file}.mp4', 'wb').write(r.content)
	except:
		pass
except KeyError:
	print(f"{merah}Url yang anda masukan salah!!!{bersih}")
except KeyboardInterrupt:
	print(f"{merah}Diberhentikan!!!{bersih}")
