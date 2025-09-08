# python shopping cart
#using file handling methods like file.write and file.read to display and save customer's orders
# and review their past orders if they feel too


#using dict to store fruits as menu
fruits ={
    "mango": 3.00,
    "orange":4.22,
    "apple": 3.99,
    "banana":1.99,
}
print("---------fruit menu-------------")
for x, obj in fruits.items():
    print(f"{x} :  ${obj}")
print("---------------------------------")


selected_fruits =[]
total_price = 0.0

while True:
    order = input("Type 'history' to view your past orders \n"
                  "(Q) to exit or what is your order?  :  ")
    if order.lower() =="q":
        break

           #Viewing order history
    if order.lower().startswith("h"):
        print(sep=" ")
        with open("order.txt", "r") as file:
            print("------Your past history orders--------")
            print("Orders    Number of orders")
            print(file.read())
            print(sep=" ")

    else:
        if not order in fruits:
            print(f"Your order {order} is unavailable!")
            print("Please select another one")
            continue
        else:
            cost = int(input(f"How many orders of {order} you are buying? :"))
            price = fruits[order]*cost

              # Saving orders to the file
            with open("order.txt", "a" ) as file:
                file.write(f"{order}   -  {cost} \n"
                           f"there total cost was ${price} \n")

        selected_fruits.append(order)
        total_price+= price


print(sep=" ")
print("------------Your cart order-----------------")
print(selected_fruits)
print(f"Your total is ${total_price}")

print("Thanks for shopping. Have nice day👋")





















# def year_of_birth(n):
#     enter = int(input("enter the year of birth :"))
#     if not enter.is_integer():
#         raise ValueError("Please enter a valid number or digit!")
#     if enter:
#         age = n - enter
#         print(f"Your are {age} years old")
#         return enter
#
# def main():
#     while True:
#         try:
#             current_year = int(input("enter the current year:"))
#             current_year = year_of_birth(current_year)
#             break
#         except ValueError:
#             print("Please enter a valid number or digit!")
#
# if __name__ == '__main__':
#     main()