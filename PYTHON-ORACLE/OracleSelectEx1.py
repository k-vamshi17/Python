#Program for Reading the Records from Employee Table
#OracleSelectEx1.py
import oracledb as orc
def  selectrecords():
	try:
		con=orc.connect("system/tiger@localhost/orcl")
		cur=con.cursor()
		sq="select * from employee"
		cur.execute(sq)
		#get the record
		print("*"*50)
		while(True):
			record=cur.fetchone()
			if(record!=None):
				for val in record:
					print("{}".format(val),end="\t")
				print()
			else:
				print("*"*50)
				break


	except orc.DatabaseError as db:
		print("Problem in Oracle Data Base:",db)

#Main Program
selectrecords()