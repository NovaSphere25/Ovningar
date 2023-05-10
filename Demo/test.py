import unittest
from demo import calculateDiscountedPrice

class TestDemo(unittest.TestCase):
    
    def test_not_member_less_than_1000_unchanged(self):
        #arrange
        isMember = False
        price = 800
        #act
        result = calculateDiscountedPrice(price,isMember)
        #assert
        self.assertEqual(result, 800)
        
    def test_member_cost_less_than_1000_price_changed(self):
        #arrange
        isMember = True
        price = 100
        #act
        result = calculateDiscountedPrice(price,isMember)
        #assert
        self.assertEqual(result, 98)
    
    def test_not_member_more_than_1000_less_than_5000_price_changed(self):
        #arrange
        isMember = False
        price = 2000
        #act
        result = calculateDiscountedPrice(price,isMember)
        #assert
        self.assertEqual(result, 1900)
        
    def test_member_more_than_1000_less_than_5000_price_changed(self):
        #arrange
        isMember = True
        price = 2000
        #act
        result = calculateDiscountedPrice(price,isMember)
        #assert
        self.assertEqual(result, 1860)
        
    def test_not_member_more_or_equal_than_5000_price_changed(self):
        #arrange
        isMember = False
        price = 5500
        #act
        result = calculateDiscountedPrice(price,isMember)
        #assert
        self.assertEqual(result, 5395)
        
    def test_member_more_or_equal_than_5000_price_changed(self):
        #arrange
        isMember = True
        price = 5500
        #act
        result = calculateDiscountedPrice(price,isMember)
        #assert
        self.assertEqual(result, 5285)
        
        
if __name__ == '__main__':
    unittest.main()
