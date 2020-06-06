n=int(input('please enter the number of students:'))
data={}
Subjects=('Physics','Math','History')
for i in range(0,n):
    name=input('please enter the name of students {}:'.format(i + 1))
    marks=[]
    for x in Subjects:
        marks.append(int(input('please enter marks of {}:'.format(x))))
    data[name]=marks
for x,y in data.items():
    total=sum(y)
    print("{}'s total marks {}".format(x,total))
    if total < 120:
        print(x,'failed :(')
    else: 
        print(x,'passed :)')
