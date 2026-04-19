import pandas as pd

data = [
    [1001, "01-01-2024", "Rice 5kg", "Grocery", "North", 2, 400, "UPI", "Delivered"],
    [1002, "02-01-2024", "Soap Pack", "FMCG", "South", 3, 120, "COD", "Delivered"],
    [1003, "03-01-2024", "iPhone 14", "Electronics", "West", 1, 70000, "Credit Card", "Delivered"],
    [1004, "04-01-2024", "Shampoo", "FMCG", "East", 2, 250, "Debit Card", "Returned"],
    [1005, "05-01-2024", "Cooking Oil 1L", "Grocery", "North", 4, 150, "UPI", "Delivered"],
    [1006, "06-01-2024", "Sugar 1kg", "Grocery", "West", 5, 50, "COD", "Delivered"],
    [1007, "07-01-2024", "Boat Headphones", "Electronics", "South", 2, 1500, "UPI", "Delivered"],
    [1008, "08-01-2024", "HP Laptop", "Electronics", "North", 1, 55000, "Credit Card", "Delivered"],
    [1009, "09-01-2024", "Detergent Powder", "FMCG", "East", 3, 350, "Debit Card", "Cancelled"],
    [1010, "10-01-2024", "Wheat Flour 10kg", "Grocery", "South", 2, 500, "UPI", "Delivered"],
    [1011, "11-01-2024", "Face Wash", "FMCG", "North", 2, 220, "COD", "Delivered"],
    [1012, "12-01-2024", "Samsung S23", "Electronics", "West", 1, 65000, "Credit Card", "Delivered"],
    [1013, "13-01-2024", "Salt 1kg", "Grocery", "East", 6, 20, "UPI", "Delivered"],
    [1014, "14-01-2024", "Toothpaste", "FMCG", "South", 3, 180, "Debit Card", "Returned"],
    [1015, "15-01-2024", "Dell Monitor", "Electronics", "North", 1, 12000, "Credit Card", "Delivered"],
    [1016, "16-01-2024", "Soap Pack", "FMCG", "West", 4, 120, "UPI", "Delivered"],
    [1017, "17-01-2024", "Cooking Oil 1L", "Grocery", "East", 3, 150, "COD", "Delivered"],
    [1018, "18-01-2024", "Rice 5kg", "Grocery", "South", 2, 400, "UPI", "Cancelled"],
    [1019, "19-01-2024", "HP Laptop", "Electronics", "West", 1, 55000, "Credit Card", "Delivered"],
    [1020, "20-01-2024", "Shampoo", "FMCG", "North", 2, 250, "Debit Card", "Delivered"]
]

columns = [
    "Order ID", "Order Date", "Product Name", "Category",
    "Region", "Quantity", "Price",
    "Payment Mode", "Order Status"
]

df = pd.DataFrame(data, columns=columns)

# Calculate Total Sales
df["Total Sales"] = df["Quantity"] * df["Price"]

# Save to Excel
df.to_excel("amazon_sales_dataset.xlsx", index=False)

print("Excel file with more data created successfully!")
