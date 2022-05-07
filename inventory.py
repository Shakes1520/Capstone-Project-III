

from tabulate import tabulate

class Shoe :
    """_
    Shoe class
    """ 
 
    def __init__(self, country, code, product, cost, quantity):
        
        # Shoe Attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
       
    # Get size method
    def get_country(self):
        """Method returns country intance variable""" 
        return self.country

    def get_code(self):
        """Method returns code intance variable""" 
        return self.code
    
    def get_product_name(self):
        """Method returns product name intance variable""" 
        return self.product

    def get_cost(self):
        """ Method product cost intance variable""" 
        return self.cost
 
    def get_quantity(self):
        """Method returns quantity of the product intance variable""" 
        return self.quantity




def search_product():
    """Function searching for the product item in the appended object list""" 

    # Prompting the user to enter the code of the product
    product_code = input("Please enter the product code of the item you are looking for: ")

    # Iterating through the nike_shoe_list list
    for products in nike_shoe_list:
        # If the shoe class code is the same as the prompted product_code print the producty code and country
        if product_code == products.get_code():

            print(f"The nike {str(products.get_product_name())} is availabe in {str(products.get_country())} ")          

def highest_stock_function():
    """Function for checking for the hhighest number in the object list"""

     # Openning the text file
    with open("inventory.txt","r") as file:
        # Reading the data from the text file
        data = file.readlines() 
        # An empty list to store quantity
        quantity = []
        max_value = 0

        # Iterating throught the text file data
        for line in data:
            # Splitting the file data by the "," and removing the whitespaces
            line = line.strip().split(",")
            # Adding the fourth index of data to the quantity empty list
            quantity.append(line[4])
            # Finding the miximum value in the quantity list 
            max_value = max(quantity)
            if max_value == line[4]:
                product_in_excess = line[2]
        #Printing the miximum value from the list
        print(f"{product_in_excess} is in excess, {product_in_excess} is on now sale!!!")


def lowest_stock_function():
    """Function searching for the lowest number of products in the invetory text file""" 

    # Openning the text file
    with open("inventory.txt","r") as file:
        # Reading the data from the text file
        data = file.readlines() 
        # An empty list to store quantity
        quantity = []
        min_value = 0

        # Iterating throught the text file data
        for line in data:
            # Splitting the file data by the "," and removing the whitespaces
            line = line.strip().split(",")
            # Adding the fourth index of data to the quantity empty list
            quantity.append(line[4])
            # Finding the minimum value in the quantity list 
            min_value = min(quantity)
            if min_value == line[4]:
                lowest_quantity_product = line[2]
        #Printing the minimum value from the list
        print(f"{lowest_quantity_product} is running out, we need to restock it")
    
    # Prompting the user the to enter no/yes
    restock_choice = input(f"Do you want to restock the {lowest_quantity_product} (yes/no): ")

    if restock_choice == "Yes" or restock_choice == "YES" or restock_choice == "yes":

        # Openning the text file, in appending mode
        with open("inventory.txt","a") as file:
            # Promt the user to enter the name of the product
            product_country = input("Please enter the country name of the product: ")
            # Promt the user to enter the code of the product
            product_code = input("Please enter the code of the product: ")
            product_name = lowest_quantity_product
            # Promt the user to enter the price of the product
            product_cost = input("Please enter the price of the product: ")
            # Promt the user to enter the quantity of the product
            product_quantity = input("Please enter the number of the product yo wish to restock: ")
            # Writing the prompted variables to the file
            file.write(str(product_country)+","+str(product_code)+","+str(product_name)+","+str(product_cost)+","+str(product_quantity)+"\n")


def read_data():
    """The function thatreads data from the invetory text file and printing the data in table format """ 

    try:

        # Openning the text file
        with open("inventory.txt","r") as file:
            # Reading the data from the text file
            data = file.readlines()
            print("The Nike store")
            # Creating the heading of the table
            table = [["Country" ,"Code" ,"Product" ,"Cost" ,"Quantity" ,"Value"]]

            # Iterating thrugh the text file data          
            for line in data:
                # Splitting the file data by the "," and removing the whitespaces
                line = line.strip().split(",")
                # Assigning the first index of the data to countries variable
                countries = line[0]
                # Assigning the second index of the data to codes variable
                codes = line[1]
                # Assigning the third index of the data to products variable
                products = line[2]
                # Assigning the fourth index of the data to costs variable
                costs = line[3]
                # Assigning the fifth index of the data to quantities variable
                quantities = line[4]
                # Adding the variable to the row list to create row for the table
                row = [countries, codes, products, costs, quantities]
                table.append(row)

            return tabulate(table)
    except FileNotFoundError:
        print("The file that you are trying to open does not exist")

    finally:
        if file is not None:
            file.close()


def value_per_item():
    """Function searching for reading data from the invetory text file and printing the data in table format """ 

    # Creating the heading of the table
    table = [["Country" ,"Code" ,"Product" ,"Cost" ,"Quantity" ,"Value"]]

    # Iterating through the nike_shoe_list list
    for line in nike_shoe_list:
        # Getting and assigning the country instance variable to the item_country variable
        item_country = line.get_country()
        # Getting and assigning the code instance variable to the item_code variable
        item_code = line.get_code()
        # Getting and assigning the product name instance variable to the item_name variable
        item_name = line.get_product_name()
        # Getting and assigning the product cost instance variable to the item_cost variable
        item_cost = line.get_cost()
         # Getting and assigning the product quantity instance variable to the item_quantity variable
        item_quantity = line.get_quantity()
        # Calculating the value of each product
        value = item_quantity*item_cost
        # Adding the variable to the row list to create row for the table
        row = [item_country, item_code,item_name,item_cost,item_quantity,value]
        table.append(row)

    return tabulate(table)

# Creating shoe objects
basketball_shoe = Shoe("Vietnam","SKU63221","Blazer",1700,20)

training_and_gym_shoe = Shoe("Russia","SKU89999","Air Force 1",2000,15)

jordan_shoe = Shoe("China","SKU90000","Jordan 1",3200,5)

lifestyle_shoe = Shoe("China","SKU93222","Air Stab",1630,12)

skateboard_shoe = Shoe("Egypt","SKU19888","Dunk SB",1500,30)

# Adding the objects to the list
nike_shoe_list = [basketball_shoe, training_and_gym_shoe, jordan_shoe, lifestyle_shoe, skateboard_shoe]

# Creating the menu 
print("""
    Nike Shoe Store
    Press : 
    1. To show all Products
    2. To search for a shoe
    3. To check the lowest stock in the warehouse
    4. To check the highest stock in the warehouse
    5. To calculate the value
    6. To exit the menu
         """ )

user_input = 0
while user_input != 6:
    user_input = int(input("Please make a choice: "))

    if user_input == 1:
        print(read_data())
      
    elif user_input == 2:
        search_product()
    
    elif user_input == 3:
        lowest_stock_function()

    elif user_input == 4:
        highest_stock_function()

    elif user_input == 5:
        print(value_per_item())