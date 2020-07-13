#coding=utf-8
import os, sys, time
os.system('clear')
logo=""" _____  _____  _____  _____  ___    _   _ 
(  _  )(_   _)(_   _)(  _  )(  _`\ ( ) ( )
| (_) |  | |    | |  | (_) || ( (_)| |/'/'
|  _  |  | |    | |  |  _  || |  _ | , <  
| | | |  | |    | |  | | | || (_( )| |\`\ 
(_) (_)  (_)    (_)  (_) (_)(____/'(_) (_)"""
logo1="""=========================================="""
logo2=('         Owner:-    Badhßhah')
logo3=('         Author:-   Sachin Shrivastv')
logo4=('         Whatsapp:- +977-9845844301')
def printing (z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
def exit():
	printing(Exit)
	os.system('exit')
def Ssi():
        os.system('clear')
        print(logo)
        print(logo1)
        print(logo2)
        print(logo3)
        print(logo4)
        print(logo1)
	print('{1}~~~~~>>  Attack on Target')
	print('{2}~~~~~>>  Insert Wordlist')
	print('{3}~~~~~>>  Contacts Us')
	print('{0}~~~~~>>  Exit')
	slop = input('Select option:- ')
	if slop =="":
		print('[!] Invalid Input')
		os.system('clear')
		Ssi()
	elif slop =="1":
		attack()
	elif slop =="2":
		wordlist()
	elif slop =="3":
		os.system('clear')
		def contact():
			print(logo)
			print(logo1)
			print(logo2)
			print(logo3)
			print(logo3)
			print(logo4)
			print(logo1)
			print('{1}~~~~~>>  Join Whatsapp Group')
			print('{2}~~~~~>>  Visit Facebook Page')
			print('{3}~~~~~>>  Youtube Channel')
			print('{0}~~~~~>>  Back')
			def choice():
				gt = input('Select option:- ')
				if gt =="":
					print('[!] Invalid Input')
					time.sleep(1)
					os.system('clear')
					contact()
				elif gt =="1":
					os.system('xdg-open https://chat.whatsapp.com/JJOVjf9DdsA9o4FeXVol6W')
					time.sleep(1)
					contact()
				elif gt =="2":
                                        os.system('xdg-open https://www.facebook.com/Badhshah-Hacker-119051486545625/')
                                        time.sleep(1)
                                        contact()
                                elif gt =="3":
                                        os.system('xdg-open https://www.youtube.com/channel/UCUltb-xVDLF6dtfgtPOBpuA')
                                        time.sleep(1)
                                        contact()
                                elif gt =="0":
                                        time.sleep(1)
                                        Ssi()
                                else:
                                      	print('[!] Invalid Input')
					time.sleep(1)
					os.system('clear')
					contact()  
                                        
			contact()
Ssi()		
