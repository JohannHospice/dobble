#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
nom: andy limmois, johann hospice
command: py limmois_hospice.py <n> <k> <l> <d>
description:
	la taille du plus gros jeu de cartes possible utilisant n symboles, 
	avec k symboles par carte, chaque symbole apparaissant au plus l fois, 
	et tel que deux cartes quelconques partagent exactement d symboles.
variables:
	n symboles (alphabet)
	k symboles par carte (longueur des mot)
	chaque symbole apparaissant au plus l fois
	deux cartes quelconques partagent exactement d symboles
'''

import argparse

def bigestSize(n, k, l, d):
	'''
	la taille maximale d’un tel jeu de cartes

	PIST: n ^ k taille maximale du jeu de cartes sans contraintes(l && d)
	'''
	return binomial(n, k)

def distinctSolutions(n, k, l, d):
	'''
	le nombre de solutions distinctes

	NEED:
		d taille maximale du jeu de cartes (deck)
		h taille d'une main de carte (hand)
	'''
	return -1

def solution(n, k, l, d, e=[]):
	'''
	la description d’une solution, sous la forme d’une suite de mots sur l’alphabet {0,1}, séparés par des espaces
	'''
	print(e)

	# verifie nombre d'apparition de symboles 
	for i in range(n):
		lsum = 0
		for c in e:
			if c[i] == 1:
				lsum += 1
		if lsum > l:
			return None
	#pour une paire de cartes
	for c1 in e:
		for c2 in e: 
			if c1 != c2:
				dsum = 0
				for i in range(n):
					if c1[i] == 1 and c1[i] == c2[i]:
						dsum += 1
				if dsum != d: return None
	# si toutes condition respectés et longueur atteinte, retourner solution
	if len(e) == n:
		return e
	# creation d'une carte
	for i in range(pow(2, n)):
		c = intToBin(i, n)
		if c not in e:
			# verifie le nombre de symbole dans c est egal a k
			ksum = sum(c)
			if ksum == k:
				s = solution(n, k, l, d, e + [c])
				if s != None:
					return s

	return None

def format(b, d, s):
	'''
	retourne une string ayant le format de sortie demandé dans le sujet

	d un tableau d'argument
	'''
	# si None alors chaine vide sinon normal
	# \n entre chaque case du tableau
	if s != None:
		s = ' '.join([''.join([str(b) for b in c]) for c in s])
	return '\n'.join(str(x) if x else "" for x in [b, d, s])
		
def	intToBin(x, n):
	if x >= pow(2, n):
		raise Exception()
	c = [0] * n
	for j in reversed(range(0, n)):
		nx = x - pow(2, j)
		if nx >= 0:
			x = nx
			c[j] = 1
	return c

def binomial(n, k):
    '''
    A fast way to calculate binomial coefficients by Andrew Dalke.
    See http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
    '''
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

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

if __name__ == '__main__':

	args = buildParser().parse_args()

	bigestSize = bigestSize(args.n, args.k, args.l, args.d)
	
	distinctSolutions = distinctSolutions(args.n, args.k, args.l, args.d)
	
	solution = solution(args.n, args.k, args.l, args.d)
	
	output = format(bigestSize, distinctSolutions, solution)
	
	print(output) # pas de nouvelle ligne à la fin
