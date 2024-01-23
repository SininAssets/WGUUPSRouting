#Student ID: 010508147
#Student Name: Ilia Shcherbinin
#Enjoy The Program

import csv
import Truck


import datetime

#Potential Future expansions are of the following
#Make the program recursive, meaning it can last forever until user ends
#The current program is just a snapshot of what it can be.
#Another Potential Expansion is allowing user to interact better by writting words
#Reason it was not implemented was due to the short time frame.



def PrintLIne():
    if not hasattr(PrintLIne,'Printed'):
        print("-------------------------------------------")
    PrintLIne.Printed = True


#This loads the CSV file into a variable
#This is needed for putting the Data from CSV
#To the AddressLoaded Variable
with open("C:\\Users\\Ilias\\OneDrive\\Desktop\\C950 Pass\\DSA 2-Ilia\\CSV\\Destinations.csv") as AddressCSV:
    AddressLoaded = list(csv.reader(AddressCSV, delimiter = ','))
#This loads Distances from CSV to the Distance Loaded Variable
with open("C:\\Users\\Ilias\\OneDrive\\Desktop\\C950 Pass\\DSA 2-Ilia\\CSV\\DrivingDistances.csv") as DistanceCSV:
    DistanceLoaded = list(csv.reader(DistanceCSV, delimiter =','))



#This is basically the first window
#This GUI will allow user multiple options
#The options are viewing all packages,Select or Total Miles
#Additionally Theres an option to quit
WGUPSControls = input("""-------------------------------------------
Western Governors University Parcel Service
-------------------------------------------
To Navigate the WGUPS system select an option from Below:"
1: View All Packages 
2: View Select Package
3: View Total Miles
4: Quit
Enter Your Option: """""

)
#This basically said as long as user didn't select 4
#It will continue the program
#if 4 Is selected the program will simply end
while WGUPSControls != '4':
    #If user selects 1 to view all packages this portion of program will activate
    if WGUPSControls == '1':
        #If 1 is selected is It will send a prompt to enter Time
        TimeInput = input("""
-------------------------------------------
Please enter current time here (HH:MM):""")
        #This part of Code basically processes User input of the time
        (Hour, Minute) = TimeInput.split(":")
        TimeChanges = datetime.timedelta(hours=int(Hour), minutes=int(Minute))
        #Once it processes it It will go through all the 40 packages
        for PackageID in range(1, 41):
            from Packages import PackageHashTable
            totalPackage = PackageHashTable.HashTableSearch(PackageID)
            totalPackage.PackageStatusTotal(TimeChanges)
            print(str(totalPackage))
            #This part of section allows the User to continue Browsing with multiple options
            #Its very complex, but in short it allows the user to continue looking at General Search at
            #A different time or Start Lookiing at a package with a specific ID
            #Additionally there is an option to just simply exit
        ExitInput = input(""""
-------------------------------------------
Choose an option?
Enter 1 for Exit
Enter 2 for Continue General Search
Enter 3 for a Specific Package
Input: """)
        if ExitInput == '1':
            exit()
        if ExitInput == '3':
            TimeInput = input("""
-------------------------------------------
Please enter current time here (HH:MM):""")

        (Hour, Minute) = TimeInput.split(":")
        TimeChanges = datetime.timedelta(hours=int(Hour), minutes=int(Minute))
        try:
            PackageInput = [int(input("Please Enter Package ID Here:"))]

        except ValueError:
            PackageInput = range(1, 41)
        for PackageID in PackageInput:
            from Packages import PackageHashTable
            totalPackage = PackageHashTable.HashTableSearch(PackageID)
            totalPackage.PackageStatusTotal(TimeChanges)
            print(str(totalPackage))
            exit()
     #This part of code triggers when the user types in 2 It will ask for Time
    #And later Package ID
    if WGUPSControls == '2':
        TimeInput = input("""
-------------------------------------------
Please enter current time here (HH:MM):""")

        (Hour, Minute) = TimeInput.split(":")
        TimeChanges = datetime.timedelta(hours=int(Hour), minutes=int(Minute))
        try:
            PackageInput = [int(input("Please Enter Package ID Here:"))]

        except ValueError:
            PackageInput = range(1, 41)
        for PackageID in PackageInput:
            from Packages import PackageHashTable
            totalPackage = PackageHashTable.HashTableSearch(PackageID)
            totalPackage.PackageStatusTotal(TimeChanges)
            print(str(totalPackage))
            #Once it provided results it also allows for continuation or an exit.
        EndProgramInput =[int(input(""""
-------------------------------------------
Choose an option?
Enter 1 for Exit
Enter 2 for Continue Specific Search
Enter 3 for a General Search
Input: """))]
        if EndProgramInput == '1':
            exit()
        if EndProgramInput == '3':
            TimeInput = input("""
-------------------------------------------
Please enter current time here (HH:MM):""")

        (Hour, Minute) = TimeInput.split(":")
        TimeChanges = datetime.timedelta(hours=int(Hour), minutes=int(Minute))

        for PackageID in range(1, 41):
            from Packages import PackageHashTable
            totalPackage = PackageHashTable.HashTableSearch(PackageID)
            totalPackage.PackageStatusTotal(TimeChanges)
            print(str(totalPackage))
    #Finally if 3 is selected It will print Total Miles
    #Unfortunately the continuation feature is experimental
    #so it has been removed
    if WGUPSControls == '3':
        from Truck import TotalMilesT
        PrintLIne()
        TotalMilesT()
    #If user types anything outside the numbers 1-4
    #It will print Invalid Input and end the program
    else:
        print("Invalid Input")
        exit()
