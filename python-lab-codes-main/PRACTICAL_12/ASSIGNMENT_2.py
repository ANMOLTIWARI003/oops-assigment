"""
Practical No: 12
Lab Assignment-2
Clothing Inventory Table (Amazon Outlet):
  ITEM_ID | ITEM_NAME      | CATEGORY    | PRICE | STOCK | SUPPLIER
  C101    | Denim Jeans    | Bottomwear  | 1500  | 30    | Levis
  C102    | Cotton Shirt   | Topwear     | 1200  | 50    | Raymond
  C103    | Silk Saree     | Ethnicwear  | 5000  | 20    | Fabindia
  C104    | Woolen Sweater | Winterwear  | 2000  | 15    | Spark
  C105    | Sports T-Shirt | Active Wear | 800   | 60    | Nike

Supplier Details Table (Amazon Outlet):
  SUPPLIER_ID | SUPPLIER_NAME | CONTACT    | LOCATION
  S201        | Levi's        | 9876543210 | Mumbai
  S202        | Raymond       | 9123456789 | Delhi
  S203        | Fabindia      | 9988776655 | Bangalore
  S204        | Monte Carlo   | 9345678123 | Chandigarh
  S205        | Nike          | 9234567890 | Pune

Perform the required operations.
"""

import pandas as pd
import sqlite3

# ── Create the DataFrames ──────────────────────────────────────────────────────
inventory_data = {
    "ITEM_ID":   ["C101","C102","C103","C104","C105"],
    "ITEM_NAME": ["Denim Jeans","Cotton Shirt","Silk Saree",
                  "Woolen Sweater","Sports T-Shirt"],
    "CATEGORY":  ["Bottomwear","Topwear","Ethnicwear","Winterwear","Active Wear"],
    "PRICE":     [1500, 1200, 5000, 2000, 800],
    "STOCK":     [30, 50, 20, 15, 60],
    "SUPPLIER":  ["Levis","Raymond","Fabindia","Spark","Nike"]
}

supplier_data = {
    "SUPPLIER_ID":   ["S201","S202","S203","S204","S205"],
    "SUPPLIER_NAME": ["Levi's","Raymond","Fabindia","Monte Carlo","Nike"],
    "CONTACT":       [9876543210, 9123456789, 9988776655, 9345678123, 9234567890],
    "LOCATION":      ["Mumbai","Delhi","Bangalore","Chandigarh","Pune"]
}

inv_df = pd.DataFrame(inventory_data)
sup_df = pd.DataFrame(supplier_data)

# ── Load into SQLite ───────────────────────────────────────────────────────────
conn = sqlite3.connect(":memory:")
inv_df.to_sql("INVENTORY", conn, index=False, if_exists="replace")
sup_df.to_sql("SUPPLIER",  conn, index=False, if_exists="replace")

def run_query(title, sql):
    print("=" * 68)
    print(f" {title}")
    print("=" * 68)
    result = pd.read_sql_query(sql, conn)
    print(result.to_string(index=False))
    print()
    return result

# ──────────────────────────────────────────────────────────────────────────────
# 1. Display all items available in the inventory
# ──────────────────────────────────────────────────────────────────────────────
run_query("ALL ITEMS IN INVENTORY",
    "SELECT * FROM INVENTORY")

# ──────────────────────────────────────────────────────────────────────────────
# 2. Display all supplier details
# ──────────────────────────────────────────────────────────────────────────────
run_query("ALL SUPPLIER DETAILS",
    "SELECT * FROM SUPPLIER")

# ──────────────────────────────────────────────────────────────────────────────
# 3. Display item with highest price
# ──────────────────────────────────────────────────────────────────────────────
run_query("MOST EXPENSIVE ITEM",
    "SELECT * FROM INVENTORY WHERE PRICE = (SELECT MAX(PRICE) FROM INVENTORY)")

# ──────────────────────────────────────────────────────────────────────────────
# 4. Display item with lowest price
# ──────────────────────────────────────────────────────────────────────────────
run_query("CHEAPEST ITEM",
    "SELECT * FROM INVENTORY WHERE PRICE = (SELECT MIN(PRICE) FROM INVENTORY)")

# ──────────────────────────────────────────────────────────────────────────────
# 5. Display items with stock less than 25
# ──────────────────────────────────────────────────────────────────────────────
run_query("ITEMS WITH STOCK < 25 (Low Stock Alert)",
    "SELECT ITEM_ID, ITEM_NAME, STOCK FROM INVENTORY WHERE STOCK < 25")

# ──────────────────────────────────────────────────────────────────────────────
# 6. Calculate total inventory value (price × stock) for each item
# ──────────────────────────────────────────────────────────────────────────────
run_query("TOTAL INVENTORY VALUE PER ITEM",
    """SELECT ITEM_ID, ITEM_NAME, PRICE, STOCK,
              (PRICE * STOCK) AS TOTAL_VALUE
       FROM INVENTORY
       ORDER BY TOTAL_VALUE DESC""")

# ──────────────────────────────────────────────────────────────────────────────
# 7. Display items sorted by price (ascending)
# ──────────────────────────────────────────────────────────────────────────────
run_query("ITEMS SORTED BY PRICE (Ascending)",
    "SELECT * FROM INVENTORY ORDER BY PRICE ASC")

# ──────────────────────────────────────────────────────────────────────────────
# 8. Display items by category
# ──────────────────────────────────────────────────────────────────────────────
run_query("ITEMS GROUPED BY CATEGORY",
    """SELECT CATEGORY, COUNT(*) AS TOTAL_ITEMS,
              SUM(STOCK) AS TOTAL_STOCK,
              ROUND(AVG(PRICE),2) AS AVG_PRICE
       FROM INVENTORY
       GROUP BY CATEGORY
       ORDER BY TOTAL_STOCK DESC""")

# ──────────────────────────────────────────────────────────────────────────────
# 9. JOIN: Inventory items with their Supplier details
# ──────────────────────────────────────────────────────────────────────────────
run_query("INVENTORY WITH SUPPLIER DETAILS (JOIN)",
    """SELECT I.ITEM_ID, I.ITEM_NAME, I.CATEGORY, I.PRICE, I.STOCK,
              S.SUPPLIER_NAME, S.CONTACT, S.LOCATION
       FROM INVENTORY I
       JOIN SUPPLIER S
         ON UPPER(TRIM(I.SUPPLIER)) = UPPER(TRIM(S.SUPPLIER_NAME))
       ORDER BY I.ITEM_ID""")

# ──────────────────────────────────────────────────────────────────────────────
# 10. Items with price between 1000 and 3000
# ──────────────────────────────────────────────────────────────────────────────
run_query("ITEMS WITH PRICE BETWEEN Rs.1000 AND Rs.3000",
    "SELECT * FROM INVENTORY WHERE PRICE BETWEEN 1000 AND 3000")

conn.close()
print("All queries executed successfully.")