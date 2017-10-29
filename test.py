import subprocess
import re

RE_OUTPUT = re.compile("^(-?\d*)\r\n(-?\d*)\r\n((\d*[ ]{0,1})*)$")

TESTS = [
	((5, 2, 4, 1), (4, None, '00011 00110 01010 10010')), 
	((4, 3, 3, 2), (4, 1, '0111 1011 1101 1110')), 
	((7, 4, 4, 2), (7, 30, '0001111 0110011 1010101 1101001 1100110 1011010 0111100'))]

print("-- test all")

for (i, t) in enumerate(TESTS):
	testInput = t[0]
	testOutput = t[1]
	testCmd = ["limmois_hospice.py"] + [str(x) for x in testInput]

	proc = subprocess.Popen(testCmd, stdout=subprocess.PIPE, shell=True)
	resultOutput = proc.communicate()[0].decode('utf-8')
	match = RE_OUTPUT.search(resultOutput)
	resultMatch = '\r\n\t'.join([str(j) + ": " + str(e == match.group(j + 1)) for (j, e) in enumerate(testOutput)]) if match else "\tsyntax error"

	print("- test " + str(i))
	print("test input: \n\t" + str(testInput))

	print("test output: \n\t" + str(testOutput))

	print("result output raw: \n\t" + repr(resultOutput))
	print("result output pretty: \n\t$" + '\n\t$'.join(resultOutput.split('\n')))

	print("result match: \n\t" + resultMatch)
