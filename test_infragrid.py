# test_infragrid.py
"""
Tests for InfraGrid module.
"""

import unittest
from infragrid import InfraGrid

class TestInfraGrid(unittest.TestCase):
    """Test cases for InfraGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InfraGrid()
        self.assertIsInstance(instance, InfraGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InfraGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
