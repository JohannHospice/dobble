'''
nom: andy limmois, johann hospice
command: py limmois_hospice.py <n> <k> <l> <d>
'''

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse

class Deck:
	'''
	la taille du plus gros jeu de cartes possible utilisant n symboles, 
	avec k symboles par carte, chaque symbole apparaissant au plus l fois, 
	et tel que deux cartes quelconques partagent exactement d symboles.
	'''

	def __init__(self, n, k, l, d):
		'''
		n symboles
		k symboles par carte
		chaque symbole apparaissant au plus l fois
		deux cartes quelconques partagent exactement d symboles
		'''
		self.n = n
		self.k = k
		self.l = l
		self.d = d

		# taille maximum
		self.maxSize = -1

		# nombre de solutions
		self.nbSol = -1

	def bigestSize(self):
		'''
		la taille maximale d’un tel jeu de cartes

		PIST: n * k taille maximale du jeu de cartes sans contraintes(l && d)
		'''
		pass

	def distinctSolutions(self):
		'''
		le nombre de solutions distinctes

		NEED:
			d taille maximale du jeu de cartes (deck)
			h taille d'une main de carte (hand)
		'''
		pass

	def solution(self):
		'''
		la description d’une solution, sous la forme d’une suite de mots sur l’alphabet {0,1}, séparés par des espaces

		d taille maximale du jeu de cartes (deck)

		TODO: backtracking algorithm
		'''
		return None

	def format(self):
		'''
		retourne une string ayant le format de sortie demandé dans le sujet

		d un tableau d'argument
		'''
		# si None alors chaine vide sinon normal
		# \n entre chaque case du tableau
		return '\n'.join(str(x) if x else "" for x in [self.maxSize, self.nbSol, self.solution()])
		
def binomial(n, k):
    '''
    A fast way to calculate binomial coefficients by Andrew Dalke.
    See http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
    '''
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
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

	dobble = Deck(args.n, args.k, args.l, args.d)
	
	output = dobble.format()
	
	print(output, end='') # pas de nouvelle ligne à la fin
