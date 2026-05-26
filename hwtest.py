# Import Streamlit
import streamlit as st

# Import pandas
import pandas as pd

# Page title
st.title("Seller Dashboard")

# Read Excel file
df = pd.read_excel("sellers.xlsx")

# Show complete table
st.subheader("Complete Sellers Table")
st.dataframe(df)

# -------------------------
# FILTER BY REGION
# -------------------------

# Get all regions
regions = df["REGION"].unique()

# Create dropdown menu
selected_region = st.selectbox(
    "Select a Region",
    regions
)

# Filter data by region
filtered_region = df[df["REGION"] == selected_region]

# Show filtered table
st.subheader(f"Data for Region: {selected_region}")
st.dataframe(filtered_region)

# -------------------------
# GRAPHS
# -------------------------

# Graph section title
st.subheader("Graphs")

# Sold Units graph
st.write("Sold Units")
st.bar_chart(filtered_region["SOLD UNITS"])

# Total Sales graph
st.write("Total Sales")
st.bar_chart(filtered_region["TOTAL SALES"])

# Sales Average graph
st.write("Sales Average")
st.bar_chart(filtered_region["SALES AVERAGE"])

# -------------------------
# VENDOR FILTER
# -------------------------

# Combine name and lastname
df["FULL NAME"] = df["NAME"] + " " + df["LASTNAME"]

# Get all vendors
vendors = df["FULL NAME"].unique()

# Vendor dropdown
selected_vendor = st.selectbox(
    "Select a Vendor",
    vendors
)

# Filter vendor data
vendor_data = df[df["FULL NAME"] == selected_vendor]

# Show vendor information
st.subheader(f"Vendor Information: {selected_vendor}")
st.dataframe(vendor_data)

# -------------------------
# METRICS
# -------------------------

# Metrics section title
st.subheader("Quick Metrics")

# Create 3 columns
col1, col2, col3 = st.columns(3)

# Total sold units
with col1:
    st.metric(
        "Total Sold Units",
        int(filtered_region["SOLD UNITS"].sum())
    )

# Total sales
with col2:
    st.metric(
        "Total Sales",
        int(filtered_region["TOTAL SALES"].sum())
    )

# Average sales
with col3:
    st.metric(
        "Average Sales",
        round(filtered_region["SALES AVERAGE"].mean(), 2)
    )


# -------------------------
# BUTTON
# -------------------------

# Show complete data button
if st.button("Show Complete Data"):
    st.write(df)