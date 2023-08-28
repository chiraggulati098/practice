sales_price = float(input("Enter Sale Price of Property in USD: "))
down_payment = int(input("Enter Percentage of Down Payment: "))
loan_amount = ((100-down_payment)/100)*sales_price
print(f"Your Loan Amount: USD {loan_amount}")
loan_term = int(input("Enter Loan term in Years: "))
interest_rate = float(input("Enter Annual Interest Rate: "))
number_of_payments = 12*loan_term
monthly_payment = (loan_amount*(interest_rate/100)*(1+(interest_rate/100))*number_of_payments)/(((1+(interest_rate/100))*number_of_payments)-1)
total_loan = monthly_payment*number_of_payments
print(f"Your total Loan Amount will be ${round(total_loan,2)}")
print(f"Your Monthly Repayment will be ${round(monthly_payment,2)}")
print(f"Total Interest to be Paid is ${round(total_loan-loan_amount,2)}")