import os
os.system('color 0f')
print("Chargement...")
from time import sleep
import sys
import datetime
import time
import requests
from tkinter import *
from tkinter import ttk
import tkinter as tk
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from PyQt5 import QtWidgets, QtCore, QtGui
from PIL import ImageGrab, Image
import numpy as np
import re
import cv2
from pytesseract import *
import urllib
import json
from urllib import request, parse
from time import time

class cashbot():
	def __init__(self, root):
		self.bot_frame = LabelFrame(root, text="Actions", padx=5, pady=5)
		self.bot_frame.pack(fill="both", expand="yes")
		self.scan_button = ttk.Button(self.bot_frame, text= 'Scan', command=bot_detect)
		self.scan_button2 = ttk.Button(root, text= 'Chat', command=start_chat)
		self.scan_button3 = ttk.Button(root, text= 'Retour', command=bot_exit)
		self.button4 = ttk.Button(root, text= 'Options', command=sett)
		self.button4.pack()
		self.scan_button.pack()
		self.scan_button2.pack(side=LEFT, padx=5, pady=5)
		self.scan_button3.pack(side=RIGHT, padx=5, pady=5)

def set_screenshot():
	global testdat
	sauvTXT = open("screen.dat") 
	with open('screen.dat', 'r') as sauvTXT:
			testdat = str(sauvTXT.read().replace('\n', ' '))
	if testdat=="Airserver":
		set_airserver()
	if testdat=="Windows":
		set_windows()

def startmsg():
	set_screenshot()
	os.system('CLS')
	print('CashBot [version {}] '.format(vers1))
	print(' Mode : {}'.format(testdat))
	print(' Auteur : Jesus')
	print()
	print('Appuyer sur "Scan" pour obtenir la reponse...')


def sett():
	os.system('CLS')
	print('')
	print("1. Mettre mode Airserver ")
	print("2. Mettre mode Windows ")
	rep_sett = int(input("Ecrire ici : "))
	if rep_sett==1:
		set_screenshot()
		sauvdat = open("screen.dat","w") 
		sauvdat.write("Airserver")
		sauvdat.close()
		startmsg()

	if rep_sett==2:
		set_screenshot()
		sauvdat = open("screen.dat","w") 
		sauvdat.write("Windows")
		sauvdat.close()
		startmsg()


def groupmsg(texttosend):
	emptyvar = texttosend

def bot_exit():
	groupmsg('* Bot déconnecté * ')
	sys.exit()

def start_chat():
	groupmsg('* Bot connecté * ')
	os.system('start cashbot_chat.bat"')



def screenshot():
	os.system('CLS')
	groupmsg('Scan...')
	print("Scan...")
	print("")
	ques1 = oScr(qx1, qy1, qx2, qy2)
	ques1.save('q.png')
	rep1 = oScr(r1x1, r1y1, r1x2, r1y2)
	rep1.save('r1.png')
	rep2 = oScr(r2x1, r2y1, r2x2, r2y2)
	rep2.save('r2.png')
	rep3 = oScr(r3x1, r3y1, r3x2, r3y2)
	rep3.save('r3.png')

def oScr(x1, y1, x2, y2):
	return ImageGrab.grab(bbox=(x1, y1, x2, y2))

def result():
	global ts
	if test_ques == "neg":
		best_rep = int(last_prob.index(min(last_prob)))
	if test_ques == "normal":
		best_rep = int(last_prob.index(max(last_prob)))
	best_rep +=1

	if best_rep == 1:
		best_repstr = text_r1
		if test_ques == "neg":
			best_repProb = (0 - last_prob[0]) + 100
		if test_ques == "normal":
			best_repProb = last_prob[0]
	if best_rep == 2:
		best_repstr = text_r2
		if test_ques == "neg":
			best_repProb = (0 - last_prob[1]) + 100
		if test_ques == "normal":
			best_repProb = last_prob[1]
	if best_rep == 3:
		best_repstr = text_r3
		if test_ques == "neg":
			best_repProb = (0 - last_prob[2]) + 100
		if test_ques == "normal":
			best_repProb = last_prob[2]
	print()
	t2 = time()
	t2 = t2 - ts

	best_repstr =  '  [  REP {0}  ] : {1}  |  {2} %'.format(best_rep, best_repstr, round(best_repProb))
	groupmsg(best_repstr)
	print()
	print(best_repstr)
	print()
	print(best_repstr)
	print()
	print("Réponse trouvée en {} s".format(round(t2, 3)))
	groupmsg("Trouvé en {} s".format(round(t2, 1)))
	groupmsg(' ')
	sleep(4) 
	startmsg()

def bestnumF(badnumF, badnumF2, goodnumF):
	badnumF /= 2 
	badnumF2 /= 2 
	goodnumF = goodnumF + badnumF + badnumF2
	BNumF_liste = []
	BNumF_liste.append(badnumF)
	BNumF_liste.append(badnumF2)
	BNumF_liste.append(goodnumF)
	return BNumF_liste

def sauv_rep(sauvText):
	sauvTXT = open("sauv.txt","w") 
	sauvTXT.write(sauvText)
	sauvTXT.close()
	with open('sauv.txt', 'r') as sauvTXT:
			return str(sauvTXT.read().replace('\n', ' '))

def replace_char(varToreplace):
	return varToreplace.replace("l'adage", "citation").replace("Qui a popularisé", "").replace("Le plus souvent", "").replace(" oo ", " ou ").replace("-", " ").replace(" ses ", " ").replace(" dont ", " ").replace(" la ", " ").replace("Quel ", "").replace(" du ", " ").replace("Mc", "Mac").replace(" le ", " ").replace("sont-ils", "").replace("sont-elles", "").replace("De qui", "").replace("est-il", "").replace("est-elle", "").replace(" fut ", " ").replace(",", "").replace(" un ", " ").replace("Parmi les propositions suivantes", "").replace("Parmi les", "").replace(" laquelle ", " ").replace("lesquels ont", "").replace("lequel a", "").replace(" typique ", " ").replace(" lequel ", " ").replace("Parmi ces", " ").replace(" étaient ", " ").replace(" était ", " ").replace(" pouvez-vous ", " ").replace("Qui est devenu", "").replace(" a été ", " ").replace("", "").replace("Lequel de ces", "").replace(" Quel ", " ").replace("Quelle", "").replace("Dans quelle", "").replace(" est ", " ").replace(":", "").replace("Identifiez ", "").replace("Identifiez lequel", "").replace("Identifiez la", "").replace("Identifiez les", "").replace("Identifiez le", "").replace("Le plus souvent,", "").replace("â", "a").replace("œ", "oe").replace('"', "'").replace("Qui a", "").replace("Quel est", "").replace("ç", "c").replace("°C", " degres").replace("£", " livres").replace("$", " dollars").replace("€", " euros").replace(".", "").replace(" ne ", " ").replace(" pas ", " ").replace(" n'", " ").replace(" jamais ", " ").replace(" rien ", " ").replace(" ", "%20").replace("é", "e").replace("è", "e").replace("à", "a").replace("Â", "A").replace("É", "E").replace("Ô", "o").replace("Ù", "U").replace("ù", "o").replace("Î", "I").replace("ï", "i").replace("î", "i").replace("ê", "e").replace("ô", "o").replace("«", '"').replace("»", '"')

def replace_char2(varToreplace):
	return varToreplace.replace("Mc", "Mac").replace("L'", "").replace("À la", "").replace("â", "a").replace("œ", "oe").replace("ï", "i").replace("€", "euros").replace("ç", "c").replace("Il", "").replace("Elle", "").replace("Elle avait ", "").replace("Il avait ", "").replace("Il a ", "").replace("Elle a ", "").replace(".", "").replace("Le ", "").replace("La ", "").replace("L'", "").replace("Un ", "").replace("Une ", "").replace("Des ", "").replace(" ", "%20").replace("é", "e").replace("è", "e").replace("à", "a").replace("Â", "A").replace("É", "E").replace("Ô", "o").replace("Ù", "U").replace("ù", "u").replace("Î", "I").replace("î", "i").replace("ê", "e").replace("ô", "o").replace("«", '"').replace("»", '"').replace("°C", " degres").replace("A la ", "").replace("Dans une ", "")

def replace_char3(varToreplace):
	return varToreplace.replace("Mc", "Mac").replace("À la", "").replace("â", "a").replace("œ", "oe").replace("ï", "i").replace("Il", "").replace("Elle", "").replace("Elle avait ", "").replace("Il avait ", "").replace("Il a ", "").replace("Elle a ", "").replace("Le ", "").replace("La ", "").replace("L'", "").replace("Un ", "").replace("Une ", "").replace("Des ", "").replace(".", "").replace("A la ", "").replace("Dans une ", "")

def proba(stat1, stat2, stat3):
	glob_prob = stat1 + stat2 + stat3
	if stat1 > 0:
		stat1 = ( stat1 / glob_prob ) * 100
	if stat2 > 0:
		stat2 = ( stat2 / glob_prob ) * 100
	if stat3 > 0:
		stat3 = ( stat3 / glob_prob ) * 100	
	prob_liste = []
	prob_liste.append(stat1)
	prob_liste.append(stat2)
	prob_liste.append(stat3)
	return prob_liste
	
def get_result(questiontocheck, reponsetocheck):
	global num
	search = "https://www.google.fr/search?q={}".format(questiontocheck) + "%20'%20{}%20'".format(reponsetocheck)
	req_google = Request(search)
	req_google.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB;    rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	html_google = urlopen(req_google).read()
	soup = BeautifulSoup(html_google, "html.parser")
	scounttext = str(soup.find('div', id='resultStats'))
	scounttext = scounttext[41:60]
	scounttext = scounttext.replace(u'\xa0', "")
	num = re.findall('\d+', scounttext)
	print()
	return int(num[0])

def findword(wordtofind, questiontocheck):
	global count_nb
	page = requests.get("https://www.google.fr/search?q={}".format(question)).text
	count_nb = re.findall(' {} '.format(wordtofind), page)
	count_nb = int(len(count_nb))
	if count_nb == 0:
		count_nb = re.findall('{} '.format(wordtofind), page)
		count_nb = int(len(count_nb))
	print()
	return count_nb

def Methodes():
	global num_rep1, num_rep2, num_rep3
	global numF_rep1, numF_rep2, numF_rep3
	num_rep1 = get_result(question, reponse1)
	num_rep2 = get_result(question, reponse2)
	num_rep3 = get_result(question, reponse3)
	num_prob = proba(num_rep1, num_rep2, num_rep3)	
	if test_ques == "neg":
		best_rep1 = int(num_prob.index(min(num_prob)))
	if test_ques == "normal":
		best_rep1 = int(num_prob.index(max(num_prob)))
	prob1= num_prob[best_rep1]
	best_rep1 +=1
	print("Methode 1 : [Rep {0}]  {1} %".format(best_rep1, round(prob1)))
	groupmsg("Methode 1 : [Rep {0}] {1} %".format(best_rep1, round(prob1)))
	text_rep1 = replace_char3(text_r1)
	text_rep2 = replace_char3(text_r2)
	text_rep3 = replace_char3(text_r3)
	numF_rep1 = findword(text_r1, question)
	print('  rep1 : {}'.format(numF_rep1))
	numF_rep2 = findword(text_r2, question)
	print('  rep2 : {}'.format(numF_rep2))
	print()
	numF_rep3 = findword(text_r3, question)
	print('  rep3 : {}'.format(numF_rep3))
	print()
	groupmsg('Methode 2 :   rep1 = {0}  rep2 = {1}  rep3 = {2}'.format(numF_rep1, numF_rep2, numF_rep3))



def pytesserX(imagetocheck):
	img_pyt = Image.open(imagetocheck)
	return pytesseract.image_to_string(img_pyt, lang = 'fra')

def bot_detect():
	global ts
	global text_q1, text_r1, text_r2, text_r3
	global question, reponse1, reponse2, reponse3
	global wordtofind, best_rep, search, last_prob, test_ques
	global numF_rep1, numF_rep2, numF_rep3
	global num_rep1, num_rep2, num_rep3
	ts = time()
	screenshot()
	text_q1 = pytesserX('q.png')
	text_r1 = pytesserX('r1.png')
	text_r2 = pytesserX('r2.png')
	text_r3 = pytesserX('r3.png')
	test_ques = "normal"
	if text_q1.count(' ne ')>0:
		test_ques = "neg"
	elif text_q1.count(" n'")>0:
		test_ques = "neg"
	if text_q1.count(' pas ')>0:
		test_ques = "neg"
	question = replace_char(sauv_rep(text_q1))
	reponse1 = replace_char2(text_r1)
	reponse2 = replace_char2(str(text_r2))
	reponse3 = replace_char2(str(text_r3))
	Methodes()
	num_prob = proba(num_rep1, num_rep2, num_rep3)
	test_numF = numF_rep1 + numF_rep2 + numF_rep3
	numF_prob = proba(numF_rep1, numF_rep2, numF_rep3)

	num_rep1 = num_prob[0]
	num_rep2 = num_prob[1]
	num_rep3 = num_prob[2]

	numF_rep1 = numF_prob[0]
	numF_rep2 = numF_prob[1]
	numF_rep3 = numF_prob[2]

	if test_numF > 0:
		if test_ques == "normal":
			numF_liste = []
			numF_liste.append(numF_rep1)
			numF_liste.append(numF_rep2)
			numF_liste.append(numF_rep3)
			best_numF = int(numF_liste.index(max(numF_liste)))
			if best_numF==0:
				testnFL = bestnumF(num_rep2, num_rep3, num_rep1)
				num_rep1 = testnFL[2]
				num_rep2 = testnFL[0]
				num_rep3 = testnFL[1]
			if best_numF==1:
				testnFL = bestnumF(num_rep1, num_rep3, num_rep2)
				num_rep1 = testnFL[0]
				num_rep2 = testnFL[2]
				num_rep3 = testnFL[1]
			if best_numF==2:
				testnFL = bestnumF(num_rep1, num_rep2, num_rep3)
				num_rep1 = testnFL[0]
				num_rep2 = testnFL[1]
				num_rep3 = testnFL[2]

		prob_rep1 = (num_rep1 + numF_rep1)
		prob_rep2 = (num_rep2 + numF_rep2)
		prob_rep3 = (num_rep3 + numF_rep3)
	else:
		prob_rep1 = num_rep1
		prob_rep2 = num_rep2
		prob_rep3 = num_rep3
	last_prob = proba(prob_rep1, prob_rep2, prob_rep3)
	result()

def set_airserver():
	global qx1, qy2, qx2, qy1
	global r1x1, r1y1, r1x2, r1y2
	global r2x1, r2y1, r2x2, r2y2
	global r3x1, r3y1, r3x2, r3y2
	qx1=105
	qy1=158
	qx2=438
	qy2=280
	r1x1=132
	r1y1=326
	r1x2=374
	r1y2=371
	r2x1=132
	r2y1=400
	r2x2=400
	r2y2=447
	r3x1=132
	r3y1=470
	r3x2=375
	r3y2=517

def set_windows():
	global qx1, qy2, qx2, qy1
	global r1x1, r1y1, r1x2, r1y2
	global r2x1, r2y1, r2x2, r2y2
	global r3x1, r3y1, r3x2, r3y2
	qx1=59
	qy1=162
	qx2=364
	qy2=264
	r1x1=85
	r1y1=303
	r1x2=341
	r1y2=350
	r2x1=85
	r2y1=370
	r2x2=342
	r2y2=416
	r3x1=85
	r3y1=434
	r3x2=342
	r3y2=482


def main():
	global vers1
	vers1 = "0.5"
	startmsg()
	root = Tk()
	root.title('Cash Bot v{}'.format(vers1))
	root.geometry("200x115") 
	root.resizable(0, 0) 
	root.iconbitmap('iconelauncher.ico')
	app = cashbot(root)	
	root.mainloop()

if __name__ == '__main__':
	main()