a= "raj"

# if (a<5):
#   print("kisore")
# elif(a==5):
#     print("aaaaa")
# elif(a==6):
#     print("bbbbb")
# elif(a==raj):
#     print("cccccc")
# else :
#     print("abul")
# print(type(a) == int)
# print(isinstance(a,str))
# aaname= "        abul"
# bbname2= "  kalam"
# cname3= aaname+bbname2+"azath"
# print(cname3.upper())
# print(cname3.lower())
# print(cname3.title())
# print(cname3.replace("abul","abdul"))
# print(len(cname3))
# print(len(cname3.strip()))



# num=str(2000)
# con="i was born "
# print(con+"in ramanathapuram   "  +num)



# a=" Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto illo ad asperiores laboriosam quae mollitia, dolorem ipsa quaerat eum, enim amet quisquam, minima autem ex! Quisquam, fuga velit! Modi, eius."
# print(a)
# b='''
#  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto illo ad asperiores laboriosam quae mollitia, dolorem ipsa quaerat eum, enim amet quisquam, minima autem ex! Quisquam, fuga velit! Modi, eius.
#   aejfhjFkFJqkgj kj                         klafhLKAFekfn
# '''
                         
# c='idon\'t know i coul\'d call you later\n ahfiauyf\thjclAEJ \tKAJFHauefhA KAJFHufhAIJFB\t'
# print(c)
# print()
tit="snakes".title()
# print(tit)
# print(tit.center(50,"@"))
# print()
# print()
# print("bonda".ljust(23,"*")+"1".rjust(10,"%"))
# print()
# print()
# print("booo".ljust(23,"*")+"kisooo".rjust(7,"-"))
# print()
# print()
# print("akkkk".ljust(23,"*")+"3".rjust(2,"-"))
# print("gggg".ljust(23,"*")+"4".rjust(2,"-"))
# print(tit[1])
# print(tit[0:-3])
# print(tit[0:3])
# import math
# aaa=12.1
# print(math.floor(aaa))

# print(math.sqrt(aaa)) 

# print(math.ceil(aaa)) 

list=["apple","ball","cat","dog","elephont","fish"]
list.append("good")
print("cat" in list)
list +=["height"]
print(list[0:5])
print(list[0:-2])
list.extend(["ice cream","juck"])
list.insert(0,"abul kalam")
print(len(list))
list[5:7]=["raa","raaa"]
list.remove("raaa")
list.pop()
list.clear()
del list[2]
list.sort()
print(list)

# good={"apple":2,
#       "orange":4,
#       "mango":6,
#       "graps":3,
#       "dragon":7}
# good["mango"]="blue berry"
# good.update({"orange":55})
# print(good)
# fill=dict(apple=12,
#       orange=14,
#       mango=16,
#       graps=13,
#       dragon=17)
# # print(fill)
# # print(good.pop("apple"))
# # print(good)
# # print(good.popitem())
# # print(good)
# # fill["malgova"]="10"
# # print(fill)
# band={
#     "good":good,
#     "fill":fill
# }
# print()
# print()
# print()
# print()
# print(band)
# print()
# print()
# print()
# print()
# print([good],["apple"])



# def add(num):
#     if (num>=9):
#         return num+1
#     total=num+1
#     print(total)
#     return add(total)
# addnum = add(0)
# print(addnum)




#from learn2 import sum
# squre= lambda num: num*num
# print(squre(5))
# def fun(x):
#     return lambda num:num+x
# addda= fun(10)
# adddb= fun(20)
# adddc= fun(30)
# print(addda(1))
# print(adddb(1))
# print(adddc(1))
# numb=[10,11,12,13,14,15,16,17,18,19,20,11,5,7,3,1,0]
# sqr=map(lambda int:int+int,numb)
# print(list(sqr))

# add =filter(lambda num:num%2 !=0,numb)
# print("add number" +str( list(add)))
# div =filter(lambda num:num%2 ==0,numb)
# print("even number"+ str(list(div)))

# numa=[1,2,3,4,5,6]
# from functools import reduce
# total= reduce(lambda acc,curr: acc+ curr,numa)
# print(total)
# print(sum(numa))

# name={"abul","raj","muja","sadheesh","cap","tamil","majee"}
# cou = reduce(lambda acc,curr:acc+len(curr),name,0)
# print(str(cou))


# class Vehicle():
#     def __init__(self,make,modul):
#         self.brand=make
#         self.type= modul
#     def action(self):
#         print("i am iron man")
#     def get_make_model(self):
#         print (f"i'm a {self.brand} {self.type}")
        
# fast= Vehicle("tesla","300")
# fast.get_make_model()
# fast.action()
# print(fast.brand)
# print(fast.type)
# print("\n\n")

# fury=Vehicle("aadi","100")
# fury.get_make_model()
# print("\n\n")


# class Aeroplane(Vehicle):
#     def __init__(self,make,model,faa_id):
#         super().__init__(make,model)
#         self.faa_id=faa_id
#     def action(self):
#         print("fly there")

# class truck(Vehicle):
#     def __init__(self,make,model,faa_id):
#         super().__init__(make,model)
#         self.faa_id=faa_id
#     def action(self):
#         print("heavy sound")

# class bus (Vehicle):
#     def __init__(self,make,model,faa_id):
#         super().__init__(make,model)
#         self.faa_id=faa_id
#     def action(self):  
#         print("burrr sound")
# buss=bus("mechlan","500","yes yemaha")
# buss.get_make_model()
# print("\n\n")
# tru=truck("hundai","400","ct100")
# tru.get_make_model()
# print("\n\n")

# aero=Aeroplane("indian","cz100","1200")     
# aero.get_make_model()
# for v in (buss,tru,aero):
#     v.get_make_model()
#     v.action()
# x=2
# try:
#     print(x/0)
    
# except NameError:
#  print("just for fun") 
# # except Exception as error:
# #  print("error")
# else:
#   ("no errror")
# finally:
#   print("always good") 


# import argparse

# parser = argparse.ArgumentParser(
#     description="personal greeting"
# )
# parser.add_argument("-n","--name",metavar="name",
#                     required=True, help= "thats fine")
# args = parser.parse_args()
# def sadhish(num):
#  if(num>=6):
#      return num+1
#   elif(num>=10):
#      return num*num
 
#  total=num+1

#  print(total)
#  return "########\nhellow every ono \n########"


# aaa=sadhish(0)

#  print(aaa)
# num1=int(input("num 1="))
# num2=int(input("num 2="))
# num3=input("add/sub/div/mul")
# if  (num3=="add"):
#     print(num1+num2)
    
# elif(num3=="sub"):
#     print(num1-num2)
# elif(num3=="mul"):
#     print(num1*num2)
# elif(num3=="div"):
#     print(num1/num2)
# else:
#     print("good student")
# sal=int(input("salry ="))
# age=int(input("age ="))
# if(sal>=30000 or age<=20):
#     loan=int(input("loan amount ="))
#     if(loan>50000):
#         print("maximum loan 50000")    
#     else:
#         print("your elogible")      
# else:
#   print("your not elogible")      
# a=int(input())
# b=int(input())
# count=0
# aount=10
# sum=0
# a=[]
# print("enter 10 number")
# for i in range(0,5):
#     i=i+1
#     num=int(input("enter number"+str(i)+" :"))
#     a.append(num)
#     num=num+num 
#     num=(num/i)
# print(a)
# print(int(num))

# for i in range(100):
#     print()
#     for  j in range(1,1+i):
#       print("#",end="")
# for j in range(j,0,-1):
#      print()
#      for k in range(j,0,-1):
     
#       print("#", end="")
     
# for i in range(30):
#     print()
#     for j in range(1,1+i):
#         print("@",end="")
# for j in range(j,0,-1):
#     print()
#     for k in range(j,0,-1):
#      print("@",end="")
# i=3
# fa=1
# while(0<i):
#     fa=fa*i
#     i=i-1
# print(fa)  
# def add():
#  a=int(input("enter number : "))
#  b=int(input("enter number : ")) 
#  print('ans',a+b)
# add()
# def sub():
#  a=int(input("enter number : "))
#  b=int(input("enter number : ")) 
#  print(a-b)
# sub()
# def mul():
#  a=int(input("enter number : "))
#  b=int(input("enter number : ")) 
#  print(a*b)
# mul()
# def div():
#  a=int(input("enter number : "))
#  b=int(input("enter number : ")) 
#  print(a/b)
# div()
# def fun(num):
#     if (num>=35):
#         print("pass")
#     else:
#         print("fail")
# a=int(input("enter mark :"))
# # fun(a)
# def num(r1,r2):
#     for i in range(r1,r2):
#       print(i) 
# a=int(input("enter no 1"))
# b=int(input("enter no 2"))
# num(a,b)

# class laptap():
#   project= ""
#   procesor=""
#   ram=""
  
# HP=laptap()  
# dell=laptap()  
# lenovo=laptap()
# HP.project="001"
# dell.project="002"
# lenovo.project="003"

# HP.procesor="10000"
# dell.procesor="15000"
# lenovo.procesor="25000"

# HP.ram="001654"
# dell.ram="002654"
# lenovo.ram="003354"

# print(HP.project)
# print(dell.project)
# print(lenovo.project)

# print(HP.procesor)
# print(dell.procesor)
# print(lenovo.procesor)

# print(HP.ram)
# print(dell.ram)
# print(lenovo.ram)

# class doc:
#     def __init__(self, name, rno):
#         self.name= name
#         self.rno= rno
#     def prin(self):
#         print("name : ",self.name)
#         print( "Rno : ", self.rno)
# p1=doc("raj","001")
# p2=doc("jar","002")
# p1.prin()
# p2.prin()
    

   
#     def add(self,n1,n2):
#         print(n1+n2)
       
#     def sub(self,n1,n2):
#         print(n1-n2)

#     def mul(self,n1,n2):
#         print(n1*n2)
            
#     def dev(self,n1,n2):
#          print(n1/n2)


# n1.add(10,10)
# n1.sub(10002,13540)
# n1.add(1055,102)
# n1.add(10565,10)


# class animal():
#     # def __init__(self):
#     #     print("a")
#     def sound(self):
#         print("g stick")
# class bird(animal):
#     # def __init__(self):
#     #     print("b")
#         # super().__init__()
#     def sound(self):
#         print("g story")
# class lion(bird):
# #     def __init__(self):
# #         print("c")
# #         super().__init__()
#      def sound(self):
#            print("g money")
# # class d():
# #        def __init__(self):
# #         print("d")
# #         super().__init__()
# #     # def snack(self):
# #     #     print("g snack")
# # class e(d,c,b,a):
# #        def __init__(self):
# #         super().__init__()
# #         print("e")
# #     #  def phone(self):
# #     #     print("g phone")

# raj=animal()
# raj.sound()

# # raj.phone()
# # raj.stick()
# # raj.story()
# # raj.money()
# # raj.snack()
# class shape():
#    def __init__(self,name):
#         self.name=name
       
# class rectangle(shape):
#    def __init__(self,name,grade):
#         super ().__init__(name)
#         self.grade=grade
#    def add(self):
#        print(self.name,self.grade)
    
        

# s1=rectangle("john","A")
# s1.add()
# class employ():
#     def __init__(self,name,salary):
#      self.name=name
#      self.salary=salary
# class manager(employ):
#     def __init__(self,name,salary,deportment):
#      super().__init__(name,salary)
#      self.department=department
#     def display(self):
#         print(self.name,self.salary,self.deportment)

# ooo=manager("rahav",22000,"developer")
# ooo.display()
# nt("type error",e)       

# try:
    
#     class com():
#         def __init__():
#             self._companyname="google"
#         def con(self):
#             self._companyname="google"
#             print(self._companyname) 
#     class company(com):
#             pass
#     a1=company()
#     a1.__companyname="goooooooggg"
#     print(a1._companyname)
# except TypeError as e:
#      pri
        
           