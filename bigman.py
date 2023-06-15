import os
import math
import string
import platform
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


os.system('clear')


lets = (f'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#£_&-+/*":;()?')
lts = len(lets)
spac = ' '
#lets_uc = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#digits = ('0123456789')
#syms = (string.punctuation)

def mainsys(text, mode, key):
	global res
	res = ''
	if mode == 'd':
		key = -key
	for let in text:
		if not let == ' ':
			index = lets.find(let)
			if index == -1:
				res += let
			else:
				new_index = index + key
				if new_index >= lts:
					new_index -= lts
				elif new_index < 0:
					new_index += lts
				res += lets[new_index]
	return res

#for letter in text:
# let = letter.lower()

####################################
# Symbols #
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# !=0
# "=1
# #=2
# $=3
# %=4
# &=5
# '=6
# (=7
# )=8
# *=9
# +=0A
# ,=1B
# -=2C
# .=3D
# /=4E
# :=5F
# ;=6G
# <=7H
# ==8I
# >=9J
# ?=0a
# @=1b
# [=2c
# \=3d
# ]=4e
# ^=5f
# _=6g
# `=7h
# {=8i
# |=9j
# }=a0
# ~=a01
#print(string.punctuation)
#######################################

class mcl():
	cl = Fore.WHITE+Style.BRIGHT
	cl1 = Fore.BLUE+Style.BRIGHT
	cl2 = Fore.YELLOW+Style.BRIGHT
	cl3 = Fore.GREEN+Style.BRIGHT

print(f"""{mcl.cl2}
=========================
={mcl.cl3} The BigMan Encryption{mcl.cl2} =
====={mcl.cl3} By ~> Anon{mcl.cl2} ========
=====++++++++++++========
""")
global creat
creat = "Anon"
userin = input(f"{mcl.cl}Encrypt Data Or Decrypt Data(E/d): ")
userin = userin.lower()
if userin == "e":
	print("Loading...")
	time.sleep(2)
	key = 24
	print(f"{mcl.cl3}[{mcl.cl1}INFO{mcl.cl3}] {mcl.cl}Encryption Is Ready!")
	enc = input(f"{mcl.cl3}[{mcl.cl2}+{mcl.cl3}] {mcl.cl}Enter The Text To Encrypt:{mcl.cl1} ")
	if enc != ' ':
		mainsys(enc, userin, key)
		print(f"{mcl.cl3}[{mcl.cl2}SUCCESS{mcl.cl3}] {mcl.cl}ENCRYPTED KEY: {mcl.cl2}{res}")
	else:
		print(f"{Fore.RED+Style.BRIGHT} Error! Try Agian")
elif userin == "d":
	print("Loading...")
	time.sleep(2)
	key = 24
	print(f"{mcl.cl3}[{mcl.cl1}INFO{mcl.cl3}]{mcl.cl} Decryption Is Ready!")
	dec = input(f"{mcl.cl3}[{mcl.cl2}+{mcl.cl3}]{mcl.cl} Enter Encrypted Code To Decrypt:{mcl.cl1} ")
	if dec != ' ':
		mainsys(dec, userin, key)
		print(f"{mcl.cl3}[{mcl.cl2}SUCCESS{mcl.cl3}] {mcl.cl}DECRYPTED KEY: {mcl.cl2}{res}")
	else:
		print(f"{Fore.RED+Style.BRIGHT} Error! Try Again")
else:
	print(f"{Fore.RED+Style.BRIGHT}User! Your Input '{userin}' is not found!")
	exit()
