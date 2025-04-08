import streamlit as st
import pandas as pd
import random
import os

# Set page config
st.set_page_config(
    page_title="Danone NutriQuest",
    page_icon="🎮",
    layout="wide",
)

# ---- UI COMPONENTS ----

def add_custom_css():
    # Define Danone-inspired colors based on the image
    danone_blue = "#0056a3"
    danone_red = "#e63329"
    danone_light_blue = "#E9F5FF"
    danone_yellow = "#FFD700"
    
    # Add a slightly different light blue for the background
    background_light_blue = "#DCF0FF"
    
    css = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=VT323&family=Space+Mono&display=swap');
        
        /* Global background color */
        .stApp {{
            background-color: {background_light_blue};
        }}
        
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
        
        /* Make sure text is readable with enhanced contrast */
        .stMarkdown {{
            color: #000000 !important;
        }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)

def pixel_divider():
    st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

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

def display_badge(number):
    html = f"""
    <div class="badge">{number}</div>
    """
    st.markdown(html, unsafe_allow_html=True)

# ---- DATA FUNCTIONS ----

# Create mock product data for Danone products
def create_mock_product_catalog():
    products = [
        {
            "ProductID": 1,
            "ProductName": "Activia Strawberry Yogurt",
            "Brand": "Activia",
            "Category": "Yogurt",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Activia",
            "Description": "Probiotic yogurt with real strawberry pieces",
            "Tags": "Gut Health;Probiotic;Lactose;Yogurt;Strawberry",
            "Protein_g": 5,
            "IsPlantBased": False,
            "IsLactoseFree": False,
            "IsGlutenFree": True
        },
        {
            "ProductID": 2,
            "ProductName": "Alpro Soya Chocolate",
            "Brand": "Alpro",
            "Category": "Plant-Based Drink",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Alpro",
            "Description": "Delicious chocolate flavored soya drink",
            "Tags": "Plant-Based;Lactose-Free;Gluten-Free;Chocolate",
            "Protein_g": 3,
            "IsPlantBased": True,
            "IsLactoseFree": True,
            "IsGlutenFree": True
        },
        {
            "ProductID": 3,
            "ProductName": "Danone Greek Honey",
            "Brand": "Danone",
            "Category": "Yogurt",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Danone",
            "Description": "Thick and creamy Greek yogurt with honey",
            "Tags": "High Protein;Lactose;Greek Yogurt;Honey",
            "Protein_g": 15,
            "IsPlantBased": False,
            "IsLactoseFree": False,
            "IsGlutenFree": True
        },
        {
            "ProductID": 4,
            "ProductName": "Evian Natural Mineral Water",
            "Brand": "Evian",
            "Category": "Water",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Evian",
            "Description": "Pure natural mineral water from the French Alps",
            "Tags": "Hydration;Mineral Water;Sugar-Free;Natural",
            "Protein_g": 0,
            "IsPlantBased": True,
            "IsLactoseFree": True,
            "IsGlutenFree": True
        },
        {
            "ProductID": 5,
            "ProductName": "Activia Vanilla Kefir",
            "Brand": "Activia",
            "Category": "Kefir",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Kefir",
            "Description": "Probiotic kefir drink with vanilla flavor",
            "Tags": "Gut Health;Probiotic;Kefir;Vanilla;High Calcium",
            "Protein_g": 4,
            "IsPlantBased": False,
            "IsLactoseFree": False,
            "IsGlutenFree": True
        },
        {
            "ProductID": 6,
            "ProductName": "Alpro Almond Unsweetened",
            "Brand": "Alpro",
            "Category": "Plant-Based Drink",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Almond",
            "Description": "Low calorie unsweetened almond drink",
            "Tags": "Plant-Based;Lactose-Free;Gluten-Free;Low Calorie;Almond",
            "Protein_g": 1,
            "IsPlantBased": True,
            "IsLactoseFree": True,
            "IsGlutenFree": True
        },
        {
            "ProductID": 7,
            "ProductName": "Danone High Protein Blueberry",
            "Brand": "Danone",
            "Category": "Yogurt",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=HighProtein",
            "Description": "High protein yogurt with blueberry flavor",
            "Tags": "High Protein;Lactose;Yogurt;Blueberry;Fitness",
            "Protein_g": 20,
            "IsPlantBased": False,
            "IsLactoseFree": False,
            "IsGlutenFree": True
        },
        {
            "ProductID": 8,
            "ProductName": "Velouté Mixed Fruit Yogurt",
            "Brand": "Danone",
            "Category": "Yogurt",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Veloute",
            "Description": "Creamy yogurt with mixed fruits",
            "Tags": "Creamy;Lactose;Yogurt;Mixed Fruit;Family",
            "Protein_g": 4,
            "IsPlantBased": False,
            "IsLactoseFree": False,
            "IsGlutenFree": True
        },
        {
            "ProductID": 9,
            "ProductName": "Alpro Oat Original",
            "Brand": "Alpro",
            "Category": "Plant-Based Drink",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Oat",
            "Description": "Creamy oat drink perfect for coffee",
            "Tags": "Plant-Based;Lactose-Free;Oat;Sustainable;Breakfast",
            "Protein_g": 2,
            "IsPlantBased": True,
            "IsLactoseFree": True,
            "IsGlutenFree": False
        },
        {
            "ProductID": 10,
            "ProductName": "Actimel Strawberry",
            "Brand": "Actimel",
            "Category": "Probiotic Drink",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Actimel",
            "Description": "Daily probiotic drink for immunity",
            "Tags": "Immunity;Probiotic;Lactose;Strawberry;Vitamin D",
            "Protein_g": 3,
            "IsPlantBased": False,
            "IsLactoseFree": False,
            "IsGlutenFree": True
        },
        {
            "ProductID": 11,
            "ProductName": "Danette Chocolate Pudding",
            "Brand": "Danone",
            "Category": "Dessert",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Danette",
            "Description": "Smooth chocolate pudding dessert",
            "Tags": "Dessert;Chocolate;Lactose;Sweet;Family",
            "Protein_g": 3,
            "IsPlantBased": False,
            "IsLactoseFree": False,
            "IsGlutenFree": True
        },
        {
            "ProductID": 12,
            "ProductName": "Alpro Coconut Yogurt",
            "Brand": "Alpro",
            "Category": "Plant-Based Yogurt",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Coconut",
            "Description": "Dairy-free coconut yogurt alternative",
            "Tags": "Plant-Based;Lactose-Free;Gluten-Free;Coconut;Creamy",
            "Protein_g": 2,
            "IsPlantBased": True,
            "IsLactoseFree": True,
            "IsGlutenFree": True
        },
        {
            "ProductID": 13,
            "ProductName": "Activia Mixed Berry",
            "Brand": "Activia",
            "Category": "Yogurt",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Activia",
            "Description": "Probiotic yogurt with mixed berries",
            "Tags": "Gut Health;Probiotic;Lactose;Yogurt;Berry",
            "Protein_g": 5,
            "IsPlantBased": False,
            "IsLactoseFree": False,
            "IsGlutenFree": True
        },
        {
            "ProductID": 14,
            "ProductName": "Evian+ Zinc & Magnesium",
            "Brand": "Evian",
            "Category": "Enhanced Water",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Evian+",
            "Description": "Mineral water enhanced with zinc and magnesium",
            "Tags": "Hydration;Mineral Water;Zinc;Magnesium;Fitness",
            "Protein_g": 0,
            "IsPlantBased": True,
            "IsLactoseFree": True,
            "IsGlutenFree": True
        },
        {
            "ProductID": 15,
            "ProductName": "Alpro Protein Chocolate",
            "Brand": "Alpro",
            "Category": "Plant-Based Drink",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=AlproProtein",
            "Description": "High protein plant-based chocolate drink",
            "Tags": "Plant-Based;High Protein;Lactose-Free;Gluten-Free;Chocolate",
            "Protein_g": 10,
            "IsPlantBased": True,
            "IsLactoseFree": True,
            "IsGlutenFree": True
        },
        {
            "ProductID": 16,
            "ProductName": "Danone Oykos Strawberry",
            "Brand": "Danone",
            "Category": "Yogurt",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Oykos",
            "Description": "Luxurious creamy yogurt with strawberry layer",
            "Tags": "Indulgent;Lactose;Yogurt;Strawberry;Dessert",
            "Protein_g": 4,
            "IsPlantBased": False,
            "IsLactoseFree": False,
            "IsGlutenFree": True
        },
        {
            "ProductID": 17,
            "ProductName": "Actimel Forest Fruits",
            "Brand": "Actimel",
            "Category": "Probiotic Drink",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Actimel",
            "Description": "Immunity-boosting probiotic drink with forest fruits flavor",
            "Tags": "Immunity;Probiotic;Lactose;Forest Fruits;Vitamin D",
            "Protein_g": 3,
            "IsPlantBased": False,
            "IsLactoseFree": False,
            "IsGlutenFree": True
        },
        {
            "ProductID": 18,
            "ProductName": "Alpro Greek Style Plain",
            "Brand": "Alpro",
            "Category": "Plant-Based Yogurt",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=AlproGreek",
            "Description": "Plant-based Greek-style yogurt alternative",
            "Tags": "Plant-Based;High Protein;Lactose-Free;Gluten-Free;Greek Style",
            "Protein_g": 8,
            "IsPlantBased": True,
            "IsLactoseFree": True,
            "IsGlutenFree": True
        },
        {
            "ProductID": 19,
            "ProductName": "Danone YoPro Vanilla",
            "Brand": "Danone",
            "Category": "High Protein Yogurt",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=YoPro",
            "Description": "High protein yogurt with vanilla flavor",
            "Tags": "High Protein;Lactose;Yogurt;Vanilla;Fitness",
            "Protein_g": 15,
            "IsPlantBased": False,
            "IsLactoseFree": False,
            "IsGlutenFree": True
        },
        {
            "ProductID": 20,
            "ProductName": "Volvic Touch of Fruit Lemon",
            "Brand": "Volvic",
            "Category": "Flavored Water",
            "ImageURL": "https://placehold.co/150x150/E9F5FF/0056a3?text=Volvic",
            "Description": "Natural mineral water with a hint of lemon",
            "Tags": "Hydration;Mineral Water;Low Calorie;Lemon;Refreshing",
            "Protein_g": 0,
            "IsPlantBased": True,
            "IsLactoseFree": True,
            "IsGlutenFree": True
        }
    ]
    
    return pd.DataFrame(products)

# Cache the data loading to improve performance
@st.cache_data
def load_product_data():
    try:
        # Try to load from CSV file if it exists
        data_path = 'data/mock_product_catalog.csv'
        if os.path.exists(data_path):
            return pd.read_csv(data_path)
        else:
            # Create mock data if file doesn't exist
            return create_mock_product_catalog()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        # Fallback to creating mock data
        return create_mock_product_catalog()

# Function to filter products based on user preferences
def filter_products(df, dietary_goals, allergies, preferred_brands, product_types):
    filtered_df = df.copy()
    
    # Filter by dietary goals
    if dietary_goals:
        # Create a temporary column to track matches
        filtered_df['match_goal'] = False
        
        # For each selected goal, mark products that have a matching tag
        for goal in dietary_goals:
            filtered_df.loc[filtered_df['Tags'].str.contains(goal, case=False), 'match_goal'] = True
        
        # Keep only products that matched at least one goal
        filtered_df = filtered_df[filtered_df['match_goal'] == True]
        
        # Drop the temporary column
        filtered_df = filtered_df.drop('match_goal', axis=1)
    
    # Filter by allergies/intolerances
    if allergies:
        if 'Lactose' in allergies:
            filtered_df = filtered_df[filtered_df['IsLactoseFree'] == True]
        if 'Gluten' in allergies:
            filtered_df = filtered_df[filtered_df['IsGlutenFree'] == True]
        if 'Nuts' in allergies:
            # For nuts, we'll filter based on tags since we don't have a specific column
            filtered_df = filtered_df[~filtered_df['Tags'].str.contains('Nut|Almond', case=False)]
    
    # Filter by preferred brands
    if preferred_brands:
        filtered_df = filtered_df[filtered_df['Brand'].isin(preferred_brands)]
    
    # Filter by product types
    if product_types:
        filtered_df = filtered_df[filtered_df['Category'] == product_types]
    
    return filtered_df

# Function to generate sample meal plan based on user goals
def generate_meal_plan(dietary_goals, products):
    # Simple meal plan generation based on primary goal
    meal_plans = {
        "High Protein": """
        🎮 YOUR PROTEIN POWER DAILY QUEST 🎮
        
        ⬛ MORNING MISSION: 
          - Danone High Protein Blueberry Yogurt with granola
          - Protein score: +50 XP!
        
        ⬛ MIDDAY BOOST: 
          - Alpro Soya Chocolate with a protein bar
          - Energy refill: +35 XP!
        
        ⬛ EVENING CHALLENGE: 
          - Greek yogurt with honey and mixed nuts
          - Recovery bonus: +45 XP!
        
        ⬛ POWER-UP SNACK: 
          - Actimel Strawberry for immunity boost
          - Defense shield activated: +25 XP!
        
        TOTAL PROTEIN SCORE: 155 XP - LEVEL UP! 💪
        """,
        
        "Gut Health": """
        🎮 GUT MICROBIOME ADVENTURE 🎮
        
        ⬛ MORNING POWER-UP: 
          - Activia Strawberry Yogurt with chia seeds
          - Probiotic boost: +40 XP!
        
        ⬛ MIDDAY MISSION: 
          - Mixed salad with Activia Vanilla Kefir dressing
          - Fiber collection: +30 XP!
        
        ⬛ EVENING QUEST: 
          - Vegetable stir-fry with prebiotic vegetables
          - Microbiome diversity: +45 XP!
        
        ⬛ BONUS STAGE: 
          - Actimel Strawberry shot before bed
          - Overnight restoration: +20 XP!
        
        TOTAL GUT HEALTH: 135 XP - DIGESTIVE SYSTEM LEVELED UP! 🌟
        """,
        
        "Plant-Based": """
        🎮 PLANT POWER ADVENTURE 🎮
        
        ⬛ SUNRISE STAGE: 
          - Alpro Oat Original with plant-based cereal
          - Morning energy: +30 XP!
        
        ⬛ MIDDAY GREEN QUEST: 
          - Vegetable wrap with Alpro Almond Unsweetened smoothie
          - Plant diversity: +45 XP!
        
        ⬛ SUNSET MISSION: 
          - Plant-based curry with Alpro Soya side
          - Protein collection: +40 XP!
        
        ⬛ HYDRATION CHECKPOINT: 
          - Evian Natural Mineral Water (1.5L daily)
          - Hydration bonus: +25 XP!
        
        TOTAL PLANT SCORE: 140 XP - ECO WARRIOR ACHIEVEMENT UNLOCKED! 🌱
        """,
        
        "Weight Management": """
        🎮 BALANCED NUTRITION QUEST 🎮
        
        ⬛ MORNING CHALLENGE: 
          - Activia Vanilla Kefir with fresh berries
          - Metabolism activation: +35 XP!
        
        ⬛ MIDDAY BALANCE: 
          - Lean protein with vegetables and Evian water
          - Satiety bonus: +40 XP!
        
        ⬛ EVENING PORTION CONTROL: 
          - Small plate with Danone Greek Honey for dessert
          - Craving defense: +30 XP!
        
        ⬛ SMART SNACK: 
          - Alpro Almond Unsweetened with apple slices
          - Low-calorie achievement: +25 XP!
        
        TOTAL BALANCE SCORE: 130 XP - STEADY PROGRESS ACHIEVEMENT! ⚖️
        """
    }
    
    if not dietary_goals:
        return """
        🎮 SELECT A DIETARY GOAL TO START YOUR NUTRITION QUEST! 🎮
        
        Choose your adventure path in the sidebar to generate your personalized meal plan.
        Each quest offers different power-ups and achievements!
        """
    
    # Return meal plan based on first selected goal, or default if not found
    primary_goal = dietary_goals[0]
    for goal_keyword, plan in meal_plans.items():
        if goal_keyword in primary_goal:
            return plan
    
    # Default meal plan if no match found
    return meal_plans["Weight Management"] if products is not None and not products.empty else "No products match your criteria. Try adjusting your preferences to create a meal plan."

# Generate a subscription box based on filtered products
def generate_subscription_box(filtered_products):
    if filtered_products is None or filtered_products.empty:
        return """
        🎮 NO ITEMS MATCH YOUR QUEST PARAMETERS! 🎮
        
        Adjust your character stats in the sidebar to discover products for your subscription box.
        """
    
    # Select up to 5 products randomly from filtered products
    num_products = min(5, len(filtered_products))
    box_products = filtered_products.sample(n=num_products)
    
    # Calculate total price (mock data)
    base_price = 15.99
    discount = 0.15 if num_products >= 4 else 0
    total_price = base_price * (1 - discount)
    
    # Add a random special item for the subscription box
    special_items = [
        "Limited Edition Pixel Art Danone Tumbler",
        "8-bit Nutrition Guide Booklet",
        "Retro Gaming Snack Container",
        "NutriQuest Character Sticker Pack",
        "Digital Power-Up Code for Bonus Content"
    ]
    special_item = random.choice(special_items)
    
    box_html = f"""
    <div style="background-color: white; border: 3px solid #0056a3; box-shadow: 8px 8px 0px 0px rgba(0,0,0,0.75); padding: 20px; margin-top: 20px;">
        <h3 style="font-family: 'VT323', monospace; font-size: 2rem; color: #0056a3; text-align: center; margin-bottom: 15px;">🎁 YOUR MONTHLY SUBSCRIPTION BOX 🎁</h3>
        
        <div style="font-family: 'Space Mono', monospace; margin-bottom: 20px; text-align: center; font-size: 1.2rem;">
            Level up your nutrition with monthly deliveries of your favorite Danone products!
        </div>
        
        <div style="border: 2px dashed #e63329; padding: 15px; margin-bottom: 20px;">
            <h4 style="font-family: 'VT323', monospace; color: #0056a3; margin-top: 0;">📦 BOX CONTENTS:</h4>
            <ul style="font-family: 'Space Mono', monospace; list-style-type: square;">
    """
    
    # Add each product to the box
    for _, product in box_products.iterrows():
        box_html += f"""
                <li><strong>{product['ProductName']}</strong> - {product['Description']}</li>
        """
    
    # Add special item
    box_html += f"""
                <li style="color: #e63329;"><strong>SPECIAL ITEM:</strong> {special_item}</li>
            </ul>
        </div>
        
        <div style="display: flex; justify-content: space-between; font-family: 'Space Mono', monospace; margin-top: 20px;">
            <div>
                <strong>Base Price:</strong> €{base_price:.2f}<br>
                <strong>Items:</strong> {num_products + 1} (including special item)<br>
                <strong>Discount:</strong> {int(discount * 100)}%
            </div>
            <div style="background-color: #FFD700; border: 3px solid black; padding: 10px; font-family: 'VT323', monospace; font-size: 1.5rem; box-shadow: 4px 4px 0px 0px rgba(0,0,0,0.5);">
                TOTAL: €{total_price:.2f}
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 20px; font-family: 'VT323', monospace; font-size: 1.2rem; color: #e63329;">
            🔄 SUBSCRIBE TO AUTOMATE YOUR NUTRITION QUEST! 🔄
        </div>
    </div>
    """
    
    return box_html

# ---- MAIN APP FUNCTION ----

def main():
    # Add custom CSS
    add_custom_css()
    
    # Load mock product data with caching
    products_df = load_product_data()
    
    # App header with retro styling
    st.markdown("<h1>DANONE NUTRIQUEST</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.5rem; margin-bottom: 30px;'>Power Up Your Nutrition Journey! 🎮</p>", unsafe_allow_html=True)
    
    # Retro-style game stats at the top
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        display_badge("LVL1")
        st.markdown("<p style='text-align: center; font-family: VT323, monospace;'>PLAYER LEVEL</p>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='text-align: center;'><h3 style='margin-bottom: 0px;'>0 XP</h3></div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-family: VT323, monospace;'>NUTRITION POINTS</p>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div style='text-align: center;'><h3 style='margin-bottom: 0px;'>0/3</h3></div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-family: VT323, monospace;'>ACHIEVEMENTS</p>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div style='text-align: center;'><h3 style='margin-bottom: 0px;'>ROOKIE</h3></div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-family: VT323, monospace;'>CURRENT RANK</p>", unsafe_allow_html=True)
    
    pixel_divider()
    
    # SIDEBAR - Create retro game-like user profile input
    st.sidebar.markdown("<h2>CHARACTER CREATION</h2>", unsafe_allow_html=True)
    
    # Dietary Goals
    st.sidebar.markdown("### SELECT YOUR QUEST")
    dietary_goals = st.sidebar.multiselect(
        "Choose your nutrition goals:",
        ["High Protein", "Gut Health", "Plant-Based", "Weight Management"],
    )
    
    # Allergies/Intolerances
    st.sidebar.markdown("### IMMUNITY SETTINGS")
    allergies = st.sidebar.multiselect(
        "Select your allergies/intolerances:",
        ["Lactose", "Gluten", "Nuts"]
    )
    
    # Preferred Brands
    st.sidebar.markdown("### FACTION ALLEGIANCE")
    preferred_brands = st.sidebar.multiselect(
        "Choose your preferred brands:",
        ["Activia", "Alpro", "Danone", "Evian", "Actimel", "Volvic"]
    )
    
    # Product Types
    st.sidebar.markdown("### ITEM CLASS")
    product_types = st.sidebar.radio(
        "Select your preferred product type:",
        ["All"] + list(products_df["Category"].unique())
    )
    
    # Convert "All" to None for filtering
    product_types = None if product_types == "All" else product_types
    
    # Game-like action button
    st.sidebar.markdown("")
    generate_button = st.sidebar.button("⚔️ GENERATE RECOMMENDATIONS ⚔️")
    
    # Health stats in sidebar
    st.sidebar.markdown("### CHARACTER STATS")
    display_health_stats(random.randint(60, 95), "PROTEIN")
    display_health_stats(random.randint(50, 85), "VITAMINS")
    display_health_stats(random.randint(40, 75), "HYDRATION")
    display_health_stats(random.randint(55, 90), "ENERGY")
    
    # MAIN AREA - Filter and display personalized recommendations
    if generate_button or dietary_goals or allergies or preferred_brands or product_types:
        # Apply filters to get personalized recommendations
        filtered_products = filter_products(products_df, dietary_goals, allergies, preferred_brands, product_types)
        
        # Retro-style loading animation
        progress_text = "ANALYZING NUTRITION DATA..."
        with st.spinner(progress_text):
            # Simulate processing time
            import time
            time.sleep(1)
        
        # Display heading with pixel styling
        st.markdown("<h2>YOUR PERSONALIZED POWER-UPS</h2>", unsafe_allow_html=True)
        
        if filtered_products.empty:
            st.error("NO ITEMS MATCH YOUR QUEST CRITERIA! Adjust your settings to discover products.")
        else:
            # Show number of recommended products
            st.markdown(f"<p style='font-family: VT323, monospace; font-size: 1.5rem;'>🎮 {len(filtered_products)} ITEMS DISCOVERED!</p>", unsafe_allow_html=True)
            
            # Display products in a grid layout
            cols = st.columns(3)
            for i, (_, product) in enumerate(filtered_products.iterrows()):
                with cols[i % 3]:
                    # Create product card with retro styling
                    html = f"""
                    <div class="product-card">
                        <div style="text-align: center;">
                            <img src="{product['ImageURL']}" style="width: 100px; height: 100px; border: 2px solid black; margin-bottom: 5px;">
                        </div>
                        <h3>{product['ProductName']}</h3>
                        <p style="font-family: 'Space Mono', monospace; font-size: 0.8rem; margin-bottom: 10px;">{product['Description']}</p>
                        <div style="margin-bottom: 10px;">
                    """
                    
                    # Add tags with pixel styling
                    tags = product['Tags'].split(';')
                    for tag in tags[:3]:  # Limit to first 3 tags
                        html += f'<span class="tag">{tag}</span>'
                    
                    # Add health stat bar
                    html += f"""
                        </div>
                        <div style="margin-top: 10px;">
                            <div class="health-stat-label">PROTEIN: {product['Protein_g']}g</div>
                            <div class="health-stat-bar">
                                <div class="health-stat-fill" style="width: {min(product['Protein_g'] * 5, 100)}%;"></div>
                            </div>
                        </div>
                    </div>
                    """
                    
                    st.markdown(html, unsafe_allow_html=True)
            
            pixel_divider()
            
            # Display sample meal plan
            st.markdown("<h2>DAILY NUTRITION QUEST</h2>", unsafe_allow_html=True)
            meal_plan = generate_meal_plan(dietary_goals, filtered_products)
            st.markdown(f"""
            <div style="background-color: white; border: 3px solid #0056a3; padding: 20px; box-shadow: 8px 8px 0px 0px rgba(0,0,0,0.75); font-family: 'Space Mono', monospace; white-space: pre-line;">
                {meal_plan}
            </div>
            """, unsafe_allow_html=True)
            
            # Generate subscription box
            st.markdown("<h2>MONTHLY LOOT BOX</h2>", unsafe_allow_html=True)
            subscription_box = generate_subscription_box(filtered_products)
            st.markdown(subscription_box, unsafe_allow_html=True)
    
    else:
        # Default screen before generating recommendations
        st.markdown("""
        <div style="text-align: center; padding: 40px 20px; background-color: white; border: 3px solid #0056a3; box-shadow: 8px 8px 0px 0px rgba(0,0,0,0.75);">
            <h2 style="margin-bottom: 20px;">WELCOME TO NUTRIQUEST!</h2>
            <p style="font-family: 'Space Mono', monospace; font-size: 1.2rem; margin-bottom: 20px;">Create your character profile in the sidebar to start your personalized nutrition adventure!</p>
            <div style="font-family: 'VT323', monospace; font-size: 2rem; color: #e63329; margin: 30px 0;">PRESS START TO BEGIN</div>
            <p style="font-family: 'Space Mono', monospace;">⬅️ Select your preferences and click "GENERATE RECOMMENDATIONS"</p>
        </div>
        """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()