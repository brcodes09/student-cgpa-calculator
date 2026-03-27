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

#Calculating Credits
Credits = []

for subject in SubjectMarks:
    for marks_obtained, total_marks in SubjectMarks[subject].items():
        credit = total_marks / 50
        Credits.append(credit)

print(Credits)


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