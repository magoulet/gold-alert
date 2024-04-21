from pathlib import Path
import sys

# Get the current directory of the context.py file
CURRENT_DIR = Path(__file__).parent

# Get the parent directory (project root) and add it 
# to the Python path
PROJECT_ROOT = CURRENT_DIR.parent
sys.path.append(str(PROJECT_ROOT))
