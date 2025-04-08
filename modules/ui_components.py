import streamlit as st

# ---- CUSTOM CSS FOR RETRO GAMING AESTHETIC ----
def add_custom_css():
    # Define Danone-inspired colors based on the image
    danone_blue = "#0056a3"
    danone_red = "#e63329"
    danone_light_blue = "#E9F5FF"
    danone_yellow = "#FFD700"
    
    css = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=VT323&family=Space+Mono&display=swap');
        
        /* Main container styling */
        .main .block-container {{
            background-color: {danone_light_blue};
            padding: 2rem;
            border: 4px solid {danone_blue};
            box-shadow: 8px 8px 0px 0px rgba(0,0,0,0.75);
        }}
        
        /* Headers */
        h1, h2, h3, h4, h5, h6 {{
            font-family: 'VT323', monospace !important;
            color: {danone_blue} !important;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-shadow: 3px 3px 0px rgba(0,0,0,0.2);
        }}
        
        h1 {{
            font-size: 4rem !important;
            border-bottom: 4px solid {danone_red};
            padding-bottom: 10px;
        }}
        
        h2 {{
            font-size: 2.5rem !important;
            border-left: 8px solid {danone_red};
            padding-left: 10px;
            margin-top: 20px !important;
        }}
        
        /* Paragraphs and text */
        p, li, div {{
            font-family: 'Space Mono', monospace !important;
        }}
        
        /* Sidebar */
        .css-1d391kg {{
            background-color: {danone_blue};
        }}
        
        .sidebar .sidebar-content {{
            background-color: {danone_blue} !important;
            color: white !important;
            border-right: 4px solid {danone_red};
        }}
        
        /* Widget labels in sidebar */
        .sidebar label {{
            font-family: 'VT323', monospace !important;
            font-size: 1.2rem !important;
            color: white !important;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        /* Button styling */
        .stButton>button {{
            font-family: 'VT323', monospace !important;
            background-color: {danone_red} !important;
            color: white !important;
            border: 3px solid black !important;
            box-shadow: 4px 4px 0px 0px black;
            transition: all 0.1s ease;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-size: 1.2rem !important;
            margin-top: 10px;
        }}
        
        .stButton>button:hover {{
            transform: translate(2px, 2px);
            box-shadow: 2px 2px 0px 0px black;
        }}
        
        .stButton>button:active {{
            transform: translate(4px, 4px);
            box-shadow: 0px 0px 0px 0px black;
        }}
        
        /* Multiselect/Selectbox styling */
        .stMultiSelect, .stSelectbox {{
            background-color: {danone_light_blue} !important;
            border: 2px solid black !important;
        }}
        
        /* Expander styling */
        .streamlit-expander {{
            border: 3px solid {danone_blue} !important;
            background-color: white !important;
            box-shadow: 5px 5px 0px 0px rgba(0,0,0,0.5);
        }}
        
        .streamlit-expander .streamlit-expanderHeader {{
            font-family: 'VT323', monospace !important;
            font-size: 1.5rem !important;
            background-color: {danone_blue} !important;
            color: white !important;
        }}
        
        /* Success/Info message styling */
        .stSuccess, .stInfo {{
            font-family: 'Space Mono', monospace !important;
            border: 3px solid black !important;
            box-shadow: 5px 5px 0px 0px rgba(0,0,0,0.5);
        }}
        
        /* Pixel-style divider */
        .pixel-divider {{
            height: 5px;
            background: repeating-linear-gradient(to right, {danone_red} 0px, {danone_red} 10px, {danone_blue} 10px, {danone_blue} 20px);
            margin: 20px 0;
        }}
        
        /* Product card styling */
        .product-card {{
            background-color: white;
            border: 3px solid {danone_blue};
            box-shadow: 5px 5px 0px 0px rgba(0,0,0,0.5);
            padding: 15px;
            margin-bottom: 15px;
            transition: all 0.2s ease;
        }}
        
        .product-card:hover {{
            transform: translateY(-5px);
            box-shadow: 5px 10px 0px 0px rgba(0,0,0,0.5);
        }}
        
        .product-card h3 {{
            font-family: 'VT323', monospace !important;
            color: {danone_blue} !important;
            font-size: 1.5rem !important;
            margin-top: 5px !important;
            margin-bottom: 5px !important;
        }}
        
        .product-card .tag {{
            background-color: {danone_light_blue};
            border: 2px solid {danone_blue};
            padding: 3px 8px;
            margin-right: 5px;
            margin-bottom: 5px;
            display: inline-block;
            font-family: 'Space Mono', monospace !important;
            font-size: 0.7rem;
            font-weight: bold;
        }}
        
        /* Progress bar styling */
        .stProgress > div > div > div > div {{
            background-color: {danone_red} !important;
        }}
        
        /* Health stats bar styling */
        .health-stat {{
            margin-bottom: 10px;
        }}
        
        .health-stat-label {{
            font-family: 'VT323', monospace !important;
            font-size: 1.2rem;
            margin-bottom: 5px;
        }}
        
        .health-stat-bar {{
            height: 25px;
            background-color: #ddd;
            border: 2px solid black;
        }}
        
        .health-stat-fill {{
            height: 100%;
            background: repeating-linear-gradient(
                45deg,
                {danone_blue},
                {danone_blue} 10px,
                {danone_yellow} 10px,
                {danone_yellow} 20px
            );
        }}
        
        /* Badge styling */
        .badge {{
            background-color: {danone_yellow};
            border: 2px solid black;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'VT323', monospace !important;
            font-size: 1.5rem;
            color: black;
            margin: 0 auto;
            box-shadow: 3px 3px 0px 0px rgba(0,0,0,0.5);
        }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)

# Function to display pixel divider
def pixel_divider():
    st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Function to display gaming-style health stats
def display_health_stats(value, label):
    html = f"""
    <div class="health-stat">
        <div class="health-stat-label">{label}</div>
        <div class="health-stat-bar">
            <div class="health-stat-fill" style="width: {value}%;"></div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# Function to display a badge
def display_badge(number):
    html = f"""
    <div class="badge">{number}</div>
    """
    st.markdown(html, unsafe_allow_html=True)