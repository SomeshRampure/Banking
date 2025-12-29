import os
from dotenv import load_dotenv

load_dotenv()

# ParaBank URL
BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"

# Browser settings
BROWSER = "chrome"
HEADLESS = False
IMPLICIT_WAIT = 10

# Test data - ParaBank demo credentials
VALID_USERNAME = "somesh8"
VALID_PASSWORD = "demo123"
            
# Paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCREENSHOT_PATH = os.path.join(PROJECT_ROOT, "screenshots")
REPORT_PATH = os.path.join(PROJECT_ROOT, "reports")

# Create directories if not exist
os.makedirs(SCREENSHOT_PATH, exist_ok=True)
os.makedirs(REPORT_PATH, exist_ok=True)
