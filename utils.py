import base64
import streamlit as st
import os

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""

def render_navbar():
    # Modern global styles with background gradient and typography
    global_styles = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

    /* Global background and font */
    .stApp {
        background: linear-gradient(135deg, #f0f4f8 0%, #d9e2ec 100%);
        font-family: 'Outfit', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}

    /* Glassmorphism Navbar */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        padding: 12px 40px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.4);
        position: sticky;
        top: 0;
        z-index: 1000;
        margin-bottom: 30px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);
        border-radius: 0 0 20px 20px;
    }

    .navbar .left-section {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .navbar .app-name {
        font-size: 28px;
        font-weight: 700;
        color: #1a365d;
        cursor: pointer;
        background: linear-gradient(90deg, #2c3e50, #3498db);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        transition: transform 0.3s ease;
    }

    .navbar .app-name:hover {
        transform: translateY(-2px);
    }

    .navbar .nav-links {
        display: flex;
        align-items: center;
        gap: 30px;
    }

    .navbar .nav-links a {
        text-decoration: none;
        color: #4a5568;
        font-size: 16px;
        font-weight: 500;
        transition: all 0.3s ease;
        padding: 8px 12px;
        border-radius: 8px;
    }

    .navbar .nav-links a:hover {
        color: #3182ce;
        background: rgba(49, 130, 206, 0.1);
    }

    .navbar img {
        height: 50px;
        width: 50px;
        border-radius: 12px;
        object-fit: cover;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    .search-container {
        position: relative;
        display: flex;
        align-items: center;
    }

    .search-bar {
        padding: 10px 18px;
        padding-left: 40px;
        font-size: 14px;
        background: rgba(255, 255, 255, 0.5);
        border: 1px solid rgba(0, 0, 0, 0.05);
        border-radius: 12px;
        width: 220px;
        outline: none;
        transition: all 0.3s ease;
    }

    .search-bar:focus {
        width: 280px;
        background: white;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        border-color: #3182ce;
    }

    .search-icon {
        position: absolute;
        left: 15px;
        color: #a0aec0;
        pointer-events: none;
    }
    </style>
    """
    st.markdown(global_styles, unsafe_allow_html=True)

    # Load and encode logo
    logo_path = "pictures/logo.jpg"
    encoded_logo = get_base64_image(logo_path)
    
    navbar_html = f"""
    <div class="navbar">
        <div class="left-section">
            <img src="data:image/jpeg;base64,{encoded_logo}" alt="Logo">
            <div class="app-name" onclick="window.location.href='/'">HealthWise</div>
        </div>
        <div class="nav-links">
            <a href="/" target="_self">Home</a>
            <a href="/about" target="_self">About</a>
            <a href="/contact" target="_self">Contact</a>
            <div class="search-container">
                <span class="search-icon">🔍</span>
                <form action="/search" method="GET" style="margin: 0; display: inline-block;">
                    <input type="text" name="q" class="search-bar" placeholder="Search diseases..." required>
                </form>
            </div>
        </div>
    </div>
    """
    st.markdown(navbar_html, unsafe_allow_html=True)
