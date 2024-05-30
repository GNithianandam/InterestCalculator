from datetime import *
from dateutil.relativedelta import *

class Calculate:
    @staticmethod
    def getTotalMonths(startDate, elapsedDays):
        #_startDate = datetime.strptime(startDate, "%Y-%m-%d")
        endDate = datetime.now()
        delta = relativedelta(endDate, startDate)      
        totalMonths = delta.years * 12 + delta.months
        if ((delta.days>= elapsedDays) and elapsedDays>0): totalMonths=totalMonths+1
        return totalMonths
    @staticmethod
    def getInterestPerMonth(interest,lendAmount):
        return lendAmount*(interest/100)
    @staticmethod
    def getTotalInterest(interest,lendAmount,months):
        monthlyInterestRate = interest / 100
        return lendAmount*monthlyInterestRate*months
    @staticmethod
    def getTotalOwe(amount,interest):
        return amount+interest
if __name__ == "__main__": 
    #Variable declaration
    d1='27/5/2023'
    lendAmount = 1000
    interest=1.0
    elapsedDay=4
    #Computation
    months = Calculate.getTotalMonths(d1,elapsedDay)
    totalInterest=Calculate.getTotalInterest(interest,lendAmount,months)
    totalAmountOwe= Calculate.getTotalOwe(totalInterest,lendAmount) 
    print('Total owe amount is ',totalAmountOwe)