a = int(input("introdusca a: "))
b = int(input("introdusca b: "))
primo=0
if 0<=a<=10000000 and 0<=b<=10000000:
    
        for i in range(a,b+1):
            c=0
            for j in range(1,i+1):
               if i%j==0:
                  c=c+1
        
            if c==2:
              primo=primo+1
print("numeros de primos ",primo)
   
