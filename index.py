print("Party ki hai to Paise to Dene Padenge")
city=str(input("Enter the city you live in: "))
distance=int(input("What is the distance between your hostel and resturant(in km): "))
member=int(input("Enter no of members: "))

Menu={
    "Starter":{
        "maggi-masala":100,
        "manchurian":120,
        "French-fries":80,
        "Burger":60
    },
    "Gravy":{
        "Paneer-butter-masala":250,
        "paneer-tika":280,
        "handi-paneer":240,
        "mushroom-do-pyaza":260
    },
    "Beverages":{
        "plane-tea":25,
        "tanduri-tea":40,
        "choco-tea":45,
        "coffee":30
    },
    "water":{
        "bislari":20,
        "vedica":70
    },
    "chapati":{
        "plane-roti":8,
        "butter-roti":10,
        "tanduri-roti":20,
        "butter-nan":30
    }
}
food_bill=0
print("Here is the Menu, Please Place your order: ")

for category , items in Menu.items():
    print(category)
    for dish, price in items.items():
        print(" ",dish,":", price)

    ordered_item=str(input("Enter your desigred dish: "))

    if ordered_item in items:
       print("Nice Choice!!")
       quantity=int(input("enter quantity: "))
       food_bill+=quantity*items[ordered_item]
       
    else:
       print("This Item is not available...")
       print("try again")
       continue
       


tip=int(input("Enter tip you paid: "))
food_bill+=tip

travelling_bill=2*4*distance
print("Your food bill is: ",food_bill)
print("Your total travelling bill is: ",travelling_bill)
print("Your Total bill is: ",food_bill+travelling_bill)
print("Each one have to pay: ",(food_bill+travelling_bill)/member)
      


