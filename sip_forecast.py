import pandas as pd
import os

def sip_calculator(monthly_inv, return_rate, years, inflation):
    months = years * 12
    monthly_rate = return_rate / 12 / 100
    
    data = []
    invested = 0
    value = 0
    
    for m in range(1, months + 1):
        invested += monthly_inv
        value = (value + monthly_inv) * (1 + monthly_rate)
        
        # Real Value = Value / (1 + inflation)^years
        real_value = value / ((1 + inflation/12/100)**m)
        
        if m % 12 == 0: # Log every year
            data.append({
                "Year": int(m/12),
                "Total Invested": round(invested, 2),
                "Portfolio Value": round(value, 2),
                "Inflation Adjusted (Real)": round(real_value, 2)
            })
            
    return pd.DataFrame(data)

# --- RUN IT ---
print("Forecasting Wealth...")
df = sip_calculator(25000, 12, 20, 6) # 25k SIP, 12% return, 20 years, 6% inflation

filename = "sip_forecast.csv"
df.to_csv(filename, index=False)
print(f"DONE! Saved to: {filename}")