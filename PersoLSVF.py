#coding:utf-8

import os
import random
from random import choice
from ListeMetiersCompetences import *
from ListeTalents import *



print ("---------------------------------------------------------------------------------------------")
# initialisation de la liste à 11 dés de zéro
#dicesList = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
dicesList = []

def dices(dicesListTmp):
	def rollDices(numbersList):
		i=0
		while i<11:
			numbersList.append(random.randint(1, 10) + random.randint(1, 10))
			i += 1
		return numbersList

	# utilisation de la fonction de génération des 11 jets de dés
	rollDices(dicesListTmp)

	# fonction qui trie les dés par ordre décroissant
	def tri(liste):
		dicesListTri = liste.sort(reverse=True)
		return liste

	# utilisation de la fonction de tri
	tri(dicesListTmp)


	# on supprime les 3 plus petits dés
	i = 10
	while i>7:
		del dicesListTmp[i]
		i -= 1

	i = 0
	while i < 3:
		dicesListTmp[7] = random.randint(1, 10) + random.randint(1, 10)
		tri(dicesListTmp)
		i += 1
	return dicesListTmp

def agitateur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[0]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(listeCompetence[1])
	randomCompTal(competencesJoueur, listeCompetenceAv, 9, 22)
	competencesJoueur.append(listeCompetence[7])
	randomCompTal(competencesJoueur, listeCompetenceAv, 60, 68)
	competencesJoueur.append(listeCompetenceAv[67])
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[75])
	talentsJoueur.append(listeTalents[25])
	talentsJoueur.append(listeTalents[29])

def apprentiSorcier():
	global carriereJoueur
	carriereJoueur = listeCarrieres[1]
	repartCaracteristiqueMage(race)
	profilSecondR["Mag"] = 1
	competencesJoueur.append(listeCompetenceAv[13])
	competencesJoueur.append(listeCompetenceAv[51])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[55])
	competencesJoueur.append(listeCompetenceAv[111])
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[107])
	randomCompTal(talentsJoueur, listeTalents, 33, 46)
	defineTalentVsProfilPpal(profilPpal["E"], listeTalents[68], listeTalents[37])
	talentsJoueur.append(listeTalents[42])

def artisan():
	global carriereJoueur
	carriereJoueur = listeCarrieres[2]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(listeCompetence[18])
	competencesJoueur.append(listeCompetence[4])
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(listeCompetenceAv[57])
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[14])
	m1 = random.randint(75, 102)
	m2 = random.randint(75, 102)
	while m1 == m2:
		m2 = random.randint(75, 102)
	competencesJoueur.append(listeCompetenceAv[m1])
	competencesJoueur.append(listeCompetenceAv[m2])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[37])

def baleinier():
	global carriereJoueur
	carriereJoueur = listeCarrieres[61]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(listeCompetence[0])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetenceAv[103])
	competencesJoueur.append(listeCompetenceAv[104])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[17])
	talentsJoueur.append(listeTalents[2])
	talentsJoueur.append(listeTalents[22])
	talentsJoueur.append(listeTalents[27])
	talentsJoueur.append(listeTalents[31])
	talentsJoueur.append(listeTalents[75])
	dotations.append("4 flasques contenant chacune 1/2L d'huile de baleine")

def bateleur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[3]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(listeCompetenceAv[22])
	m1 = random.randint(37, 49)
	m2 = random.randint(37, 49)
	while m1 == m2:
		m2 = random.randint(37, 49)
	competencesJoueur.append(listeCompetenceAv[m1])
	competencesJoueur.append(listeCompetenceAv[m2])
	competencesJoueur.append(listeCompetenceAv[67])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(choice([listeCompetence[9],listeCompetenceAv[35],listeCompetenceAv[34],listeCompetenceAv[33]]))
	t1 = choice([listeTalents[3],listeTalents[27],listeTalents[52],listeTalents[67],listeTalents[84]])
	t2 = choice([listeTalents[3],listeTalents[27],listeTalents[52],listeTalents[67],listeTalents[84]])
	while t1 == t2:
		t2 = choice([listeTalents[3],listeTalents[27],listeTalents[52],listeTalents[67],listeTalents[84]])
	talentsJoueur.append(t1)
	talentsJoueur.append(t2)
	if listeCompetenceAv[33] in competencesJoueur:
		dotations.append(choice(["un chien", "un chien de guerre", "un corbeau"]))
	dotations.append("3 haches de jet")
	
def batelier():
	global carriereJoueur
	carriereJoueur = listeCarrieres[4]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(listeCompetence[0])
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence[17]]))
	competencesJoueur.append(choice([listeCompetenceAv[22],listeCompetenceAv[25]]))
	competencesJoueur.append(choice([listeCompetenceAv[58],listeCompetenceAv[65]]))
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetenceAv[103])
	competencesJoueur.append(listeCompetenceAv[104])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[19])
	talentsJoueur.append(listeTalents[31])
	talentsJoueur.append(listeTalents[80])
	
def berserkNorse():
	global carriereJoueur
	carriereJoueur = listeCarrieres[5]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetenceAv[27])
	competencesJoueur.append(listeCompetenceAv[44])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetenceAv[66])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetence[17])
	talentsJoueur.append(listeTalents[28])
	talentsJoueur.append(listeTalents[55])
	talentsJoueur.append(listeTalents[61])
	talentsJoueur.append(listeTalents[84])
	
def bourgeois():
	global carriereJoueur
	carriereJoueur = listeCarrieres[6]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[4])
	#competencesJoueur.append(choice([listeCompetenceAv[22],listeCompetence[17]])
	competencesJoueur.append(listeCompetenceAv[22])
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(choice([listeCompetenceAv[60],listeCompetenceAv[65],listeCompetenceAv[68]]))
	competencesJoueur.append(listeCompetenceAv[67])
	competencesJoueur.append(listeCompetence[14])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[23])
	talentsJoueur.append(listeTalents[37])
	
def bucheron():
	global carriereJoueur
	carriereJoueur = listeCarrieres[7]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetenceAv[1])
	competencesJoueur.append(listeCompetenceAv[105])
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetence[7])
	competencesJoueur.append(listeCompetence[9])
	competencesJoueur.append(listeCompetenceAv[58])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[7])
	defineTalentVsProfilPpal(profilPpal["E"], listeTalents[68], listeTalents[20])
	talentsJoueur.append(listeTalents[55])
	
def charbonnier():
	global carriereJoueur
	carriereJoueur = listeCarrieres[8]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(listeCompetenceAv[1])
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence[4]]))
	competencesJoueur.append(listeCompetence[7])
	competencesJoueur.append(listeCompetence[9])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[14])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[19])
	defineTalentVsProfilPpal(profilPpal["F"], listeTalents[27], listeTalents[37])
	talentsJoueur.append(listeTalents[29])
	
def chasseurPrimes():
	global carriereJoueur
	carriereJoueur = listeCarrieres[9]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetenceAv[50])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[105])
	competencesJoueur.append(listeCompetence[19])
	t1 = random.randint(1,2)
	if t1 == 1:
		talentsJoueur.append(listeTalents[3])
		talentsJoueur.append(listeTalents[89])
	elif t1 == 2:
		talentsJoueur.append(listeTalents[19])
		talentsJoueur.append(listeTalents[17])
	talentsJoueur.append(listeTalents[7])
	talentsJoueur.append(listeTalents[55])
	dotations.append("des bolas")
	dotations.append("1 filet")
	
def chasseur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[10]
	repartCaracteristiqueCT(race)
	competencesJoueur.append(listeCompetenceAv[1])
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetence[7])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[105])
	competencesJoueur.append(listeCompetence[19])
	talentsJoueur.append(listeTalents[89])
	talentsJoueur.append(listeTalents[49])
	# SI ELF : talentsJoueur.append(listeTalents[22])
	talentsJoueur.append(listeTalents[66])
	defineTalentVsProfilPpal(profilPpal["E"], listeTalents[68], listeTalents[67])
	
def chiffonnier():
	global carriereJoueur
	carriereJoueur = listeCarrieres[11]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(listeCompetence[4])
	competencesJoueur.append(listeCompetenceAv[22])
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[14])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[18])
	talentsJoueur.append(listeTalents[75])
	talentsJoueur.append(listeTalents[22])
	
def chirurgienBarbier():
	global carriereJoueur
	carriereJoueur = listeCarrieres[12]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(choice([listeCompetence[4],listeCompetence[15]]))
	competencesJoueur.append(choice([listeCompetenceAv[60],listeCompetenceAv[67],listeCompetenceAv[68]]))
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[14])
	competencesJoueur.append(listeCompetenceAv[75])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[108])
	talentsJoueur.append(listeTalents[11])
	talentsJoueur.append(listeTalents[37])
	talentsJoueur.append(listeTalents[68])
	
def cocher():
	global carriereJoueur
	carriereJoueur = listeCarrieres[13]
	repartCaracteristiqueCT(race)
	competencesJoueur.append(listeCompetenceAv[1])
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence[14]]))
	competencesJoueur.append(listeCompetence[4])
	competencesJoueur.append(listeCompetenceAv[108])
	competencesJoueur.append(choice([listeCompetenceAv[60],listeCompetenceAv[65],listeCompetenceAv[68]]))
	competencesJoueur.append(listeCompetenceAv[104])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[18])
	talentsJoueur.append(listeTalents[84])
	talentsJoueur.append(listeTalents[50])
	dotations.append("1 putain de tromblon !")	
	
def collecteurTaxes():
	global carriereJoueur
	carriereJoueur = listeCarrieres[14]
	repartCaracteristiqueCT(race)
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence[14]]))
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(choice([listeCompetenceAv[60],listeCompetenceAv[65],listeCompetenceAv[68]]))
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(choice([listeTalents[67],listeTalents[89]]))
	
def combattantTunnels():
	global carriereJoueur
	carriereJoueur = listeCarrieres[15]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetence[9])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetenceAv[50])
	competencesJoueur.append(listeCompetenceAv[104])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(choice([listeTalents[1],listeTalents[75]]))
	talentsJoueur.append(listeTalents[17])
	talentsJoueur.append(listeTalents[18])
	talentsJoueur.append(listeTalents[19])
	talentsJoueur.append(listeTalents[80])
	
def contrebandier():
	global carriereJoueur
	carriereJoueur = listeCarrieres[16]
	repartCaracteristiqueFurtif(race)
	competencesJoueur.append(listeCompetenceAv[3])
	competencesJoueur.append(listeCompetence[0])
	competencesJoueur.append(listeCompetenceAv[59])
	competencesJoueur.append(listeCompetence[4])
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[14])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[23])
	
def coupeJarret():
	global carriereJoueur
	carriereJoueur = listeCarrieres[17]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetence[13])
	competencesJoueur.append(listeCompetenceAv[59])
	competencesJoueur.append(listeCompetence[17])
	talentsJoueur.append(listeTalents[17])
	talentsJoueur.append(listeTalents[18])
	talentsJoueur.append(listeTalents[21])
	talentsJoueur.append(listeTalents[67])
	talentsJoueur.append(listeTalents[84])
	
def diestroEstalien():
	global carriereJoueur
	carriereJoueur = listeCarrieres[18]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetenceAv[17])
	competencesJoueur.append(listeCompetenceAv[23])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetenceAv[62])
	competencesJoueur.append(listeCompetenceAv[74])
	talentsJoueur.append(choice([listeTalents[14],listeTalents[67]]))
	talentsJoueur.append(choice([listeTalents[18],listeTalents[84]]))
	talentsJoueur.append(listeTalents[19])
	talentsJoueur.append(listeTalents[54])
	dotations.append("1 rapière")
	
def eclaireur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[19]
	repartCaracteristiqueFurtif(race)
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetence[8])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[104])
	competencesJoueur.append(listeCompetenceAv[105])
	competencesJoueur.append(listeCompetence[18])
	competencesJoueur.append(listeCompetence[19])
	defineTalentVsProfilPpal(profilPpal["F"], listeTalents[27], listeTalents[75])
	talentsJoueur.append(listeTalents[57])
	talentsJoueur.append(listeTalents[80])
	dotations.append("1 lasso")
	dotations.append("des bolas")
	
def ecuyer():
	global carriereJoueur
	carriereJoueur = listeCarrieres[20]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(choice([listeCompetenceAv[12],listeCompetenceAv[20]]))
	competencesJoueur.append(listeCompetenceAv[33])
	competencesJoueur.append(listeCompetence[8])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(choice([listeCompetenceAv[12],listeCompetenceAv[20]]))
	competencesJoueur.append(choice([listeCompetenceAv[60],listeCompetenceAv[67]]))
	competencesJoueur.append(listeCompetence[18])
	talentsJoueur.append(listeTalents[19])
	talentsJoueur.append(listeTalents[26])
	talentsJoueur.append(listeTalents[51])

def emissaireElfe():
	global carriereJoueur
	carriereJoueur = listeCarrieres[21]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(listeCompetence[3])
	competencesJoueur.append(choice([listeCompetenceAv[22],listeCompetenceAv[29]]))
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(listeCompetenceAv[57])
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[14])
	competencesJoueur.append(listeCompetenceAv[95])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[23])

def esclavagiste():
	global carriereJoueur
	carriereJoueur = listeCarrieres[67]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetence[4])
	competencesJoueur.append(listeCompetenceAv[choice([20,22,31])])
	competencesJoueur.append(listeCompetence[8])
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetenceAv[(random.randint(60,72))])
	competencesJoueur.append(listeCompetenceAv[(random.randint(60,72))])
	competencesJoueur.append(listeCompetenceAv[(random.randint(60,72))])
	competencesJoueur.append(listeCompetence[14])
	competencesJoueur.append(listeCompetenceAv[105])
	competencesJoueur.append(listeCompetenceAv[109])
	talentsJoueur.append(listeTalents[choice([12,31])])
	talentsJoueur.append(listeTalents[17])
	talentsJoueur.append(listeTalents[23])
	talentsJoueur.append(listeTalents[61])

def escroc():
	global carriereJoueur
	carriereJoueur = listeCarrieres[22]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(listeCompetenceAv[3])
	competencesJoueur.append(listeCompetenceAv[4])
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence[14]]))
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(choice([listeCompetenceAv[38],listeCompetenceAv[44]]))
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[67])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[10])
	talentsJoueur.append(listeTalents[29])
	talentsJoueur.append(listeTalents[25])
	
def etudiant():
	global carriereJoueur
	carriereJoueur = listeCarrieres[23]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(listeCompetence[3])
	d = random.randint(6,19)
	competencesJoueur.append(listeCompetenceAv[d])
	competencesJoueur.append(choice([listeCompetence[11],listeCompetenceAv[108]]))
	competencesJoueur.append(listeCompetenceAv[111])
	competencesJoueur.append(listeCompetenceAv[67])
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(choice([listeTalents[6],listeTalents[31]]))
	talentsJoueur.append(choice([listeTalents[26],listeTalents[40]]))
	talentsJoueur.append(listeTalents[37])
	
def fanatique():
	global carriereJoueur
	carriereJoueur = listeCarrieres[24]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(listeCompetenceAv[19])
	competencesJoueur.append(listeCompetenceAv[22])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetenceAv[74])
	talentsJoueur.append(listeTalents[22])
	talentsJoueur.append(listeTalents[25])
	defineTalentVsProfilPpal(profilPpal["F"], listeTalents[27], listeTalents[75])
	talentsJoueur.append(listeTalents[58])
	dotations.append("arme : fléau")
	
def gardeCorps():
	global carriereJoueur
	carriereJoueur = listeCarrieres[25]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[108])
	talentsJoueur.append(listeTalents[13])
	talentsJoueur.append(listeTalents[17])
	talentsJoueur.append(choice([listeTalents[21],listeTalents[84]]))
	defineTalentVsProfilPpal(profilPpal["F"], listeTalents[27], listeTalents[68])
	talentsJoueur.append(listeTalents[52])
	talentsJoueur.append(listeTalents[53])
	dotations.append("3 haches de jet")
	dotations.append("1 rondache")
	dotations.append("1 brise lame")
	
def garde():
	global carriereJoueur
	carriereJoueur = listeCarrieres[26]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetence[3])
	competencesJoueur.append(listeCompetenceAv[9])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[105])
	talentsJoueur.append(listeTalents[21])
	talentsJoueur.append(listeTalents[17])
	talentsJoueur.append(listeTalents[19])
	talentsJoueur.append(listeTalents[37])
	
def gardienTribal():
	global carriereJoueur
	carriereJoueur = listeCarrieres[27]
	repartCaracteristiqueCT(race)
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetence[7])
	competencesJoueur.append(listeCompetence[9])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(choice([listeCompetence[11],listeCompetenceAv[108]]))
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[105])
	competencesJoueur.append(listeCompetence[19])
	talentsJoueur.append(listeTalents[89])
	talentsJoueur.append(listeTalents[66])
	
def geolier():
	global carriereJoueur
	carriereJoueur = listeCarrieres[28]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetence[2])
	competencesJoueur.append(listeCompetenceAv[108])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetence[17])
	talentsJoueur.append(listeTalents[41])
	talentsJoueur.append(listeTalents[57])
	talentsJoueur.append(listeTalents[71])
	talentsJoueur.append(listeTalents[72])
	dotations.append("1 filet")
	dotations.append("1 fouet")
	dotations.append("1 paire de menottes")
	
def gladiateur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[29]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[12])
	talentsJoueur.append(choice([listeTalents[18],listeTalents[84]]))
	talentsJoueur.append(listeTalents[19])
	talentsJoueur.append(listeTalents[21])
	talentsJoueur.append(listeTalents[27])
	talentsJoueur.append(listeTalents[55])
	talentsJoueur.append(listeTalents[53])
	talentsJoueur.append(listeTalents[58])
	dotations.append("1 brise lame")
	dotations.append("arme : fléau")

def hierogrammate():
	global carriereJoueur
	carriereJoueur = listeCarrieres[69]
	repartCaracteristiqueMage(race)
	profilSecondR["Mag"] = 1
	competencesJoueur.append(listeCompetenceAv[13])
	competencesJoueur.append(listeCompetenceAv[19])
	competencesJoueur.append(listeCompetenceAv[51])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[53])
	competencesJoueur.append(listeCompetenceAv[55])
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[107])
	talentsJoueur.append(listeTalents[33])
	talentsJoueur.append(listeTalents[42])
	talentsJoueur.append(listeTalents[110])

def hommeLige():
	global carriereJoueur
	carriereJoueur = listeCarrieres[62]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetence[3])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetence[13])
	competencesJoueur.append(listeCompetence[17])
	talentsJoueur.append(listeTalents[19])
	talentsJoueur.append(listeTalents[choice([37,75])])
	talentsJoueur.append(listeTalents[choice([55,84])])
	talentsJoueur.append(listeTalents[61])
	talentsJoueur.append(listeTalents[91])

def horsLaLoi():
	global carriereJoueur
	carriereJoueur = listeCarrieres[30]
	repartCaracteristiqueFurtif(race)
	competencesJoueur.append(listeCompetenceAv[3])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(choice([listeCompetence[4],listeCompetence[8]]))
	competencesJoueur.append(choice([listeCompetenceAv[22],listeCompetence[18]]))
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetence[7])
	competencesJoueur.append(listeCompetence[9])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(choice([listeTalents[3],listeTalents[17]]))
	talentsJoueur.append(listeTalents[7])

def ingenieurChaos():
	global carriereJoueur
	carriereJoueur = listeCarrieres[68]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(listeCompetence[4])
	competencesJoueur.append(listeCompetenceAv[11])
	competencesJoueur.append(listeCompetenceAv[13])
	competencesJoueur.append(listeCompetenceAv[(random.randint(20,31))])
	competencesJoueur.append(listeCompetenceAv[(random.randint(20,31))])
	competencesJoueur.append(listeCompetenceAv[(random.randint(60,72))])
	competencesJoueur.append(listeCompetenceAv[(random.randint(60,72))])
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetenceAv[76])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[47])
	talentsJoueur.append(listeTalents[50])
	dotations.append("1 putain de tromblon !")
	
def initie():
	global carriereJoueur
	carriereJoueur = listeCarrieres[31]
	repartCaracteristiquePretre(race)
	profilSecondR["Mag"] = 1
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(choice([listeCompetenceAv[7],listeCompetenceAv[10]]))
	competencesJoueur.append(listeCompetenceAv[19])
	competencesJoueur.append(listeCompetenceAv[111])
	competencesJoueur.append(listeCompetenceAv[67])
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[108])
	competencesJoueur.append(listeCompetenceAv[51])
	talentsJoueur.append(listeTalents[25])
	talentsJoueur.append(listeTalents[27])
	talentsJoueur.append(listeTalents[32])
	
def kossarKislevite():
	global carriereJoueur
	carriereJoueur = listeCarrieres[32]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence[13]]))
	competencesJoueur.append(listeCompetenceAv[25])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[65])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[17])
	competencesJoueur.append(listeCompetence[19])
	talentsJoueur.append(listeTalents[18])
	talentsJoueur.append(listeTalents[55])

def maledictor():
	global carriereJoueur
	carriereJoueur = listeCarrieres[63]
	repartCaracteristiqueMage(race)
	profilSecondR["Mag"] = 1
	competencesJoueur.append(listeCompetenceAv[8])
	competencesJoueur.append(listeCompetenceAv[13])
	competencesJoueur.append(listeCompetenceAv[51])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[53])
	competencesJoueur.append(listeCompetenceAv[(random.randint(60,72))])
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[107])
	talentsJoueur.append(listeTalents[choice([33,46])])
	defineTalentVsProfilPpal(profilPpal["E"], listeTalents[68], listeTalents[37])
	talentsJoueur.append(listeTalents[42]) # ajouté, voir avec Thib
	talentsJoueur.append(listeTalents[83])
	# ajouter une mutation obligatoire pour cette carrière

def maraudeur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[60]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetenceAv[112])
	competencesJoueur.append(listeCompetence[8])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[114])
	competencesJoueur.append(listeCompetenceAv[104])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[105])
	competencesJoueur.append(listeCompetence[17])
	competencesJoueur.append(listeCompetence[18])
	competencesJoueur.append(listeCompetence[19])
	talentsJoueur.append(listeTalents[18])
	talentsJoueur.append(listeTalents[51])
	talentsJoueur.append(listeTalents[80])

def marin():
	global carriereJoueur
	carriereJoueur = listeCarrieres[33]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetence[0])
	competencesJoueur.append(choice([listeCompetenceAv[20],listeCompetenceAv[27],listeCompetenceAv[29],listeCompetenceAv[31]]))
	competencesJoueur.append(listeCompetence[9])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(choice([listeCompetenceAv[60],listeCompetenceAv[66],listeCompetenceAv[68]]))
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[22])
	talentsJoueur.append(choice([listeTalents[14],listeTalents[19]]))
	talentsJoueur.append(listeTalents[31])
	
def matelot():
	global carriereJoueur
	carriereJoueur = listeCarrieres[34]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetence[0])
	competencesJoueur.append(choice([listeCompetence[3],listeCompetenceAv[56]]))
	competencesJoueur.append(choice([listeCompetenceAv[29],listeCompetence[13]]))
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetence[17])
	talentsJoueur.append(listeTalents[17])
	talentsJoueur.append(listeTalents[19])
	talentsJoueur.append(choice([listeTalents[21],listeTalents[84]]))
	
def mercanti():
	global carriereJoueur
	carriereJoueur = listeCarrieres[35]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(listeCompetence[3])
	competencesJoueur.append(choice([listeCompetence[4],listeCompetence[18]]))
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[14])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(choice([listeCompetenceAv[35],listeCompetenceAv[60],listeCompetenceAv[65],listeCompetenceAv[68]]))
	competencesJoueur.append(choice([listeCompetenceAv[76],listeCompetenceAv[80],listeCompetenceAv[85],listeCompetenceAv[87],listeCompetenceAv[88],listeCompetenceAv[89],listeCompetenceAv[92],listeCompetenceAv[93],listeCompetenceAv[95],listeCompetenceAv[100]]))
	talentsJoueur.append(listeTalents[23])
	talentsJoueur.append(listeTalents[22])
	talentsJoueur.append(listeTalents[29])
	talentsJoueur.append(choice([listeTalents[31],listeTalents[71]]))
	
def mercenaire():
	global carriereJoueur
	carriereJoueur = listeCarrieres[36]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence[14]]))
	competencesJoueur.append(choice([listeCompetence[4],listeCompetence[8]]))
	competencesJoueur.append(choice([listeCompetenceAv[20],listeCompetenceAv[25],listeCompetenceAv[31]]))
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(choice([listeCompetence[13],listeCompetence[18]]))
	competencesJoueur.append(listeCompetenceAv[56])
	competencesJoueur.append(choice([listeCompetenceAv[68],listeCompetence[15]]))
	talentsJoueur.append(choice([listeTalents[3],listeTalents[17]]))
	if listeTalents[3] in talentsJoueur:
		talentsJoueur.append(listeTalents[66])
		talentsJoueur.append(listeTalents[84])
	elif listeTalents[17] in talentsJoueur:
		talentsJoueur.append(listeTalents[19])
		talentsJoueur.append(listeTalents[21])
	
def messager():
	global carriereJoueur
	carriereJoueur = listeCarrieres[37]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(listeCompetenceAv[0])
	competencesJoueur.append(choice([listeCompetence[3],listeCompetenceAv[22],listeCompetenceAv[29]]))
	competencesJoueur.append(listeCompetence[8])
	competencesJoueur.append(listeCompetenceAv[67])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetenceAv[104])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[18])
	competencesJoueur.append(listeCompetence[19])
	talentsJoueur.append(listeTalents[31])
	talentsJoueur.append(listeTalents[80])
	
def milicien():
	global carriereJoueur
	carriereJoueur = listeCarrieres[38]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence[13]]))
	competencesJoueur.append(choice([listeCompetence[4],listeCompetence[15]]))
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[random.randint(75, 102)])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[18])
	competencesJoueur.append(listeCompetence[19])
	talentsJoueur.append(listeTalents[19])
	talentsJoueur.append(choice([listeTalents[55],listeTalents[66]]))
	
def mineur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[39]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetence[7])
	competencesJoueur.append(listeCompetence[9])
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(choice([listeCompetenceAv[97],listeCompetenceAv[99]]))
	competencesJoueur.append(listeCompetenceAv[104])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[18])
	defineTalentVsProfilPpal(profilPpal["E"], listeTalents[68], listeTalents[32])
	talentsJoueur.append(listeTalents[55])
	talentsJoueur.append(listeTalents[80])

def noble():
	global carriereJoueur
	carriereJoueur = listeCarrieres[40]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(choice([listeCompetenceAv[4],listeCompetence[2]]))
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence13]))
	competencesJoueur.append(listeCompetenceAv[22])
	competencesJoueur.append(listeCompetence[8])
	competencesJoueur.append(choice([listeCompetenceAv[49],listeCompetence[17]]))
	competencesJoueur.append(listeCompetenceAv[67])
	competencesJoueur.append(listeCompetenceAv[74])
	talentsJoueur.append(listeTalents[10])
	talentsJoueur.append(listeTalents[26])
	talentsJoueur.append(listeTalents[54])
	talentsJoueur.append(listeTalents[53])
	dotations.append("1 rapière")
	dotations.append("1 brise lame")

def oracle():
	global carriereJoueur
	carriereJoueur = listeCarrieres[64]
	repartCaracteristiqueMage(race)
	profilSecondR["Mag"] = 1
	competencesJoueur.append(listeCompetenceAv[choice([4,53,55])])
	competencesJoueur.append(listeCompetenceAv[34])
	competencesJoueur.append(listeCompetenceAv[51])
	competencesJoueur.append(listeCompetenceAv[107])
	talentsJoueur.append(listeTalents[45])
	talentsJoueur.append(listeTalents[25])
	talentsJoueur.append(listeTalents[79])
	
def passeur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[41]
	repartCaracteristiqueCT(race)
	competencesJoueur.append(listeCompetence[0])
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetenceAv[22])
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(listeCompetence[14])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[50])
	talentsJoueur.append(listeTalents[89])
	dotations.append("1 pistolet")
	
def patrouilleur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[42]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(listeCompetenceAv[105])
	competencesJoueur.append(choice([listeCompetence[3],listeCompetenceAv[22]]))
	competencesJoueur.append(listeCompetence[4])
	competencesJoueur.append(listeCompetence[8])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[104])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[18])
	competencesJoueur.append(listeCompetence[19])
	talentsJoueur.append(listeTalents[50])
	talentsJoueur.append(choice([listeTalents[66],listeTalents[84]]))
	dotations.append("1 pistolet")
	dotations.append("1 putain de tromblon !")
	
def paysan():
	global carriereJoueur
	carriereJoueur = listeCarrieres[43]
	repartCaracteristiqueFurtif(race)
	competencesJoueur.append(choice([listeCompetenceAv[5],listeCompetence[0]]))
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(choice([listeCompetence[4],listeCompetenceAv[87]]))
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetence[7])
	competencesJoueur.append(choice([listeCompetenceAv[33],listeCompetence[15]]))
	if listeCompetenceAv[33] in competencesJoueur:
		dotations.append(choice(["un chien", "un chien de guerre", "un corbeau"]))
		competencesJoueur.append(listeCompetenceAv[34])
	else:
		competencesJoueur.append(choice([listeCompetenceAv[34],listeCompetenceAv[85]]))
	competencesJoueur.append(choice([listeCompetenceAv[40],listeCompetenceAv[46],listeCompetence[13]]))
	competencesJoueur.append(choice([listeCompetenceAv[91],listeCompetence[19]]))
	talentsJoueur.append(listeTalents[22])
	talentsJoueur.append(choice([listeTalents[29],listeTalents[59]]))
	if listeTalents[59] in talentsJoueur:
		dotations.append("1 fustibale")
	
def pecheur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[44]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(listeCompetence[0])
	competencesJoueur.append(choice([listeCompetenceAv[22],listeCompetenceAv[29]]))
	competencesJoueur.append(choice([listeCompetenceAv[67],listeCompetenceAv[66]]))
	competencesJoueur.append(choice([listeCompetence[14],listeCompetence[17]]))
	competencesJoueur.append(listeCompetenceAv[104])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetenceAv[103])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[19])
	talentsJoueur.append(listeTalents[80])
	talentsJoueur.append(listeTalents[22])

def pillard():
	global carriereJoueur
	carriereJoueur = listeCarrieres[65]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(listeCompetence[0])
	competencesJoueur.append(listeCompetenceAv[choice([20,22,27,29,31,115,116])])
	competencesJoueur.append(listeCompetence[9])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetenceAv[choice([60,61,67,68])])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetenceAv[103])
	competencesJoueur.append(listeCompetence[17])
	talentsJoueur.append(listeTalents[22])
	talentsJoueur.append(listeTalents[19])
	talentsJoueur.append(listeTalents[31])
	
def pilleurTombes():
	global carriereJoueur
	carriereJoueur = listeCarrieres[45]
	repartCaracteristiqueFurtif(race)
	competencesJoueur.append(choice([listeCompetenceAv[3],listeCompetenceAv[22]]))
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetence[7])
	competencesJoueur.append(listeCompetence[9])
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[choice([111,64,61])])
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[8])
	talentsJoueur.append(listeTalents[10])
	
def porterune():
	global carriereJoueur
	carriereJoueur = listeCarrieres[46]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetenceAv[0])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetenceAv[104])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[19])
	talentsJoueur.append(choice([listeTalents[20],listeTalents[81]]))
	defineTalentVsProfilPpal(profilPpal["E"], listeTalents[68], listeTalents[27])
	talentsJoueur.append(listeTalents[29])
	talentsJoueur.append(listeTalents[66])
	talentsJoueur.append(listeTalents[80])
	
def ratier():
	global carriereJoueur
	carriereJoueur = listeCarrieres[47]
	repartCaracteristiqueFurtif(race)
	competencesJoueur.append(listeCompetenceAv[5])
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetence[7])
	competencesJoueur.append(listeCompetenceAv[33])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetence[18])
	talentsJoueur.append(listeTalents[8])
	talentsJoueur.append(listeTalents[59])
	talentsJoueur.append(listeTalents[71])
	talentsJoueur.append(listeTalents[72])
	dotations.append(choice(["un chien", "un chien de guerre", "un corbeau"]))
	dotations.append("1 fustibale")
	
def regisseur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[48]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(choice([listeCompetence[2],listeCompetenceAv[104]]))
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence[18]]))
	competencesJoueur.append(listeCompetenceAv[9])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetence[8])
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[26])
	talentsJoueur.append(listeTalents[25])

def scalde():
	global carriereJoueur
	carriereJoueur = listeCarrieres[66]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(listeCompetenceAv[4])
	competencesJoueur.append(listeCompetence[1])
	competencesJoueur.append(listeCompetence[3])
	competencesJoueur.append(listeCompetenceAv[10])
	competencesJoueur.append(listeCompetenceAv[27])
	competencesJoueur.append(listeCompetenceAv[112])
	competencesJoueur.append(listeCompetenceAv[(random.randint(37,49))])
	competencesJoueur.append(listeCompetenceAv[(random.randint(37,49))])
	competencesJoueur.append(listeCompetenceAv[66])
	competencesJoueur.append(listeCompetenceAv[110])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[25])
	talentsJoueur.append(listeTalents[34])
	talentsJoueur.append(listeTalents[37])
	talentsJoueur.append(listeTalents[82])
	
def scribe():
	global carriereJoueur
	carriereJoueur = listeCarrieres[49]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(choice([listeCompetence[3],listeCompetenceAv[22]]))
	competencesJoueur.append(listeCompetenceAv[random.randint(6,19)])
	competencesJoueur.append(listeCompetenceAv[57])
	competencesJoueur.append(listeCompetenceAv[60])
	competencesJoueur.append(listeCompetenceAv[111])
	competencesJoueur.append(choice([listeCompetenceAv[67],listeCompetenceAv[68]]))
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetenceAv[79])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[40])
	dotations.append("1 bic 4 couleurs et du tipex !")
	
def sentinelleHalfling():
	global carriereJoueur
	carriereJoueur = listeCarrieres[50]
	repartCaracteristiqueCT(race)
	competencesJoueur.append(choice([listeCompetenceAv[14],listeCompetenceAv[22]]))
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetence[7])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[105])
	competencesJoueur.append(listeCompetence[19])
	talentsJoueur.append(listeTalents[84])
	talentsJoueur.append(choice([listeTalents[20],listeTalents[37]]))
	competencesJoueur.append(listeCompetenceAv[66])
	
def serviteur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[51]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(listeCompetenceAv[4])
	competencesJoueur.append(listeCompetence[3])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[35])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(choice([listeCompetenceAv[85],listeCompetence[18]]))
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[29])
	talentsJoueur.append(listeTalents[22])
	defineTalentVsProfilPpal(profilPpal["E"], listeTalents[68], listeTalents[67])
	
def soldat():
	global carriereJoueur
	carriereJoueur = listeCarrieres[52]
	repartCaracteristiquePolyvalent(race)
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence[13]]))
	competencesJoueur.append(choice([listeCompetence[4],listeCompetence[8]]))
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetenceAv[108])
	talentsJoueur.append(choice([listeTalents[3],listeTalents[19]]))
	if listeTalents[3] in talentsJoueur:
		talentsJoueur.append(listeTalents[88])
		talentsJoueur.append(listeTalents[66])
		talentsJoueur.append(listeTalents[84])
		talentsJoueur.append(listeTalents[50])
		dotations.append("1 pistolet")
		dotations.append("1 arquebuse !")
	elif listeTalents[19] in talentsJoueur:
		talentsJoueur.append(listeTalents[17])
		talentsJoueur.append(listeTalents[18])
		talentsJoueur.append(listeTalents[21])
		talentsJoueur.append(listeTalents[55])
	
def sorcierVillage():
	global carriereJoueur
	carriereJoueur = listeCarrieres[53]
	repartCaracteristiqueMage(race)
	profilSecondR["Mag"] = 1
	competencesJoueur.append(choice([listeCompetence[1],listeCompetence[12]]))
	competencesJoueur.append(choice([listeCompetenceAv[34],listeCompetenceAv[75]]))
	competencesJoueur.append(listeCompetenceAv[51])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[108])
	competencesJoueur.append(choice([listeCompetence[14],listeCompetence[18]]))
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[107])
	talentsJoueur.append(listeTalents[42])
	talentsJoueur.append(choice([listeTalents[83],listeTalents[104]]))
	
def spadassin():
	global carriereJoueur
	carriereJoueur = listeCarrieres[54]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence[14]]))
	competencesJoueur.append(listeCompetence[8])
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[12])
	talentsJoueur.append(listeTalents[13])
	competencesJoueur.append(listeCompetenceAv[17])
	competencesJoueur.append(listeCompetenceAv[18])
	competencesJoueur.append(listeCompetenceAv[19])
	talentsJoueur.append(choice([listeTalents[21],listeTalents[84]]))
	competencesJoueur.append(listeCompetenceAv[61])
	
def trafiquantCadavres():
	global carriereJoueur
	carriereJoueur = listeCarrieres[55]
	repartCaracteristiqueFurtif(race)
	competencesJoueur.append(listeCompetenceAv[3])
	competencesJoueur.append(choice([listeCompetence[3],listeCompetence[14]]))
	competencesJoueur.append(listeCompetence[4])
	competencesJoueur.append(listeCompetence[6])
	# competencesJoueur.append(listeCompetence[7])?
	competencesJoueur.append(listeCompetence[9])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(choice([listeTalents[12],listeTalents[74]]))
	talentsJoueur.append(listeTalents[29])
	talentsJoueur.append(listeTalents[71])
	
def tueurTrolls():
	global carriereJoueur
	carriereJoueur = listeCarrieres[56]
	repartCaracteristiqueCAC(race)
	competencesJoueur.append(listeCompetenceAv[36])
	competencesJoueur.append(listeCompetence[12])
	competencesJoueur.append(listeCompetence[17])
	talentsJoueur.append(listeTalents[13])
	talentsJoueur.append(listeTalents[19])
	talentsJoueur.append(choice([listeTalents[21],listeTalents[84]]))
	talentsJoueur.append(listeTalents[22])
	talentsJoueur.append(listeTalents[55])
	defineTalentVsProfilPpal(profilPpal["E"], listeTalents[68], listeTalents[67])
	
def vagabond():
	global carriereJoueur
	carriereJoueur = listeCarrieres[57]
	repartCaracteristiqueFurtif(race)
	competencesJoueur.append(choice([listeCompetenceAv[choice([1,3])],listeCompetenceAv[choice([40,44,46])]]))
	competencesJoueur.append(choice([listeCompetence[3],listeCompetenceAv[1],listeCompetenceAv[3]]))
	competencesJoueur.append(listeCompetenceAv[choice([20,23,25,31])])
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetence[15])
	competencesJoueur.append(listeCompetenceAv[104])
	competencesJoueur.append(listeCompetence[16])
	competencesJoueur.append(listeCompetenceAv[108])
	competencesJoueur.append(listeCompetence[19])
	talentsJoueur.append(choice([listeTalents[7],listeTalents[20]]))
	talentsJoueur.append(listeTalents[31])
	talentsJoueur.append(listeTalents[89])
	
def valet():
	global carriereJoueur
	carriereJoueur = listeCarrieres[58]
	repartCaracteristiqueNaze(race)
	competencesJoueur.append(listeCompetenceAv[4])
	competencesJoueur.append(choice([listeCompetence[3],listeCompetenceAv[60],listeCompetenceAv[67]]))
	competencesJoueur.append(listeCompetenceAv[12])
	competencesJoueur.append(listeCompetence[10])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetenceAv[74])
	competencesJoueur.append(listeCompetence[14])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(choice([listeTalents[23],listeTalents[31]]))
	talentsJoueur.append(listeTalents[26])
	talentsJoueur.append(listeTalents[75])
	dotations.append("1 cosplay de soubrette des plus seyant !")
	
def voleur():
	global carriereJoueur
	carriereJoueur = listeCarrieres[59]
	repartCaracteristiqueFurtif(race)
	competencesJoueur.append(choice([listeCompetenceAv[3],listeCompetenceAv[59]]))
	competencesJoueur.append(choice([listeCompetence[1],listeCompetence[9]]))
	competencesJoueur.append(listeCompetenceAv[32])
	competencesJoueur.append(choice([listeCompetence[5],listeCompetence[10]]))
	competencesJoueur.append(listeCompetence[6])
	competencesJoueur.append(listeCompetence[7])
	competencesJoueur.append(listeCompetenceAv[35])
	competencesJoueur.append(listeCompetence[11])
	competencesJoueur.append(listeCompetence[16])
	talentsJoueur.append(listeTalents[15])
	talentsJoueur.append(listeTalents[9])



reponse = "o"

while reponse == "o":

	dicesList = []

	profilPpal = {
		"CC": 20,
		"CT": 20,
		"F": 20,
		"E": 20,
		"Ag": 20,
		"Int": 20,
		"FM": 20,
		"Soc": 20,
	}
	profilSecondR = {
		"A": 1,
		"B": 0,
		"BF": 0,
		"BE": 0,
		"M": 0,
		"Mag": 0,
		"PF": 0,
		"PD": 0,
	}

	tmp = 0

	def defineMutation():
		global profilPpal
		global profilSecondR
		mut = random.randint(1,100)
		if 1 <= mut <= 27:
			print("*** Vous avez des cornes ! Elles sont utilisables pour attaquer, BF-1. ***")
		elif 28 <= mut <= 45:
			print("*** Votre corps entier est recouvert d'écailles ! Vous gagnez 1 pt d'armure partout ! ***")
		elif 46 <= mut <= 54:
			print("*** Votre corps entier est recouvert d'une épaisse fourrure ! Vous gagnez 1 pt d'armure partout ! ***")
		elif 55 <= mut <= 63:
			print("*** Vous avez les jambes... d'un animal ! Vous gagnez +1 en Mouvement ! ***")
			profilSecondR["M"] += 1
		elif 64 <= mut <= 72:
			print("*** Sur votre visage... vous avez un museau ! Vous gagnez la compétence Pistage. ***")
			competencesJoueur.append(listeCompetenceAv[105])
		elif 73 <= mut <= 81:
			tmp = random.randint(1,10)
			print("*** Vous êtes obèse. Vous gagnez +1 PV et +{}% en Force ! ***".format(tmp))
			profilPpal["F"] += tmp
			profilSecondR["B"] += 1
		elif 82 <= mut <= 90:
			tmp = random.randint(1,10)
			print("*** Vous avez... une queue ! Vous gagnez +{}% en Ag ! ***".format(tmp))
			profilPpal["Ag"] += tmp
		elif 91 <= mut <= 100:
			print("*** Sur votre visage... vous avez un 3ème oeil ! Vous gagnez +5% en perception visuelle. ***")

	# utilisation de la fonction de génération des 11 jets de dés
	dices(dicesList)

	# menu du choix de la race
	print("Saisissez le D10 de votre joueur pour déterminer sa race")
	print("Mémo :")
	print("1 à 5 : Humain")
	print("    6 : Humain Kurgan")
	print("    7 : Humain Norse")
	print("    8 : Nain")
	print("    9 : Nain du Chaos")
	print("   10 : Nain Norse")
	print("   11 : Halfling")
	print("   12 : Elf")

	race = input(">:")


	while race != "1" and race != "2" and race != "3" and race != "4" and race != "5" and race != "6" and race != "7" and race != "8" and race != "9" and race != "10" and race != "11" and race != "12": 
		print("Merci de taper un nombre, entre 1 et 10.")
		race = input(">:")

	# saisie du score du joueur lors de son jet de D100 pour choisir sa carrière
	print("Saisissez le D100 de votre joueur pour déterminer sa carrière.")
	scoreD100 = input (">:")
	
	while scoreD100.isdigit() == False: 
		print("Merci de taper un nombre.")
		scoreD100 = input (">:")

	"""
	while scoreD100.isalpha() or scoreD100.isalnum() or scoreD100.isdecimal():
		print("Merci de taper un nombre, et non une lettre.")
		scoreD100 = input (">:")
	"""

	scoreD100 = int(scoreD100)

	while scoreD100 < 1 or scoreD100 > 100:
		print("Merci de taper un nombre, entre 1 et 100.")
		scoreD100 = input(">:")
		scoreD100 = int(scoreD100)

	os.system('cls')

	print("Nos 8 dés définitifs sont : {}".format(dicesList))
	print ("---------------------------------------------------------------------------------------------")

	competencesJoueur = []
	talentsJoueur = []
	dotations = []
	carriereJoueur = ""

	# fonction de repartition des dés en fonction de la race carrière	
	# x1 à x8 représentent les bonus / malus de chaque race pour chacune des caractéristiques ppales
	def repartCaracteristique(listeCaracProfilPpal, CC, x0, CT, x1, F, x2, E, x3, Ag, x4, Int, x5, FM, x6, Soc, x7):
		listeCaracProfilPpal["CC"] += (dicesList[CC] + x0)
		listeCaracProfilPpal["CT"] += (dicesList[CT] + x1)
		listeCaracProfilPpal["F"] += (dicesList[F] + x2)
		listeCaracProfilPpal["E"] += (dicesList[E] + x3)
		listeCaracProfilPpal["Ag"] += (dicesList[Ag] + x4)
		listeCaracProfilPpal["Int"] += (dicesList[Int] + x5)
		listeCaracProfilPpal["FM"] += (dicesList[FM] + x6)
		listeCaracProfilPpal["Soc"] += (dicesList[Soc] + x7)
		return listeCaracProfilPpal

	def repartCaracteristiqueCAC(a):
		global profilPpal
		if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "7":
			"""	
			la suite de nombre est construite comme suit : 
			- le 1er nombre est la priorité que l'on souhaite donner à la CC, de 0 à 7 
			(car le nombre représente l'index de notre dicesList classé par ordre décroissant)
			- le 2ème nombre est le bonus / malus de la race à la CC, en partant 20 (CC humaine)
			- le 3ème nombre est la priorité que l'on souhaite donner à la CT, de 0 à 7
			- le 4ème nombre est le bonus / malus de la race à la CT, en partant 20 (CT humaine) 
			- etc.
			"""
			repartCaracteristique(profilPpal, 0, 0, 6, 0, 1, 0, 2, 0, 3, 0, 5, 0, 4, 0, 7, 0)
		elif a == "6":
			repartCaracteristique(profilPpal, 0, 0, 6, 0, 1, +5, 2, +5, 3, 0, 5, -5, 4, 0, 7, -5)
		elif a == "8" or a == "9" or a == "10":
			repartCaracteristique(profilPpal, 0, +10, 6, 0, 1, 0, 2, +10, 3, -10, 5, 0, 4, 0, 7, 0)
		elif a == "11":
			repartCaracteristique(profilPpal, 0, 0, 6, +10, 1, -10, 2, -10, 3, +10, 5, 0, 4, 0, 7, +10)
		elif a == "12":
			repartCaracteristique(profilPpal, 0, 0, 6, +10, 1, 0, 2, 0, 3, +10, 5, 0, 4, 0, 7, 0)

	def repartCaracteristiqueCT(a):
		global profilPpal
		if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "7":
			repartCaracteristique(profilPpal, 4, 0, 0, 0, 5, 0, 2, 0, 1, 0, 6, 0, 3, 0, 7, 0)
		elif a == "6":
			repartCaracteristique(profilPpal, 4, 0, 0, 0, 5, +5, 2, +5, 1, 0, 6, -5, 3, 0, 7, -5)
		elif a == "8" or a == "9" or a == "10":
			repartCaracteristique(profilPpal, 4, +10, 0, 0, 5, 0, 2, +10, 1, -10, 6, 0, 3, 0, 7, 0)
		elif a == "11":
			repartCaracteristique(profilPpal, 4, 0, 0, +10, 5, -10, 2, -10, 1, +10, 6, 0, 3, 0, 7, +10)
		elif a == "12":
			repartCaracteristique(profilPpal, 4, 0, 0, +10, 5, 0, 2, 0, 1, +10, 6, 0, 3, 0, 7, 0)

	def repartCaracteristiquePolyvalent(a):
		global profilPpal
		if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "7":
			repartCaracteristique(profilPpal, 0, 0, 1, 0, 2, 0, 4, 0, 3, 0, 5, 0, 6, 0, 7, 0)
		elif a == "6":
			repartCaracteristique(profilPpal, 0, 0, 1, 0, 2, +5, 4, +5, 3, 0, 5, -5, 6, 0, 7, -5)
		elif a == "8" or a == "9" or a == "10":
			repartCaracteristique(profilPpal, 0, +10, 1, 0, 2, 0, 4, +10, 3, -10, 5, 0, 6, 0, 7, 0)
		elif a == "11":
			repartCaracteristique(profilPpal, 0, 0, 1, +10, 2, -10, 4, -10, 3, +10, 5, 0, 6, 0, 7, +10)
		elif a == "12":
			repartCaracteristique(profilPpal, 0, 0, 1, +10, 2, 0, 4, 0, 3, +10, 5, 0, 6, 0, 7, 0)

	def repartCaracteristiqueNaze(a):
		global profilPpal
		if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "7":
			repartCaracteristique(profilPpal, 0, 0, 1, 0, 3, 0, 5, 0, 4, 0, 2, 0, 6, 0, 7, 0)
		elif a == "6":
			repartCaracteristique(profilPpal, 0, 0, 1, 0, 3, +5, 5, +5, 4, 0, 2, -5, 6, 0, 7, -5)
		elif a == "8" or a == "9" or a == "10":
			repartCaracteristique(profilPpal, 0, +10, 1, 0, 3, 0, 5, +10, 4, -10, 2, 0, 6, 0, 7, 0)
		elif a == "11":
			repartCaracteristique(profilPpal, 0, 0, 1, +10, 3, -10, 5, -10, 4, +10, 2, 0, 6, 0, 7, +10)
		elif a == "12":
			repartCaracteristique(profilPpal, 0, 0, 1, +10, 3, 0, 5, 0, 4, +10, 2, 0, 6, 0, 7, 0)

	def repartCaracteristiqueMage(a):
		global profilPpal
		if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "7":
			repartCaracteristique(profilPpal, 3, 0, 6, 0, 5, 0, 1, 0, 4, 0, 2, 0, 0, 0, 7, 0)
		elif a == "6":
			repartCaracteristique(profilPpal, 3, 0, 6, 0, 5, +5, 1, +5, 4, 0, 2, -5, 0, 0, 7, -5)
		elif a == "8" or a == "9" or a == "10":
			repartCaracteristique(profilPpal, 3, +10, 6, 0, 5, 0, 1, +10, 4, -10, 2, 0, 0, 0, 7, 0)
		elif a == "11":
			repartCaracteristique(profilPpal, 3, 0, 6, +10, 5, -10, 1, -10, 4, +10, 2, 0, 0, 0, 7, +10)
		elif a == "12":
			repartCaracteristique(profilPpal, 3, 0, 6, +10, 5, 0, 1, 0, 4, +10, 2, 0, 0, 0, 7, 0)

	def repartCaracteristiquePretre(a):
		global profilPpal
		if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "7":
			repartCaracteristique(profilPpal, 0, 0, 6, 0, 2, 0, 1, 0, 4, 0, 5, 0, 3, 0, 7, 0)
		elif a == "6":
			repartCaracteristique(profilPpal, 0, 0, 6, 0, 2, +5, 1, +5, 4, 0, 5, -5, 3, 0, 7, -5)
		elif a == "8" or a == "9" or a == "10":
			repartCaracteristique(profilPpal, 0, +10, 6, 0, 2, 0, 1, +10, 4, -10, 5, 0, 3, 0, 7, 0)
		elif a == "11":
			repartCaracteristique(profilPpal, 0, 0, 6, +10, 2, -10, 1, -10, 4, +10, 5, 0, 3, 0, 7, +10)
		elif a == "12":
			repartCaracteristique(profilPpal, 0, 0, 6, +10, 2, 0, 1, 0, 4, +10, 5, 0, 3, 0, 7, 0)


	def repartCaracteristiqueFurtif(a):
		global profilPpal
		if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "7":
			repartCaracteristique(profilPpal, 0, 0, 2, 0, 3, 0, 4, 0, 1, 0, 6, 0, 5, 0, 7, 0)
		elif a == "6":
			repartCaracteristique(profilPpal, 0, 0, 2, 0, 3, +5, 4, +5, 1, 0, 6, -5, 5, 0, 7, -5)
		elif a == "8" or a == "9" or a == "10":
			repartCaracteristique(profilPpal, 0, +10, 2, 0, 3, 0, 4, +10, 1, -10, 6, 0, 5, 0, 7, 0)
		elif a == "11":
			repartCaracteristique(profilPpal, 0, 0, 2, +10, 3, -10, 4, -10, 1, +10, 6, 0, 5, 0, 7, +10)
		elif a == "12":
			repartCaracteristique(profilPpal, 0, 0, 2, +10, 3, 0, 4, 0, 1, +10, 6, 0, 5, 0, 7, 0)

	def randomTalentHumain():
		global talentsJoueur
		A = random.randint(1, 100)
		B = random.randint(1, 100)
		while B == A:
			B = random.randint(1, 100)
		if 1 <= A <= 4:
			talentsJoueur.append(listeTalentsRandom[0])
		elif 5 <= A <= 9:
			talentsJoueur.append(listeTalentsRandom[1])
		elif 10 <= A <= 14:
			talentsJoueur.append(listeTalentsRandom[2])
		elif 15 <= A <= 18:
			talentsJoueur.append(listeTalentsRandom[3])
		elif 19 <= A <= 22:
			talentsJoueur.append(listeTalentsRandom[4])
		elif 23 <= A <= 26:
			talentsJoueur.append(listeTalentsRandom[5])
		elif 27 <= A <= 30:
			talentsJoueur.append(listeTalentsRandom[6])
		elif 31 <= A <= 35:
			talentsJoueur.append(listeTalentsRandom[7])
		elif 36 <= A <= 39:
			talentsJoueur.append(listeTalentsRandom[8])
		elif 40 <= A <= 44:
			talentsJoueur.append(listeTalentsRandom[9])
		elif 45 <= A <= 48:
			talentsJoueur.append(listeTalentsRandom[10])
		elif 49 <= A <= 53:
			talentsJoueur.append(listeTalentsRandom[11])
		elif 54 <= A <= 57:
			talentsJoueur.append(listeTalentsRandom[12])
		elif 58 <= A <= 61:
			talentsJoueur.append(listeTalentsRandom[13])
		elif 62 <= A <= 65:
			talentsJoueur.append(listeTalentsRandom[14])
		elif 66 <= A <= 69:
			talentsJoueur.append(listeTalentsRandom[15])
		elif 70 <= A <= 73:
			talentsJoueur.append(listeTalentsRandom[16])
		elif 74 <= A <= 77:
			talentsJoueur.append(listeTalentsRandom[17])
		elif 78 <= A <= 81:
			talentsJoueur.append(listeTalentsRandom[18])
		elif 82 <= A <= 85:
			talentsJoueur.append(listeTalentsRandom[19])
		elif 86 <= A <= 90:
			talentsJoueur.append(listeTalentsRandom[20])
		elif 91 <= A <= 95:
			talentsJoueur.append(listeTalentsRandom[21])
		elif 96 <= A <= 100:
			talentsJoueur.append(listeTalentsRandom[22])
		if 1 <= B <= 4:
			talentsJoueur.append(listeTalentsRandom[0])
		elif 5 <= B <= 9:
			talentsJoueur.append(listeTalentsRandom[1])
		elif 10 <= B <= 14:
			talentsJoueur.append(listeTalentsRandom[2])
		elif 15 <= B <= 18:
			talentsJoueur.append(listeTalentsRandom[3])
		elif 19 <= B <= 22:
			talentsJoueur.append(listeTalentsRandom[4])
		elif 23 <= B <= 26:
			talentsJoueur.append(listeTalentsRandom[5])
		elif 27 <= B <= 30:
			talentsJoueur.append(listeTalentsRandom[6])
		elif 31 <= B <= 35:
			talentsJoueur.append(listeTalentsRandom[7])
		elif 36 <= B <= 39:
			talentsJoueur.append(listeTalentsRandom[8])
		elif 40 <= B <= 44:
			talentsJoueur.append(listeTalentsRandom[9])
		elif 45 <= B <= 48:
			talentsJoueur.append(listeTalentsRandom[10])
		elif 49 <= B <= 53:
			talentsJoueur.append(listeTalentsRandom[11])
		elif 54 <= B <= 57:
			talentsJoueur.append(listeTalentsRandom[12])
		elif 58 <= B <= 61:
			talentsJoueur.append(listeTalentsRandom[13])
		elif 62 <= B <= 65:
			talentsJoueur.append(listeTalentsRandom[14])
		elif 66 <= B <= 69:
			talentsJoueur.append(listeTalentsRandom[15])
		elif 70 <= B <= 73:
			talentsJoueur.append(listeTalentsRandom[16])
		elif 74 <= B <= 77:
			talentsJoueur.append(listeTalentsRandom[17])
		elif 78 <= B <= 81:
			talentsJoueur.append(listeTalentsRandom[18])
		elif 82 <= B <= 85:
			talentsJoueur.append(listeTalentsRandom[19])
		elif 86 <= B <= 90:
			talentsJoueur.append(listeTalentsRandom[20])
		elif 91 <= B <= 95:
			talentsJoueur.append(listeTalentsRandom[21])
		elif 96 <= B <= 100:
			talentsJoueur.append(listeTalentsRandom[22])

	def randomTalentHalfling():
		global talentsJoueur
		A = random.randint(1, 100)
		if 1 <= A <= 5:
			talentsJoueur.append(listeTalentsRandom[0])
		elif 6 <= A <= 10:
			talentsJoueur.append(listeTalentsRandom[1])
		elif 11 <= A <= 15:
			talentsJoueur.append(listeTalentsRandom[2])
		elif 16 <= A <= 20:
			talentsJoueur.append(listeTalentsRandom[3])
		elif 21 <= A <= 25:
			talentsJoueur.append(listeTalentsRandom[4])
		elif 26 <= A <= 30:
			talentsJoueur.append(listeTalentsRandom[5])
		elif 31 <= A <= 35:
			talentsJoueur.append(listeTalentsRandom[6])
		elif 36 <= A <= 39:
			talentsJoueur.append(listeTalentsRandom[7])
		elif 40 <= A <= 43:
			talentsJoueur.append(listeTalentsRandom[8])
		elif 44 <= A <= 48:
			talentsJoueur.append(listeTalentsRandom[9])
		elif 49 <= A <= 53:
			talentsJoueur.append(listeTalentsRandom[10])
		elif 54 <= A <= 58:
			talentsJoueur.append(listeTalentsRandom[11])
		elif 59 <= A <= 62:
			talentsJoueur.append(listeTalentsRandom[12])
		elif 63 <= A <= 64:
			talentsJoueur.append(listeTalentsRandom[13])
		elif 65 <= A <= 68:
			talentsJoueur.append(listeTalentsRandom[14])
		elif 69 <= A <= 72:
			talentsJoueur.append(listeTalentsRandom[15])
		elif 73 <= A <= 76:
			talentsJoueur.append(listeTalentsRandom[16])
		elif 77 <= A <= 81:
			talentsJoueur.append(listeTalentsRandom[17])
		elif 82 <= A <= 86:
			talentsJoueur.append(listeTalentsRandom[18])
		elif 87 <= A <= 91:
			talentsJoueur.append(listeTalentsRandom[19])
		elif 92 <= A <= 96:
			talentsJoueur.append(listeTalentsRandom[20])
		elif 97 <= A <= 100:
			talentsJoueur.append(listeTalentsRandom[21])

	def randomTalentElf():
		global talentsJoueur
		talentsJoueur.append(listeTalents[2])
		talentsJoueur.append(listeTalents[49])
		b = random.randint(1, 2)
		if b == 1:
			talentsJoueur.append(listeTalents[37])
		elif b == 2:
			talentsJoueur.append(listeTalents[75])
		talentsJoueur.append(listeTalents[92])

	def randomCompTal(liste , listeRef, i1, i2):
		a = random.randint(1, 2)
		if a == 1:
			liste.append(listeRef[i1])
		elif a == 2:
			liste.append(listeRef[i2])

	def defineCompetenceTalentRace():
		global competencesJoueur
		global talentsJoueur
		if race == "1" or race == "2" or race == "3" or race == "4" or race == "5":
			competencesJoueur.append(listeCompetence[3])
			competencesJoueur.append(listeCompetenceAv[22])
			competencesJoueur.append(listeCompetenceAv[67])
			randomTalentHumain()

		elif race == "6":
			competencesJoueur.append(choice([listeCompetenceAv[112],listeCompetenceAv[113]]))
			competencesJoueur.append(listeCompetence[8])
			competencesJoueur.append(listeCompetenceAv[114])
			competencesJoueur.append(listeCompetence[19])
			talentsJoueur.append(listeTalents[22])
			talentsJoueur.append(listeTalents[32])
			talentsJoueur.append(listeTalents[108])

		elif race == "7":
			competencesJoueur.append(listeCompetenceAv[27])
			competencesJoueur.append(listeCompetenceAv[66])
			competencesJoueur.append(listeCompetenceAv[103])
			competencesJoueur.append(listeCompetence[17])
			competencesJoueur.append(listeCompetence[19])
			talentsJoueur.append(listeTalents[108])
			talentsJoueur.append(listeTalentsRandom[random.randint(0,22)])
			# je ne mets pas la fin de la liste de talents dans le random, car ils sont incohérents
			# ajouter 20% de chance d'avoir une mutation, ou pas ?

		elif race == "8":
			competencesJoueur.append(listeCompetenceAv[26])
			competencesJoueur.append(listeCompetenceAv[64])
			competencesJoueur.append(listeCompetenceAv[67])
			competencesJoueur.append(listeCompetenceAv[choice([92,94,97])])
			talentsJoueur.append(listeTalents[30])
			talentsJoueur.append(listeTalents[69])
			talentsJoueur.append(listeTalents[73])
			talentsJoueur.append(listeTalents[77])
			talentsJoueur.append(listeTalents[91])
			talentsJoueur.append(listeTalents[92])
			#Fureur vengeresse, Résistance à la magie, Robuste, Savoir-faire nain,Valeureux,Vision nocturne.

		elif race == "9":
			competencesJoueur.append(listeCompetenceAv[26])
			competencesJoueur.append(listeCompetenceAv[117])
			competencesJoueur.append(listeCompetence[11])
			competencesJoueur.append(listeCompetenceAv[63])
			competencesJoueur.append(listeCompetenceAv[76])
			talentsJoueur.append(listeTalents[73])
			talentsJoueur.append(listeTalents[77])
			talentsJoueur.append(listeTalents[91])
			talentsJoueur.append(listeTalents[92])

		elif race == "10":
			competencesJoueur.append(listeCompetenceAv[27])
			competencesJoueur.append(listeCompetenceAv[64])
			competencesJoueur.append(listeCompetenceAv[66])
			competencesJoueur.append(listeCompetenceAv[choice([92,94,97])])
			competencesJoueur.append(listeCompetence[17])
			talentsJoueur.append(listeTalents[30])
			talentsJoueur.append(listeTalents[69])
			talentsJoueur.append(listeTalents[73])
			talentsJoueur.append(listeTalents[108])
			talentsJoueur.append(listeTalents[77])
			talentsJoueur.append(listeTalents[91])
			talentsJoueur.append(listeTalents[92])
			#Fureur vengeresse, Résistance à la magie, Rompu au Chaos, Robuste, Savoir-faire nain,Valeureux,Vision nocturne.
		
		elif race == "11":
			competencesJoueur.append(listeCompetence[3])
			competencesJoueur.append(listeCompetenceAv[12])
			competencesJoueur.append(listeCompetenceAv[24])
			competencesJoueur.append(listeCompetenceAv[63])	
			competencesJoueur.append(listeCompetenceAv[67])
			randomCompTal(competencesJoueur, listeCompetenceAv, 85, 91)
			talentsJoueur.append(listeTalents[59])
			talentsJoueur.append(listeTalents[70])
			talentsJoueur.append(listeTalents[92])
			randomTalentHalfling()
			# Maîtrise (lance-pierres), Résistance au Chaos,Vision nocturne et 1 talent donné par la Table 2-4 : détermination aléatoire des talents.

		elif race == "12":
			competencesJoueur.append(listeCompetenceAv[21])
			competencesJoueur.append(listeCompetenceAv[61])
			competencesJoueur.append(listeCompetenceAv[67])
			randomTalentElf()
			#Acuité visuelle, Harmonie aethyrique ou Maîtrise (arcs longs), Intelligent ou Sang-froid,Vision nocturne.

	def defineTalentVsProfilPpal(carac, talent1, talent2):
		if (carac + 5) // 10 > carac // 10:
			talentsJoueur.append(talent1)
		else:
			talentsJoueur.append(talent2)

	def defineCompetenceTalentCarriere(score):
		global competencesJoueur
		global talentsJoueur
		global carriereJoueur
		global profilSecondR
		global dotations
		if race == "1" or race == "2" or race == "3" or race == "4" or race == "5":
			if 1 <= score <= 2:
				agitateur()
			elif 3 <= score <= 4:
				apprentiSorcier()
			elif 5 <= score <= 6:
				artisan()
			elif 7 <= score <= 8:
				bateleur()
			elif 9 <= score <= 10:
				batelier()
			elif score == 11:
				berserkNorse()
			elif 12 <= score <= 13:
				bourgeois()
			elif 14 <= score <= 15:
				bucheron()
			elif 16 <= score <= 17:
				charbonnier()
			elif 18 <= score <= 19:
				chasseurPrimes()
			elif 20 <= score <= 21:
				chasseur()
			elif 22 <= score <= 23:
				chiffonnier()
			elif score == 24:
				chirurgienBarbier()
			elif 25 <= score <= 26:
				cocher()
			elif 27 <= score <= 28:
				collecteurTaxes()
			elif 29 <= score <= 30:
				contrebandier()
			elif 31 <= score <= 32:
				coupeJarret()
			elif score == 33:
				diestroEstalien()
			elif 34 <= score <= 35:
				eclaireur()
			elif 36 <= score <= 37:
				ecuyer()
			elif 38 <= score <= 39:
				escroc()
			elif 40 <= score <= 41:
				etudiant()
			elif 42 <= score <= 43:
				fanatique()
			elif 44 <= score <= 45:
				gardeCorps()
			elif 46 <= score <= 47:
				garde()
			elif score == 48:
				geolier()
			elif 49 <= score <= 50:
				gladiateur()
			elif 51 <= score <= 52:
				horsLaLoi()
			elif 53 <= score <= 54:
				initie()
			elif score == 55:
				kossarKislevite()
			elif 56 <= score <= 57:
				marin()
			elif 58 <= score <= 59:
				matelot()
			elif 60 <= score <= 61:
				mercanti()
			elif 62 <= score <= 63:
				mercenaire()
			elif 64 <= score <= 65:
				messager()
			elif 66 <= score <= 67:
				milicien()
			elif 68 <= score <= 69:
				mineur()
			elif 70 <= score <= 71:
				noble()
			elif score == 72:
				passeur()
			elif 73 <= score <= 74:
				patrouilleur()
			elif 75 <= score <= 76:
				paysan()
			elif 77 <= score <= 78:
				pecheur()
			elif 79 <= score <= 80:
				pilleurTombes()
			elif 81 <= score <= 82:
				ratier()
			elif score == 83:
				regisseur()
			elif 84 <= score <= 85:
				scribe()
			elif 86 <= score <= 87:
				serviteur()
			elif 88 <= score <= 89:
				soldat()
			elif score == 90:
				sorcierVillage()
			elif 91 <= score <= 92:
				spadassin()
			elif 93 <= score <= 94:
				trafiquantCadavres()
			elif 95 <= score <= 96:
				vagabond()
			elif 97 <= score <= 98:
				valet()
			elif 99 <= score <= 100:
				voleur()
		
		elif race == "6":
			if 1 <= score <= 10:
				berserkNorse()
			elif 11 <= score <= 20:
				chasseur()
			elif 21 <= score <= 33:
				coupeJarret()
			elif 34 <= score <= 37:
				eclaireur()
			elif 38 <= score <= 39:
				sorcierVillage()
			elif 40 <= score <= 49:
				gladiateur()
			elif score == 50:
				horsLaLoi()
			elif 51 <= score <= 90:
				maraudeur()
			elif 90 <= score <= 100:
				mercenaire()

		elif race == "7":
			if 1 <= score <= 5:
				artisan()
			elif 6 <= score <= 8:
				baleinier()
			elif 9 <= score <= 10:
				bateleur()
			elif 11 <= score <= 20:
				berserkNorse()
			elif score == 21:
				bourgeois()
			elif 22 <= score <= 23:
				bucheron()
			elif 24 <= score <= 27:
				chasseur()
			elif 28 <= score <= 29:
				gardeCorps()
			elif 30 <= score <= 31:
				gladiateur()
			elif 32 <= score <= 34:
				hommeLige()
			elif score == 35:
				horsLaLoi()
			elif score == 36:
				maledictor()
			elif 37 <= score <= 58:
				maraudeur()
			elif score == 59:
				marin()
			elif 60 <= score <= 74:
				mercenaire()
			elif score == 75:
				oracle()
			elif 76 <= score <= 80:
				paysan()
			elif 81 <= score <= 90:
				pecheur()
			elif 91 <= score <= 97:
				pillard()
			elif 98 <= score <= 99:
				scalde()
			elif score == 100:
				serviteur()

		elif race == "8":
			if 1 <= score <= 2:
				agitateur()
			elif 3 <= score <= 6:
				artisan()
			elif 7 <= score <= 9:
				bateleur()
			elif 10 <= score <= 13:
				bourgeois()
			elif 14 <= score <= 17:
				chasseur()
			elif 18 <= score <= 19:
				cocher()
			elif 20 <= score <= 22:
				collecteurTaxes()
			elif 23 <= score <= 26:
				combattantTunnels()
			elif 27 <= score <= 29:
				contrebandier()
			elif 30 <= score <= 31:
				etudiant()
			elif 32 <= score <= 35:
				gardeCorps()
			elif 36 <= score <= 37:
				garde()
			elif 38 <= score <= 41:
				geolier()
			elif 42 <= score <= 46:
				gladiateur()
			elif 47 <= score <= 49:
				horsLaLoi()
			elif score == 50:
				marin()
			elif score == 51:
				matelot()
			elif 52 <= score <= 57:
				mercenaire()
			elif 58 <= score <= 61:
				milicien()
			elif 62 <= score <= 67:
				mineur()
			elif 68 <= score <= 69:
				noble()
			elif 70 <= score <= 72:
				pilleurTombes()
			elif 73 <= score <= 77:
				porterune()
			elif 78 <= score <= 81:
				ratier()
			elif 82 <= score <= 83:
				scribe()
			elif 84 <= score <= 85:
				serviteur()
			elif 86 <= score <= 89:
				soldat()
			elif 90 <= score <= 93:
				spadassin()
			elif 94 <= score <= 97:
				tueurTrolls()
			elif 98 <= score <= 100:
				voleur()

		elif race =="9":
			if 1 <= score <= 8:
				artisan()
			elif 9 <= score <= 15:
				bourgeois()
			elif 16 <= score <= 21:
				combattantTunnels()
			elif 22 <= score <= 27:
				esclavagiste()
			elif 28 <= score <= 33:
				gardeCorps()
			elif 34 <= score <= 38:
				geolier()
			elif 39 <= score <= 44:
				gladiateur()
			elif 45 <= score <= 49:
				hierogrammate()
			elif 50 <= score <= 56:
				ingenieurChaos()
			elif 57 <= score <= 76:
				maraudeur()
			elif 77 <= score <= 88:
				mercenaire()
			elif 89 <= score <= 94:
				mineur()
			elif 95 <= score <= 100:
				soldat()

		elif race == "10":
			if 1 <= score <= 10:
				artisan()
			elif score == 11:
				bateleur()
			elif 12 <= score <= 21:
				berserkNorse()
			elif 22 <= score <= 25:
				bourgeois()
			elif 26 <= score <= 28:
				chasseur()
			elif 29 <= score <= 33:
				combattantTunnels()
			elif 34 <= score <= 38:
				gardeCorps()
			elif 39 <= score <= 40:
				gladiateur()
			elif 41 <= score <= 45:
				hommeLige()
			elif score == 46:
				horsLaLoi()
			elif score == 47:
				marin()
			elif 48 <= score <= 59:
				mercenaire()
			elif 60 <= score <= 64:
				milicien()
			elif 35 <= score <= 74:
				mineur()
			elif score == 75:
				pillard()
			elif 76 <= score <= 79:
				scalde()
			elif score == 80:
				serviteur()
			elif 81 <= score <= 90:
				soldat()
			elif 91 <= score <= 100:
				tueurTrolls()

		elif race == "11":
			if 1 <= score <= 3:
				agitateur()
			elif 4 <= score <= 8:
				artisan()
			elif 9 <= score <= 11:
				bateleur()
			elif 12 <= score <= 13:
				bourgeois()
			elif 14 <= score <= 16:
				charbonnier()
			elif 17 <= score <= 18:
				chasseurPrimes()
			elif 19 <= score <= 23:
				chasseur()
			elif score == 24:
				chiffonnier()
			elif score == 25:
				chirurgienBarbier()
			elif 26 <= score <= 27:
				collecteurTaxes()
			elif 28 <= score <= 30:
				contrebandier()
			elif 31 <= score <= 35:
				escroc()
			elif 36 <= score <= 37:
				etudiant()
			elif 38 <= score <= 41:
				garde()
			elif 42 <= score <= 44:
				horsLaLoi()
			elif 45 <= score <= 46:
				mercanti()
			elif 47 <= score <= 50:
				mercenaire()
			elif 51 <= score <= 55:
				messager()
			elif 56 <= score <= 60:
				milicien()
			elif score == 61:
				passeur()
			elif 62 <= score <= 67:
				paysan()
			elif score == 68:
				pecheur()
			elif 69 <= score <= 73:
				pilleurTombes()
			elif score == 74:
				ratier()
			elif 75 <= score <= 78:
				sentinelleHalfling()
			elif 79 <= score <= 83:
				serviteur()
			elif 84 <= score <= 85:
				soldat()
			elif 86 <= score <= 88:
				trafiquantCadavres()
			elif 89 <= score <= 92:
				vagabond()
			elif 93 <= score <= 94:
				valet()
			elif 95 <= score <= 100:
				voleur()

		elif race == "12":
			if 1 <= score <= 7:
				apprentiSorcier()
			elif 8 <= score <= 14:
				artisan()
			elif 15 <= score <= 19:
				bateleur()
			elif 20 <= score <= 27:
				chasseur()
			elif 28 <= score <= 33:
				eclaireur()
			elif 34 <= score <= 40:
				emissaireElfe()
			elif 41 <= score <= 46:
				escroc()
			elif 47 <= score <= 51:
				etudiant()
			elif 52 <= score <= 58:
				gardienTribal()
			elif 59 <= score <= 64:
				horsLaLoi()
			elif 65 <= score <= 70:
				marin()
			elif 71 <= score <= 75:
				mercenaire()
			elif 76 <= score <= 81:
				messager()
			elif 82 <= score <= 87:
				scribe()
			elif 88 <= score <= 94:
				vagabond()
			elif 95 <= score <= 100:
				voleur()



	# on teste la présence de chaque talent dans la liste de talent du joueur 
	# et on impacte si nécessaire les bonus au profil principal 
	def impactTalentProfilPpal():
		global profilPpal
		# force accrue
		if listeTalents[27] in talentsJoueur:
			profilPpal["F"] += 5
		# guerrier né
		if listeTalents[32] in talentsJoueur:
			profilPpal["CC"] += 5
		# intelligent
		if listeTalents[37] in talentsJoueur:
			profilPpal["Int"] += 5
		# réflexe eclair
		if listeTalents[67] in talentsJoueur:
			profilPpal["Ag"] += 5
		# résistance accrue
		if listeTalents[68] in talentsJoueur:
			profilPpal["E"] += 5
		# sang-froid
		if listeTalents[75] in talentsJoueur:
			profilPpal["FM"] += 5
		# sociable
		if listeTalents[82] in talentsJoueur:
			profilPpal["Soc"] += 5
		# tirreur d'élite
		if listeTalents[89] in talentsJoueur:
			profilPpal["CT"] += 5

	def impactTalentProfilSecondR():
		# course à pied
		global profilSecondR
		if listeTalents[20] in talentsJoueur:
			profilSecondR["M"] += 1
		# dur à cuir
		if listeTalents[22] in talentsJoueur:
			profilSecondR["B"] += 1

	defineCompetenceTalentRace()

	defineCompetenceTalentCarriere(scoreD100)

	def printProfil():
		print()
		print("Votre carrière est : {}.".format(carriereJoueur)) 
		print()
		print("PROFIL PRINCIPAL :")
		print("CC : {} | CT : {} | F : {}  | E : {}  | Ag : {} | Int : {} | FM : {} | Soc : {}".format(profilPpal["CC"],profilPpal["CT"],profilPpal["F"],profilPpal["E"],profilPpal["Ag"],profilPpal["Int"],profilPpal["FM"],profilPpal["Soc"]))
		print()
		print("PROFIL SECONDAIRE :")
		print("A : {}   | B : {}  | BF : {}  | BE : {}  | M : {}   | Mag : {}  | PF : {}  | PD : {}".format(profilSecondR["A"],profilSecondR["B"],profilSecondR["BF"],profilSecondR["BE"],profilSecondR["M"],profilSecondR["Mag"],profilSecondR["PF"],profilSecondR["PD"]))

	if race == "1" or race == "2" or race == "3" or race == "4" or race == "5" or race == "7":	
		#humain2["A"] pas de modif pour le moment
		print()
		if race == "1" or race == "2" or race == "3" or race == "4" or race == "5":
			print("Vous êtes un HUMAIN.")
		elif race == "7":
			print("Vous êtes un HUMAIN NORSE.")
			tmp2 = random.randint(1,5)
			if tmp2 == 1:
				defineMutation()
		impactTalentProfilPpal()
		pv = random.randint(1, 10)
		if 1 <= pv <= 3:
			profilSecondR["B"] += 10
		elif 4 <= pv <= 6:
			profilSecondR["B"] += 11
		elif 7 <= pv <= 9:
			profilSecondR["B"] += 12
		elif pv == 10:
			profilSecondR["B"] += 13		
		profilSecondR["BF"] = (profilPpal["F"]//10) 
		profilSecondR["BE"] = (profilPpal["E"]//10)
		profilSecondR["M"] = 4
		# profilSecondR["M"] pas de modif pour le moment
		# profilSecondR["PF"] pas de modif pour le moment
		profilSecondR["PD"] = random.randint(1, 10)
		if 1 <= profilSecondR["PD"] <= 4:
			profilSecondR["PD"] = 2
		elif 5 <= profilSecondR["PD"] <= 10:
			profilSecondR["PD"] = 3
		impactTalentProfilSecondR()
		printProfil()

	elif race == "6" :
		#profilSecondR["A"] pas de modif pour le moment
		print()
		print("Vous êtes un HUMAIN KURGAN.")
		tmp2 = random.randint(1,4)
		if tmp2 == 1:
			defineMutation()
		impactTalentProfilPpal()
		pv = random.randint(1, 10)
		if 1 <= pv <= 3:
			profilSecondR["B"] += 11
		elif 4 <= pv <= 6:
			profilSecondR["B"] += 12
		elif 7 <= pv <= 9:
			profilSecondR["B"] += 13
		elif pv == 10:
			profilSecondR["B"] += 14		
		profilSecondR["BF"] = (profilPpal["F"]//10) 
		profilSecondR["BE"] = (profilPpal["E"]//10)
		profilSecondR["M"] += 4
		# profilSecondR["PF"] pas de modif pour le moment
		profilSecondR["PD"] = random.randint(1, 10)
		if 1 <= profilSecondR["PD"] <= 7:
			profilSecondR["PD"] = 0
		elif 8 <= profilSecondR["PD"] <=10:
			profilSecondR["PD"] = 1
		impactTalentProfilSecondR()
		printProfil()

	elif race == "8" or race == "9" or race == "10":
		#profilSecondR["A"] pas de modif pour le moment
		print()
		if race == "8":
			print("Vous êtes un NAIN.")
		if race == "9":
			print("Vous êtes un NAIN DU CHAOS.")
			tmp2 = random.randint(1,4)
			if tmp2 == 1:
				defineMutation()
		elif race == "10":
			print("Vous êtes un NAIN NORSE.")
			tmp2 = random.randint(1,5)
			if tmp2 == 1:
				defineMutation()
		impactTalentProfilPpal()
		pv = random.randint(1, 10)
		if 1 <= pv <= 3:
			profilSecondR["B"] += 11
		elif 4 <= pv <= 6:
			profilSecondR["B"] += 12
		elif 7 <= pv <= 9:
			profilSecondR["B"] += 13
		elif pv == 10:
			profilSecondR["B"] += 14		
		profilSecondR["BF"] = (profilPpal["F"]//10) 
		profilSecondR["BE"] = (profilPpal["E"]//10)
		profilSecondR["M"] += 3
		# profilSecondR["PF"] pas de modif pour le moment
		profilSecondR["PD"] = random.randint(1, 10)
		if 1 <= profilSecondR["PD"] <= 4:
			profilSecondR["PD"] = 1
		elif 5 <= profilSecondR["PD"] <=7:
			profilSecondR["PD"] = 2
		elif 8 <= profilSecondR["PD"] <=10:
			profilSecondR["PD"] = 3
		impactTalentProfilSecondR()
		print()
		printProfil()

	elif race == "11" :
		#profilSecondR["A"] pas de modif pour le moment
		print()
		print("Vous êtes un HALFLING.")
		impactTalentProfilPpal()
		pv = random.randint(1, 10)
		if 1 <= pv <= 3:
			profilSecondR["B"] = 8
		elif 4 <= pv <= 6:
			profilSecondR["B"] = 9
		elif 7 <= pv <= 9:
			profilSecondR["B"] = 10
		elif pv == 10:
			profilSecondR["B"] = 11		
		profilSecondR["BF"] = (profilPpal["F"]//10) 
		profilSecondR["BE"] = (profilPpal["E"]//10)
		profilSecondR["M"] += 4
		# profilSecondR["PF"] pas de modif pour le moment
		profilSecondR["PD"] = random.randint(1, 10)
		if 1 <= profilSecondR["PD"] <= 7:
			profilSecondR["PD"] = 2
		elif 8 <= profilSecondR["PD"] <=10:
			profilSecondR["PD"] = 3
		impactTalentProfilSecondR()
		print()
		print("Vous êtes un HALFLING.")
		printProfil()

	elif race == "12" :
		#profilSecondR["A"] pas de modif pour le moment
		print()
		print("Vous êtes un ELF.")
		impactTalentProfilPpal()
		pv = random.randint(1, 10)
		if 1 <= pv <= 3:
			profilSecondR["B"] = 9
		elif 4 <= pv <= 6:
			profilSecondR["B"] = 10
		elif 7 <= pv <= 9:
			profilSecondR["B"] = 11
		elif pv == 10:
			profilSecondR["B"] = 12		
		profilSecondR["BF"] = (profilPpal["F"]//10) 
		profilSecondR["BE"] = (profilPpal["E"]//10)
		profilSecondR["M"] += 5
		# profilSecondR["PF"] pas de modif pour le moment
		profilSecondR["PD"] = random.randint(1, 10)
		if 1 <= profilSecondR["PD"] <= 4:
			profilSecondR["PD"] = 1
		elif 5 <= profilSecondR["PD"] <=10:
			profilSecondR["PD"] = 2
		impactTalentProfilSecondR()
		printProfil()

	print()

	# chance	
	if listeTalents[10] in talentsJoueur:
		print("Points de fortune : {}.".format((profilSecondR["PD"]+1)))
		print()
	else:
		print("Points de fortune : {}.".format(profilSecondR["PD"]))
		print() 

	print("Vos compétences sont : ") 
	for competence in competencesJoueur:
		if competencesJoueur.count(competence) == 1:
			if "(F)" in competence:
				print("                      ", profilPpal["F"], " | ", competence)
			elif "(E)" in competence:
				print("                      ", profilPpal["E"], " | ", competence)
			elif "(Ag)" in competence:
				print("                      ", profilPpal["Ag"], " | ", competence)
			elif "(Int)" in competence:
				print("                      ", profilPpal["Int"], " | ", competence)
			elif "(FM)" in competence:
				print("                      ", profilPpal["FM"], " | ", competence)
			elif "(Soc)" in competence:
				print("                      ", profilPpal["Soc"], " | ", competence)
		elif competencesJoueur.count(competence) == 2:
			if "(F)" in competence:
				print("                      ", profilPpal["F"] + 10, " | ", competence)
			elif "(E)" in competence:
				print("                      ", profilPpal["E"] +10, " | ", competence)
			elif "(Ag)" in competence:
				print("                      ", profilPpal["Ag"] +10, " | ", competence)
			elif "(Int)" in competence:
				print("                      ", profilPpal["Int"] +10, " | ", competence)
			elif "(FM)" in competence:
				print("                      ", profilPpal["FM"] +10, " | ", competence)
			elif "(Soc)" in competence:
				print("                      ", profilPpal["Soc"] +10, " | ", competence)
		

	print("Vos talents sont : ") 
	for talent in talentsJoueur:
		print("                  ", talent)
	print()

	if dotations != []:
		print("Petit chateux de tes morts, tu as des dotations : ") 
		for item in dotations:
			print("                                                ", item)
	
	print()
	print()

	print("Voulez-vous créer un autre personnage ? Tapez 'o' pour oui, ou 'n' pour non." )
	reponse = input(">:")

	while reponse != "o" and reponse != "n":
		print("Merci de taper 'o' pour oui, ou 'n' pour non.")
		reponse = input(">:")