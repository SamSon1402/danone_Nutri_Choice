import pandas as pd
import streamlit as st

# Cache the data loading to improve performance
@st.cache_data
def load_product_data():
    try:
        # Try to load from CSV file
        return pd.read_csv('data/mock_product_catalog.csv')
    except FileNotFoundError:
        # If file doesn't exist, create mock data
        from data.generate_data import create_mock_product_catalog
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