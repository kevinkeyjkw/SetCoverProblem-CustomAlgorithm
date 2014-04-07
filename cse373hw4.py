import sys


def isSolution(a):
	guessArray = [subsets[i] for i in range(len(a)) if a[i]]
	print(guessArray)
	isSol = False
	for e in numsToCover:
		isSol = False
		for element in guessArray:
			if e in element:
				isSol = True
				break
		if(not isSol):
			return False
	return True
def processSolution(guessArray):
	if len(guessArray) < len(minSolution):
		minSolution = guessArray
#print(len(guessArray))
#def candidates():	
def minCover(a,k,data):
	candidates
	
	

minSolution = []		
f = open(sys.argv[1],'r')
content = []
numsToCover = []
subsets = []
finished = False

for line in f:
	content.append(line.strip('\n'))
numOfSubsets = int(content[1])
for x in range(1,int(content[0])+1):
	numsToCover.append(x)
content = content[2:]
for element in content:
	temp = [int(x) for x in element.split(' ')]
	subsets.append(temp)
minSolution = subsets
print(isSolution([1,0,0,0,1,0]))
#print(subsets)
#if(isSolution([1,2,3,4,5,6],[[1,2,3],[4,5,6]])):
#	processSolution([[1,2,3],[4,5,6]])
#Example of variables/
#subsets = [[1,2,3],[2,3],[3,4,5]]
#numOfSubsets = 12
#numsToCover = [1,2,3,4,5]
#finished = true




		
