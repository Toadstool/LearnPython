import sys
import random

R = "123456789"
l = list(R)
random.shuffle(l)
R = ''.join(l)
print(R)

def wczytaj(nazwa):
  t = {}
  f=open(nazwa,"r")
  for w in range(0,9):
    line=f.readline()
    for k in range(0,9):
      t[w,k]=line[k]
    # end for
  # end for
  f.close()
  return t
# end def

def wypisz(t):
  for w in range(0,9):
    for k in range(0,9):
      sys.stdout.write(' '+t[w,k])
    # end for
    sys.stdout.write('\n')
  # end for
  sys.stdout.write('\n')
# end def

def puste(t):
  res = []
  for w in range(0,9):
    for k in range(0,9):
      if t[w,k]=='-':
        res.append((w,k))
      # end ifhttps://github.com/Toadstool/LearnPython/tree/master/Lab2
    # end for
  # end for
  return res
# end def

def mozliwe(t,w,k):
  res = R  
  for i in range(0,9): res=res.replace(t[w,i],'')
  for i in range(0,9): res=res.replace(t[i,k],'')
  for i in range(k//3*3,k//3*3+3):
    for j in range(w//3*3,w//3*3+3): res=res.replace(t[j,i],'')
  # end for
  return res
# end def

def ruch(t,lp,n):
  global lg
  if n==len(lp):
    wypisz(t)
    sys.exit()
  else:
    w,k = lp[n]    
    for x in (mozliwe(t,w,k)):
      t[w,k]=x
      ruch(t,lp,n+1)
      t[w,k]='-'
    # end for
  # end if
# end def


d=wczytaj("dane.txt")
ruch(d,puste(d),0)



