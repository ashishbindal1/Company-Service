print("Welcome to Bindal Group of Industries Pvt. Ltd.")
print("Please press 1.)For Salary Collection & 2.)For other Servies")
x=0
while x==0:
    sc=input()
    c=len(sc)
    while c!=1:
        print("You have entered an invalid Service Input. Please Enter a valid Service Input")
        print("Please enter 1.)For Salary Collection & 2.)For other Servies")
        break
    while c==1:
        for ckr in sc:
            try:
                dr=int(ckr)
                x=dr
                c=0
                if(x==0):
                    print("You have entered an invalid Service Input. Please Enter a valid Service Input")
                    print("Please enter 1.)For Salary Collection & 2.)For other Servies")
            except:
                c=0
                print("You have entered an invalid Service Input. Please Enter a valid Service Input")
                print("Please enter 1.)For Salary Collection & 2.)For other Servies")
                break
     while x>2:
        x=0
        print("You have entered an invalid Service Input. Please Enter a valid Service Input")
        print("Please enter 1.)For Salary Collection & 2.)For other Servies")
        break
while x==1:
    print("To collect your Salary Plz follow the Instuctions...")
    print("Please Enter Your Name")
    nam = input()
    kty=""
    for let in nam:
        try:
            k=int(let)
            print("Enter a Valid Name")
            break
        except:
            kty=kty+let
    if kty == 'Ashish Singh Bindal':
        print("Welcome Mr. Owner")
        trn = input("Please Enter Turnover of this month: $")
        trnovr = float(trn)
        print("Your Salary: $", trnovr)
        print("Please Press 1.)To transfer Salary to Account & 2.)To Exit")
        inp = input()
        acc = int(inp)

        if acc==1:
            print("Amount of $",trnovr, "will be Transferred to your Linked Bank Account in 24 hours. In case of any discrepancy Please Contact Your Bank")
            break

        elif acc==2:
            print("Transaction cancelled")
            break

        elif acc<1 or acc>2:
            print("Please Enter a Valid Service Input")
            continue

    elif nam == kty:
        hours = input("Enter Your Company Working Hours For this Month: ")

        try:
            hrs = float(hours)

        except:
            print("Please Enter a valid Number input")

        rte = 20.50

        if hrs<=40:
            pay = hrs*rte
            print("Employee Name: Mr./Mrs. ",nam)
            print("Gross Salary = $",pay)

        elif hrs>40:
            hrs = hrs-40
            pay = (40*rte)+(hrs*rte*5.5)
            print("Employee Name: ",nam)
            print("Gross Salary = $",pay)

        print("Facility Charges Deducted = $30")
        pay = pay-30
        print("Net Salary = $",pay)
        print("Amount of $",pay, "will be Transferred to your Linked Bank Account in 24 hours. In case of any discrepancy Please Contact Your Company")
        break

while x == 2:
    print("Welcome to Company Help Desk service")
    print("Please Enter your name")
    nme = input()
    ght=""
    for ckr in nme:
        try:
            vbd=int(ckr)
            print("Enter Valid Name")
            break
        except:
            ght=ght+ckr
    if ght==nme:
        print("Please Press 3.)To Fix a meeting with owner, 4.)To Have a Mobile Conversation with owner, 5.)To Resign the Company, 6.)To Send a Resume to the Company")
        src = input()
        y = int(src)

        if y == 3:
            print("For the Reason Please Press 1.)For Business Deal & 2.)For General Problems")
            sei = input()
            z = int(sei)

            if z == 1:
                print("Please Enter Time between 9:00 A.M and 11:00 A.M in the format 'hh mm'")
                hrs, mints = input().split()
                hrs = int(hrs)
                mints = int(mints)
                if hrs<9 or hrs>11:
                    print("oops! Your meeting hours are not available. Please Re-Enter Time hours between 9 TO 11")
                    continue
                elif mints>60:
                    print("oops! Your meeting hours are not available. Please Re-Enter Time hours between 9 TO 11")
                    continue
                else:
                    print("Mr./Mrs.",ght,"Your Meeting has been fixed on Friday at ",hrs,":",mints,"A.M")
                    print("Wish You All the Best")
                    break

            elif z == 2:
                print("Please Write to the owner describing your greivances on his personal mail")
                break

        elif y == 4:
            print("Call the owner on His personal mobile number: +918279431119")
            break

        elif y == 5:
            print("Write to the owner explaining the reason to resign on his personal mail: ashishbindal169@gmail.com")
            break

        elif y== 6:
            print("Send your resume n documents copy to Owner on his mail: ashishbindal169@gmail.com")
            break

        elif y<3 or y>6:
            print("Enter Valid Service Input")
            continue

while x<1 or x > 2:
    print("Please Enter a valid Service Input")
    break

print("Thank You")
print("Authorized Signatory : Ashish Singh Bindal(Owner Bindal Group)")
