'''
- Personal investment
Create a single recursive function (or more if you wish), which can answer the first three questions below
For each question, make an appropriate call to the function. (5pts each)
'''

#1.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY, so MPR is APR/12).
# Assuming you make no payments for 6 months, what is your new balance?  Solve recursively.
def personal_investment(money, apr, months, month, payment):
    mpr = apr / 12
    money = money + (money * (mpr)) - payment
    month += 1
    if month != months:
        personal_investment(money, apr, months, month, payment)
    else:
        print(round(money), month)
personal_investment(10000, 0.2, 6, 0, 0)
#2.  You have $5000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).
# You make the minimum payment of $100 per month for 36 months.  What is your new balance?  Solve recursively.
personal_investment(5000,0.2,36,0,100)

#3.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).
# If you make the minimum payment of $100 per month, how many months will it take to pay it off?  Solve recursively.
personal_investment(10000,0.2,100,0,100)
#You can never pay it off

#4  Pyramid of Cubes - (10pts) If you stack boxes in a pyramid, the top row would have 1 box,
# the second row would have two, the third row would have 3 and so on.
# Make a recursive function which calculates the TOTAL NUMBER OF BOXES for a pyramid of boxes n high.
# For instance, a pyramid that is 3 high would have a total of 6 boxes.  A pyramid 4 high would have 10.
def pyramid(start, n, count):
    start += 1
    count += start
    if start < n:
        pyramid(start,n,count)
    else:
        print(count)

pyramid(0, 3, 0)