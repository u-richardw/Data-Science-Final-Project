
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sales_data = pd.read_csv("../data/e_commerce_sales.csv")
share_data = pd.read_csv("../data/e_commerce_share.csv")
growth_data = pd.read_csv("../data/country_growth_2023.csv")


print(sales_data.isnull().sum())
print(share_data.isnull().sum())
print(growth_data.isnull().sum())

#Global E-Commerce Sales (2017–2027)
plt.figure(figsize=(10, 6))
plt.plot(sales_data["Year"], sales_data["Sales ($ Billion)"], marker='o', color='blue', label="E-Commerce Sales")
plt.title("Global E-Commerce Sales (2017–2027)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Sales ($ Billion)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.savefig("../graph/e_commerce_sales_trend.png")  
plt.show()

#E-Commerce Share of Retail Sales (2021–2027)
plt.figure(figsize=(10, 6))
sns.barplot(x="Year", y="E-Commerce Share (%)", data=share_data, color="teal")
plt.title("E-Commerce Share of Retail Sales (2021–2027)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Percentage Share (%)", fontsize=12)
plt.savefig("../graph/retail_share_growth.png")
plt.show()

#Top Countries for E-Commerce Growth (2023)
plt.figure(figsize=(10, 6))
sns.barplot(y="Country", x="Growth Rate (%)", data=growth_data, palette="viridis")
plt.title("Top Countries for E-Commerce Growth in 2023", fontsize=14)
plt.xlabel("Growth Rate (%)", fontsize=12)
plt.ylabel("Country", fontsize=12)
plt.savefig("../graph/country_growth_2023.png")
plt.show()
