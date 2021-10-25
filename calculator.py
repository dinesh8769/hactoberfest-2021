def sum(n1,n2):
  return n1+n2
def subs(n1,n2):
  return n1+n2
def Multi(n1,n2):
  return n1+n2
def Divi(n1,n2):
  return n1+n2

n1=int(input('Enter First Number: '))
n2=int(input('Enter Second Number: '))

print("1.Summation")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
x=int(input('Enter your Choice: '))
while(x==5):
  if x==1:
    print('sum is ',sum(n1,n2))
  elif x==2:
    print('Subs is ',subs(n1,n2))
  elif x==3:
    print('Multi is ',Multi(n1,n2))
  elif x==4:
    print('divi is ',Divi(n1,n2))
  elif x==5:
    pass
  else:
    print('Enter valid Number')
