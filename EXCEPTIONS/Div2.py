#program for Performing Division of Two Numbers
#Div2.py
try:
	print("Program Execution Started")
	s1=input("Enter First Value:")
	s2=input("Enter Second Value:")
	#Convert str type value into int type
	a=int(s1) #------------------------------- exception generated stmt--ValueError
	b=int(s2)#------------------------------- exception generated stmt--ValueError
	c=a/b  #------------------------------- exception generated stmt--ZeroDivisionError
except ZeroDivisionError:
	print("\tDon't Enter Zero for Den....")
except ValueError:
	print("\tDon't enter alnums,stmbols and str")
else:
	print("-----else block------")
	print("First Value:",a)
	print("Second Value:",b)
	print("Div=",c)
finally:
	print("-----finally block------")
	print("Program Execution Ended")

