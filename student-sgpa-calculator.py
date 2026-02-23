print("Welcome To Average Grade Pointer App")

#Inputing marks per subject from user
MDC=float(input("Enter your MDC marks out of 150:"))
EG=float(input("Enter your EG marks out of 150:"))
PF=float(input("Enter your PF marks out of 200:"))
FESD=float(input("Enter your FESD marks out of 150:"))
ECSE=float(input("Enter your ECSE marks out of 100:"))
IDT=float(input("Enter your IDT marks out of 50:"))
AOC=float(input("Enter yout AOC marks out of 100:"))
MITT=float(input("Enter your MITT marks out of 100:"))

UserMarks=[MDC,EG,PF,FESD,ECSE,IDT,AOC,MITT] #Adding it to a list if user needs only marks

print(UserMarks) #Prints marks

#Calculating percentage per  subject for Users marks
MDCcent=(MDC/150)*100
EGcent=(EG/150)*100
PFcent=(PF/200)*100
FESDcent=(FESD/150)*100
ECSEcent=(ECSE/100)*100
IDTcent=(IDT/50)*100
AOCcent=(AOC/100)*100
MITTcent=(MITT/100)*100

UserMarkscent=[MDCcent,EGcent,PFcent,FESDcent,ECSEcent,IDTcent,AOCcent,MITTcent]  #Adding it to a list if user needs only Percent

print(UserMarkscent) #Prints percent per subject

#Creating a list with 0's, no of 0's in the list is equal to the number of subjects
UserGrPointer=[] 

#Accesing each index in the UserGrPointer list to assign equivalent Grade pointer
for i, marks in enumerate(UserMarkscent):

    if marks >= 85:
        UserGrPointer.append(10)
    elif marks >= 80:
        UserGrPointer.append(9)
    elif marks >= 70:
        UserGrPointer.append(8)
    elif marks >= 60:
        UserGrPointer.append(7)
    elif marks >= 50:
        UserGrPointer.append(6)
    elif marks >= 45:
        UserGrPointer.append(5)
    elif marks >= 40:
        UserGrPointer.append(4)
    else:
        UserGrPointer.append(0)

print(UserGrPointer) #prints Grade pointer for each subject

#Formula for calculating SGPA
SGPA=(UserGrPointer[0]*3+UserGrPointer[1]*3+UserGrPointer[2]*4+UserGrPointer[3]*3+UserGrPointer[4]*2+UserGrPointer[5]*1+UserGrPointer[6]*2+UserGrPointer[7]*2)/20


print(SGPA) #Prints SGPA

