import random

class MasterMind:

   def gen(self):
      res=""
      for i in range(4):
        res=res+str(random.randint(1,6))
      return res
   # end def

   def spr(self,kod,proba):
      k=list(kod)
      p=list(proba)
      lc=0
      for i in range(4):
         if p[i]==k[i]:
            lc=lc+1
            p[i]=-1
            k[i]=-2
          # end if
      # end for
      lb=0
      for i in range(4):
         for j in range(4):
            if p[i]==k[j]:
              lb=lb+1
              p[i]=-1
              k[j]=-2
            # end if
         # end for
      return (lc,lb)
   # end def



   def play(self):
      theEnd = 10
      data = self.gen()
      while theEnd:
         theEnd = theEnd -1
         userInput = input(">>")
         if userInput=="q":
            break
         
         kod=self.spr(data, userInput)
         if kod==(4,0):            
            theEnd = 0
            print("Win")
         else:
            print(kod)
            print("Try again")
   #end def         

#end class

master = MasterMind()
master.play()



         

