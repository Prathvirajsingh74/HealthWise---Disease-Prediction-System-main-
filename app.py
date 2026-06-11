import streamlit as st
from utils import get_base64_image, render_navbar

# Set page configuration
st.set_page_config(page_title="HealthWise | Home", layout="wide", initial_sidebar_state="collapsed")



# Render consistent navbar
render_navbar()

# Load and encode images
hero_image_path = "pictures/fp.jpg"
pm_image = "pictures/pm.jpg"
ddi_image = "pictures/dsi.jpg"
feature_image_path = "pictures/predict.png"

encoded_hero_image = get_base64_image(hero_image_path)
encoded_feature_image = get_base64_image(feature_image_path)
encoded_pm_image = get_base64_image(pm_image)
encoded_ddi_image = get_base64_image(ddi_image)

# --- Hero Section ---
hero_section_html = f"""
<style>
    .hero {{
        position: relative;
        width: 100%;
        height: 550px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        overflow: hidden;
        border-radius: 30px;
        margin-bottom: 60px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        background: #000;
    }}
    
    .hero img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0.75;
        transition: transform 0.8s ease;
    }}

    .hero:hover img {{
        transform: scale(1.05);
    }}

    .hero-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(0,0,0,0.7));
    }}

    .hero-content {{
        position: absolute;
        z-index: 2;
        padding: 0 20px;
    }}

    .hero-text {{
        font-size: 64px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 20px;
        line-height: 1.1;
        letter-spacing: -1px;
    }}

    .hero-subtext {{
        font-size: 20px;
        font-weight: 300;
        color: rgba(255, 255, 255, 0.9);
        max-width: 650px;
        margin: 0 auto;
        line-height: 1.6;
    }}
</style>
<div class="hero">
    <img src="data:image/jpeg;base64,{encoded_hero_image}" alt="Health Banner">
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <div class="hero-text">Empowering Your<br>Health Journey</div>
        <div class="hero-subtext">
            Advanced disease prediction, essential precautions, and comprehensive health insights—all in one place to help you lead a healthier life.
        </div>
    </div>
</div>
"""
st.markdown(hero_section_html, unsafe_allow_html=True)

# --- Explore Our Features Section ---
st.markdown("""
<style>
    .features-heading {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        color: #1a365d;
        margin-bottom: 40px;
        position: relative;
    }
    .features-heading::after {
        content: '';
        width: 60px;
        height: 4px;
        background: #3182ce;
        display: block;
        margin: 15px auto 0;
        border-radius: 10px;
    }
</style>
<div class="features-heading">Our Core Capabilities</div>
""", unsafe_allow_html=True)


# --- Feature Cards ---
def feature_card(image_b64, title, description, link_url, btn_text):
    return f"""
    <style>
        .feature-card {{
            display: flex;
            align-items: center;
            background: rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 24px;
            padding: 30px;
            margin: 0 auto 30px;
            width: 90%;
            max-width: 950px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        }}
        .feature-card:hover {{
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.1);
            background: rgba(255, 255, 255, 0.8);
        }}
        .feature-card img {{
            width: 300px;
            height: 220px;
            object-fit: cover;
            border-radius: 18px;
            margin-right: 40px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        }}
        .feature-card-content {{
            flex: 1;
        }}
        .feature-card h3 {{
            font-size: 28px;
            color: #2d3748;
            margin-bottom: 15px;
            font-weight: 700;
        }}
        .feature-card p {{
            font-size: 17px;
            color: #4a5568;
            line-height: 1.6;
            margin-bottom: 25px;
        }}
        .feature-card button {{
            background: #3182ce;
            color: white;
            padding: 14px 32px;
            border: none;
            border-radius: 14px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 14px rgba(49, 130, 206, 0.4);
        }}
        .feature-card button:hover {{
            background: #2b6cb0;
            box-shadow: 0 6px 20px rgba(49, 130, 206, 0.6);
            transform: translateY(-2px);
        }}
        @media (max-width: 768px) {{
            .feature-card {{
                flex-direction: column;
                text-align: center;
            }}
            .feature-card img {{
                margin-right: 0;
                margin-bottom: 20px;
                width: 100%;
            }}
        }}
    </style>
    <div class="feature-card">
        <img src="data:image/jpeg;base64,{image_b64}" alt="{title}">
        <div class="feature-card-content">
            <h3>{title}</h3>
            <p>{description}</p>
            <a href="{link_url}" target="_self">
                <button>{btn_text}</button>
            </a>
        </div>
    </div>
    """

# Render Feature Cards
st.markdown(feature_card(
    encoded_feature_image, 
    "Disease Prediction", 
    "Leverage our advanced machine learning model to analyze your symptoms and identify potential health risks with high accuracy.", 
    "/diseaseprediction", 
    "Start Prediction"
), unsafe_allow_html=True)

st.markdown(feature_card(
    encoded_pm_image, 
    "Precautionary Measures", 
    "Stay ahead of health issues with tailored advice and preventive steps for a wide range of common medical conditions.", 
    "/precautions", 
    "View Precautions"
), unsafe_allow_html=True)

st.markdown(feature_card(
    encoded_ddi_image, 
    "Disease Information", 
    "Deep dive into our medical database to understand causes, symptoms, and care guidelines for various diseases.", 
    "/description", 
    "Learn More"
), unsafe_allow_html=True)

