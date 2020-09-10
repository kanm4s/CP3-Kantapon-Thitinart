from forex_python.converter import CurrencyRates
from datetime import datetime
import pandas as pd

currency = CurrencyRates()

currency_list = ["AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD",
                "BIF","BMD","BND","BOB","BRL","BSD","BTC","BTN","BWP","BYR","BZD","CAD","CDF","CHF","CLP",
                "CNY","COP","CRC","CUC","CVE","CZK","DJF","DKK","DOP","DZD","EEK","EGP","ERN","ETB","EUR",
                "FJD","FKP","GBP","GEL","GHS","GIP","GMD","GNF","GQE","GTQ","GYD","HKD","HNL","HRK","HTG",
                "HUF","IDR","ILS","INR","IQD","IRR","ISK","JMD","JOD","JPY","KES","KGS","KHR","KMF","KPW",
                "KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LTL","LVL","LYD","MAD","MDL","MGA",
                "MKD","MMK","MNT","MOP","MRO","MUR","MVR","MWK","MXN","MYR","MZM","NAD","NGN","NIO","NOK",
                "NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","SAR",
                "SBD","SCR","SDG","SEK","SGD","SHP","SLL","SOS","SRD","SYP","SZL","THB","TJS","TMT","TND",
                "TRY","TTD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VEB","VND","VUV","WST","XAF","XCD",
                "XDR","XOF","XPF","YER","ZAR","ZMK","ZWR"]
                
start_date = ""
end_date = ""

def date_input():
    date_check = False
    date_list = []
    while date_check == False:
        start_date = input("Please enter start date in Year-month-date (EX:2019-01-29) format: ")
        end_date = input("Please enter end date in Year-month-date (EX:2019-01-29) format: ")
        try:
            date_list = pd.date_range(start_date,end_date)
            if len(date_list) == 0:
                date_check = False
                print("Please enter date format correctly.")
            else:
                date_check = True
                average_currency(date_list,user_first_currency_input,user_second_currency_input)
        except:
            print("Please enter date format correctly.")
            date_check = False
    

def average_currency(date_list,first_currency_type,second_currency_type):
    sum_currency_per_day = 0
    for number in range(len(date_list)):
        convert_panda_date_to_string = (datetime.strptime(str(date_list[number]), '%Y-%m-%d %H:%M:%S'))
        sum_currency_per_day += currency.get_rate(first_currency_type,second_currency_type,convert_panda_date_to_string)
        if number == len(date_list)-1:             #-1 because number is come from range, range begin with 0
            sum_currency_per_day /= len(date_list)
    print('Average currency is %.2f' % (sum_currency_per_day))


print("Please select your action.")
print("==========================")
print("1. Check average currency.")
print("2. Convert currency.")

user_action_input = input("Please enter number of action list: ")
while user_action_input not in ("1","2"):
    user_action_input = input("Please enter number of action list: ")

user_first_currency_input = input("Please provide first currency type: ")
user_second_currency_input = input("Please provide second currency type: ")
while user_first_currency_input not in currency_list and user_second_currency_input not in currency_list:
    user_first_currency_input = input("Please provide first currency type: ")
    user_second_currency_input = input("Please provide second currency type: ")

if user_action_input == "1":
    date_input()
elif user_action_input == "2":
    result = None
    while result is None:
        try:
            user_amount_input = int(input("Please enter amount number you want to convert: "))
            result = currency.convert(user_first_currency_input,user_second_currency_input,user_amount_input)
            print("%d %s to %s is %.2f" % (user_amount_input,user_first_currency_input,user_second_currency_input,result))
        except:
            print("Please enter number only.")
    






