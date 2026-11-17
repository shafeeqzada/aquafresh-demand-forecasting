import io
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image

st.set_page_config(page_title = "Aquafresh Dashboard", layout = "wide")
st.title("AquaFresh Demand Forecast Dashboard")

preds = pd.read_csv("backtest_results.csv")
data = pd.read_csv("data.csv")
region_err = pd.read_csv("error_by_region.csv")
product_err = pd.read_csv("error_by_product.csv")

merged = preds.merge(data[["date", "region", "product_type"]], on = "date")
merged["date"] = pd.to_datetime(merged["date"])

merged["abs_error"] = (merged["actual"] - merged["prophet_pred"]).abs()
merged["pct_error"] = merged["abs_error"] / merged["actual"] * 100

st.sidebar.header("Filters")
region = st.sidebar.selectbox("Region", sorted(merged["region"].unique()))
product = st.sidebar.selectbox("Product Type", sorted(merged["product_type"].unique()))

min_date = merged["date"].min().date()
max_date = merged["date"].max().date()
date_range = st.sidebar.date_input(
    "Date range", value = (min_date, max_date), min_value = min_date , max_value = max_date
)

if len(date_range) != 2:
    st.info("Please select both start and end dates.")
    st.stop()

start_date = pd.to_datetime(date_range[0])
end_date = pd.to_datetime(date_range[1])

seg = merged[
    (merged["region"] == region) &
    (merged["product_type"] == product) &
    (merged["date"] >= start_date) &
    (merged["date"]<= end_date)]

if len(seg) == 0:
    st.warning("No data for this selection. Try another region, product or date range")
    st.stop()

seg_mae = seg["abs_error"].mean()
seg_mape = seg["pct_error"].mean()

region_mae = region_err[region_err["region"] == region]["MAE"].iloc[0]
region_mape = region_err[region_err["region"]==region]["MAPE"].iloc[0]
product_mae = product_err[product_err["product_type"] == product]["MAE"].iloc[0]
product_mape = product_err[product_err["product_type"]== product]["MAPE"].iloc[0]
col1, col2, col3 = st.columns(3)
col1.metric("Days in segment", len(seg))
col2.metric("Segment MAE (liters)", round(seg_mae, 2))
col3.metric("Segment MAPE (%)", round(seg_mape, 2))

fig1 , ax1 = plt.subplots(figsize = (8, 3.5))
ax1.plot(seg["date"], seg["actual"], marker = "o", label = "Actual")
ax1.plot(seg["date"], seg["prophet_pred"], marker = "o", label = "Prophet Forcast")
ax1.set_title("Actual vs Prophet forcast: " + region + " / " + product)
ax1.set_xlabel("Date")
ax1.set_ylabel("Volume (liters)")
ax1.legend()
fig1.autofmt_xdate()
st.pyplot(fig1)

labels = ["Region:" + region, "Prophet: " + product, "Segment"]
maes = [region_mae, product_mae, seg_mae]
mapes = [region_mape, product_mape, seg_mape]

fig2 , axes = plt.subplots(1,2,figsize = (8, 3.5))
axes[0].bar(labels, maes, color = "steelblue")
axes[0].set_title("MAE (liters)")
axes[0].tick_params(axis = "x", labelrotation = 15, labelsize = 8)
axes[1].bar(labels , mapes, color = "black")
axes[1].set_title("MAPE (%)")
axes[1].tick_params(axis = "x", labelrotation = 15, labelsize = 8)
fig2.tight_layout()
st.pyplot(fig2)

with st.expander("Overall error charts from task 4"):
    st.image("region_error.png")
    st.image("product_error.png")

def fig_to(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format = "png", dpi = 120, bbox_inches= "tight")
    buf.seek(0)
    return buf

def make_pdf():
    pdf_buf = io.BytesIO()
    doc = SimpleDocTemplate(pdf_buf, pagesize = A4)
    styles = getSampleStyleSheet()
    story = []    

    story.append(Paragraph("Auqafresh Forcast Summary", styles["Title"]))
    story.append(Paragraph(
        "Region: " + region + " | Product: " + product + " | " 
        + str(start_date.date()) + " to " + str(end_date.date()),
        styles["Normal"]
    ))        
    story.append(Spacer(1,10))

    table_data = [
        ["level", "MAE (liters)", "MAPE (%)"],
        ["Region: " + region, round(region_mae, 2), round(region_mape, 2)],
        ["Product: " + product, round(product_mae, 2), round(product_mape, 2)],
        ["Segment (" +str(len(seg)) + "days)", round(seg_mae,2), round(seg_mape,2)],

    ]
    table = Table(table_data)
    table.setStyle(TableStyle([
        ("GRID", (0,0),(-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey)
    ]))
    story.append(table)
    story.append(Spacer(1,10))

    story.append(Image(fig_to(fig1), width = 450, height = 200))
    story.append(Spacer(1,6))
    story.append(Image(fig_to(fig2), width = 450, height= 200))
    doc.build(story)
    return pdf_buf.getvalue()


st.download_button(
    "Download PDF Summary",
    data = make_pdf(),
    file_name = "aquafresh_summary.pdf",
    mime = "application/pdf",
)    