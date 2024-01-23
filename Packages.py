import csv
import datetime


#This hash table includes chaining in order to prevent collisions
class HashTableOutline:
    #This defines maximum capacity of the packages
    #It can be altered in the future for more capacity
    def __init__(self, PackageCapacity=40):
        self.TableList = []
        for i in range(PackageCapacity):
            self.TableList.append([])

    #This inserts Items into the hash table and Updates the list
    def TableInsert(self, key, item):
        KeyBucket = hash(key) % len(self.TableList)
        KeyBucket_List = self.TableList[KeyBucket]

    #Defines the key or an Item
        #The Key is the Package ID
        #Which is the part I stated will be made into key
        for KeyStatus in KeyBucket_List:

            if KeyStatus[0] == key:
                KeyStatus[1] = item
                return True

        keys_value = [key, item]
        KeyBucket_List.append(keys_value)

        return True
    #Searches the hash table for an item with the matching key
    #Will return the item if founcd, or None if not found
    def HashTableSearch(self, key):
        KeyBucket = hash(key) % len(self.TableList)
        KeyBucket_List = self.TableList[KeyBucket]
        #Checks the key if its in bucket list and then it removes it
        for KeyStatus in KeyBucket_List:
            #print(key_value)
            if KeyStatus[0] == key:
                return KeyStatus[1]  #value
        return None

    #Removes an Item if it has a matching Key
    def HashTableDelete(self, key):
        KeyBucket = hash(key) % len(self.TableList)
        KeyBucket_List = self.TableList[KeyBucket]
        if key in KeyBucket_List:
            KeyBucket_List.remove(key)


#This is needed for other parts of the
PackageHashTable = HashTableOutline()
#The Package Class is defined
class Packagey:
    def __init__(self, Id, Street, City, State, Zip_Code,Weight, Notes, Delivery_Status,Due,Departure_Time, Delivery_Time):
        self.Id = Id
        self.Street = Street
        self.City = City
        self.State = State
        self.Zip_Code = Zip_Code
        self.Weight = Weight
        self.Notes = Notes
        self.Delivery_Status = Delivery_Status
        self.Due = Due

        self.Departure_Time = None

        self.Delivery_Time = None
    #This loads it all
    def __str__(self):
        return "Id: %s, %-20s, %s, %s,%s, Due: %s,%s,%s,Departure Time: %s,Delivery Time :%s" % (self.Id,self.Street,self.City,self.State,self.Zip_Code,self.Weight,self.Notes,self.Delivery_Status, self.Departure_Time, self.Delivery_Time)
    #def StatusTotal(self,timey):
    def PackageStatusTotal(self, Timey):
        if self.Delivery_Time == None:
            self.Delivery_Status = "At the Hub"
        elif Timey < self.Departure_Time:
            self.Delivery_Status = "At the Hub"
        elif Timey < self.Delivery_Time:
            self.Delivery_Status = "Arriving"
        else:
            self.Delivery_Status = "Delivered"
        if self.Id == 9:
            if Timey > datetime.timedelta (hours=10,minutes=20):
                self.Street = "410 South State Street"
                self.Zip_Code = "84111"
            else:
                self.Street = "300 State Street"
                self.Zip_Code = "84103"

#loads package data from the info from the CSV, It is needed for the hash table
def PackageLoader(file):
    with open(file) as packageGeneral:
        packageCSV = csv.reader(packageGeneral, delimiter=',')
        next (packageCSV)
        for package in packageCSV:
            Package_ID = int(package[0])
            Package_Street = package[1]
            Package_City = package[2]
            Package_State = package[3]
            Package_Zip_Code = package[4]
            Package_Weight = package[5]
            Package_Notes = package[6]
            Package_Delivery_Status = "Delivery Hub"
            Package_Due = package[7]
            Package_Depart = None
            Delivery_Time = None

            packageInfo = Packagey(Package_ID, Package_Street, Package_City, Package_State, Package_Zip_Code, Package_Weight, Package_Notes, Package_Delivery_Status,Package_Due,Package_Depart, Delivery_Time)
            #print(packageInfo)
            #This is used for a different part of program
            #In the truck section
            PackageHashTable.TableInsert(Package_ID, packageInfo)
#This is for the potential future feature, basically it defines PackageHashTable as HashTableOutline
PackageHashTable = HashTableOutline()
#This loads data for packages
PackageLoader('C:\\Users\\Ilias\\OneDrive\\Desktop\\C950 Pass\\DSA 2-Ilia\\CSV\\PackageInfo.csv')
