import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+996507959966")
print(geocoder.description_for_number(phone_number1,"kg"))
