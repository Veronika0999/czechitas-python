def phone_number(number):
    if len(number) == 9:
        return True
    elif len(number) == 13:
        return True
    else:
        return False


def price_for_text(text):
    lenght_of_text = (len(text) //180) + 1
    price = lenght_of_text * 3
    return price


phone = input("Insert phone number: ")
if phone_number(phone):
    message = input("Insert your message: ")
    final_price = price_for_text(message)
    print(final_price)
else:
    print("Wrong phone number.")