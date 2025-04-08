import unittest
import pandas as pd
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import module to test
from modules.recommendation import filter_products

class TestRecommendations(unittest.TestCase):
    
    def setUp(self):
        # Create a small test dataset
        self.test_data = pd.DataFrame({
            'ProductID': [1, 2, 3, 4],
            'ProductName': ['Test Yogurt', 'Test Drink', 'Test Water', 'Test Dessert'],
            'Brand': ['Activia', 'Alpro', 'Evian', 'Danone'],
            'Category': ['Yogurt', 'Plant-Based Drink', 'Water', 'Dessert'],
            'Tags': ['Gut Health;Probiotic', 'Plant-Based;High Protein', 'Hydration;Natural', 'Dessert;Sweet'],
            'IsPlantBased': [False, True, True, False],
            'IsLactoseFree': [False, True, True, False],
            'IsGlutenFree': [True, True, True, False]
        })
    
    def test_dietary_goal_filter(self):
        # Test filtering by dietary goal
        filtered = filter_products(self.test_data, ['High Protein'], [], [], None)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered.iloc[0]['ProductName'], 'Test Drink')
    
    def test_allergy_filter(self):
        # Test filtering by allergies
        filtered = filter_products(self.test_data, [], ['Lactose'], [], None)
        self.assertEqual(len(filtered), 2)
        self.assertTrue('Test Drink' in filtered['ProductName'].values)
        self.assertTrue('Test Water' in filtered['ProductName'].values)
    
    def test_brand_filter(self):
        # Test filtering by brand
        filtered = filter_products(self.test_data, [], [], ['Evian'], None)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered.iloc[0]['ProductName'], 'Test Water')
    
    def test_product_type_filter(self):
        # Test filtering by product type
        filtered = filter_products(self.test_data, [], [], [], 'Yogurt')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered.iloc[0]['ProductName'], 'Test Yogurt')
    
    def test_combined_filters(self):
        # Test combining multiple filters
        filtered = filter_products(self.test_data, [], ['Lactose', 'Gluten'], ['Alpro', 'Evian'], None)
        self.assertEqual(len(filtered), 2)
        self.assertTrue('Test Drink' in filtered['ProductName'].values)
        self.assertTrue('Test Water' in filtered['ProductName'].values)

if __name__ == '__main__':
    unittest.main()