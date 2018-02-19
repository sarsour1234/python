import random
my_randoms = random.sample(xrange(-30,30), 30)
print my_randoms
for x in my_randoms:
     for y in my_randoms:
      for z in my_randoms:
        sum=x+y+z
        if sum == 0 :
            print x,y,z
        else :
            print('did not find the 3 available numbers')
