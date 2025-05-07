import time
import copy

def modify_by_reference(arr):
	for i in range(len(arr)):
		arr[i] += 1

def modify_by_value(arr):
	arr_copy = copy.deepcopy(arr)
	for i in range(len(arr_copy)):
		arr_copy[i] += 1
	return arr_copy

size = 10**6

array = [i for i in range(size)]

start_time = time.time()
modify_by_reference(array)
end_time = time.time()
print(f'Czas wykonania dla przekazania przez referencję: {end_time - start_time:.6f} s')

array = [i for i in range(size)]

start_time = time.time()
modify_by_value(array)
end_time = time.time()
print(f'Czas wykonania dla przekazania przez wartość: {end_time - start_time:.6f} s')