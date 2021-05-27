import random

BOX_SIZE = 6
MIN_ITEM_SIZE = 1
MAX_ITEM_SIZE = 4
ITEMS_COUNT = 12

def leq_k_count(items, k):
	count = 0
	for i in items:
		if i <= k:
			count += 1
	return count

def pack_items(items):
	boxes = {}
	i = 1
	while True:
		boxes[i] = []
		k = 0
		while sum(boxes[i]) < BOX_SIZE:
			elem_to_fit = min(BOX_SIZE - sum(boxes[i]) - k, MAX_ITEM_SIZE)
			cnt = leq_k_count(items, elem_to_fit)
			if cnt <= 0:
				break
			if elem_to_fit in items:
				boxes[i].append(elem_to_fit)
				items.remove(elem_to_fit)
				k = 0
			else:
				k += 1
		if len(items) == 0:
			break
		i += 1
	return boxes
	

if __name__ == "__main__":
	items = [random.randint(MIN_ITEM_SIZE, MAX_ITEM_SIZE) for _ in range(ITEMS_COUNT)]
	print(items)
	res = pack_items(items)
	for k,v in res.items():
		print(f"{k} : {v}")