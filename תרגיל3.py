# START
import time

_time: int = int(input('How long did it take for the restaurant to deliver the dish? (in minutes)'))
_price : int = int(input('What is the price of the dish? (in shekels)'))

is_quick_service = _time < 15
is_expensive = _price > 100

if is_quick_service and not is_expensive:
    print('recommended')
else:
    print('not recommended')


# STOP
