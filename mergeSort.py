arr = [3,5,1,7,8,12,9,2,2,0]

def mergesort(arr):
	n=len(arr)
	if n==1:
		return
	mid=n//2
	left = arr[:mid]
	right = arr[mid:]
	
	mergesort(left)
	mergesort(right)
	l=0
	m=0
	p=0
	nl=len(left)
	nr=len(right)
	while l < nl and m < nr :
		if left[l] <= right[m]:
			arr[p]=left[l]
			l += 1
		else:
			arr[p]=right[m]
			m += 1
		p += 1
	while l < nl:
		arr[p]=left[l]
		p += 1
		l += 1
	while m < nr:
		arr[p]=right[m]
		p += 1
		m += 1

mergesort(arr)
print(arr)
