import datetime #Datetime python module for accessing dates/time info
account = [['Date', 'Credit', 'Debit', 'Balance']]
 
def transaction():
    now = datetime.datetime.now()
    dayMonthYear = str(now.day)+'/'+str(now.month)+'/'+str(now.year)  #used to make a date in the format D/M/Y for today's date
    validInput = False
    while validInput == False: #while loop which prompts user for entering a valid creditQ input
        creditQ = input('Do you want to credit your account in this transaction? Y/N').lower()
        if (creditQ == 'y'):
            validInput = True # creditQ == 'y' so we then break out of loop
            credit = float(input('How much do you want to credit your account? '))
            if len(account) > 1:
                lastRow = account[len(account) - 1]
                newRow = [dayMonthYear, credit, 0, credit + lastRow[3]]
                account.append(newRow)
                print('Added ', credit, 'to your account.')
                print('Your new balance is: ', account[len(account)-1][3])
            else: 
                newRow = [dayMonthYear, credit, 0, credit]
                account.append(newRow)
                print('Added ', credit, 'to your account.')
                print('Your new balance is: ', account[len(account)-1][3])
        elif(creditQ == 'n'):
            validInput = True # creditQ == 'n' so we then break out of loop
        else:
            print('Please enter a valid input.')
 
    validInput = False
    while validInput == False: #while loop which prompts user for entering a valid debitQ input
        debitQ = input('Do you want to debit your account in this transaction? Y/N').lower()
        if (debitQ == 'y'):
            validInput = True #debitQ == 'n' so we then break out of loop
            debit = float(input('How much do you want to debit your account? '))
            if len(account) > 1:
                lastRow = account[len(account) - 1]
                newRow = [dayMonthYear, 0, debit, lastRow[3] - debit]
                account.append(newRow)
                print('Subtracted ', debit, 'from your account.')
                print('Your new balance is: ', account[len(account)-1][3])
            else: 
                newRow = [dayMonthYear, 0, debit, -debit]
                account.append(newRow)
                print('Subtracted ', debit, 'from your account.')
                print('Your new balance is: ', account[len(account)-1][3])
        elif (debitQ == 'n'):
            validInput = True #debitQ == 'n' so we then break out of loop
        else: 
            print('Please enter a valid input.')
    print('Thank you for the transaction. Have a nice day.')

#Code block for seeing the account populate over time with transactions
userQuestion = input('Do you still want to run the program? Y/N').lower()
while (userQuestion == 'y'):
    transaction()
    print('Your new account looks like this: ')
    for i in account: 
        print (i)
    userQuestion = input('Do you still want to run the program? Y/N').lower()
