



# Im creating a fucntion  giving it a name and telling it what i want to do wit city , the number of nights and als how many days i whant to be renting the car
def holiday_cost(city, num_nights, rental_days):
    total_cost = plain_cost(city) + (num_nights * hotel_cost(city)) + (rental_days * car_cost(city))
    return total_cost

# i am satating how much a plain ticket would cost if you go to serten places      
def plain_cost (city):
    if city == "Cape Town":
        return 1200
    elif city == "Durban":
        return 700
    elif city == "Johannesburg":
        return 1000
    else:
        print("City not available !")
        return 0

#here you can see howmuch it would each night were you are
def hotel_cost(city):
    if city == "Cape Town":
        return 900
    elif city == "Durban":
        return 400
    elif city == "Johannesburg":
        return 700
    else:
        print("Hotel not available !")
        return 0
    
# here you can see how much a car cost per day depending on wich city you are staying
def car_cost(city):
    if city == "Cape Town":
        return 200
    elif city == "Durban":
        return 120
    elif city == "Johannesburg":
        return 160
    else:
        print("Hotel not available !")
        return 0
#this is a input fow the user to state where thry are going how many nights they are sataying and also how many days they are staying
city_choice = input("Wich city do you whant to go to (Cape Town, Durban, Johannesburg) :")
number_of_nights = int(input(" how many nights do you whant to stay :"))
number_of_days = int(input("how many days would you be staying :"))
        
#calculates the information givin 
total_cost = holiday_cost(city_choice, number_of_nights , number_of_days)
#print the total of the holiday
print(f"Your holiday in{city_choice} is: R{total_cost} ")

    
#if there is things i can approve pleas let me know and send it back with eany material you can provide for me to learn