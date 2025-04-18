#Program for Demonstrating keyword args
#KeywordArgsEx2.py
def  disp(a,b,c,d,PI=3.14):
	print("{}\t{}\t{}\t{}\t{}".format(a,b,c,d,PI))

#Main Program
print("-"*50)
print("A\tB\tC\tD\tPI")
print("-"*50)
disp(10,20,30,40)  # Function call with Posstional Args
disp(d=40,b=20,a=10,c=30)  # Function call with Keyword Args
disp(d=40,a=10,b=20,c=30) # Function call with Keyword Args
disp(10,20,d=40,c=30) # Function call with Posstional Args and Keyword Args
#disp(d=40,c=30,10,20)  SyntaxError: positional argument follows keyword argument
disp(d=40,c=30,a=10,b=20) # Function call with Keyword Args
#disp(d=40,c=30,a=10,b1=20) # TypeError: disp() got an unexpected keyword argument 'b1'
disp(b=20,a=10,PI=3.147324,d=40,c=30) # Function call with  Keyword Args and deafult args
print("-"*50)