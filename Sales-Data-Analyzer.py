import pandas as pd
import matplotlib.pyplot as plt
# Store csv as DataFrame
dataframe = pd.read_csv(r"E:\coding\DATASETS\Sales Data\sales_data.csv")
# Calculate the total amount of each row
total_amt=dataframe.Quantity_Sold*dataframe.Unit_Price*(1-dataframe.Discount)
# Calculating the total revenue it made in year 2023
total_rev = round(total_amt.sum(),2)
print(f"Total Revenue: ₹{total_rev}")
# Calculating total profit
row_profit=dataframe.Quantity_Sold*(dataframe.Unit_Price - dataframe.Unit_Cost)*(1-dataframe.Discount)
profit = round(row_profit.sum(),2)
print(f"Total Profit: ₹{profit}")
# Checking for product-wise-sales
prod_wise_sale=dataframe.Product_Category.value_counts()
prod_wise_sale.to_csv("Product-Wise-Sale-Data")
# Picking the best-selling-product
best_selling_prod=prod_wise_sale.idxmax()
# For tracking the Monthly-Sales-Trend
months = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER' }
months_list = list(months.values())
sale_month = dataframe.Sale_Date.map(lambda x: months[x[3:5]])
monthly_sales_trend=sale_month.value_counts().reindex(months_list)
# Plotting graph for Data Visualization
graph = monthly_sales_trend.plot(kind='bar')
plt.title('Monthly Sales Data')
plt.xlabel('Months')
plt.ylabel('Number of Items')
plt.xticks(rotation=90)
plt.show()