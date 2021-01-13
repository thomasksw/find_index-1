
from fractions import Fraction


# r1 = r2
def assign(r1,r2):
  r1[0] = r2[0]
  r1[1] = r2[1]
  r1[2] = r2[2]
  r1[3] = r2[3]


def divide(r1,c):
  r4 = [0,0,0,0]
  r4[0] = r1[0] / c
  r4[1] = r1[1] / c
  r4[2] = r1[2] / c
  r4[3] = r1[3] / c
  return r4


def multiply(r,c):
  r4 = [0,0,0,0]
  r4[0] = c * r[0]
  r4[1] = c * r[1]
  r4[2] = c * r[2]
  r4[3] = c * r[3]

  return r4

def add(r1,r2):
  r4 = [0,0,0,0]
  r4[0] = r2[0] + r1[0]
  r4[1] = r2[1] + r1[1]
  r4[2] = r2[2] + r1[2]
  r4[3] = r2[3] + r1[3]
  return r4

def sub(r1,r2):
  r4 = [0,0,0,0]
  r4[0] = r1[0] - r2[0]
  r4[1] = r1[1] - r2[1]
  r4[2] = r1[2] - r2[2]
  r4[3] = r1[3] - r2[3]
  return r4


r1 = [3,4,5,8]
r2 = [2,3,4,5]
r3 = [3,2,4,5]
array = [r1,r2,r3]

print("A)\n",array[0],"\n", array[1], "\n", array[2],"\n")

k = r1[0]*r2[0]*r3[0]
m = r2[0]
n = r1[0]
p = r2[0]

assign(r1,multiply(r1,m))
assign(r2,multiply(r2,n))
assign(r3,multiply(r3,p))

print("B)\n",array[0],"\n", array[1], "\n", array[2],"\n") 

assign(r2,sub(r2,r1))
assign(r3,sub(r3,r1))

print("C)\n ",array[0],"\n", array[1],"\n", array[2],"\n")

a = r3[1]
b = r2[1]
assign(r2,multiply(r2,a))
assign(r3,multiply(r3,b))

print("D)\n",array[0],"\n", array[1], "\n", array[2],"\n")

assign(r3,sub(r3,r2))

print("E)\n",array[0],"\n", array[1], "\n", array[2],"\n")

x3 = Fraction(r3[3],r3[2])*1

r3[3]  = x3
r3[2]  = 1
r2[3]  = r2[3] - r2[2]*x3 
r3[2]  = 1
r2[2] =  0
x2 = Fraction(r2[3],r2[1])

print("F)\n",array[0],"\n", array[1], "\n", array[2],"\n")

r2[2]=0

print("G)\n",array[0],"\n", array[1], "\n", array[2],"\n")

r1[3]  = r1[3] - r1[1]*x2 - r1[2]*x3

print("H)\n",array[0],"\n", array[1], "\n", array[2],"\n")

x1 = Fraction(r1[3],r1[0])
r1[0]=1
r1[1]=0
r1[2]=0
r2[1]=1
r3[2]=1
r1[3]=x1
r2[3]=x2
r3[3]=x3

print("I)\n",array[0],"\n", array[1], "\n", array[2],"\n")