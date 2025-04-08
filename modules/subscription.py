import random

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