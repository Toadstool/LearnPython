import random



def waga(l,w,p,wyn):
   if w==0: return wyn
   if w<0: return False
   if(p==len(l)): return False
   
   return  waga(l,w,p+1,wyn) or waga(l,w-l[p],p+1,wyn + [l[p]]) or waga(l,w+l[p],p+1,wyn + [-l[p]])
   
   

L = [1,2,5,10,23]
for i in range(0,50):
   r= waga(L,i,0,[])
   print("%s %s" % ( i,r))
