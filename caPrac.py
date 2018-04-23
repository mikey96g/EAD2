curr_xe = {'USD':1.2,'CAD':1.6,'GBP':1.4 }

def convert(currencey,value):
	curr = value * curr_xe[currencey]
	return curr


def re_convert(currencey,value):
	curr= value * 1/curr_xe[currencey]
	return curr


temp = convert('USD',10)

print(convert('USD',10))
print(re_convert('USD',temp))