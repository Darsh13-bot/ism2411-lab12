# Lab 12 - Working with Files and CSV's
# Darsheel Panchal
#
# Q1: Python vs. Excel
# Python lets me write the steps once and rerun them automatically on huge
# files or new data every day, while Excel needs the same manual clicks each
# time. Excel is better for quick visual exploration, charts, and formatting,
# especially for non-programmers.

# Q2: Append mode
# An online store could log every order with a timestamp. Append mode is right
# because it adds new entries without erasing past ones, keeping a permanent
# record, whereas write mode would wipe the log on every run.

print("--- Exercise 2 ---")

import csv

with open("data/sales.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   

print("--- Exercise 3 ---")

with open("data/sales.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)
        
print("--- Exercise 4 ---")

total_revenue = 0
with open("data/sales.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        product, price, qty = row
        price = float(price)
        qty = int(qty)
        total = price * qty
        total_revenue += total
        print(f"{product}: {qty} units × ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:,.2f}")

print("--- Exercise 5 ---")

original_count = 0
written_count = 0
with open("data/sales.csv", "r", encoding="utf-8", newline="") as f_in, \
     open("data/cleaned.csv", "w", encoding="utf-8", newline="") as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    next(reader)  # skip input header
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        original_count += 1
        product, price, qty = row
        total = float(price) * int(qty)
        if total > 100:
            writer.writerow([product, price, qty, f"{total:.2f}"])
            written_count += 1
print(f"Wrote {written_count} of {original_count} rows to data/cleaned.csv")

print("--- Exercise 6 ---")

total_revenue = 0
with open("data/sales.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        qty = int(row["quantity"])
        total = price * qty
        total_revenue += total
        print(f"{product}: {qty} units * ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:,.2f}")

# The csv.reader gives plain lists, so its important to remember column positions
# but it is fine for simple, fixed files. csv.DictReader accesses columns by
# name, which is clearer and survives column reordering, so I prefer it over the csv.reader for the files.

print("--- Exercise 7 ---")

summary = {}
with open("data/sales.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:,.2f}")

print("--- Exercise 8 ---")

from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", "a", encoding="utf-8") as f:
    f.write(f"{timestamp} - Total revenue: ${total_revenue:,.2f}\n")
print("Appended one line to data/run_log.txt")