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

def computeIndexMustHaveSets(data,range):
	minOcc = 999
	minNum = range[0]
	mustHaveSets = []
	mustHaveIndex = []
	for i in range:
		occ = 0
		sets = []
		for k in data:
			if i in k:
				occ = occ + 1
				sets.append(k)
		if occ < minOcc:
			minNum = i
			minOcc = occ
			mustHaveSets = sets
	for i in mustHaveSets:
		mustHaveIndex.append(data.index(i))
	return mustHaveIndex

def solutionContainsMustHaveSets(a):
	for i in mustHaveIndex:
		if a[i] == True:
			return True
	return False
def combo(a,k):
	if k == len(a):
		if isSolution(a):
			processSolution(a)
	else:
		if k == mustHaveIndex[len(mustHaveIndex)-1] and not solutionContainsMustHaveSets(a):
			a[k] = 1 
			combo(a,k+1)
		else:
			a[k] = 0
			combo(a,k+1)
			a[k] = 1
			combo(a,k+1)
	
def pruneExcessiveSets(a):
	pdb.set_trace()
	toRemove=[]
	for i in range(len(a)):
		for j in range(len(a)):
			if a[i] <= a[j] and i != j:
				toRemove.append(a[i])
				break
	for i in toRemove:
		a.remove(i)

def pruneExcessiveSets2(a):
	x = len(a)
	count = 0
	while count < x:
		for j in range(len(a)):
			if a[count] <= a[j] and count != j:
				a.remove(a[count])		
				x -= 1
				count -= 1
				break
		count += 1
	
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
	if element == '':
		temp = []
	else:
		if element[len(element)-1] == ' ':
			element = element[:len(element)-1]
		if(' ' in element):
			temp = [int(x) for x in element.split(' ')]
		else:
			temp = [int(element)]
	subsets.append(set(temp))
minSolution = subsets

print('original subsets =',subsets)
pruneExcessiveSets2(subsets)
a = [0 for i in range(len(subsets))]
print('new subsets =',subsets)
mustHaveIndex = computeIndexMustHaveSets(subsets,numsToCover)

combo(a,0)
print('Minimum cover set =',minSolution)
#Example of variables/
#subsets = [[1,2,3],[2,3],[3,4,5]]
#numOfSubsets = 12
#numsToCover = [1,2,3,4,5]
#finished = true




		
