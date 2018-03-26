import sys
import heapq

# Generate a next sequence
def getNextA(prev_A, a, b):
	if prev_A  == None:
		# A[0] = 1983
		return 1983
	else:
		# A[i] = (A[i-1] * a + b) % 20090711
		return (prev_A * a + b) % 20090711

# Do main work
large_heap = []
small_heap = []
def getMedianWith(a):
	if len(small_heap) == 0:
		heapq.heappush(small_heap, -a)
	elif len(large_heap) == 0:
		prev = -small_heap[0]

		if a >= prev:
			# just insert into large heap
			heapq.heappush(large_heap, a)
		else:
			heapq.heappush(large_heap, prev)
			heapq.heappop(small_heap)
			heapq.heappush(small_heap, -a)
	else:
		smallest_large_heap = large_heap[0]
		largest_small_heap = -small_heap[0]		# Because heapq supports 'min-heap', we should negative for small heap

		if a >= smallest_large_heap:
			heapq.heappush(large_heap, a)

			# if large_heap contains more-than-1 elements compared to small_heap,
			if len(large_heap) > len(small_heap):
				# move the smallest one to small_heap
				smallest_large_heap = heapq.heappop(large_heap)
				heapq.heappush(small_heap, -smallest_large_heap)	# Because heapq supports 'min-heap', we should negative for small heap
		else:
			heapq.heappush(small_heap, -a)

			# if small_heap contains more-than-2 elements compared to large_heap
			if len(small_heap) > len(large_heap) + 1:
				# move the largest one to large_heap
				largest_small_heap = -heapq.heappop(small_heap)
				heapq.heappush(large_heap, largest_small_heap)

	return -small_heap[0]

###-----------------------------------------
rl = lambda: sys.stdin.readline()
number_of_test_case = int(rl())

for idxTest in range(number_of_test_case):
	test_case = rl().split(" ")

	N = int(test_case[0])
	a = int(test_case[1])
	b = int(test_case[2])

	# initialize to test
	prev_A = None
	large_heap = []
	small_heap = []
	sum = 0
	for idxElement in range(N):
		A_i = getNextA(prev_A, a, b)

		# print("a_"+str(idxElement), A_i)

		# Do Work!
		median = getMedianWith(A_i)
		# print(A_i, large_heap, small_heap, median)
		sum += median

		prev_A = A_i
	print(sum % 20090711)