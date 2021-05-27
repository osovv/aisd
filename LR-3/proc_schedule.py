import random

PROC_NUMBER = 4
T_SIZE = 11
MIN_TIME = 1
MAX_TIME = 8

def less_filled_proc(procs):
	s, i = 1e16, None
	for k, v in procs.items():
		if sum(v) < s:
			s, i = sum(v), k
	return s, i

def max_filling(procs):
	s, i = -1e16, None
	for k, v in procs.items():
		if sum(v) > s:
			s, i = sum(v), k
	return s, i

def schedule(t):
	res = {i : [] for i in range(1, PROC_NUMBER+1)}

	while True:
		min_fill, min_idx = less_filled_proc(res)
		max_fill, max_fill = max_filling(res)
		max_item = max(t)
		res[min_idx].append(max_item)
		t.remove(max_item)
		if len(t) == 0:
			break
	return res

if __name__ == "__main__":
	t = [random.randint(MIN_TIME, MAX_TIME) for _ in range(T_SIZE)]
	print(f"{sorted(t)}, sum(t)/{PROC_NUMBER} = {sum(t)/PROC_NUMBER}")
	res = schedule(t)
	for k,v in res.items():
		print(f"{k} : {v}, sum = {sum(v)}")
