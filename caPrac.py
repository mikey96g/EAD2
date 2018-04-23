curr_xe = {'USD':1.2,'CAD':1.6,'GBP':1.4 }

def convert(currencey,value):
	curr = value * curr_xe[currencey]
	return curr


def re_convert(currencey,value):
	curr = value * 1/curr_xe[currencey]
	return curr


temp = convert('USD',10)

print(convert('USD',10))
print(re_convert('USD',temp))

bankAccount = []

def debit(value):
	bankAccount.append(value)
	
def credit(value):
	try:
		if value < 0:
			bankAccount.append(value)
	except ValueError:
		val = print("That is an error must be minus")
		
def balAccount(bankAccount):
	if len(bankAccount)==0:
		return 0;
	else:
		return bankAccount[0] + balAccount(bankAccount[1:])


print(len(bankAccount))
credit(-23)
debit(50)

print(balAccount(bankAccount))	

