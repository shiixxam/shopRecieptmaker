sum = 0
while(True):
    userInput = input('Enter the price of item or press q to quit: \n')
    if(userInput!='q'):
        sum = sum + int(userInput)
        print(f"order total so far: {sum}")
    else:
        print(F"your bill total is {sum}. thanks for shopping with us " )
        break