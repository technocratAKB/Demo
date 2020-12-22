def compute_min_refills(distance,miles,n,stops):
	stops.insert(0,0)
	stops.append (distance)
	print (stops)
	curnt_refil=0
	refils=0
	while (curnt_refil<n):
		last_refil=curnt_refil
		while (curnt_refil<n and (stops[curnt_refil+1]-stops[last_refil]<=miles)):
			curnt_refil+=1
			
			
		if curnt_refil==last_refil:
			return (-1)
		if curnt_refil<=n:
			refils+=1
	return (refils)
	
d,m,n,*stp=map(int,input().rstrip().split())
print (compute_min_refills(d,m,n,stp))




