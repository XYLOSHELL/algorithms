from math import *

def bucket_sort(array, bucket_size):
	if len(array) == 1:
		return array
	min_val = array[0]
	max_val = array[0]
	for i in range(0, len(array)):
		if array[i] < min_val:
			min_val = array[i]
		if array[i] > max_val:
			max_val = array[i]
	num_bucket = floor((max_val - min_val) / bucket_size) + 1
	buckets = []
	for i in range(0, num_bucket):
		buckets.append([])
	for i in range(0, len(array)):
		buckets[floor((array[i] - min_val) / bucket_size)].append(array[i])
	sort_arr = []
	for i in range(0, len(buckets)):
		buckets[i].sort()
		for j in range(0, len(buckets[i])):
			sort_arr.append(buckets[i][j])
	return sort_arr

array = [int(s) for s in input().split()]
print(bucket_sort(array, len(array)))