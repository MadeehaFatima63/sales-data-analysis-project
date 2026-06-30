# ==========================================
# SALES DATA ANALYSIS PROJECT
# Author: Madeeha Fatima
# ==========================================

# ==========================================
# IMPORT LIBRARIES
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("SampleSuperstore.csv")

print("=" * 60)
print("SALES DATA ANALYSIS PROJECT")
print("=" * 60)

print("\nFirst 5 Rows")
print(df.head())

# ==========================================
# DATA EXPLORATION
# ==========================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print(df.info())

print("\n" + "=" * 60)
print("STATISTICAL SUMMARY")
print("=" * 60)

print(df.describe())

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)

duplicates = df.duplicated().sum()
print(f"Duplicate Rows: {duplicates}")

# ==========================================
# DATA CLEANING
# ==========================================

df = df.drop_duplicates()

print(f"\nDataset Shape After Cleaning: {df.shape}")

# Save cleaned dataset
df.to_csv("Cleaned_Superstore.csv", index=False)

print("Cleaned dataset saved successfully!")

# ==========================================
# EXPLORATORY DATA ANALYSIS
# ==========================================

print("\n" + "=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# Total Sales & Profit

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print(f"\nTotal Sales : ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")

# ==========================================
# SALES BY CATEGORY
# ==========================================

sales_by_category = (
    df.groupby("Category")["Sales"]
      .sum()
)

print("\nSales by Category")
print(sales_by_category)

# ==========================================
# SALES BY REGION
# ==========================================

sales_by_region = (
    df.groupby("Region")["Sales"]
      .sum()
)

print("\nSales by Region")
print(sales_by_region)

# ==========================================
# PROFIT BY CATEGORY
# ==========================================

profit_by_category = (
    df.groupby("Category")["Profit"]
      .sum()
)

print("\nProfit by Category")
print(profit_by_category)

# ==========================================
# TOP 10 STATES
# ==========================================

top_states = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop 10 States by Sales")
print(top_states)

# ==========================================
# TOP 10 SUB-CATEGORIES
# ==========================================

top_subcategories = (
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop 10 Sub-Categories by Sales")
print(top_subcategories)

# ==========================================
# PROFIT BY SUB-CATEGORY
# ==========================================

profit_subcategory = (
    df.groupby("Sub-Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print("\nProfit by Sub-Category")
print(profit_subcategory)

# ==========================================
# BAR CHART FUNCTION
# ==========================================

def create_bar_chart(
    data,
    title,
    filename,
    colors,
    ylabel="Amount ($)",
    rotate_labels=False
):

    plt.figure(figsize=(10,6))

    ax = data.plot(
        kind="bar",
        color=colors,
        edgecolor="black",
        width=0.7
    )

    plt.title(title, fontsize=18, fontweight="bold")
    plt.xlabel(data.index.name, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)

    if rotate_labels:
        plt.xticks(rotation=30, ha="right")
    else:
        plt.xticks(rotation=0)

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    max_value = data.max()

    for bar in ax.patches:
        plt.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height() + max_value*0.01,
            f"${bar.get_height():,.0f}",
            ha="center",
            fontsize=9
        )

    plt.tight_layout()

    plt.savefig(
        filename,
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
# ==========================================
# VISUALIZATION 1
# SALES BY CATEGORY
# ==========================================

create_bar_chart(
    sales_by_category,
    "Total Sales by Category",
    "charts/sales_by_category.png",
    [
        "#4E79A7",
        "#F28E2B",
        "#59A14F"
    ],
    ylabel="Sales ($)"
)

# ==========================================
# VISUALIZATION 2
# SALES BY REGION
# ==========================================

create_bar_chart(
    sales_by_region,
    "Total Sales by Region",
    "charts/sales_by_region.png",
    [
        "#E15759",
        "#76B7B2",
        "#59A14F",
        "#EDC948"
    ],
    ylabel="Sales ($)"
)

# ==========================================
# VISUALIZATION 3
# PROFIT BY CATEGORY
# ==========================================

create_bar_chart(
    profit_by_category,
    "Total Profit by Category",
    "charts/profit_by_category.png",
    [
        "#4E79A7",
        "#F28E2B",
        "#59A14F"
    ],
    ylabel="Profit ($)"
)

# ==========================================
# VISUALIZATION 4
# TOP 10 STATES
# ==========================================

create_bar_chart(
    top_states,
    "Top 10 States by Sales",
    "charts/top_10_states.png",
    [
        "#4E79A7",
        "#F28E2B",
        "#59A14F",
        "#E15759",
        "#76B7B2",
        "#EDC948",
        "#B07AA1",
        "#FF9DA7",
        "#9C755F",
        "#BAB0AC"
    ],
    ylabel="Sales ($)",
    rotate_labels=True
)

# ==========================================
# VISUALIZATION 5
# DISCOUNT VS PROFIT
# ==========================================

plt.figure(figsize=(10,6))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.6,
    color="#4E79A7"
)

plt.title(
    "Discount vs Profit",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Discount", fontsize=12)
plt.ylabel("Profit ($)", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "charts/discount_vs_profit.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================
# VISUALIZATION 6
# TOP 10 SUB-CATEGORIES
# ==========================================

create_bar_chart(
    top_subcategories,
    "Top 10 Sub-Categories by Sales",
    "charts/top_10_subcategories.png",
    [
        "#4E79A7",
        "#F28E2B",
        "#59A14F",
        "#E15759",
        "#76B7B2",
        "#EDC948",
        "#B07AA1",
        "#FF9DA7",
        "#9C755F",
        "#BAB0AC"
    ],
    ylabel="Sales ($)",
    rotate_labels=True
)

# ==========================================
# VISUALIZATION 7
# PROFIT BY SUB-CATEGORY
# ==========================================

create_bar_chart(
    profit_subcategory.head(10),
    "Top 10 Most Profitable Sub-Categories",
    "charts/profit_subcategory.png",
    [
        "#59A14F",
        "#76B7B2",
        "#4E79A7",
        "#F28E2B",
        "#EDC948",
        "#E15759",
        "#B07AA1",
        "#FF9DA7",
        "#9C755F",
        "#BAB0AC"
    ],
    ylabel="Profit ($)",
    rotate_labels=True
)
# ==========================================
# BUSINESS INSIGHTS
# ==========================================

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

print(f"Total Sales               : ${total_sales:,.2f}")
print(f"Total Profit              : ${total_profit:,.2f}")

print(f"\nHighest Sales Category    : {sales_by_category.idxmax()}")
print(f"Highest Profit Category   : {profit_by_category.idxmax()}")

print(f"\nBest Performing Region    : {sales_by_region.idxmax()}")

print(f"Best Performing State     : {top_states.idxmax()}")

print(f"\nBest Selling Sub-Category : {top_subcategories.idxmax()}")

print(f"Most Profitable Sub-Category : {profit_subcategory.idxmax()}")

print("\nProject Completed Successfully!")