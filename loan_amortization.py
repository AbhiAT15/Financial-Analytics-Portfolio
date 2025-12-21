import pandas as pd
import numpy as np
import os

def generate_schedule(principal, annual_rate, years):
    # Standard EMI Formula
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    emi = principal * monthly_rate * (1 + monthly_rate)**months / ((1 + monthly_rate)**months - 1)
    
    schedule = []
    balance = principal
    
    for month in range(1, months + 1):
        interest_payment = balance * monthly_rate
        principal_payment = emi - interest_payment
        balance -= principal_payment
        
        schedule.append({
            "Month": month,
            "Opening Balance": round(balance + principal_payment, 2),
            "EMI": round(emi, 2),
            "Interest": round(interest_payment, 2),
            "Principal": round(principal_payment, 2),
            "Closing Balance": round(max(0, balance), 2)
        })
        
    return pd.DataFrame(schedule)

# --- RUN IT ---
loan_amount = 5000000  # 50 Lakhs
rate = 8.5
years = 20

print(f"Calculating Schedule for ₹{loan_amount} Loan...")
df = generate_schedule(loan_amount, rate, years)

filename = "loan_schedule.csv"
df.to_csv(filename, index=False)
print(f"DONE! Saved to: {filename}")