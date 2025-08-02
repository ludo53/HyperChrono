# test_hyperchrono.py
"""
Tests for HyperChrono module.
"""

import unittest
from hyperchrono import HyperChrono

class TestHyperChrono(unittest.TestCase):
    """Test cases for HyperChrono class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HyperChrono()
        self.assertIsInstance(instance, HyperChrono)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HyperChrono()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
