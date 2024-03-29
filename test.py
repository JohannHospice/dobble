#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import re

RE_OUTPUT = re.compile("^(-?\d*)\r?\n(-?\d*)\r?\n((\d*[ ]{0,1})*)$(\r?\n)?")

TESTS = [
	((5, 2, 4, 1), (4, None, '00011 00110 01010 10010')), 
	((4, 3, 3, 2), (4, 1, '0111 1011 1101 1110')), 
	((7, 4, 4, 2), (7, 30, '0001111 0110011 1010101 1101001 1100110 1011010 0111100'))]

print("-- test all")

def binStrToArr(m):
	return [[int(a) for a in x] for x in m.split(' ')]

for (i, t) in enumerate(TESTS):
	testCmd = ["./limmois_hospice.py " + " ".join([str(x) for x in t[0]])] 
	proc = subprocess.Popen(testCmd, stdout=subprocess.PIPE, shell=True)
	resultOutput = proc.communicate()[0].decode('utf-8')
	match = RE_OUTPUT.search(resultOutput)
	resultMatch = '\r\n\t'.join([str(j) + ": " + str(e == match.group(j + 1)) for (j, e) in enumerate(t[1])]) if match else "\tsyntax error"

	s = binStrToArr(t[1][2])
	g = binStrToArr(match.group(3))
	
	ok = True
	for b in g:
		if ok:
			ok = b in s
	print("- test " + str(i))
	print("test input: \n\t" + str(t[0]))

	print("test output: \n\t" + str(t[1]))

	print("result output raw: \n\t" + repr(resultOutput))
	print("result output pretty: \n\t$" + '\n\t$'.join(resultOutput.split('\n')))

	print("result match: \n\t" + resultMatch)
	print("verify solution whithout order: " + str(ok))