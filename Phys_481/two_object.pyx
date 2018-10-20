
cdef two_object():
	
	cdef double dt,a,dv,ds,p2
	L=1.0
	p1=-L
	p2=L
	dt=0.1
	G=6.67*10**-11

	T=0.0
	while p2>0.01:

		a=-G*1*1/((2*p2)**2)
		dv=a*dt
		ds=dv*dt
		p2=p2+ds
	return T