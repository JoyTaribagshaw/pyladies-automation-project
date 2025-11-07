#!/bin/bash
# Quick Test Script for PyLadies Automation Demo
# Run this to verify everything works before your presentation

echo "======================================"
echo "  PyLadies Automation - Quick Test"
echo "======================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test 1: Check Python version
echo "📌 Checking Python version..."
python3 --version
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Python 3 is installed${NC}"
else
    echo -e "${RED}✗ Python 3 not found${NC}"
    exit 1
fi
echo ""

# Test 2: Check virtual environment
echo "📌 Checking virtual environment..."
if [ -d "venv" ]; then
    echo -e "${GREEN}✓ Virtual environment exists${NC}"
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        echo -e "${GREEN}✓ Virtual environment is activated${NC}"
    else
        echo -e "${YELLOW}⚠ Virtual environment exists but not activated${NC}"
        echo "  Run: source venv/bin/activate"
    fi
else
    echo -e "${YELLOW}⚠ Virtual environment not found${NC}"
    echo "  Creating virtual environment..."
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
    echo "  Run: source venv/bin/activate"
fi
echo ""

# Test 3: Check dependencies
echo "📌 Checking dependencies..."
if [[ "$VIRTUAL_ENV" != "" ]]; then
    pip install -q -r requirements.txt
    echo -e "${GREEN}✓ Dependencies installed${NC}"
else
    echo -e "${YELLOW}⚠ Activate virtual environment first to install dependencies${NC}"
fi
echo ""

# Test 4: Check .env file
echo "📌 Checking email configuration..."
if [ -f ".env" ]; then
    echo -e "${GREEN}✓ .env file exists${NC}"
    if grep -q "SENDER_EMAIL=your.email" .env; then
        echo -e "${YELLOW}⚠ .env file needs to be configured with real credentials${NC}"
    else
        echo -e "${GREEN}✓ .env file appears configured${NC}"
    fi
else
    echo -e "${YELLOW}⚠ .env file not found${NC}"
    echo "  Copy .env.example to .env and configure it"
    if [ -f ".env.example" ]; then
        echo "  Run: cp .env.example .env"
    fi
fi
echo ""

# Test 5: Check test directory
echo "📌 Checking test directory..."
TEST_DIR="$HOME/test_downloads"
if [ -d "$TEST_DIR" ]; then
    echo -e "${GREEN}✓ Test directory exists: $TEST_DIR${NC}"
    FILE_COUNT=$(ls -1 "$TEST_DIR" 2>/dev/null | wc -l)
    echo "  Contains $FILE_COUNT items"
else
    echo -e "${YELLOW}⚠ Test directory not found${NC}"
    echo "  Creating test directory with sample files..."
    mkdir -p "$TEST_DIR"
    cd "$TEST_DIR"
    touch report.pdf document.docx notes.txt
    touch photo1.jpg photo2.png screenshot.png
    touch script.py code.js style.css
    touch song.mp3 video.mp4
    touch archive.zip data.csv
    cd - > /dev/null
    echo -e "${GREEN}✓ Test directory created with sample files${NC}"
fi
echo ""

# Test 6: Test Python modules
echo "📌 Testing Python modules..."

echo "  - Testing file_organizer..."
python3 -c "import file_organizer; print('    ✓ file_organizer loaded')" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${RED}    ✗ Failed to load file_organizer${NC}"
fi

echo "  - Testing email_sender..."
python3 -c "import email_sender; print('    ✓ email_sender loaded')" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${RED}    ✗ Failed to load email_sender${NC}"
fi

echo "  - Testing web_automation..."
python3 -c "from web_automation import WebAutomation; print('    ✓ web_automation loaded')" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${RED}    ✗ Failed to load web_automation${NC}"
    echo -e "${YELLOW}    Note: Selenium requires Chrome/Chromium${NC}"
fi

echo "  - Testing schedule_demo..."
python3 -c "import schedule_demo; print('    ✓ schedule_demo loaded')" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${RED}    ✗ Failed to load schedule_demo${NC}"
fi
echo ""

# Test 7: Check Chrome/Chromium
echo "📌 Checking Chrome/Chromium for Selenium..."
if command -v chromium-browser &> /dev/null; then
    echo -e "${GREEN}✓ Chromium browser found${NC}"
elif command -v google-chrome &> /dev/null; then
    echo -e "${GREEN}✓ Google Chrome found${NC}"
else
    echo -e "${YELLOW}⚠ Chrome/Chromium not found${NC}"
    echo "  Install with: sudo apt-get install chromium-browser"
    echo "  Or webdriver-manager will download it automatically"
fi
echo ""

# Summary
echo "======================================"
echo "  Summary"
echo "======================================"
echo ""
echo "Your project structure:"
ls -1 *.py 2>/dev/null | sed 's/^/  - /'
echo ""

echo "Next steps:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Configure .env file with your email credentials"
echo "  3. Test each module individually"
echo "  4. Read TESTING_GUIDE.md for detailed instructions"
echo ""
echo -e "${GREEN}You're ready to start testing! 🚀${NC}"
