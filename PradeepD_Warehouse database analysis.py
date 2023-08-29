#!/usr/bin/env python
# coding: utf-8


import mysql.connector
import mysql_modules as m
from tabulate import tabulate



def connection_string():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'de18_mysql'
    )
    return mydb
mydb = connection_string()  


mycursor = mydb.cursor(buffered=True)


#1 Select all warehouses.

result = m.Q1(mycursor)
print(tabulate(result,headers=[i[0] for i in mycursor.description], tablefmt='psql'))


#2 Select all boxes with a value larger than $150.

result = m.Q2(mycursor)
print(tabulate(result,headers=[i[0] for i in mycursor.description], tablefmt='psql'))


#3 Select all distinct contents in all the boxes.

result = m.Q3(mycursor)
print(tabulate(result,headers=[i[0] for i in mycursor.description], tablefmt='psql'))


#4 Select the average value of all the boxes.

result = m.Q4(mycursor)
print(tabulate(result,headers=[i[0] for i in mycursor.description], tablefmt='psql'))



#5 Select the warehouse code and the average value of the boxes in each warehouse.

result = m.Q5(mycursor)
print(tabulate(result,headers=[i[0] for i in mycursor.description], tablefmt='psql'))


#6 Select only those warehouses where the average value of the boxes is greater than 150.

result = m.Q6(mycursor)
print(tabulate(result,headers=[i[0] for i in mycursor.description], tablefmt='psql'))



#7 Select the code of each box, along with the name of the city the box is located in.

result = m.Q7(mycursor)
print(tabulate(result,headers=[i[0] for i in mycursor.description], tablefmt='psql'))

#8 Select the warehouse codes, along with the number of boxes in each warehouse.

result = m.Q8(mycursor)
print(tabulate(result,headers=[i[0] for i in mycursor.description], tablefmt='psql'))


#9 Optionally, take into account that some warehouses are empty (i.e., the box count should show up as zero, instead of omitting the warehouse from the result).

result = m.Q9(mycursor)
print(tabulate(result,headers=[i[0] for i in mycursor.description], tablefmt='psql'))


#10 Select the codes of all warehouses that are saturated (a warehouse is saturated if the number of boxes in it is larger than the warehouse's capacity).

result = m.Q10(mycursor)
print(tabulate(result,headers=[i[0] for i in mycursor.description], tablefmt='psql'))


#11 Select the codes of all the boxes located in Chicago.

result = m.Q11(mycursor)
print(tabulate(result,headers=[i[0] for i in mycursor.description], tablefmt='psql'))



#12 Create a new warehouse in New York with a capacity for 3 boxes.

result = m.Q12(mycursor,mydb)
print(result)


#13 Create a new box, with code "H5RT", containing "Papers" with a value of $200, and located in warehouse 2.

result = m.Q13(mycursor,mydb)
print(result)


#14 Reduce the value of all boxes by 15%.

result = m.Q14(mycursor,mydb)
print(result)


#15 Remove all boxes with a value lower than $100.

result = m.Q15(mycursor,mydb)
print(result)


#16 Remove all boxes from saturated warehouses.

result = m.Q16(mycursor)
print(result)



#17 Add Index for column "Warehouse" in table "boxes".

result = m.Q17(mycursor,mydb)
print(result)



#18 Print all the existing indexes.

result = m.Q18(mycursor,mydb)
print(tabulate(result,headers=[i[0] for i in mycursor.description], tablefmt='psql'))



#19 Remove (drop) the index you added just.

result = m.Q19(mycursor,mydb)
print(result)




