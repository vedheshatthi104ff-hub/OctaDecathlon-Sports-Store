from tabulate import tabulate
import mysql.connector as e
f=e.connect(host='localhost',user='root',passwd='root')
m=f.cursor()
m.execute('use octodecathlon')
def update():
    ab=0
    while ab==0:
        g=input('Enter the sport you want to update')
        head=['Item id','Item Name','Brand','Item Type','Stock Availability','Price']
        m.execute("select * from %s "%(g))
        ht=m.fetchall()
        print(tabulate(ht,headers=head,tablefmt='fancy_grid'))
        h=int(input('enter the item id you want to update'))
        i=input('enter the field you want to update')
        ij=['Price','item_id']
        if i not in ij:
            j=input('Enter the correct value to be added')
            m.execute("update %s set %s='%s' where item_id='%d'"%(g,i,j,h))
            f.commit()
            print('Succesfully updated')
            
        else:
            j=int(input('Enter the correct value to be added'))
            m.execute("update %s set %s='%d' where item_id='%d'"%(g,i,j,h))
            f.commit()
            print('Succesfully updated')
        ab=int(input('do you want to continue Updating\n 0:yes\n 1:no'))
        
def delete():
    aa=0
    while aa==0:
        sp=input('enter the sport you want to delete the item from')
        head1=['Item id','Item Name','Brand','Item Type','Stock Availability','Price']
        m.execute("select * from %s"%(sp))
        ht1=m.fetchall()
        print(tabulate(ht1,headers=head1,tablefmt='fancy_grid'))
        iid=int(input('enter the item id you want to delete'))
        m.execute("delete from %s where item_id='%d'"%(sp,iid))
        f.commit()
        print('Succesfully Deleted')
        aa=int(input('do you want to continue Deleting\n 0:yes\n 1:no'))

def add():
    bb=0
    while bb==0:
        bsp=input('enter the sport you want to add the item to:')
        head2=['Item id','Item Name','Brand','Item Type','Stock Availability','Price']
        m.execute("select * from %s "%(bsp))
        ht2=m.fetchall()
        print(tabulate(ht2,headers=head2,tablefmt='fancy_grid'))
        bbb=0
        while bbb==0:
            bi=int(input('Enter the item id'))
            bn=input('enter the item name')
            br=input('enter the brand name')
            bt=input('Enter the item type')
            bs=input('enter the stock availability')
            bp=float(input('Enter the price with two numbers after decimal point'))
            m.execute("insert into %s values('%d','%s','%s','%s','%s','%d')"%(bsp,bi,bn,br,bt,bs,bp))
            f.commit()
            print('Succesfully added')
            bbb=int(input('do you want to continue adding in the same sport\n 0:yes\n 1:no'))
        bb=int(input('do you want to continue adding \n 0:yes\n 1:no'))

def check():
    cc=0
    while cc==0:
        cy=int(input('Do you want to check purchases of specific customer\n 1:yes\n 2:no'))
        head4=['Customer id','Customer Name','Item id','Sport','Date of purchase','Payment method']
        if cy==1:
            cy1=input('Enter customer id you are looking for')
            m.execute("select * from Order_history where customer_id='%s'"%(cy1))
            abc=m.fetchall()
            print(tabulate(abc,headers=head4,tablefmt='fancy_grid'))
        else:
            m.execute("select * from Order_history")
            abc1=m.fetchall()
            print(tabulate(abc1,headers=head4,tablefmt='fancy_grid'))
        cc=int(input('Do you want to continue Checking\n 0:Yes\n 1:No'))

def Filter():
    QQ=0
    while QQ==0:
        Q=int(input('Enter the item type you are looking for\n 0:Equipment\n 1:Jersey\n 2:Kit\nEnter your choice'))
        head5=['Item id','Item Name','Brand','Item Type','Stock Availability','Price']
        if Q==0:
            m.execute('select * from %s where item_type="Equipment"'%(A))
            Q1=m.fetchall()
            print(tabulate(Q1,headers=head5,tablefmt='fancy_grid'))
            break
        elif Q==1:
            m.execute('select * from %s where item_type="Jersey"'%(A))
            Q2=m.fetchall()
            print(tabulate(Q2,headers=head5,tablefmt='fancy_grid'))
            break
        elif Q==2:
            m.execute('select * from %s where item_type="Kit"'%(A))
            Q3=m.fetchall()
            print(tabulate(Q3,headers=head5,tablefmt='fancy_grid'))
            break
        else:
            print('Enter appropriate value')
def table():
    m.execute("select * from %s"%(A))
    headd=['Item id','Item Name','Brand','Item Type','Stock Availability','Price']
    xyz=m.fetchall()
    print(tabulate(xyz,headers=headd,tablefmt='fancy_grid'))

def purchase():
    vk=1
    while vk==1:
        #table()
        z=int(input('Enter the item id you want to buy'))
        m.execute("select * from %s where item_id='%d'"%(A,z))
        z1=m.fetchall()
        su=z1[0]
        kk=float(su[5])
        ab1=kk+(0.10*kk)
        price=ab1-(ab1*0.05)
        print('Your total will be:',price)
        z2=int(input('Do you want to continue the payment\n 0:Yes\n 1:no\n enter your choice:'))
        if z2==0:
               name=input('Enter your name')
               num=input('Enter you Phone number')
               dat=input('Enter date of purchase in yyyy-mm-dd format')
               paym=input('Enter the method of payment')
               m.execute("insert into Order_history values('%s','%s','%d','%s','%s','%s')"%(num,name,z,A,dat,paym))
               f.commit()
               #(customer_id,Name,itemid_bought,Sport,Date_of_Purchace,Payment_method)
               print('Succesfully ordered')
               vk=int(input('Do you want to continue buying in the same sport\n 1:yes\n 0:no\n enter your choice:'))
               
def check_history():
    numb=input('Enter your number which is used for your purchases')
    headd4=['Customer id','Customer Name','Item id','Sport','Date of purchase','Payment method']
    m.execute("select * from Order_history where customer_id='%s'"%(numb))
    chy=m.fetchall()
    print(tabulate(chy,headers=headd4,tablefmt='fancy_grid'))

def tq():
    print('|--------------------------------------------------------------------------------------------|')
    print('|-------------------------------------THANK YOU----------------------------------------------|')
    print('|---------------------------------SHOPPING WITH US-------------------------------------------|')
    print('|--------------------------------------------------------------------------------------------|')
    
           
    
def interface():
    print('|--------------------------------------------------------------------------------------------|')
    print('|------------------------------------WELCOME TO----------------------------------------------|')
    print('|----------------------------OCTODECATHLON SPORTS STORE--------------------------------------|')
    print('|--------------------------------------------------------------------------------------------|')
    print('welcome to octodecathlon sports store')
    print('our shop provides items related to following sports:\n 1:Cricket\n 2:Football\n 3:Basketball\n 4:Volleyball\n 5:Racing\n 6: Check Your Previous Purchases\n 0:Exit')
    

    
b=int(input('you are here as:\n 1:Manager\n 2:Customer\n enter your choice:'))
if b==1:
    while True:
        c=input('press 0 to go to customer\n enter password:')
        if c=='root':
            while True:
                d=int(input('Welcome do you want to:\n 1:Update\n 2:Delete\n 3:Add\n 4:Check Purchases\n 5:Exit\n enter your choice:'))
                if d==1:
                    update()
                   
                elif d==2:
                    delete()
                    
                elif d==3:
                    add()
                    
                elif d==4:
                    check()
                elif d==5:
                    break
                else:
                    print('enter related input')
        elif c=='0':
            break
        else:
            print('wrong password')
while True:
    interface()
    head6=['Item id','Item Name','Brand','Item Type','Stock Availability','Price']
    a=int(input("enter the number respected to the sport's item you are looking for:"))
    if a==1:
        m.execute('select * from Cricket')
        AB=m.fetchall()
        print(tabulate(AB,headers=head6,tablefmt='fancy_grid'))
        A='Cricket'
        AbC=int(input('Do you want to filter\n 0:Yes\n 1:no\n enter your choice:'))
        if AbC==0:
            Filter()
        purchase()
        tq()
        
    elif a==2:
        m.execute('select * from Football')
        AB=m.fetchall()
        print(tabulate(AB,headers=head6,tablefmt='fancy_grid'))
        A='Football'
        AbC=int(input('Do you want to filter\n 0:Yes\n 1:no\n enter your choice:'))
        if AbC==0:
            Filter()
        purchase()
        tq()
        
    elif a==3:
        m.execute('select * from Basketball')
        AB=m.fetchall()
        print(tabulate(AB,headers=head6,tablefmt='fancy_grid'))
        A='Basketball'
        AbC=int(input('Do you want to filter\n 0:Yes\n 1:no\n enter your choice:'))
        if AbC==0:
            Filter()
        purchase()
        tq()
        
    elif a==4:
        m.execute('select * from Volleyball')
        AB=m.fetchall()
        print(tabulate(AB,headers=head6,tablefmt='fancy_grid'))
        A='Volleyball'
        AbC=int(input('Do you want to filter\n 0:Yes\n 1:no\n enter your choice:'))
        if AbC==0:
            Filter()
        purchase()
        tq()
        
    elif a==5:
        m.execute('select * from Motor_Sport')
        AB=m.fetchall()
        print(tabulate(AB,headers=head6,tablefmt='fancy_grid'))
        A='Motor_Sport'
        AbC=int(input('Do you want to filter\n 0:Yes\n 1:no\n enter your choice:'))
        if AbC==0:
            Filter()
        purchase()
        tq()
        
    elif a==6:
        check_history()
      #  break
    elif a==0:
        tq()
        break
        
    else:
        print('enter related value')
