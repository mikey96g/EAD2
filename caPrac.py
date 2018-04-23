from functools import reduce

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
	return bankAccount
	
def credit(value):
	if value > 0:
		if value <= balAccount(bankAccount):
			bankAccount.append(-value)
		else:
			raise ValueError('Insufficent funds')
	else:
		raise ValueError('Invalid amount, must be positive')
		
		
def balAccount(bankAccount):
	if len(bankAccount)==0:
		return 0;
	else:
		return bankAccount[0] + balAccount(bankAccount[1:])


		
print(len(bankAccount))
debit(50)
credit(25)
debit(50)

print(balAccount(bankAccount))	

dollars = map(lambda euro: convert('USD',euro), bankAccount)

# format transactions for display
def format(a, b):
    output = ''
    if b < 0:
        output += 'credit: '
    else:
        output += 'debit: '
    return str(a) + output + str(b) + ' '
output = reduce(format, bankAccount, '')
print (output)
