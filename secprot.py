import time
import os

class SCP:#security protocol
	def __double_auth_activate(self):
		'''This is double authentification method'''
		updct = {
            #user-password dictionary
			'user': 'pk33.mskobr.ru',
			'admin': 'lvl__admin',
			'delete':'delete',

		}
		
		passcode=input("Введите пароль для доступа к программе: ")
		
		if passcode == updct['delete']:
			print("Access automatically denied")
			time.sleep(3)
			print('deleting file..'*100)
		else:
			while passcode != updct['user']:
				print("Access Denied")
				passcode=input("Введите пароль для доступа к программе: ")
			else:
				print("Access Granted")

				
				
				
				

	def __init__(self):
		self.__double_auth_activate()


SCP()