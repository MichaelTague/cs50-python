#import decimal
from decimal import Decimal


ctx = decimal.getcontext()
ctx.rounding = decimal.ROUND_HALF_UP

x = Decimal('2.25')
y = Decimal('3.35')

print(round(x, 1))
print(round(y, 1))