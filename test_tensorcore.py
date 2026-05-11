# test_tensorcore.py
"""
Tests for TensorCore module.
"""

import unittest
from tensorcore import TensorCore

class TestTensorCore(unittest.TestCase):
    """Test cases for TensorCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TensorCore()
        self.assertIsInstance(instance, TensorCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TensorCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
