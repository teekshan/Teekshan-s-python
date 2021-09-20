def credit_card_valiadtor():
    sum_of_digit=0
    credit_card_number=input("enter a 16 digit credit card number\n")
    if len(credit_card_number) ==16 and credit_card_number[0] !="0" and credit_card_number.isdigit():
        for digit in str(credit_card_number):
            sum_of_digit+= int(credit_card_number)
        if (sum_of_digit%10)==0:
                print("card no. is valid")
        else:
                print("card no. is not valid")
    else:
        print("please enter a valid number")
				
credit_card_valiadator()
