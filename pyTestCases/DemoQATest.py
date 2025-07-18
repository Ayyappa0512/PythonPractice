import sys
import os

# Add parent directory (project root) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from webTesting.Test1 import demoQATextBox
from webTesting.Test1 import add

def test_demo_QA_textbox():
    demoQATextBox()

# demoQATextBox()

def test_add():
    assert add(2, 3) == 5