#1 Select all warehouses.
def Q1(mycursor):
    mycursor.execute('select * from Warehouses')
    return mycursor.fetchall()


#2 Select all boxes with a value larger than $150.
def Q2(mycursor):
    mycursor.execute('select * from boxes where value > 150')
    return mycursor.fetchall()

#3 Select all distinct contents in all the boxes.
def Q3(mycursor):
    mycursor.execute('select distinct contents from boxes')
    return mycursor.fetchall()

#4 Select the average value of all the boxes.
def Q4(mycursor):
    mycursor.execute('select avg(value) from boxes')
    return mycursor.fetchall()

#5 Select the warehouse code and the average value of the boxes in each warehouse.
def Q5(mycursor):
    mycursor.execute('select warehouse, avg(value) from boxes group by code')
    return mycursor.fetchall()

#6 Select only those warehouses where the average value of the boxes is greater than 150.
def Q6(mycursor):
    mycursor.execute('select warehouse from boxes group by code having avg(value) > 150')
    return mycursor.fetchall()

#7 Select the code of each box, along with the name of the city the box is located in.
def Q7(mycursor):
    mycursor.execute('select b.code,w.location city_name from boxes b left join warehouses w on w.code = b.warehouse')
    return mycursor.fetchall()

#8 Select the warehouse codes, along with the number of boxes in each warehouse.
def Q8(mycursor):
    mycursor.execute('select w.code,count(b.code) as no_of_boxes from warehouses w left join boxes b on b.warehouse = w.code group by w.code')
    return mycursor.fetchall()

#9 Optionally, take into account that some warehouses are empty (i.e., the box count should show up as zero, instead of omitting the warehouse from the result).
def Q9(mycursor):
    mycursor.execute('select w.code,coalesce(count(b.code),0) as no_of_boxes from warehouses w left join boxes b on b.warehouse = w.code group by w.code')
    return mycursor.fetchall()

#10 Select the codes of all warehouses that are saturated (a warehouse is saturated if the number of boxes in it is larger than the warehouse's capacity).
def Q10(mycursor):
    mycursor.execute('with temp as( select w.code,coalesce(count(b.code),0) as no_of_boxes,w.capacity from warehouses w left join boxes b on b.warehouse = w.code group by w.code ) select code from temp where no_of_boxes > capacity')
    return mycursor.fetchall()

#11 Select the codes of all the boxes located in Chicago.
def Q11(mycursor):
    mycursor.execute("select b.code from warehouses w left join boxes b on b.warehouse = w.code where w.location='Chicago' group by w.code ")
    return mycursor.fetchall()

#12 Create a new warehouse in New York with a capacity for 3 boxes.
def Q12(mycursor, mydb):
    mycursor.execute("INSERT INTO Warehouses(Code,Location,Capacity) VALUES(6,'New York',3);")
    mydb.commit()
    return "Record inserted successfully!"

#13 Create a new box, with code "H5RT", containing "Papers" with a value of $200, and located in warehouse 2.
def Q13(mycursor, mydb):
    mycursor.execute("INSERT INTO Boxes(Code,Contents,Value,Warehouse) VALUES('H5RT','Papers',200,2);")
    mydb.commit()
    return "Record inserted successfully!"

#14 Reduce the value of all boxes by 15%.
def Q14(mycursor, mydb):
    mycursor.execute("update Boxes set value=value-(value*0.15);")
    mydb.commit()
    return "Record(s) updated successfully!"

#15 Remove all boxes with a value lower than $100.
def Q15(mycursor, mydb):
    mycursor.execute("delete from Boxes where value < 100")
    mydb.commit()
    return "Record(s) deleted successfully!"

#16 Remove all boxes from saturated warehouses.
def Q16(mycursor):
    mycursor.execute('delete from boxes where code in (with temp as( select w.code,coalesce(count(b.code),0) as no_of_boxes,w.capacity from warehouses w left join boxes b on b.warehouse = w.code group by w.code ) select code from temp where no_of_boxes > capacity)')
    return "Record(s) deleted successfully!"

#17 Add Index for column "Warehouse" in table "boxes".
def Q17(mycursor, mydb):
    mycursor.execute("create index ind_warehouse on Boxes (warehouse)")
    mydb.commit()
    return "Index created successfully!"

#18 Print all the existing indexes.
def Q18(mycursor, mydb):
    mycursor.execute("show index from Boxes")
    mydb.commit()
    return mycursor.fetchall()

#19 Remove (drop) the index you added just.
def Q19(mycursor, mydb):
    mycursor.execute("SET foreign_key_checks = 0")
    mycursor.execute("alter table Boxes drop index ind_warehouse")
    mycursor.execute("SET foreign_key_checks = 1")
    mydb.commit()
    return "Index altered successfully!"


