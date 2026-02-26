print("Welcome To Average Grade Pointer App")

NoofSub=int(input("How many subjects do you have this semester?:"))

SubjectMarks={}


for i in range(NoofSub):
    Subject=input(f"Enter the name of the subject {i+1}:")
    Marks={
        float(input(f"Enter the marks of {Subject}:")):
    int(input(f"Enter the Total marks of {Subject}:"))
    }
    SubjectMarks[Subject]=Marks
    
print(SubjectMarks)

Credits=[]

#Calculating Credits(needs fix)
for i in range(NoofSub):
    Credits[i]=SubjectMarks[Subject][Marks]/50

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
UserGrPointer=[0,0,0,0,0,0,0,0] 

#Accesing each index in the UserGrPointer list to assign equivalent Grade pointer
for i, marks in enumerate(UserMarkscent):

    if marks >= 85:
        UserGrPointer[i] = 10
    elif marks >= 80:
        UserGrPointer[i] = 9
    elif marks >= 70:
        UserGrPointer[i] = 8
    elif marks >= 60:
        UserGrPointer[i] = 7
    elif marks >= 50:
        UserGrPointer[i] = 6
    elif marks >= 45:
        UserGrPointer[i] = 5
    elif marks >= 40:
        UserGrPointer[i] = 4
    else:
        UserGrPointer[i] = 0

print(UserGrPointer) #prints Grade pointer for each subject

#Formula for calculating SGPA
SGPA=(UserGrPointer[0]*3+UserGrPointer[1]*3+UserGrPointer[2]*4+UserGrPointer[3]*3+UserGrPointer[4]*2+UserGrPointer[5]*1+UserGrPointer[6]*2+UserGrPointer[7]*2)/20


print(SGPA) #Prints SGPA