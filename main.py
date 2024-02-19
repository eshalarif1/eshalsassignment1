# Eshal Arif Assignment 1 Algorithms and Data Structures
import time

# main function, that loads the product_data file, and stores the data into arrays
product_list = []
search_found = False


def main():
    global product_list
    with open("product_data.txt", 'r') as file_data:
        for line in file_data:
            data = line.strip().split(',')
            product_list.append(data)


# function for the insert method of the list
def insert():
    global product_list

    product_id = input("Enter a product id (5 digits):")
    product_name = input("Enter a name for the product:")
    product_price = input("Enter a price for the product:")
    product_category = input("Enter a category for the product:")
    inserted_product = [product_id, product_name, product_price, product_category]
    product_list.append(inserted_product)
    print("The product has been inserted!")

    for product in product_list:
        print(product)


# function for the update method of the list

def update():
    product_id = input("please enter the id of the product you would like to update:")
    for product in product_list:
        if product[0] == product_id:
            updated_product = input("What would you like to update: \n 1.id, \n 2.name, \n 3.price \n 4.category:")
            if updated_product == "1" or updated_product == "id":
                new_id = input("please enter the new id:")
                print("The product has been updated")
                product[0] = new_id
            elif updated_product == "2" or updated_product == "name":
                new_name = input("please enter the new name:")
                product[1] = new_name
                print("The product has been updated")
            elif updated_product == "3" or updated_product == "price":
                new_price = input("please enter the new price:")
                product[2] = new_price
                print("The product has been updated")
            elif updated_product == "4" or updated_product == "category":
                new_category = input("please enter the new category:")
                product[3] = new_category
                print("The product has been updated!")

            else:
                print("There is no such product.")

    for product in product_list:
        print(product)


# function for the delete method
def delete():
    global product_list
    product_id = input("please enter the id of the product you would like to delete:")
    for product in product_list:

        if product[0] == product_id:
            product_list.remove(product)
            print("The product has been deleted!")
            break

    else:
        print("There is no such product.")

    for product in product_list:
        print(product)


def search():
    global product_list
    global search_found
    product_choice = input(
        "enter which attribute you would like to search by \n1. id \n2. name\n3. price \n4. category:")
    if product_choice == "1" or product_choice == "id":
        id_search = input("please enter a product ID you want to search for:")
        search_found = False
        for product in product_list:
            if product[0] == id_search:
                search_found = True
                print("here is the product(s) found:", product)

        if not search_found:
            print("no product found")

    elif product_choice == "2" or product_choice == "name":
        name_search = input("please enter a product name you want to search for:")
        search_found = False
        for product in product_list:
            if product[1].strip() == name_search:
                search_found = True
                print("here is the product(s) found:", product)
        if not search_found:
            print("no product found")

    elif product_choice == "3" or product_choice == "price":
        price_search = input("please enter a product price you want to search for:")
        search_found = False
        for product in product_list:
            if product[2].replace(" ", "") == price_search:
                search_found = True
                print("here is the product(s) found:", product)
        if not search_found:
            print("no product found")

    elif product_choice == "4" or product_choice == "category":
        category_search = input("please enter a product category you want to search for:")
        search_found = False
        for product in product_list:
            if product[3].replace(" ", "") == category_search:
                search_found = True
                print("here is the product(s) found:", product)

        if not search_found:
            print("no product found")

    else:
        print("invalid input")


# bubble sort method and complexities
def bubble_sort():
    global product_list
    start_time = time.time()
    n = len(product_list)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if float(product_list[j][2]) > float(product_list[j + 1][2]):
                product_list[j], product_list[j + 1] = product_list[j + 1], product_list[j]
                swapped = True

        if not swapped:
            break
    end_time = time.time()
    total_time = end_time - start_time
    print("the time taken for the average case is: {:.20f} seconds".format(total_time))


# calling main function

if __name__ == "__main__":
    main()

    # while loop for asking user inputs
    while True:
        options = input(
            "what would you like to do?\n1. insert\n2. update\n3. delete\n4. search\n5. bubble sort\n6. stop or exit:")

        if options == "1" or options == "insert":
            insert()
        elif options == "2" or options == "update":
            update()
        elif options == "3" or options == "delete":
            delete()
        elif options == "4" or options == "search":
            search()
        elif options == "5" or options == "bubble sort":
            bubble_sort()

        elif options == "6" or options == "stop" or options == "exit":
            print("exiting and saving file!")

            with open("product_data.txt", 'w') as file_data:
                for product in product_list:
                    file_data.write(f'{product[0]},{product[1]},{product[2]},{product[3]}\n')
            break
        else:
            print("sorry, pick one of the options provided!")
