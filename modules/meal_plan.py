import pandas as pd

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
    return meal_plans["Balanced Nutrition Quest"] if products is not None and not products.empty else "No products match your criteria. Try adjusting your preferences to create a meal plan."