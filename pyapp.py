import requests
from bs4 import BeautifulSoup
import smtplib #Simple Mail Transfer Protocol Library
import time

URL="https://www.amazon.in/HP-Express-Backpack-15-6-inch-laptops/dp/B07H5YQ1MS" #Url of the product to track

headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

def check_price():
    page=requests.get(URL,headers=headers)

    soup1=BeautifulSoup(page.content,'html.parser')
    soup2=BeautifulSoup(soup1.prettify(),"html.parser")

    title=soup2.find(id="productTitle").get_text() #To find productTitle .get_text to remove html tags

    print(title) #Product Name

    price= soup2.find(id="priceblock_dealprice").get_text() #To find price, to remove html tags
    converted_price=float(price[15:19]) #slicing out the price and converting it from str to float
    print(converted_price)#Product_Price

    if(converted_price<600):
        send_mail()

def send_mail():#creating your email connection with google to send mail when price drops
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo() #extended helo cmd sent by email server to identify itself
    server.starttls() #encrypts our connection
    server.ehlo()

    server.login('YOUR-EMAIL-HERE@gmail.com',"VERIFICATION-CODE-HERE")

    subject = "Price Drop!!"
    body="Check the amazon link https://www.amazon.in/HP-Express-Backpack-15-6-inch-laptops/dp/B07H5YQ1MS "

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
            'YOUR-EMAIL-HERE@gmail.com',
            'RECEIVER-EMAIL-HERE@gmail.com',
            msg
    )
    print("Email Sent")

    server.quit()

while True:
        check_price()
        time.sleep(60*60) #checks price every hour