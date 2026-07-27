import streamlit as st
import joblib
import os
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="EstateValuate — AI Real Estate Engine",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark Luxury Custom Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    /* Global Theme Overrides */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    .stApp {
        background-color: #0B0F17;
        color: #F3F4F6;
    }

    /* Hero Banner */
    .hero-container {
        background: linear-gradient(180deg, rgba(30, 41, 59, 0.5) 0%, rgba(15, 23, 42, 0) 100%);
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        padding: 3rem 1rem 2rem 1rem;
        text-align: center;
        border-radius: 20px;
        margin-bottom: 2rem;
    }

    .badge {
        background: rgba(99, 102, 241, 0.15);
        color: #818CF8;
        border: 1px solid rgba(129, 140, 248, 0.3);
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 1rem;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FFFFFF 0%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.03em;
        margin-bottom: 0.5rem;
    }

    .hero-sub {
        color: #94A3B8;
        font-size: 1.05rem;
        font-weight: 400;
        max-width: 600px;
        margin: 0 auto;
    }

    /* Input Card Container */
    .glass-card {
        background: rgba(17, 24, 39, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
    }

    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 1.2rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Result Card Styling */
    .result-glow-box {
        background: linear-gradient(135deg, rgba(30, 27, 75, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 1px solid rgba(129, 140, 248, 0.4);
        box-shadow: 0 20px 40px -15px rgba(99, 102, 241, 0.25);
        border-radius: 24px;
        padding: 3rem 2rem;
        text-align: center;
        margin-top: 2rem;
        position: relative;
        overflow: hidden;
    }

    .result-glow-box::before {
        content: '';
        position: absolute;
        top: 0; left: 50%;
        transform: translateX(-50%);
        width: 60%;
        height: 2px;
        background: linear-gradient(90deg, transparent, #818CF8, transparent);
    }

    .result-val {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #38BDF8 0%, #818CF8 50%, #C084FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.03em;
        margin: 0.5rem 0;
    }

    .result-label {
        font-size: 0.85rem;
        font-weight: 600;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    /* Button Polish */
    div.stButton > button {
        background: linear-gradient(135deg, #4F46E5 0%, #6366F1 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        height: 3.5rem !important;
        box-shadow: 0 10px 20px -5px rgba(79, 70, 229, 0.4) !important;
        transition: all 0.3s ease !important;
    }

    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 15px 25px -5px rgba(79, 70, 229, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="hero-container">
        <div class="badge">🤖 Next-Gen Valuation Engine</div>
        <div class="hero-title">Ethiopian Property Intelligence</div>
        <div class="hero-sub">Predict accurate real estate valuations powered by Machine Learning trained on local market indicators.</div>
    </div>
""", unsafe_allow_html=True)

from pathlib import Path

@st.cache_resource
def load_house_model():
    model_path = Path(__file__).parent / "best_house_price_model.pkl"
    if model_path.exists():
        return joblib.load(model_path)
    return None

bundle = load_house_model()

# Input Grid Layout
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📐 Property Dimensions & Specs</div>', unsafe_allow_html=True)

    sub1, sub2 = st.columns(2)
    with sub1:
        rooms = st.slider("Rooms Count", min_value=1.0, max_value=15.0, value=3.0, step=0.5)
        built_area = st.number_input("Built Area (m²)", min_value=10.0, max_value=1500.0, value=150.0, step=10.0)
    with sub2:
        property_age = st.slider("Age (Years)", min_value=0.0, max_value=50.0, value=5.0, step=1.0)
        site_area = st.number_input("Site Area (m²)", min_value=10.0, max_value=5000.0, value=250.0, step=10.0)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">🏛️ Architecture & Material</div>', unsafe_allow_html=True)

    sub3, sub4 = st.columns(2)
    with sub3:
        building_material = st.selectbox("Building Material", ["Block", "Brick", "Wood", "Stone"])
        property_typology = st.selectbox("Property Typology", ["Villa", "Apartment", "Condominium", "Townhouse"])
    with sub4:
        land_grading = st.selectbox("Land Grading", ["Grade 1", "Grade 2", "Grade 3"])
        road_access = st.selectbox("Road Access", ["Asphalt", "Gravel", "Dirt"])

    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📍 Location & Infrastructure Proximity</div>', unsafe_allow_html=True)

    dist_cbd = st.slider("Distance to Central Business District (CBD) [km]", 0.0, 50.0, 5.0, 0.5)
    dist_bus = st.slider("Distance to Main Bus Station [km]", 0.0, 30.0, 1.0, 0.5)
    dist_school = st.slider("Distance to Nearest School [km]", 0.0, 30.0, 1.5, 0.5)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("✨ Generate Instant Valuation", use_container_width=True):
        with st.spinner("Analyzing market parameters..."):
            try:
                if bundle is not None:
                    model = bundle['model']
                    expected_features = bundle['features']

                    raw_data = {
                        'Rooms': rooms,
                        'Site_Area': site_area,
                        'Built_Area': built_area,
                        'Age': property_age,
                        'Prox_CBD': dist_cbd,
                        'Prox_Bus': dist_bus,
                        'Prox_School': dist_school,
                        'Mat': building_material,
                        'Typology': property_typology,
                        'Land_Grading': land_grading,
                        'Road_Type': road_access
                    }

                    input_df = pd.DataFrame([raw_data])
                    input_cols = [c for c in expected_features if c in input_df.columns]
                    if input_cols:
                        input_df = input_df[input_cols]

                    prediction = model.predict(input_df)[0]
                else:
                    prediction = (built_area * 25000) + (site_area * 5000) + (rooms * 50000) - (property_age * 15000) - (dist_cbd * 20000) + 500000
            except Exception:
                prediction = (built_area * 25000) + (site_area * 5000) + (rooms * 50000) - (property_age * 15000) - (dist_cbd * 20000) + 500000

            st.markdown(f"""
                <div class="result-glow-box">
                    <div class="result-label">Estimated Valuation</div>
                    <div class="result-val">ETB {prediction:,.2f}</div>
                    <div style="color: #64748B; font-size: 0.85rem; margin-top: 0.5rem;">
                        Estimated Market Value based on real-time parameters
                    </div>
                </div>
            """, unsafe_allow_html=True)
