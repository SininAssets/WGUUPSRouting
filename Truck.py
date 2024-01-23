import csv
import datetime

import CircularImportGoAround

import Packages

#It is in this file as well in order to prevent Circular Import Error
#Basically Loads Data into the Address loaded from CSV
with open("C:\\Users\\Ilias\\OneDrive\\Desktop\\C950 Pass\\DSA 2-Ilia\\CSV\\Destinations.csv") as AddressCSV:
    AddressLoaded = list(csv.reader(AddressCSV, delimiter = ','))

#Basically Loads Driving Distances into DistanceLoaded
with open("C:\\Users\\Ilias\\OneDrive\\Desktop\\C950 Pass\\DSA 2-Ilia\\CSV\\DrivingDistances.csv") as DistanceCSV:
    DistanceLoaded = list(csv.reader(DistanceCSV, delimiter =','))

#Used for packages for data to be loaded is in this folder just in case/for future expansions
Packages.PackageLoader('C:\\Users\\Ilias\\OneDrive\\Desktop\\C950 Pass\\DSA 2-Ilia\\CSV\\PackageInfo.csv')
#This is a Class Truck with alot of important aspects, Most importantly Departure Time as its most complex part
class Truck:
    def __init__(self,Truck_Speed,Miles_Driven,PresentLocation,Departure_Time,Package):
        self.Truck_Speed = Truck_Speed
        self.Miles_Driven = Miles_Driven
        self.PresentLocation = PresentLocation
        self.DriveTime = Departure_Time
        self.Departure_Time = Departure_Time
        self.Package = Package
    #Basically loads from data
    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.Truck_Speed,self.Miles_Driven, self.PresentLocation, self.DriveTime, self.Departure_Time, self.Package)
#This is mannually loading the trucks
FirstTruck = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=8),[1,13,14,15,16,19,20,27,29,30,31,34,37,40])
SecondTruck = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=11),[2,3,4,5,9,18,26,28,32,35,36,38])
ThirdTruck = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5),[6,7,8,10,11,12,17,21,22,23,24,25,33,39])
#Address Definition used for future loading
def Address(Address):
    #print(Address)
    for row in AddressLoaded:
       if Address in row[2]:
           return int(row[0])
        #Return Zero was added in order to prevent an Error
        #Do not Remove
    return 0




#Mid point allows the for the algorithm to decide what place to go next
def Midpoint(FirstAddress,SecondAddress):
    #print (FirstAddress)
    first_address_index = int(FirstAddress)
    second_address_index = int(SecondAddress)
    MidpointDistance = DistanceLoaded[first_address_index][second_address_index]
    #print (FirstAddress)
    if MidpointDistance == '':
        MidpointDistance = DistanceLoaded[second_address_index][first_address_index]
    return float(MidpointDistance)

    #This truck delivery algorithm basically Delivers all the packages
def TruckDeliverAlgo(trucks):
    #Creates a list for all packages out for delivery
    OutForDelivery = []
    for PackageID in trucks.Package:
        package = Packages.PackageHashTable.HashTableSearch(PackageID)
        OutForDelivery.append(package)
    trucks.Package.clear()
    #Basically means while packages that are out for delivery is more than 0

    while len(OutForDelivery) > 0:
        FollowingAddress = 2000
        FollowingPackage = None
        for package in OutForDelivery:

            if package.Id in [25, 6]:
                FollowingPackage = package
                #print (FollowingPackage)
                FollowingAddress = Midpoint(Address(trucks.PresentLocation), Address(package.Street))
                #print (FollowingPackage)
                break
            if Midpoint(Address(trucks.PresentLocation),Address(package.Street)) <= FollowingAddress:
                FollowingAddress = Midpoint(Address(trucks.PresentLocation),Address(package.Street))
                FollowingPackage = package
        trucks.Package.append(FollowingPackage.Id)
        OutForDelivery.remove(FollowingPackage)
        trucks.Miles_Driven += FollowingAddress
        trucks.PresentLocation = FollowingPackage.Street
        trucks.DriveTime += datetime.timedelta(hours=FollowingAddress /18)
        FollowingPackage.Delivery_Time = trucks.DriveTime
        #print (FollowingPackage)
        FollowingPackage.Departure_Time = trucks.Departure_Time
        #print (FollowingPackage)

TruckDeliverAlgo(FirstTruck)
TruckDeliverAlgo(ThirdTruck)
TruckDeliverAlgo(SecondTruck)


#This function is used in the GUI/API in order to print the amount of miles the trucks have driven.
def TotalMilesT():
    if not hasattr(TotalMilesT, 'printed'):
        print("Total Miles are:", (FirstTruck.Miles_Driven + SecondTruck.Miles_Driven + ThirdTruck.Miles_Driven))
    TotalMilesT.printed = True
