import unittest
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import module to test
from modules.meal_plan import generate_meal_plan
from modules.subscription import generate_subscription_box

class TestUI(unittest.TestCase):
    
    def test_meal_plan_generation(self):
        # Test meal plan generation for different dietary goals
        high_protein_plan = generate_meal_plan(['High Protein'], None)
        self.assertIn('PROTEIN POWER', high_protein_plan)
        
        gut_health_plan = generate_meal_plan(['Gut Health'], None)
        self.assertIn('GUT MICROBIOME', gut_health_plan)
        
        plant_based_plan = generate_meal_plan(['Plant-Based'], None)
        self.assertIn('PLANT POWER', plant_based_plan)
        
        # Test default case with no goals
        default_plan = generate_meal_plan([], None)
        self.assertIn('SELECT A DIETARY GOAL', default_plan)
    
    def test_subscription_box_generation(self):
        # Test subscription box with empty products
        empty_box = generate_subscription_box(None)
        self.assertIn('NO ITEMS MATCH', empty_box)
        
        # Create a mock dataframe with minimal required columns for testing
        import pandas as pd
        mock_products = pd.DataFrame({
            'ProductName': ['Test Product 1', 'Test Product 2'],
            'Description': ['Test Description 1', 'Test Description 2'],
        })
        
        # Test with mock products
        box_with_products = generate_subscription_box(mock_products)
        self.assertIn('YOUR MONTHLY SUBSCRIPTION BOX', box_with_products)
        self.assertIn('Test Product', box_with_products)

if __name__ == '__main__':
    unittest.main()