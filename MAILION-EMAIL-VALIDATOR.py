import subprocess
import requests
from bs4 import BeautifulSoup
from functools import cache
import time

with open("API_KEYS.txt") as file:
    text_file = file.readlines()

api_one = text_file[0]
api_two = text_file[1]
api_three = text_file[2]

index1 = api_one.index(":")
index2 = api_two.index(":")
index3 = api_three.index(":")

my_api_key_1 = api_one[index1 + 1:-1].split(" ")
my_api_key_2 = api_two[index2 + 1:-1].split(" ")
my_api_key_3 = api_three[index3 + 1:-1].split(" ")

ascii_image = '''
            +-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
                        MAILION EMAIL VALIDATOR
            Other products available are:
                - Mailion Sender 
                - Mailion Mail Fetcher
                        ---------contact--------
                        t.me/mailon_official
            +-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
'''
saved_file_name = input("Enter what you want to save the file with: ")

@cache
def api_debounce_code(API, saved_file_name):
    with open("loaded_email.txt", "r") as file:
        file_read = file.readlines()
    for item in file_read:
        item = item.replace("\n","")
        response = requests.get(
            "https://isitarealemail.com/api/email/validate",
            params = {'email': item},
            headers = {'Authorization': "Bearer " + API })

        status = response.json()['status']
        if status == "valid":
            try:
                with open(f"{saved_file_name}.txt", "a") as file1:
                    file1.write(item + "\n")
            except Exception as e:
                with open(f"{saved_file_name}.txt", "w") as file2:
                    file2.write(item + "\n")
            else:
                print(f"{item} is saved")
        elif status == "invalid":
            print(f"{item} is invalid")
        else:
            print(f"{item} is UNKNOWN")


@cache
def validation_f():
    print(ascii_image)
    try:
        api_debounce_code(my_api_key_1, saved_file_name)
    except Exception as a:
        api_debounce_code(my_api_key_2, saved_file_name)
    else:
        try:
            api_debounce_code(my_api_key_3, saved_file_name)
        except:
            pass


@cache
def check_hwid():
    current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'),
                             'utf-8').split('\n')[1].strip()
    # 4C4C4544-0057-3010-8059-C2C04F544E32 
    if current_machine_id == "4C4C4544-0057-3010-8059-C2C04F544E32" or current_machine_id =="EC27E223-FF62-9642-6C61-A85BD44F3712" or current_machine_id =="8D6D2C11-CC4F-4C9D-B50A-C3C65E0E1CC6":
        return True
    else:
        return False

@cache
def get_date():
    try:
        r = requests.get("https://www.calendardate.com/todays.htm")
    except requests.exceptions.ConnectionError:
        pass

    else:
        soup = BeautifulSoup(r.text, "html.parser")
        a = soup.find_all(id="tprg")[6].get_text()
        a = a.replace("-", "")
        return a

if check_hwid() == True:
    limit = 20301010
    try:
        current_date = int(get_date())
    except TypeError:
        poor_network = '''
                +-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
                        CHECK NETWORK, NO NETWORK AVAILABLE
                +-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
                    '''
        print(poor_network)
        time.sleep(10000)
    else:
        if limit >= current_date:
            validation_f()
            ascii_done = '''
                +-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
                            MAILS VALIDATION COMPLETED
                        --------checked saved file---------
                +-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
            '''
            print(ascii_done)
            time.sleep(10000)

        else:
            ascii_outdated = '''
                +-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
                                APP OUTDATED
                            ---contact developer---
                            t.me/mailon_official
                +-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
                        '''
            print(ascii_outdated)
            time.sleep(10000)
else:
    ascii_unauthorised = '''
                +-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
                            UNAUTHORIZED USER
                        ---contact developer---
                            t.me/mailon_official
                +-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
                            '''
    print(ascii_unauthorised)
    time.sleep(10000)
