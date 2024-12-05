import matplotlib.pyplot as plt
import numpy as np


years_sales = np.arange(2017, 2028)
sales = [2382, 2982, 3351, 4248, 4988, 5311, 5784, 6330, 6876, 7467, 8034]

years_share = np.arange(2021, 2028)
share_percent = [18.8, 18.7, 19.4, 20.1, 21.0, 21.8, 22.6]

countries = ["Mexico", "Philippines", "Malaysia", "Argentina", "Brazil", "India", "Russia", "Japan", "Vietnam", "China"]
growth = [25.1, 24.1, 18, 17, 15.4, 15, 14, 12.7, 12, 11.4]

#Global E-Commerce Sales
plt.figure(figsize=(10, 6))
plt.plot(years_sales, sales, marker='o', label="E-Commerce Sales ($ Billion)")
plt.title("Global E-Commerce Sales (2017–2027)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Sales ($ Billion)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()

#E-Commerce Share of Retail Sales
plt.figure(figsize=(10, 6))
plt.bar(years_share, share_percent, color='teal', alpha=0.7)
plt.title("E-Commerce as Percentage of Total Retail Sales (2021–2027)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Percentage Share (%)", fontsize=12)
plt.tight_layout()
plt.show()

#Leading Countries in Retail E-Commerce Growth
plt.figure(figsize=(10, 6))
plt.barh(countries, growth, color='orange')
plt.title("Top Countries for E-Commerce Growth in 2023", fontsize=14)
plt.xlabel("Growth Rate (%)", fontsize=12)
plt.ylabel("Country", fontsize=12)
plt.gca().invert_yaxis() 
plt.tight_layout()
plt.show()
