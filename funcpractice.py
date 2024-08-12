
    
#  num1 = int(input("insert your first number here :"))
#  num2 = int(input("insert your second number here :"))
# num3 = int (input("insert your yherd number here :"))
    
# hole_sum = num1 + num2 + num3
    
# return hole_sum

#result = add_three()
#print("end result of all enterd numbers added to each other is : " , result)

'''def add_three( num1, num2, num3):
    y = num1 + num2 + num3
    return y

sum = add_three(52 ,25 , 1403)

print(str(sum))'''

'''
def add_one(x):
    y = x + 1
    return y 
result = add_one( 5 )

print(result)'''

'''
def cape_town(hotel_cost, plane_cost, car_rental, num_nights, num_days):
    return hotel_cost + plane_cost + (car_rental * num_days) + (700 * num_nights)


def durban(hotel_cost, plane_cost, car_rental, num_nights, num_days):
    return hotel_cost + plane_cost + (car_rental * num_days) + (250 * num_nights)


def johannesburg(hotel_cost, plane_cost, car_rental, num_nights, num_days):
    return hotel_cost + plane_cost + (car_rental * num_days) + (400 * num_nights)


def plane_cost(city_flight):
    if city_flight == "Cape Town":
        return 1200
    elif city_flight == "Durban":
        return 700
    elif city_flight == "Johannesburg":
        return 1000
    else:
        print("City not available !")
        return 0


def holiday_expense(city, hotel_cost, city_flight, car_rental, num_nights, num_days):
    if city == "Cape Town":
        total_cost = cape_town(hotel_cost, plane_cost(city_flight), car_rental, num_nights, num_days)
    elif city == "Durban":
        total_cost = durban(hotel_cost, plane_cost(city_flight), car_rental, num_nights, num_days)
    elif city == "Johannesburg":
        total_cost = johannesburg(hotel_cost, plane_cost(city_flight), car_rental, num_nights, num_days)
    else:
        print("City not available")
        return 0

    return total_cost'''

'''
city_flight = input("Which city are you flying to (Cape Town, Durban, Johannesburg): ")
num_nights = int(input("How many nights are you staying: "))
num_days = int(input("How many days would you be renting a car: "))
hotel_cost = int(input("Enter hotel cost per night: "))
car_rental_cost = int(input("Enter car rental cost per day: "))

hotel_cost *= num_nights
car_rental = car_rental_cost * num_days

total_expense = holiday_expense(
    city_flight, hotel_cost, city_flight, car_rental, num_nights, num_days)
if total_expense != 0:
    print(f'Total holiday expense for {city_flight} for {
    num_nights} nights: R{total_expense}')'''













