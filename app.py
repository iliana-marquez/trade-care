import streamlit as st
from app_pages.multipage import MultiPage

# Import page scripts
from app_pages.page1_project_summary import page1_project_summary_body
from app_pages.page2_project_study import page2_project_study_body
from app_pages.page3_project_price_trade_predictor import page3_project_price_trade_predictor_body
from app_pages.page4_project_hypothesis import page4_project_hypothesis_body
from app_pages.page5_technical_overview import page5_technical_overview_body

# Create MultiPage instance
app = MultiPage(app_name="TradeCare - Bitcoin ML Prediction Tool")

# Add pages
app.add_page("📊 Project Summary", page1_project_summary_body)
app.add_page("📈 Data Study", page2_project_study_body)
app.add_page("🎯 Price & Trade Predictor", page3_project_price_trade_predictor_body)
app.add_page("🔬 Hypothesis Validation", page4_project_hypothesis_body)
app.add_page("⚙️ Technical Overview", page5_technical_overview_body)

# Run the app
app.run()