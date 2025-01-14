#MySQL CONNECTION
import mysql.connector as sql
import maskpass
con = sql.connect(host = "localhost", user = "root", password = "sanj@2005")
cr = con.cursor()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#CREATING TABLES
cr.execute("create database cs_empdata")
cr.execute("use cs_empdata")
cr.execute("create table logins(username varchar(30) PRIMARY KEY, password varchar(20) not null)")
cr.execute("create table emp_det(empno int primary key, empname varchar(30) not null, age int not null, gender char(1), basicsal float(2) not null, othours float(2))")
cr.execute("create table calcs(empno int primary key, empname varchar(30) not null, monthlysal float(8,3) not null, otcharges float(8,1) not null, grosspay float(8,1) not null, deducts float(8,1) not null, netpay float(8,1) not null)")
con.commit()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#LOGIN DETAILS
cr.execute("Select username FROM LOGINS")
users = cr.fetchall()

print('='*120)
print("\t "*5," EMPLOYEE PAYROLL MANAGEMENT")
print('='*120)
print()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#LOGIN
def login():
    a=True
    while a==True:
        log = input("\nLogin(L)/Sign up(S): ")
        cr.execute("Select username FROM LOGINS")
        users = cr.fetchall()
        if log.upper()=='S':
            a1=True
            while a1==True:
                u = input("Username: ")
                v = (u,)
                if v in users:
                    print("> USER ALREADY EXISTS")
                    a1=False
                    break
                
                else:
                    p = maskpass.askpass(prompt="Password: ", mask = "*")                    
                    c1 = "insert into LOGINS values('%s','%s')"%(u,p)
                    cr.execute(c1)
                    con.commit()
                    print(">> USER HAS BEEN CREATED(login again to continue)")
                    a1=False
                    pass

        cr.execute("Select*FROM logins")
        u1 = cr.fetchall()

        if log.upper()=='L':
            while True:
                print('\nLogin:- ')
                user = input('Username: ')
                pas = maskpass.askpass(prompt = "Password: ", mask = "*")                
                log1=(user,pas)
                if log1 in u1:
                    print('>> LOGGED IN SUCCESSFULLY')
                    print()                    
                    a=False
                    break
                else:
                    print('> USER NOT FOUND')
                    break
login()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#ENTERING DETAILS
def enter_det():
    ans='y'
    while ans.lower()=='y':
        print();print(' - '*40),print()
        print("Entering Employee Details:-")
        print("1. Add one Employee")
        print("2. Add numerous Employees")
        print("3. Main Menu")
        print()
        c = int(input("> Enter choice: "))
        print()

        if c==1:
            print("  .  "*24);print()
            cr.execute("Select empno from emp_det")
            en = cr.fetchall()
            print("--> Add one Employee:-")
            print()
            print("Enter following details -")
            eno = int(input("Employee No.: "))
            teno = (eno,)
            if teno in en:
                print()
                print('> Emp No. already exists.')
            else:
                name = input("Name: ")
                age = int(input("Age: "))
                w1=1
                while w1==1:
                    gender = input("Gender (M/F/O): ")            
                    if gender.upper()=='M' or gender.upper()=='F' or gender.upper()=='O':
                        w1=0
                    else:
                        print("> Enter valid choice")
                print('.'*20)
                bs = float(input("Basic Salary: "))
                ov = float(input("Overtime(hrs): "))
                print()                
                det = "insert into emp_det values(%s, '%s', %s, '%s', %s, %s)"%(eno,name.upper(),age,gender.upper(),bs,ov)
                cr.execute(det)
                cr.execute("insert into calcs values(%s, '%s', %s, %s, %s, %s, %s)"%(eno,name.upper(),bs,0,0,0,0))
                con.commit()
                print(">> EMPLOYEE ADDED\n")
                w2=1
                while w2:
                    ans1 = input("Add more records?(y/n): ")
                    if ans1.lower()=='y':
                        ans='y'
                        w2=0
                    elif ans1.lower()=='n':
                        ans='n'
                        w2=0
                    else:                        
                        print("> Enter valid choice")
        
        elif c==2:
            print("  .  "*24);print()
            print("--> Adding numerous Employees:-")
            print()
            n = int(input("Number of employees to be added: "))
            cr.execute("Select empno from emp_det")
            en = cr.fetchall()
            for a in range(1,n+1):
                
                enob = int(input("Employee No.: "))
                tenob = (enob,)
                if tenob in en:
                    print()
                    print('> Emp No. already exists.')
                    break
                else:
                    nameb = input("Name: ")
                    ageb = int(input("Age: "))
                    w3=1
                    while w3:
                        genderb = input("Gender (M/F/O): ")
                        if genderb.upper()=='M' or genderb.upper()=='F' or genderb.upper()=='O':
                            w3=0
                        else:
                            print("> Enter valid choice")
                    print('.'*20)
                    bsb = float(input("Basic Salary: "))
                    ovb = float(input("Overtime(hrs): "))
                    print()
                    det = "insert into emp_det values(%s, '%s', %s, '%s', %s, %s)"%(enob,nameb.upper(),ageb,genderb.upper(),bsb,ovb)
                    cr.execute(det)
                    cr.execute("insert into calcs values(%s, '%s', %s, %s, %s, %s, %s)"%(enob,nameb.upper(),bsb,0,0,0,0))
                    con.commit()
                    print(">> EMPLOYEE ADDED")
                    print()
                if a==n:
                    w4=1
                    while w4:
                        ans2 = input("Add more records?(y/n): ")
                        if ans2.lower()=='y':
                            ans='y'
                            w4=0
                        elif ans2.lower()=='n':
                            ans='n'
                            w4=0
                        else:                        
                            print("> Enter valid choice")                    
                else:
                    pass
        elif c==3:
            break
        
        else:
            print("> INVALID CHOICE, Enter again")        

#-----------------------------------------------------------------------------------------------------

#VIEW DETAILS
def view_det():
    while True:
        print();print(' - '*40),print()        
        print("View Details:-")
        print("1. Search Employee")        
        print("2. View All Employees")
        print("3. Main Menu")
        print()
        ve = int(input("> Enter choice: "))
        print()
    
        if ve==1:
            while True:
                print("  .  "*24);print()
                print("--> Search Employee:-")
                print("\ta. Search by Employee Name")
                print("\tb. Search by Employee No.")
                print("\tc. Back to Menu")
                print()
                sch = input("> Enter choice: ")

                if sch.upper()=='A':
                    print()
                    en = input("Enter Employee Name: ")
                    cr.execute("select count(empno) from emp_det where empname = '{}'".format(en.upper()))
                    empcount1 = cr.fetchall()
                    print("No. of search results = ", empcount1[0][0])
                    print()
                    if empcount1[0][0]==0:
                        print("> No records were found")
                        print()
                    else:
                        cr.execute("select*from emp_det where empname = '{}' ORDER BY empno asc".format(en.upper()))
                        semp = cr.fetchall()
                        print('-'*80)
                        print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                        print('-'*80)
                        for i in semp:
                            print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                            print('-'*80)
                        print()

                elif sch.upper()=='B':
                    print()
                    en1 = int(input("Enter Employee No.: "))
                    cr.execute("select count(empno) from emp_det where empno = '{}'".format(en1))
                    empcount1 = cr.fetchall()                
                    print()
                    if empcount1[0][0]==0:
                        print("> No records were found")
                        print()
                    else:
                        cr.execute("select*from emp_det where empno = {} ORDER BY empno asc".format(en1))
                        semp = cr.fetchall()
                        print('-'*80)
                        print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                        print('-'*80)
                        for i in semp:
                            print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                            print('-'*80)
                        print()

                elif sch.upper()=='C':
                    break

                else:
                    print()
                    print("> INVALID CHOICE, Enter again")
                    print()

        elif ve==2:
            while True:
                print("  .  "*24);print()
                print("--> Order by -")
                print("\ta. Employee no.")
                print("\tb. Employee Name")
                print("\tc. Employee Salary")
                print("\td. Back to Menu")
                print()
                vd = input("> Enter choice: ")                

                cr.execute("select count(empno) from emp_det")
                empcount = cr.fetchall()             

                if vd.upper()=='A':
                    print()
                    print("Total no. of employees = ",empcount[0][0])
                    print()
                    print('-'*80)
                    cmd = "select*from emp_det ORDER BY empno asc"
                    cr.execute(cmd)
                    semp = cr.fetchall()
                    print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                    print('-'*80)
                    for i in semp:
                        print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                        print('-'*80)
                    print()
                    break

                elif vd.upper()=='B':
                    print()
                    print("Total no. of employees = ",empcount[0][0])
                    print()
                    print('-'*80)
                    cmd = "select*from emp_det ORDER BY empname asc"
                    cr.execute(cmd)
                    semp = cr.fetchall()
                    print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                    print('-'*80)
                    for i in semp:
                        print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                        print('-'*80)
                    print()                    
                    break

                elif vd.upper()=='C':
                    print()
                    print("Total no. of employees = ",empcount[0][0])
                    print()
                    print('-'*80)
                    cmd = "select*from emp_det ORDER BY basicsal asc"
                    cr.execute(cmd)
                    semp = cr.fetchall()
                    print("BASIC SALARY\tEMP NO.\t AGE\tGENDER\tOVERTIME(hrs)\t|\tNAME")
                    print('-'*80)
                    for i in semp:
                        print('  ',i[4],'\t',i[0],'\t',i[2],'\t',i[3],'\t',i[5],'\t\t|',i[1])
                        print('-'*80)
                    print()
                    break

                elif vd.upper()=='D':
                    break

                else:
                    print()
                    print("> INVALID CHOICE, Enter again")
                    print()

        elif ve==3:            
            break

        else:
            print("> INVALID CHOICE, Enter again")

#------------------------------------------------------------------------------------------------------

#UPDATE DETAILS
def update_det():
    menu = 'n'
    while menu.lower()=='n':
        print();print(' - '*40),print()
        print("Updating Employee Details:-")
        print("1. Individual Update")
        print("2. Update numerous records")
        print("3. Delete Records")
        print("4. Main Menu")
        print()
        ib = input("> Enter choice: ")
        print()
    
        if ib=='1':
            print("Current details of Employees")
            print('-'*80)
            cmd = "select*from emp_det ORDER BY empno asc"
            cr.execute(cmd)
            semp = cr.fetchall()
            print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
            print('-'*80)
            for i in semp:
                print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                print('-'*80)
            print()
            up = int(input("Enter Emp no. to be updated: "))
            print()
            cr.execute("select count(empno) from emp_det where empno = {}".format(up))
            emcount = cr.fetchall()
            if emcount[0][0]==0:
                print("> No record(s) found")                
            else:                
                cr.execute("select*from emp_det where empno = {}".format(up))
                update = cr.fetchall()
                print('-'*80)
                print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                print('-'*80)
                for i in update:
                    print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                    print('-'*80)
                print()
                    
                ans = 'y'
                while ans.lower()=='y':
                    print("  .  "*24);print()
                    print("--> Updating Elements -")
                    print("\ta. Employee Name")
                    print("\tb. Age")
                    print("\tc. Gender")
                    print("\td. Basic Salary")
                    print("\te. Overtime(hrs)")
                    print("\tf. Back to Menu")
                    print()
                    ch = input("> Enter choice: ")
                    print()

                    if ch.upper()=='A':
                        namenew = input("Enter updated Name: ")
                        cr.execute("update emp_det set empname = '{}' where empno = {}".format(namenew.upper(),up))
                        cr.execute("update calcs set empname = '{}' where empno = {}".format(namenew.upper(),up))
                        con.commit()
                        print(">> Details have been updated")
                        print()
                        cr.execute("select*from emp_det where empno = {}".format(up))
                        update = cr.fetchall()
                        print('-'*80)
                        print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                        print('-'*80)
                        for i in update:
                            print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                            print('-'*80)
                        print()
                        ans = input("Update more details?(y/n): ")
                        print()

                    elif ch.upper()=='B':                                                
                        agenew = int(input("Enter updated Age: "))
                        cr.execute("update emp_det set age = {} where empno = {}".format(agenew,up))
                        con.commit()
                        print(">> Details have been updated")
                        print()
                        cr.execute("select*from emp_det where empno = {}".format(up))
                        update = cr.fetchall()
                        print('-'*80)
                        print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                        print('-'*80)
                        for i in update:
                            print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                            print('-'*80)
                        print()
                        ans = input("Update more details?(y/n): ")
                        print()
                        
                    elif ch.upper()=='C':
                        w5=1
                        while w5==1:
                            gennew = input("Enter updated Gender(M/F/O): ")            
                            if gennew.upper()=='M' or gennew.upper()=='F' or gennew.upper()=='O':
                                w5=0
                            else:
                                print("> Enter valid choice")
                        
                        cr.execute("update emp_det set gender = '{}' where empno = {}".format(gennew.upper(),up))
                        con.commit()
                        print(">> Details have been updated")
                        print()
                        cr.execute("select*from emp_det where empno = {}".format(up))
                        update = cr.fetchall()
                        print('-'*80)
                        print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                        print('-'*80)
                        for i in update:
                            print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                            print('-'*80)
                        print()
                        ans = input("Update more details?(y/n): ")
                        print()
                        
                    elif ch.upper()=='D':
                        bsnew = float(input("Enter updated Salary: "))
                        cr.execute("update emp_det set basicsal = {} where empno = {}".format(bsnew,up))
                        cr.execute("update calcs set monthlysal = {} where empno = {}".format(bsnew,up))
                        con.commit()
                        print(">> Details have been updated")
                        print()
                        cr.execute("select*from emp_det where empno = {}".format(up))
                        update = cr.fetchall()
                        print('-'*80)
                        print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                        print('-'*80)
                        for i in update:
                            print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                            print('-'*80)
                        print()
                        ans = input("Update more details?(y/n): ")
                        print()
                        
                    elif ch.upper()=='E':
                        otnew = float(input("Enter updated Overtime(hrs): "))
                        cr.execute("update emp_det set othours = {} where empno = {}".format(otnew,up))
                        con.commit()
                        print(">> Details have been updated")
                        print()
                        cr.execute("select*from emp_det where empno = {}".format(up))
                        update1 = cr.fetchall()
                        print('-'*80)
                        print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                        print('-'*80)
                        for i in update1:
                            print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                            print('-'*80)
                        print()
                        ans = input("Update more details?(y/n): ")
                        print()

                    elif ch.upper()=='F':
                        break

                    else:
                        print("> INVALID CHOICE, Enter again")
                        print()
            
        elif ib=='2':
            print("Current details of Employees")
            print('-'*80)
            cmd = "select*from emp_det ORDER BY empno asc"
            cr.execute(cmd)
            semp = cr.fetchall()
            print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
            print('-'*80)
            for i in semp:
                print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                print('-'*80)

            ans1='y'
            while ans1.lower()=='y':
                print()
                print("--> Updating Elements -")
                print("\ta. Basic Salary")
                print("\tb. Overtime(hrs)")
                print("\tc. Back to Menu")
                print()
                bch = input("> Enter choice: ")
                print()
                
                if bch.upper()=='A':                    
                    aos = input(">>> Add(A) or Subract(S) from data?: ")
                    print()
                    if aos.upper() == 'A':
                        while True:
                            print("Salary to be updated (between x and y)-")
                            ob1 = int(input("Starting value(x): "))
                            ob2 = int(input("Ending value(y): "))
                            print()
                            if ob1>=ob2:                            
                                print("> Starting value should be less than Ending value")
                                print()
                            else:
                                nb = int(input("Updated Salary (salary + z): "))
                                print()
                                cr.execute("select empno from emp_det where basicsal between {} and {}".format(ob1,ob2))
                                count = cr.fetchall()
                                if len(count)==0:                                
                                    print("> No records found with the condition given")
                                    print()
                                else:
                                    cr.execute("update emp_det set basicsal=basicsal+{} where basicsal between {} and {}".format(nb,ob1,ob2))
                                    cr.execute("update calcs set monthlysal=monthlysal+{} where monthlysal between {} and {}".format(nb,ob1,ob2))
                                    con.commit()
                                    print('-'*80)
                                    print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                                    print('-'*80)
                                    for j in count:
                                        cr.execute("select*from emp_det where empno = {}".format(j[0]))                                        
                                        semp1 = cr.fetchall()                                        
                                        for i in semp1:
                                            print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                                            print('-'*80)
                                    print()
                                    print(">> Details have been updated")
                                    ans1 = input("Update more details?(y/n): ")
                                    break
                            

                    elif aos.upper() == 'S':
                        while True:
                            print("Salary to be updated (between x and y)-")
                            ob1 = int(input("Starting value(x): "))
                            ob2 = int(input("Ending value(y): "))
                            print()
                            if ob1>=ob2:                            
                                print("> Starting value should be less than Ending value")
                                print()
                            else:
                                nb = int(input("Updated Salary (salary - z): "))
                                print()
                                cr.execute("select empno from emp_det where basicsal between {} and {}".format(ob1,ob2))
                                count = cr.fetchall()
                                if len(count)==0:                                
                                    print("> No records found with the condition given")
                                    print()
                                else:
                                    cr.execute("update emp_det set basicsal=basicsal-{} where basicsal between {} and {}".format(nb,ob1,ob2))
                                    cr.execute("update calcs set monthlysal=monthlysal-{} where monthlysal between {} and {}".format(nb,ob1,ob2))
                                    con.commit()
                                    print('-'*80)
                                    print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                                    print('-'*80)
                                    for j in count:
                                        cr.execute("select*from emp_det where empno = {}".format(j[0]))                                        
                                        semp1 = cr.fetchall()                                        
                                        for i in semp1:
                                            print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                                            print('-'*80)
                                    print()
                                    print(">> Details have been updated")
                                    ans1 = input("Update more details?(y/n): ")
                                    break

                    else:
                        print("> INVALID CHOICE, Enter again")

                elif bch.upper()=='B':
                    aos = input(">>> Add(A) or Subract(S) from data?: ")
                    print()
                    if aos.upper() == 'A':
                        while True:
                            print("Time(hrs) to be updated (between x and y)-")
                            ov1 = float(input("Starting value(x): "))
                            ov2 = float(input("Ending value(y): "))
                            print()

                            if ov1==ov2==0:
                                nov = float(input("Updated Overtime(+z): "))
                                print()
                                cr.execute("select empno from emp_det where othours = {}".format(0))
                                count = cr.fetchall()
                                if len(count)==0:                                    
                                    print("> No records found with the condition given")
                                    print()
                                else:
                                    cr.execute("update emp_det set othours = othours+{} where othours = {}".format(nov,0))
                                    con.commit()
                                    print('-'*80)
                                    print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                                    print('-'*80)
                                    for j in count:
                                        cr.execute("select*from emp_det where empno = {}".format(j[0]))                            
                                        semp1 = cr.fetchall()                                        
                                        for i in semp1:
                                            print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                                            print('-'*80)
                                    print()
                                    print(">> Details have been updated")
                                    ans1 = input("Update more details?(y/n): ")
                                    break
                                
                            elif ov1>=ov2:                                
                                print("> Starting value should be less than Ending value")
                                print()
                                
                            else:
                                nov = float(input("Updated Overtime(+z): "))
                                print()
                                cr.execute("select empno from emp_det where othours between {} and {}".format(ov1,ov2))
                                count = cr.fetchall()
                                if len(count)==0:
                                    print()
                                    print("> No records found with the condition given")
                                else:
                                    cr.execute("update emp_det set othours = othours+{} where othours between {} and {}".format(nov,ov1,ov2))
                                    con.commit()
                                    print('-'*80)
                                    print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                                    print('-'*80)
                                    for j in count:
                                        cr.execute("select*from emp_det where empno = {}".format(j[0]))                            
                                        semp1 = cr.fetchall()                                    
                                        for i in semp1:
                                            print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                                            print('-'*80)
                                    print()
                                    print(">> Details have been updated")
                                    ans1 = input("Update more details?(y/n): ")
                                    break

                    elif aos.upper()=='S':
                        while True:
                            print("Time(hrs) to be updated (between x and y)-")
                            ov1 = float(input("Starting value(x): "))
                            ov2 = float(input("Ending value(y): "))
                            print()

                            if ov1==ov2==0:
                                print("> The value Zero cannot be subtracted further, Enter valid number")
                                print()                                                       
                    
                            elif ov1>=ov2:
                                print()
                                print("> Starting value should be less than Ending value")
                                
                            else:
                                while True:
                                    nov = float(input("Updated Overtime(-z): "))
                                    print()
                                    if nov>ov1:
                                        print("> Time to be subtracted(z) should be less than starting value(x)")
                                        print()

                                    else:                                    
                                        cr.execute("select empno from emp_det where othours between {} and {}".format(ov1,ov2))
                                        count = cr.fetchall()
                                        if len(count)==0:
                                            print()
                                            print("> No records found with the condition given")
                                        else:
                                            cr.execute("update emp_det set othours = othours-{} where othours between {} and {}".format(nov,ov1,ov2))
                                            con.commit()
                                            print('-'*80)
                                            print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                                            print('-'*80)
                                            for j in count:
                                                cr.execute("select*from emp_det where empno = {}".format(j[0]))                            
                                                semp1 = cr.fetchall()                                                
                                                for i in semp1:
                                                    print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                                                    print('-'*80)
                                            print()
                                            print(">> Details have been updated")
                                            ans1 = input("Update more details?(y/n): ")
                                            break
                                    break
                            break
                    else:
                        print("> INVALID CHOICE, Enter again")

                elif bch.upper()=='C':
                    break

                else:
                    print("> INVALID CHOICE, Enter again")

        elif ib=='3':
            print("Deleting Records:-")
            print()
            print("Current Records-")
            print('-'*80)            
            cr.execute("select*from emp_det ORDER BY empno asc")
            semp2 = cr.fetchall()
            print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
            print('-'*80)
            for i in semp2:
                print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                print('-'*80)

            ans2='y'
            while ans2.lower()=='y':
                print()
                print("--> Deleting Elements -")
                print("\ta. Individual Delete")
                print("\tb. Delete numerous records")
                print("\tc. Back to Menu")
                print()
                bch = input("> Enter choice: ")
                print()
                
                if bch.upper()=='A':
                    di = int(input("Emp no. to be deleted: "))
                    print()
                    cr.execute("select count(empno) from emp_det where empno = {}".format(di))
                    emcount = cr.fetchall()
                    if emcount[0][0]==0:
                        print("> No record(s) found")
                        print()
                    else:   
                        cr.execute("delete from emp_det where empno = {}".format(di))
                        cr.execute("delete from calcs where empno = {}".format(di))
                        con.commit() 
                        print(">> Record has been deleted")
                        print()
                        ans2 = input("Delete more records?(y/n): ")

                        if ans2=='n':
                            print()
                            print("Updated Records-")
                            print('-'*80)            
                            cr.execute("select*from emp_det ORDER BY empno asc")
                            semp2 = cr.fetchall()
                            print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                            print('-'*80)
                            for i in semp2:
                                print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                                print('-'*80)

                elif bch.upper()=='B':
                    a1='y'
                    while a1.lower()=='y':
                        print("   --> Delete numerous records-")
                        print("\t1. Based on Salary")
                        print("\t2. Based on Overtime hours")
                        print("\t3. Back to Menu")
                        print()
                        de = input("> Enter choice: ")
                        print()

                        if de=='1':
                            while True:
                                print("On basis of Salary(between x and y)-")                            
                                ob1 = int(input("Starting value(x): "))
                                ob2 = int(input("Ending value(y): "))
                                print()
                                if ob1>=ob2:                                    
                                    print("> Starting value should be less than Ending value")
                                    print()
                                else:
                                    cr.execute("select count(empno) from emp_det where basicsal between {} and {}".format(ob1,ob2))
                                    num = cr.fetchone()
                                    cr.execute("select empno from emp_det where basicsal between {} and {}".format(ob1,ob2))
                                    count = cr.fetchall()
                                    if len(count)==0:
                                        print("> No records found with the condition given")
                                        print()
                                    else:
                                        cr.execute("delete from emp_det where basicsal between {} and {}".format(ob1,ob2))                                                                               
                                        cr.execute("delete from calcs where monthlysal between {} and {}".format(ob1,ob2))
                                        con.commit() 
                                        print(">>",num[0],"Record(s) have been deleted")
                                        print()
                                        a1 = input("Delete more records?(y/n): ")
                                        print()
                                        break

                        elif de=='2':
                            while True:
                                print("On basis of Overtime hours (between x and y)-")
                                ov1 = float(input("Starting value(x): "))
                                ov2 = float(input("Ending value(y): "))                        

                                if ov1==ov2==0:
                                    cr.execute("select empno from emp_det where othours = {}".format(0))
                                    count = cr.fetchall()
                                    if len(count)==0:
                                        print("> No records found with the condition given")
                                        print()
                                    else:
                                        cr.execute("select count(empno) from emp_det where othours = {}".format(0))
                                        num = cr.fetchone()
                                        cr.execute("select empno from emp_det where othours = {}".format(0))
                                        dc = cr.fetchall()
                                        L = []
                                        for i in dc:                              
                                            L.append(i[0])
                                        cr.execute("delete from emp_det where othours = {}".format(0))
                                        con.commit()
                                        for j in L:
                                            cr.execute("delete from calcs where empno= {}".format(j))
                                            con.commit() 
                                        print(">>",num[0],"Record(s) have been deleted")
                                        print()
                                        a1 = input("Delete more records?(y/n): ")
                                        break

                                elif ov1>=ov2:                                    
                                    print("> Starting value should be less than Ending value")
                                    print()
                                    
                                else:                                    
                                    cr.execute("select empno from emp_det where othours between {} and {}".format(ov1,ov2))
                                    count = cr.fetchall()
                                    if len(count)==0:
                                        print("> No records found with the condition given")
                                        print()
                                    else:
                                        cr.execute("select count(empno) from emp_det where othours between {} and {}".format(ov1,ov2))
                                        num = cr.fetchone()
                                        cr.execute("select empno from emp_det where othours between {} and {}".format(ov1,ov2))
                                        dc = cr.fetchall()
                                        L = []
                                        for i in dc:                              
                                            L.append(i[0])
                                        cr.execute("delete from emp_det where othours between {} and {}".format(ov1,ov2))
                                        con.commit()
                                        for j in L:
                                            cr.execute("delete from calcs where empno= {}".format(j))
                                            con.commit() 
                                        print(">>",num[0],"Record(s) have been deleted")
                                        print()
                                        a1 = input("Delete more records?(y/n): ")
                                        break

                        elif de=='3':
                            break

                        else:
                            print("> INVALID CHOICE, Enter again")
                            print()

                    if a1=='n':                        
                        print("Updated Records-")
                        print('-'*80)            
                        cr.execute("select*from emp_det ORDER BY empno asc")
                        semp2 = cr.fetchall()
                        print("EMP NO.\t AGE\tGENDER\t BASIC SALARY\tOVERTIME(hrs)\t|\tNAME")
                        print('-'*80)
                        for i in semp2:
                            print('  ',i[0],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t\t|',i[1])
                            print('-'*80)
                           
                elif bch.upper()=='C':
                    break

                else:
                    print("> INVALID CHOICE, Enter again")

        elif ib=='4':
            break

        else:
            print("> INVALID CHOICE, Enter again")            

#------------------------------------------------------------------------------------------------------

#CALCULATING DETAILS
def calc_det():
    cr.execute("select empno,basicsal,othours from emp_det order by empno asc")
    cc = cr.fetchall()    
    mso = []
    for i in cc:        
        mso+=[[i[0],i[1],i[2]]]
        #hourly salary = monthly sal/240
        #overtime charges = ovetimehrs*1.5*hourly
        
    #overtime charges
    for j in mso:
        hs = j[1]/240
        otch = j[2]*1.5*hs           
        cr.execute("update calcs set otcharges={} where empno={} order by empno".format(otch,j[0]))
        con.commit()
        
    #gross pay
    for j in mso:
        hs = j[1]/240
        otch = j[2]*1.5*hs
        gpay = otch+j[1]
        cr.execute("update calcs set grosspay={} where empno={} order by empno".format(gpay,j[0]))
        con.commit()
        
    #deductions
    for j in mso:
        hs = j[1]/240
        otch = j[2]*1.5*hs
        gpay = otch+j[1]
        ESI = (0.75/100)*gpay
        PF = (0.12)*gpay
        ded = ESI + PF
        cr.execute("update calcs set deducts={} where empno={} order by empno".format(ded,j[0]))
        con.commit()
        
    #net pay
    for j in mso:
        hs = j[1]/240
        otch = j[2]*1.5*hs
        gpay = otch+j[1]
        ESI = (0.75/100)*gpay
        PF = (0.12)*gpay
        ded = ESI + PF
        net = gpay - ded
        cr.execute("update calcs set netpay={} where empno={} order by empno".format(net,j[0]))
        con.commit()

    cr.execute("select count(empno) from calcs")
    empco = cr.fetchall()

    print();print(' - '*40),print()
    print("Calculating Employee Salary...")    
    print()
    print('-'*120)
    cmd = "select*from calcs ORDER BY empno asc"
    cr.execute(cmd)
    semp = cr.fetchall()

    #display
    print("EMP NO.\t MONTHLY SALARY\t OVETIME CHARGES\t GROSSPAY\t DEDUCTS\t NET PAY\t|\tNAME")
    print('-'*120)
   
    for i in semp:
        print(' ',i[0],'\t',i[2],'\t',i[3],'\t\t\t',i[4],'\t',i[5],'\t',i[6],'\t|\t',i[1])
        print('-'*120)

    print()
    print("Total no. of results = ",empco[0][0])
    print()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

while True:
    print('='*120)
    print()
    print("EMPLOYEE DETAILS:-")
    print("1. Enter Employee details")
    print("2. View Employee details")
    print("3. Update Employee details")
    print("4. Calculations")
    print("5. Exit") 
    print()
    op = int(input("> Enter choice: "))

    if op == 1:
        enter_det()

    elif op == 2:
        view_det()

    elif op == 3:
        update_det()

    elif op == 4:
        calc_det()        

    elif op == 5:
        print()
        print(">> EXITING PROGRAM")
        break
    
    else:
        print("> INVALID CHOICE, Enter again")
