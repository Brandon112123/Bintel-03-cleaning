from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
data_file = PROJECT_ROOT / "data/prepared/customers_data_prepared.csv"
image_file = PROJECT_ROOT / "docs/images/customer_tiers.png"

df = pd.read_csv(data_file)

avg_points = df.groupby("CustomerTier")["LoyaltyPointsPts"].mean().round(2)
region_counts = df["Region"].value_counts()
tier_counts = df["CustomerTier"].value_counts()

print("\nAverage Loyalty Points by Tier")
print(avg_points)

print("\nCustomers by Region")
print(region_counts)

print("\nCustomer Tier Distribution")
print(tier_counts)

plt.figure(figsize=(7, 5))
avg_points.plot(kind="bar")
plt.title("Average Loyalty Points by Customer Tier")
plt.xlabel("Customer Tier")
plt.ylabel("Average Loyalty Points")
plt.xticks(rotation=0)
plt.tight_layout()

image_file.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(image_file)
plt.close()

print(f"\nChart saved to: {image_file}")
