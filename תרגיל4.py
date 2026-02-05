# START

while True:

    _last_name:str = str(input('Enter your last name: '))
    ans = _last_name.isupper()
    if ans:
        break

while True:
    _first_name:str = str(input('Enter your first name: '))
    ans = _first_name.islower()
    if ans:
        break
while True:
    _country:str = str(input('Enter country: '))
    ans = _country.isalpha()
    if ans and len(_country) <= 3:
        break

_city_address:str = str(input('Enter your city address: '))

while True:
    _zip_code:str = str(input('Enter your zip code: '))
    ans = _zip_code.isdigit()
    if ans and len(_zip_code) >= 4:
        break
        
print()
print(f"FOR: {_last_name},{_first_name}\n"
      f"COUNTRY: {_country.upper()}\n"
      f"ADDRESS: {_city_address.title()}\n"
      f"ZIPCODE: {_zip_code}")



# STOP
