with open("Text File7.txt", "w") as f:
    id = input("Enter Order ID: ")
    name = input("Enter Customer Name: ")
    product = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    total = quantity * price

    f.write("----- ORDER SUMMARY -----\n")
    f.write("Order ID: " + id + "\n")
    f.write("Customer Name: " + name + "\n")
    f.write("Product Name: " + product + "\n")
    f.write("Quantity: " + str(quantity) + "\n")
    f.write("Price: " + str(price) + "\n")
    f.write("Total Amount: " + str(total) + "\n")

    print("\nOrder saved successfully!")

with open("Text File7.txt","r") as f:
    l=f.readlines()
    print("Order id: ",l[0])
    print("Customer name: ",l[1])