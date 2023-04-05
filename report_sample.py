from plugins.send_to_slack import send_to_slack
from plugins.transform.read_transform import append_all_files
import matplotlib.pyplot as plt



file_bytes = "output/sales_per_month.png"

    # analyze and create graph
    # read data
data = append_all_files('/Users/sanvi/Documents/project-1/automate_reports/data/sales_product_data/Sales_December_2019.csv')
    
    # transform data

data.drop(
    data[data["Quantity Ordered"] == "Quantity Ordered"].index, inplace=True)

data["total_price"] = data["Quantity Ordered"].astype(
    float) * data["Price Each"].astype(float)

data_transformed = data.groupby('Product').agg({"total_price": "sum"}).reset_index().tail(3)

print(data_transformed)

fig, ax = plt.subplots(2)

    # Membuat grafik Sales by Product
ax[0].bar(data_transformed['Product'], data_transformed['total_price'])
ax[0].set_xlabel('Product')
ax[0].set_ylabel('Total Sales (USD)')
  

#     # Membuat grafik Sales by Month
#     ax[1].bar(data_month['Order Date'].dt.month.astype(str), data_month['total_price'])
#     ax[1].set_xlabel('Month')
#     ax[1].set_ylabel('Total Sales (USD)')
#     ax[1].set_yticklabels(data_month['total_price'])

#     # Save graph ke image png
fig.savefig(file_bytes, bbox_inches='tight')

#     # send graph to slack channel
#     message = "This is the Revenue per product performance"
#     channel = "#automate_report"

send_to_slack.execute('Ini report hari ini', '#auto_report', file_bytes)

# if __name__ == '__main__':
#     run()
