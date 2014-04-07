import sys

def isSolution(numsToCoverArray,guessArray):
	isSol = False
	for e in numsToCoverArray:
		isSol = False
		for element in guessArray:
			if e in element:
				isSol = True
				break
		if(not isSol):
			return False
	return True
			
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
#print(subsets)
print(isSolution([1,2,3,4,5,6],[[1,2],[4,5,6]]))
#Example of variables/
#subsets = [[1,2,3],[2,3],[3,4,5]]
#numOfSubsets = 12
#numsToCover = [1,2,3,4,5]
#finished = true

#def minCover(set):
	
#def candidates():


		
