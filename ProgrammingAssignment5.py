# Programmers: Alex Bean
# Course: CS151, Dr. Rajeev
# Programming Assignment: 5
# Program Inputs: The file of trip information, the operation they would like to do, the date they are interested in, the payment type, their longitude and latitude, the maximum distance in miles from their position, the name of the file they would like to store information of the trips in, and if they would like to continue.
# Program Outputs: Average payment for either cash or credit card, the number of trips on a specific date, as well as a file that contains all of the trips from a maximum distance of their position.

import math

def MakeListOfLists(filename):
    list = []
    try:
        file = open(filename, "r")
        for lines in file:
            lines = lines.split(",")
            lines[-1] = lines[-1].strip()
            list.append(lines)
        file.close()
        return list
    except FileNotFoundError:
        print("The file you entered could not be found.")
        exit()


def AverageCost(list):
    CashCount = 0
    CreditCount = 0
    CashSum = float(0)
    CreditSum = float(0)

    for lines in list:
        price = float(lines[5])
        if lines[6] == "Credit Card":
            CreditSum += (price)
            CreditCount += 1
        elif lines[6] == "Cash":
            CashSum += (price)
            CashCount += 1
    CreditAvg = CreditSum/CreditCount
    CashAvg = CashSum/CashCount
    return CreditAvg, CashAvg



def TripsOnDate(date,list):
    TripCount = 0
    for lines in list:
        lines[1] = lines[1].split()
        lines[2] = lines[2].split()
        if lines[1][0] == date or lines[2][0] == date:
            TripCount += 1
    return TripCount



def DistanceOfAllTrips(distance, list, output_file_name, lat1, lon1):
    file = open(output_file_name, 'w')
    for lines in list:
        CalcPickupDistance = CalculateDistance(lat1, lon1, lines[8], lines[9])
        CalcDropoffDistance = CalculateDistance(lat1, lon1, lines[10], lines[11])
        if CalcPickupDistance <= distance or CalcDropoffDistance <= distance:
            print(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9], lines[10], lines[11], sep=",", file = file)
    file.close()



def ValidateDate(list):
    year = input("What year are you interested in?")
    while not(year.isdigit()):
        print("Invalid input")
        year = input("What year are you interested in?")

    month = input("What month are you interested in (1-12)?")
    while not(month.isdigit()):
        print("Invalid input")
        month = input("What month are you interested in (1-12)?")

    day = int(input("What day are you interested in (1-31)?"))
    while not(1 <= day <= 31):
        print("Invalid day")
        day = int(input("What day are you interested in (1-31)?"))

    date = year + "-" + month + "-" + str(day)
    trip_count = TripsOnDate(date, list)

    print("The number of trips on", date, "are:", trip_count)



def ValidatePayment(list):
    PaymentType = input("Would you like to see the average payment with cash or credit card?")
    PaymentType = PaymentType.strip().lower()

    while not(PaymentType == "Cash" or PaymentType == "Credit Card"):
        print("Invalid input")
        PaymentType = input("Would you like to see the average payment with cash or credit card?")
        PaymentType = PaymentType.strip().lower()

    CashAverage, CreditAverage = AverageCost(list)

    if PaymentType == "Cash":
        AveragePayment = CashAverage
    else:
        AveragePayment = CreditAverage
    print("The average", PaymentType, "is:", AveragePayment)


def ValidateDistance(list):
    distance = float(input("What distance away from either drop off or pickup are you interested in? (in miles)"))

    while not(distance >= 0):
        print("Invalid distance")
        distance = float(input("What distance away for either dropoff or pickup are you interested in? (in miles)"))

    lat1 = float(input("What is your latitude?"))
    lon1 = float(input("What is your longitude?"))

    while not(-90 <= lat1 <= 90):
        print("Invalid latitude.")
        lat1 = float(input("What is your latitude?"))
    while not(-180 <= lon1 <= 180):
        print("Invalid longitude.")
        lon1 = float(input("What is your longitude?"))

    output_file_name = input("Create the file name that will store all the information of the trips:")
    DistanceOfAllTrips(distance, list, output_file_name, lat1, lon1)


def calculate_distance(lat1, lon1, lat2, lon2):
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    CalcDistance = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * 3959
    return CalcDistance


def main():
    filename = input("What file would you like to use?")
    list = MakeListOfLists(filename)
    resume = 'Yes'

    while resume == 'Yes':
        Operation = input("What operation would you like to look at (local trips, average cost, trips on a certain date)?")
        Operation = Operation.strip().lower()
        while not(Operation == "local trips" or Operation == "average cost" or Operation == "trips on a certain date"):
            print("Invalid input")
            operation = input("What operation would you like to look at (local trips, average cost, trips on a certain date)?")
            operation = operation.strip().lower()
        if Operation == "Local Trips":
            ValidateDistance(list)
        elif Operation == "Average Cost":
            ValidatePayment(list)
        elif Operation == "Trips on a certain date":
            ValidateDate(list)

        resume = input("Would you like to continue (yes or no)?")
        resume = resume.strip().lower()

        while not(resume == "Yes" or resume == "No"):
            resume = input("Would you like to continue (yes or no)?")
            resume = resume.strip().lower()

main()