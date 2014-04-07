import sys
import pdb

def isSolution(a):
	guessArray = [subsets[i] for i in range(len(a)) if a[i]]
	#print(guessArray)
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

def printSolution(a):
	guessArray = [subsets[i] for i in range(len(a)) if a[i]]
	print(guessArray)
# 
# We put a=[T,T,T...,T] -> a=[F,F,F,...] means no more moves left
# def backtrack(a,k,n):
# 	c = [0,0]
# 	ncandidates=2
# 	if(is_a_solution(a,k,n)):
# 		process_solution(a,k)
# 	else:
# 		k += 1
# 		if k < n:
# 			construct_candidates(a,c)
# 			for i in range(2):
# 				a[k] = c[i]
# 				backtrack(a,k,n)


def combo(a,k):
	if k == len(a):
		if isSolution(a):
			processSolution(a)
	else:
		a[k] = 0
		combo(a,k+1)
		a[k] = 1
		combo(a,k+1)
		
	
def processSolution(a):
	global minSolution
	guessArray = [subsets[i] for i in range(len(a)) if a[i]]
	if len(guessArray) < len(minSolution):
		minSolution = guessArray


			
# 	c = [True,False]
# 	if(k > len(subsets)):
# 		return
# 	else:
# 		if(isSolution(a)):
# 			processSolution(a)
# 		k = k + 1
# 		if k > len(a):
# 			return
# 		a[k] = c[0]
# 		minCover(a,k)
# 		a[k] = c[1]
# 		minCover(a,k)
# 		return
				
# 			
# def test(a):
# 	c = [0,0]
# 	test2(c)
# 	print(c)
# def test2(b):
# 	b[0] = True
# 	b[1] = False
	
	

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
	if element[len(element)-1] == ' ':
		element = element[:len(element)-1]
	if(' ' in element):
		temp = [int(x) for x in element.split(' ')]
	else:
		temp = [int(element)]
	subsets.append(temp)
minSolution = subsets
a = [0 for i in range(len(subsets))]

combo(a,0)
print(minSolution)
#Example of variables/
#subsets = [[1,2,3],[2,3],[3,4,5]]
#numOfSubsets = 12
#numsToCover = [1,2,3,4,5]
#finished = true




		
