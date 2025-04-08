import pandas as pd
import os

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
    
    # Create DataFrame
    df = pd.DataFrame(products)
    
    # Create directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Save to CSV
    df.to_csv('data/mock_product_catalog.csv', index=False)
    print("Mock product catalog created successfully!")
    return df

# Run the function if script is executed directly
if __name__ == "__main__":
    create_mock_product_catalog()