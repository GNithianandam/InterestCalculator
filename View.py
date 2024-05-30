import streamlit as st
import datetime 
from Model import Calculate
st.set_page_config(
    page_title="Interest Calculator",
    
)
st.title("Interest calculator")
maxValueDate = datetime.date.today()
startDate = st.date_input("Select lend date", value=None,min_value = datetime.date(2001, 1, 12),max_value=maxValueDate)
interest = st.number_input("Interest per month in percentage")
lendAmount = st.number_input("Lent amount",min_value=0)
elapsedDay = st.number_input("Elapsed Days count as a month",min_value=0,max_value=30)
if st.button("Calculate"):
    months = Calculate.getTotalMonths(startDate,elapsedDay)
    totalInterest=Calculate.getTotalInterest(interest,lendAmount,months)
    totalAmountOwe= Calculate.getTotalOwe(totalInterest,lendAmount) 
    st.write("Total month is " ,months)   
    st.write("Interest per month is ", Calculate.getInterestPerMonth(interest,lendAmount)) 
    st.write("Total interest  ", totalInterest) 
    result="Total amount owe is " + str(totalAmountOwe)
    st.subheader(result)

