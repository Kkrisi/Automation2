# Cmd-ben pip install-old a szükséges modulokat/könyvtárakat
import pyautogui as py
import time
import random
import keyboard



# Hogy könnyne megtaláljuk parancssorban a program kezdetét
print("***********************************************************************************************************************")
print("***********************************************************************************************************************")






def kepcsinalas():
	time.sleep(2)
	for i in range(1):
		time.sleep(2)
		image=py.screenshot()
		image.save(r"C:\Users\banan\Desktop\kepcsinalas.png")



# Szétszedve a szó, mert elsőre nem mindig tölti be
py.press("winleft")
time.sleep(1)
py.write(".i")
time.sleep(1)
py.write("so")
time.sleep(1)

# Ha nincs iso fájl a gépen, akkor letölti valamelyik, pl 2012-t

# Választási lehetőségek, amiből a program majd választ
lista=["2022","2012","2008"]



# Start menübe iso fájlok keresése, ha lehet akkor a legujabbat haszánlja
		# Ugy is lehet hogy nem remove-olja, hanem else-nél adja hozzá a listához a számokat, akkor érdemes ha sorokat spórolunk vele
try:
	x, y = py.locateCenterOnScreen('2022iso.png', confidence=0.9)
except TypeError:
	print("Nincs 2022-iso fájl a gépen")
	print("--------------------------")
	lista.remove("2022")

	try:
		x, y = py.locateCenterOnScreen('2012iso.png', confidence=0.9) # confidence = ha a legjobban ráhasonlíto dolgot keressük
	except TypeError:
		print("Nincs 2012-iso fájl a gépen")
		print("--------------------------")
		lista.remove("2012")

		try:
			x, y = py.locateCenterOnScreen('2008iso.png', confidence=0.9)
		except TypeError:
			print("Nincs 2008-iso fájl a gépen")
			print("--------------------------")
			print("Nincs egy szerver iso fájl se ezen a gépen, menj lovásznak!")
			print("-----------------------------------------------------------")
			lista.remove("2008")

		else:
			print(f"Siker, ellenben van 2008-iso a gépen")
			py.moveTo(x,y)
	else:
		print(f"Siker, ellenben van 2012-iso a gépen")
		lista.remove("2008")
		py.moveTo(x,y)
else:
	print(f"Siker, van 2022-iso a gépen")
	lista.remove("2012")
	lista.remove("2008")
	py.moveTo(x,y)
time.sleep(1)



# Virtualbox indítása
		# ? Ellenorzes hogy van e virtualbox azon a gépen e? (nem muszaly)
py.press("winleft")
time.sleep(1)
py.write("VirtualBox")
time.sleep(1)
py.press("enter")
time.sleep(3)



# Virtualbox frissités pop up ablak esetére
		# Muszály 1mp-re rakni a várakozási időt, vagy különben bugok merülnek fel és nem találja a fájlt
x = True
while x == True:
	try:
		x, y = py.locateCenterOnScreen('infoicon.png', confidence=0.7)
		py.moveTo(x,y)
		time.sleep(0.5)
		try:
			x, y = py.locateCenterOnScreen('ok.png', confidence=0.6)
			py.moveTo(x,y)
			time.sleep(0.5)
			py.click()
			print("Siker, frissítés infó letudva")
		except:
			print("Nincs vagy nem sikerült megtalálni a pop up ablakot 1.0")
			break
	except:
		print("Nincs vagy nem sikerült megtalálni a pop up ablakot 2.0")
		break
time.sleep(1)



# Teljes képernyőre rakni a virtualboxot
py.keyDown("winleft")
py.press("up")
py.keyUp("winleft")
time.sleep(1)



# 'Új' gomb keresése (új virtuális gépnek)
try:
	x, y = py.locateCenterOnScreen('newbutton.png', confidence=0.9)
	py.moveTo(x,y)
	time.sleep(1)
	py.click(x,y)
except TypeError:
	print("Szerecsétlen vagyok és nem találtam meg az 'új' gombot")
	print("------------------------------------------------------")
else:
	pass
time.sleep(1)


	#ide bele kellene írni az aktuálisan használt win fajtát is pl Windows_2012_5235324523
	#ˇˇˇ
# Random virtuális gép név adás
randomlist = []
for i in range(0,5):
	n = random.randint(1,100000000)
	randomlist.append(n)
py.write("WindowsServer_")
time.sleep(0.5)
py.write(lista[0])
time.sleep(0.5)
py.write("_")
time.sleep(0.5)
py.write(str(randomlist[0]))
time.sleep(1)



# Név megadástól elmenni az verzió kiválasztásáig
for click in range(3):
	py.press("tab")
	time.sleep(0.5)



# Verzió választás, a talált iso fájlhoz
if("2008" in lista):
	x = True
	while x == True:
		try:
			x, y = py.locateCenterOnScreen('win2008.png')
			print("Sikerült kiválasztani a megfelelő win2008 iso fájlt")
			print("---------------------------------------------------")
			x = False
		except:
			x = True
			py.press("down")
elif("2012" in lista):
	x = True
	while x == True:
		try:
			x, y = py.locateCenterOnScreen('win2012.png')
			print("Sikerült kiválasztani a megfelelő win2012 iso fájlt")
			print("---------------------------------------------------")
			x = False
		except:
			x = True
			py.press("down")
elif("2022" in lista):
	x = True
	while x == True:
		try:
			x, y = py.locateCenterOnScreen('win11.png')
			print("Sikerült kiválasztani a megfelelő win11 iso fájlt")
			print("-------------------------------------------------")
			x = False
		except:
			x = True
			py.press("down")


			# Ha nincs a gépen win11, akkor a win2019-et válassza
			x = True
			while x == True:
				try:
					x, y = py.locateCenterOnScreen('win2019.png')
					print("Sikerült kiválasztani a megfelelő win2019 iso fájlt")
					print("---------------------------------------------------")
					x = False
				except:
					x = True
					py.press("down")

		else:
			pass
else:
	print("Egy zsák krumpli vagyok és nem tudom megoldani a kiválasztást rendesen")
	print("----------------------------------------------------------------------")
time.sleep(0.8)



# Lekokézza az infókat és a memóriához ugrik
for i in range(2):
	py.press("tab")
	time.sleep(0.5)
py.press("enter")
time.sleep(1)



# Memória beállítás
# A win fajtájának megfelelő memóriát állítson be magának, pl 2022nek többet (probléma: mindenkinek más gépe van otthon)
py.press("tab")
time.sleep(0.5)
if("2008" in lista):
	keyboard.send("2") # itt melyik py. parancsal írtunk bele amit elfogadott?
	keyboard.send("0")
	keyboard.send("4")
	keyboard.send("8")
elif("2012" in lista):
	keyboard.send("2")
	keyboard.send("0")
	keyboard.send("4")
	keyboard.send("8")
elif("2012" in lista):
	keyboard.send("2") # kell ennek több?
	keyboard.send("0")
	keyboard.send("4")
	keyboard.send("8")
py.press("tab")
time.sleep(0.5)
py.press("enter")
time.sleep(0.5)



# Maradék személyreszabás leokézása
for i in range(4):
	py.press("enter")
	time.sleep(0.5)
time.sleep(1)





# 2 db hálózati kártya beállítása, egyik NAT, másik Belső internet intnet



# Létrehozott gép keresése, indítása
try:
	x, y = py.locateCenterOnScreen('newcompstart.png')
	py.moveTo(x,y)
	time.sleep(1)
	py.doubleClick(x,y)
	time.sleep(1)
except TypeError:
	print("Szerecsétlen vagyok és nem találtam meg az 'új' virtuális gépet")
	print("---------------------------------------------------------------")
else:
	print(f"Sikeres virt.box gép inditás")
	print("-----------------------------")
time.sleep(1)



# Vbox ablak megkeresése, belépése
x = True
while(x==True):
	try:
		py.keyDown("alt")
		py.press("tab")
		x, y = py.locateCenterOnScreen('vboxpics.png', confidence=0.6)
		py.moveTo(x,y+50)
		time.sleep(1)
		py.click()
		py.keyUp("alt")
		print("Vboxba váltás siker")
		print("-------------------")
		time.sleep(1)
	except TypeError:
		print("Vboxba vátlás sikertelen")
		print("------------------------")
		py.moveTo(50, 50)
		time.sleep(0.5)
		py.click()
		time.sleep(0.5)
time.sleep(1)



# Mappa ikon kiválasztása hogy iso fájlt választhassunk
x = True
while x == True:
	try:
		x, y = py.locateCenterOnScreen('folder.png', confidence=0.6)
		py.moveTo(x,y)
		time.sleep(0.5)
		py.click()
		print("Sikerült megtalálni a kis mappa ikont")
		x = False
	except:
		x = True
		print("Nem sikerült megtalálni a kis mappa ikont[")
time.sleep(1)



# Hozzáadás ikonra kattintás
x = True
while x == True:	
	try:
		x, y = py.locateCenterOnScreen('addisoicon.png')
		py.moveTo(x,y)
		time.sleep(1)
		py.click()
		print("Sikerült megtalálni a hozzáadás gombot")
		x = False
	except:
		x = True
		print("Nem sikerült megtalálni a hozzáadás gombot") 	# ne irja ki 5milioszor, inkább csak1x, majd utánna vár, és egy adott keresési ido után break
		pass													# Egy counter-t tenni ide hogy számolja ha 30-nál töbször probálja és nem megy akkor hagyja abba
time.sleep(1)



# Következő kódsorhoz való rövidítés miatt functionba rakás
def shorting():
	print("Sikerült kiválasztani a megfelelő iso fájlt")
	print("---------------------------------------------------")
	x = False
	py.moveTo(x+1000,y) # odakoardinálás a gépen levő iso fájlhoz
	time.sleep(1)
	py.click()
	time.sleep(1)
	py.press("enter") # hozzáadtuk a kiválasztott iso fájlt
	time.sleep(1)
	py.press("enter") # leokézzuk a kiválasztott iso fájlt
	time.sleep(1)
	py.press("enter") # elindítjuk a kiválasztott sio fájlt



# Választott windows iso megtalálása
		# Megnézni hogy "return" értékkel tudunk e játszani hogy a png-ket is bele lehessen írni a functionba, csak akkor ha lehet ilyet..
			# Megnézni hogy az "x = True" állítást nem tudnánk e mindig igazzá tenni, így a program összes kisebb ciklusánál ki lehetne hagyni
if("2008" in lista):
	x = True
	while x == True:
		try:
			x, y = py.locateCenterOnScreen('find2008.png')
			shorting()
		except:
			x = True
			print("Nem sikerült, valamit nagyon elnéztünk")
elif("2012" in lista):
	x = True
	while x == True:
		try:
			x, y = py.locateCenterOnScreen('find2012.png')
			shorting()
		except:
			x = True
			print("Nem sikerült, valamit nagyon elnéztünk")
elif("2022" in lista):
	x = True
	while x == True:
		try:
			x, y = py.locateCenterOnScreen('find2022.png')
			shorting()
		except:
			x = True
			print("Nem sikerült, valamit nagyon elnéztünk")
time.sleep(1)


# Leírni a telepítéseknél hogy sikerült a lépés vagy sem a cmd-be

# Magyar nyelv kiválasztása
for i in range(3):
	keyboard.send("tab")
	time.sleep(0.5)
keyboard.send("enter")
time.sleep(1)



# Telepítés gomb	#2012nél 12mp, 2022nél 15mp
keyboard.send("enter")
time.sleep(20)


# Gui kiválasztása
time.sleep(1)
if("2012" in lista):
	for i in range(3):
		keyboard.send("down")
		time.sleep(0.5)
	keyboard.send("enter")
elif("2022" in lista):
	keyboard.send("tab")
	time.sleep(0.5)
	keyboard.send("enter")
elif("2008" in lista):
	print("segitseg482.sorkb")
time.sleep(6)



# Elfogadom a "licence" feltételeket
for i in range(3):
	keyboard.send("tab")
	time.sleep(1)
keyboard.send("space")
time.sleep(1)
keyboard.send("enter")
time.sleep(3)



# Egyéni szerver telepítés választása
keyboard.send("down")
time.sleep(1)
keyboard.send("enter")
time.sleep(3)



# Partíciók beállítása (D partíció létrehozása)
for i in range(2):
	keyboard.send("tab")
time.sleep(1)
keyboard.send("enter")
time.sleep(1)
keyboard.send("right")
time.sleep(0.3)
keyboard.send("backspace")
time.sleep(0.3)
keyboard.send("3")
time.sleep(0.3)
keyboard.send("tab")
time.sleep(0.5)
for i in range(2):
	keyboard.send("enter")
	time.sleep(1)
time.sleep(4)



# Tovább, egészen a Windows fájlok letöltéséig, majd várakozás míg tölt
for i in range(6):
	keyboard.send("tab")
	time.sleep(0.5)
keyboard.send("enter")
time.sleep(600) # Nekem a betöltés ideje 9 perc volt = 540mp 		2022= 14perc
# ezt ki lehet küszöbölni úgy hogy néha kikattint és megnézi locateonscreen-el hogy betöltött e már a windows stb


# Termékkulcs nincs
if("2022" in lista):
	keyboard.send("tab")
	time.sleep(0.5)
	keyboard.send("enter")
time.sleep(1)



# Felhasználónév, jelszó megadása
		# Megnézni hogy a jelszót return-be be lehet e rakni, vagy input pop up ablakba meg lehet e adni
for i in range(2):
	keyboard.write("Almafa12;")
	time.sleep(0.5)
	keyboard.send("tab")
	time.sleep(0.5)
keyboard.send("enter")
time.sleep(180)	# 2012: 3 perc volt nekem (egutolsó telepítés betöltés)  # 202: 5mp




































# Nem mukodik 2022-snél
# Bejelentkezés
	#bal oldali ctrl + bal oldali lenti delete gomb
	#upperline2

time.sleep(1)
keyboard.send("esc") # Nekem behozza a feladatkezelőt norm ablakba
time.sleep(1)
keyboard.write("Almafa12;")
time.sleep(1)
keyboard.send("enter")
time.sleep(30) # Betölti a windowst és behozza a kiszolgálókezelőt



# Internet beállítása, majd python + pip telepítése(hogy minél hamarabb létrehozhassuk a képfelismerést pythonban), shared folder trükközés



# Indulhat a tényleges szerver kreálás
# Ip-cím csekkolás cmd-ben és beállítása
		# Esetleg kérhet a python program egy inputot hogy milyen ip címet akarok megadni
keyboard.send("win+r")
time.sleep(1)
keyboard.write("cmd")
time.sleep(1)
keyboard.send("enter")
time.sleep(1)
keyboard.write("start msedge.exe")
time.sleep(7)

# url beírása
keyboard.send("ctrl+l")
time.sleep(1)
keyboard.write("https://www.python.org/downloads/")
time.sleep(1)
keyboard.send("enter")
time.sleep(4)

# download python
for i in range(20):
	keyboard.send("tab")
	time.sleep(0.5)
keyboard.send("enter")
time.sleep(1)


# letöltés megnyitása
ctrl + e
6x tab
1 db "->" nyil
enter
9x tab
le
fel

















# github monitorozás, azon nézzuk hogy betöltött e már a windows,
#		kivéve ha a virtualbox előnézet ablak is megfelel erre
#			akkora vboxot ugy kell helyezni hogy a program lássa box előlnézetet
#				plsu akkor ugrálni kell az ablakok közt a kattintások, billentyűnyomások miatt






# ha egy kódsor csoport nem indul el, akkor kell valami ellenőrzés hogy lássa a kód hogy tovább mehet e vagy sem

# kód titkosítása hogy csak mi lássuk

# esetleg stoppert állítani hogy mennyi ideg programozunk, utánna szolna ha szünetet kell tartani

# várakozási időt +3 clicket össze lehet vonni egy darab functionba a kód röviditéséért

# az alap pip letöltéseket pendrivera ráírhatjuk, cmd-n kereszül powershellbe

# ismétlődő sorokat functionba tenni, pl iso v álasztásn ál

# function-ba tenni egy kisebb kódsort ha később még jól jön

# kivenni a "x = True"-ket ahol felesleges, ahol nincs "x = True", ott nem fut le mégegyszer ha nem találja, át kell gondolni

# minden kisebb kódsorcsoport mögött/végén legyen 1mp várakozási idő

# megosztott mappa arra jo lehet hogy abbarakjuk a scriptet?

# csinálja inkább a youtube automalizálást, az legalább ér valamit!

#parancsosrba tájékoztasson hogy mely lépések sikerültek

#képeket zipbe tenni, esetleg kulon utvonaalt irni a kodba hogy megtalélja a képet