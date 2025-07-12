# test_tradepilot.py
"""
Tests for TradePilot module.
"""

import unittest
from tradepilot import TradePilot

class TestTradePilot(unittest.TestCase):
    """Test cases for TradePilot class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TradePilot()
        self.assertIsInstance(instance, TradePilot)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TradePilot()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
