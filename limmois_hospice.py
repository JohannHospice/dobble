#!/usr/bin/python3
# *- coding: utf-8 -*-

'''
nom: andy limmois, johann hospice
command: py limmois_hospice.py <n> <k> <l> <d>
description:
	la taille du plus gros jeu de cartes possible utilisant n symboles, 
	avec k symboles par carte, chaque symbole apparaissant au plus l fois, 
	et tel que deux cartes quelconques partagent exactement d symboles.
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
	retourne une string ayant le format de sortie demandé dans le sujet

	b: taille maximal
	d: nombre de solutions distinctes
	s: une solution
	'''
	return '\n'.join(str(x) for x in [b, d, s])

def longest(A):
	'''
	retourne le plus grand sous ensemble d'un ensemble A
	
	O(A)
	'''
	lmax = -1
	amax = None
	for a in A:
		if len(a) > lmax:
			amax = a
			lmax = len(a)
	return amax

def binStrToArr(m):
	return [[int(a) for a in x] for x in m.split(' ')]

def binArrToStr(m):
	return ' '.join([''.join([str(b) for b in c]) for c in m])

def	intToBin(x, n):
	'''
	convertit un entier x en list d'entier binaire de taille n

	O(N^2) // reverse * range
	'''
	if x >= pow(2, n):
		raise Exception()
	c = [0] * n
	for j in reversed(range(0, n)):
		nx = x - pow(2, j)
		if nx >= 0:
			x = nx
			c[j] = 1
	return c

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

	def prepare(self):
		'''
		un ensemble de cartes ayant k symboles par cartes parmis n symboles

		O(2^N) * intoBin
		'''
		D = []
		for i in range(pow(2, self.n)):
			c = intToBin(i, self.n)
			ksum = sum(c)
			if ksum == self.k:
				D += [c]
		return D

	def checkL(self, D):
		'''
		verifie que les symboles n'apparaissent pas trop de fois (en fonction de l) 
		
		O(D * N)
		'''
		for i in range(self.n):
			lsum = 0
			for c in D:
				if c[i] == 1:
					lsum += 1
			if lsum > self.l:
				return False
		return True

	def checkD(self, D):
		'''
		vérifie que toutes pairs de cartes respecte le nombre de symboles en commun (en fonction de d)

		O(D^2 * N)
		'''
		if len(D) < 2:
			return False # puisquil n'y a pas de pairs
		for c1 in D:
			for c2 in D: 
				if c1 != c2:
					dsum = 0
					for i in range(self.n):
						if c1[i] == 1 and c1[i] == c2[i]:
							dsum += 1
					if dsum != self.d:
						return False
		return True

	def solutions(self, D):
		'''
		WARN: inefficace, fait de multiple fois des memes calcules sur de memes ensemble. revoir arbre backtracking

		toutes les description des solutions distinctes de D
		D: un ensemble de de liste d'entier binaire

		O(?)
		'''

		if len(D) < self.n:
			return []
		
		# print(binArrToStr(D))
		
		S = []

		if self.checkL(D) and self.checkD(D):
			S += [D]

		# enlever une carte
		for c in D:
			nS = self.solutions([x for x in D if x != c])
			S += [x for x in nS if x not in S]

		return S

'''
Main
'''
if __name__ == '__main__':

	args = buildParser().parse_args()

	deck = Deck(args.n, args.k, args.l, args.d)
	
	p = deck.prepare()

	print("# paquet préparé: " + binArrToStr(p))

	solutions = deck.solutions(p)

	print("# toutes solutions: \n#\t" + '\n#\t '.join([binArrToStr(s) for s in solutions])) # pas de nouvelle ligne à la fin

	longest = longest(solutions)

	if longest != None:
		output = syntax(len(longest), len(solutions), binArrToStr(longest))
	else:
		output = syntax(d=len(solutions))
	
	print(output)