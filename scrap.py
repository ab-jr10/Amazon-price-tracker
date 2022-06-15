from calendar import c
import requests     # it will help us to get our url directed
from bs4 import BeautifulSoup       # it will help us to scrap us the data
import os
import smtplib
from email.message import EmailMessage
import time


email_id = os.environ.get("EMAIL_ADDR")
email_pass = os.environ.get("EMAIL_PASS")

print(email_id)
print(email_pass)
# exit()



# URL = "https://www.amazon.in/OnePlus-Certified-Android-55Q1IN-1-Without/dp/B07W5QZQ45/ref=sr_1_3?crid=38TIFA1X6UATY&keywords=oneplus+138.8+cm+55+inches+q1+series+4k&qid=1655091150&sprefix=%2Caps%2C547&sr=8-3"

site = input("Enter Shopping site name : ")
URL = input("Enter URL of the product : ")
Current_price = input("Enter current price of the product : ")
receiver_email = input("Enter Email Id : ")

def check_price():
    headers = {"user-Agent" :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'}


    page = requests.get(URL, headers= headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_ ="a-size-large a-spacing-none").get_text()
    price = soup.find(class_ ="a-offscreen").get_text()
    converted_price = price[1:7].replace(",","")
    print(title.strip())
    print(converted_price)

    if converted_price <= Current_price:
        send_mail()
    
def send_mail():
    msg = EmailMessage()
    msg['Subject'] = "Product price has fallen down"
    msg['from'] = email_id
    msg['To'] = receiver_email
    message = "Hey check out this " + site + " link : https://www.amazon.in/OnePlus-Certified-Android-55Q1IN-1-Without/dp/B07W5QZQ45/ref=sr_1_3?crid=38TIFA1X6UATY&keywords=oneplus+138.8+cm+55+inches+q1+series+4k&qid=1655091150&sprefix=%2Caps%2C547&sr=8-3"
    # print(message)
    msg.set_content(message)
    
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:       # 465 is the port number
        smtp.login(email_id, email_pass)
        smtp.send_message(msg)
        
        
        
while True:       
    check_price()
    # time.sleep(10)
    

