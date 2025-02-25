marks1 = int(input("enter the marks of 1st subject :"))
marks2 = int(input("enter the marks of 2nd subject :"))
marks3 = int(input("enter the marks of 3rd subject :"))

#percentage check 
total_perc = (100*(marks1 + marks2 + marks3 ))/300

percent = total_perc
marks = marks1 + marks2+marks3

if( percent>=40 and marks1>=33 and marks2>=33 and marks3>=33):{
    print (f"then ur pass in avery assepcts by marks as well as percentage ur percentage is{percent} and total marks are {marks}")
}
else :{
    print("ur are failed b'coz ur haven't meet all the chriteria for passing")

}

