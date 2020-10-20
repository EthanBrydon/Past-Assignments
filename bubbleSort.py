def bubbleSort(lis):
	'''this function sorts a given input list IN-PLACE in ascending order 
	using the Bubble sort algorithm, and returns nothing'''
	#for n passes:
	for _ in range(len(lis)):
		#for each pair of items:
		for j in range(1,len(lis)):  #n-1 pairs
			#if two elements are out of order
			if lis[j-1] > lis[j]:
				#swap
				temp = lis[j-1]
				lis[j-1] = lis[j]
				lis[j] = temp

def bubbleSort2(lis):
	'''this function sorts a given input list IN-PLACE in ascending order 
	using the Bubble sort algorithm, and returns nothing,
	and avoids some extra comparisons'''
	#for n passes:
	for i in range(len(lis)):
		#for each pair of items:
		for j in range(1,len(lis)-i):  #n-1 pairs
			#if two elements are out of order
			if lis[j-1] > lis[j]:
				#swap
				temp = lis[j-1]
				lis[j-1] = lis[j]
				lis[j] = temp

def bubbleSort3(lis):
	'''this function sorts a given input list IN-PLACE in ascending order 
	using the Bubble sort algorithm, and returns nothing
	with early stopping'''

	
	#for n passes:
	for _ in range(len(lis)):
		isSorted=True
		#for each pair of items:
		for j in range(1,len(lis)):  #n-1 pairs
			#if two elements are out of order
			if lis[j-1] > lis[j]:
				#swap
				temp = lis[j-1]
				lis[j-1] = lis[j]
				lis[j] = temp
				isSorted = False
		if isSorted:
			return #early stopping

def main():
	names = ['Kelly', 'Ray', 'Quinn', 'Isabelle', 'Leo', 'Mariam', 'Gandalf', 'Zelda', 'Ursala', 'Cade', 'Xander', 'John', 'Ophelia', 'Yasmine', 'Peter', 'Bob', 'Victor', 'Frodo', 'Wendy', 'Hodor', 'Nick', 'Alice', 'Sarah', 'Tom', 'Dean','Ellen']
	
	print(f"Names before sorting: {names}")
	bubbleSort3(names)
	print(f"Names after sorting: {names}")
	
main()