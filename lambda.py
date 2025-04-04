s1="Hello Good Morning"
s2=lambda func:func.upper()
print(s2(s1))

n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))
print(n(-3))
print(n(0))


sq = lambda x: x ** 2
print(sq(3))

def sqdef(x):
    return x ** 2
print(sqdef(4))

li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())
  #  print(i)# not readable form
    
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(6))
print(check(7))

#lambda with multiple statements
calc = lambda x, y: (x + y, x * y)#two expression statement
res = calc(3, 4)
print(res)  # returns a tuple

n=[1,2,3,4,5,6]
even=filter(lambda x: x % 2 == 0, n) #filter() applies this condition to each element
print(list(even))
# print(even) non readable format

a = [1, 2, 3, 4]
b = (lambda x: x * 2, a)
#map() iterates through a and applies the transformation(X*2)
print(list(b))

from functools import reduce
a=[1,2,3,4]
b=reduce(lambda x, y: x * y, a) 
print(b)