print("Welcome To Average Grade Pointer App")
MDC = EG = PF = FESD = ECSE = IDT = AOC = MITT = 0
UserMarks=[MDC,EG,PF,FESD,ECSE,IDT,AOC,MITT]
MDC=int(input("Enter your MDC marks out of 150"))
EG=int(input("Enter your EG marks out of 150"))
PF=int(input("Enter your PF marks out of 200"))
FESD=int(input("Enter your FESD marks out of 150"))
ECSE=int(input("Enter your ECSE marks out of 100"))
IDT=int(input("Enter your IDT marks out of 50"))
AOC=int(input("Enter yout AOC marks out of 100"))
MITT=int(input("Enter your MITT marks out of 100"))

MDCcent=(MDC/150)*100
EGcent=(EG/150)*100
PFcent=(PF/200)*100
FESDcent=(FESD/150)*100
ECSEcent=(ECSE/100)*100
IDTcent=(IDT/50)*100
AOCcent=(AOC/100)*100
MITTcent=(MITT/100)*100

UserMarkscent=[MDCcent,EGcent,PFcent,FESDcent,ECSEcent,IDTcent,AOCcent,MITTcent]

MDCgrpointer,EGgrpointer,PFgrpointer,FESDgrpointer,ECSEgrpointer,IDTgrpointer,AOCgrpointer,MITTgrpointer=0

UserGrPointer=[MDCgrpointer,EGgrpointer,PFgrpointer,FESDgrpointer,ECSEgrpointer,IDTgrpointer,AOCgrpointer,MITTgrpointer]
for items in UserMarkscent:
    if items>=85:
        for items in UserGrPointer:
            if UserGrPointer[items]==UserMarkscent[items]:
                UserGrPointer[items]=10
    if 84>items and items>80:
        for items in UserGrPointer:
            if UserGrPointer[items]==UserMarkscent[items]:
                UserGrPointer[items]=9
    if 79>items and items>=70:
        for items in UserGrPointer:
            if UserGrPointer[items]==UserMarkscent[items]:
                UserGrPointer[items]=8
    if 69>items and items>=60:
       for items in UserGrPointer:
            if UserGrPointer[items]==UserMarkscent[items]:
                UserGrPointer[items]=7
    if 59>items and items>=50:
        for items in UserGrPointer:
            if UserGrPointer[items]==UserMarkscent[items]:
                UserGrPointer[items]=6
    if 49>items and items>=45:
        for items in UserGrPointer:
            if UserGrPointer[items]==UserMarkscent[items]:
                UserGrPointer[items]=5
    if 44>items and items>=40:
        for items in UserGrPointer:
            if UserGrPointer[items]==UserMarkscent[items]:
                UserGrPointer[items]=4
    if 40>items:
        for items in UserGrPointer:
            if UserGrPointer[items]==UserMarkscent[items]:
                UserGrPointer[items]=0


Sgpa=(MDCgrpointer*3+EGgrpointer*3+PFgrpointer*4+FESDgrpointer*4+ECSEgrpointer*2+IDTgrpointer+AOCgrpointer*2+MITTgrpointer*2)/20
