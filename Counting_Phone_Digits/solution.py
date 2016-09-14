def phone_number(Phone):

    number = str(Phone)
    length = len(str(number))
    first = number[0]
    if isinstance(Phone, int)is True and(length>9):
        if (length == 10):
            return "Good Number"
        elif (length==11)and (first==1):
            phone = int(number.rstrp(first))
            return "Good Number"
        else:
            return "Bad Number"
    else:
        return "Bad Number"
print phone_number(Phone)