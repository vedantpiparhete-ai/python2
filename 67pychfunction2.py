def bill(amount):
    if amount >=10000:
      return amount * 0.10
    else:
        return amount * 0.5
print("Trends apka swagat hai 🙏🏻")
amount=int(input("Enter bill amount: "))
discount=bill(amount)
final=amount-discount
print('Discount: ',discount)
print('Final Bill to pay: ',final)
print("Apka Dhanyavad ane ka liya 🙏🏻")