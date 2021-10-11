i = list(input("Enter a credit card number ::"))
print(i[1::2])
Step_1 = []
for x in i[1::2]:
  x = int(x)*2
  Step_1.append(x)
print(Step_1)
Step_2 = []
for j in Step_1:
  if j>9:
   number = str(j)
   first,second = number[0],number[1]
   final=int(first)+int(second)
   Step_2.append(final)
  else:
    Step_2.append(j)
print(Step_2)    
rest=i[::2]
Step_3 = []
for a in rest:
  Step_3.append(int(a))
print(Step_3)
total=Step_3+Step_2
print(total)
print(sum(total))
#Step_4
if sum(total)%10==0:
  print("It is a valid credit card")
else:
  print("It is a invalid credit card")

