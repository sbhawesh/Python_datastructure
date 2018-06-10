arr = [3,5,1,7,8,12,9,2,2,0]
for i in range(len(arr)):

	 min=arr[i]
	 l=i+1
	 for x in range(l,len(arr)) :
		 if(min>arr[x]):
			 min=arr[x]
			 index=x
	 
	 if(min<arr[i]):
		 arr[index]=arr[i]
		 arr[i]=min



for j in range(0,len(arr)):
	 print(arr[j])
