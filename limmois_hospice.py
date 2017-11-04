#!/usr/bin/python3
# *- coding: utf-8 -*-

'''
nom: andy limmois, johann hospice
command: py limmois_hospice.py <n> <k> <l> <d>
'''

import argparse

'''
Outils
'''
def buildParser():
	parser = argparse.ArgumentParser(
		description='Generate a deck of dobble card game')
	parser.add_argument(
		'n', 
		type=int,
 		help='nombre de symboles')
	parser.add_argument(
		'k', 
		type=int,
 		help='nombre de symboles par carte')
	parser.add_argument(
		'l', 
		type=int,
 		help='nombre d\'apparition maximum pour chaque symboles')
	parser.add_argument(
		'd', 
		type=int,
 		help='nombre de symboles partagés par deux cartes quelconques')
	return parser

def syntax(b=0, d=0, s=""):
	'''
	retourne une chaine de caracteres ayant le format de sortie demandé dans le sujet
	'''
	return '\n'.join(str(x) for x in [b, d, s])

def longest(L):
	'''
	retourne le plus grand element quelconque d'un ensemble L
	L: list contenant des elements ayant une certaine taille
	'''
	lmax = -1
	amax = None
	for e in L:
		if len(e) > lmax:
			amax = e
			lmax = len(e)
	return amax

def binStrToArr(S):
	return [[int(a) for a in x] for x in S.split(' ')]

def binArrToStr(A):
	return ' '.join([''.join([str(b) for b in c]) for c in A])

def	intToBin(x, n):
	'''
	retourne la convertion d'un entier x en list d'entier binaire de taille n
	x: entier (valeur decimal)
	n: entier (taille du mot binaire)
	'''
	if x >= pow(2, n):
		raise Exception()
	c = ["0"] * n
	for j in reversed(range(0, n)):
		nx = x - pow(2, j)
		if nx >= 0:
			x = nx
			c[j] = "1"
	return ''.join(c)

def issubsubset(a, E):
	'''
	retourne si un element a est inclus dans un sous ensemble de E
	E: ensemble
	a: ensemble
	'''
	for e in E:
		if a <= e:
			return True
	return False

'''
Deck
'''
class Deck:
	def __init__(self, n, k, l, d):
		'''
		n symboles (alphabet)
		k symboles par carte (longueur des mot)
		chaque symbole apparaissant au plus l fois
		deux cartes quelconques partagent exactement d symboles
		'''
		self.n = n
		self.k = k
		self.l = l
		self.d = d

	def possibilities(self):
		'''
		retourne un ensemble de cartes ayant k symboles par cartes parmis n symboles
		'''
		D = []
		for i in range(pow(2, self.n)):
			c = intToBin(i, self.n)
			if self.checkK(c): 
				D += [c]
		return D

	def checkK(self, C):
		'''
		retourne si une carte contient bien k symboles
		C: chaine de caractere (carte)

		'''
		ksum = 0
		for s in C:
			if s == "1":
				ksum += 1
		if ksum == self.k:
			return True
		return False

	def checkL(self, P):
		'''
		retourne si les symboles n'apparaissent pas trop de fois dans un paquet (en fonction de l)
		P: ensemble de chaine de caractere (paquet de cartes)
		'''
		for i in range(self.n):
			lsum = 0
			for c in P:
				if c[i] == "1":
					lsum += 1
			if lsum > self.l:
				return False
		return True

	def checkD(self, P):
		'''
		retourne si toutes pairs de cartes respecte le nombre de symboles en commun (en fonction de d)
		P: ensemble de chaine de caractere (paquet de cartes)
		'''
		for c1 in P:
			for c2 in P:
				if c1 != c2: # pour deux cartes differentes du paquet
					dsum = 0
					for i in range(self.n):
						if c1[i] == "1" and c1[i] == c2[i]: # si meme symbole est present
							dsum += 1
					if dsum != self.d:
						return False
		return True
	
	def solutions(self):
		'''
		retourne toutes les descriptions de solutions distinctes
		'''
		def aux(SP, P=set()):
			'''
			fonction auxiliaire permettant d'utiliser S,
			une variable en dehors de l'environnement de recursion
			permettant d'y ajouter simplement des elements
			SP: liste d'ensemble de chaine de caractere (liste des possibilités)
			P: ensemble de chaine de caractere (le paquet traité)
			'''
			if not self.checkL(P) or not self.checkD(P):
				return None
			
			elif len(SP) == 0:
				return P

			else:
				s1 = aux(SP[1::], P | {SP[0]}) # appel recursif avec solution retirée
				s2 = aux(SP[1::], P) # appel recursif sans solution retirée

				if s1 and not issubsubset(s1, S):
					S.append(s1)
				if s2 and not issubsubset(s2, S):
					S.append(s2)
				return None

		SP = self.possibilities()
		S = [] # liste contenant toutes les solutions
		aux(SP)
		return S

'''
Main
'''
if __name__ == '__main__':

	args = buildParser().parse_args()

	deck = Deck(args.n, args.k, args.l, args.d)
	
	solutions = deck.solutions()

	longest = longest(solutions)
	
	if longest:
		output = syntax(len(longest), len(solutions), binArrToStr(longest))
	else:
		output = syntax()

	'''
	display
	'''

	#print("# toutes solutions: \n#\t" + '\n#\t'.join([binArrToStr(s) for s in solutions]))
	
	print(output)