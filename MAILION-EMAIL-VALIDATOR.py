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
def main_func():
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


main_func()
