# 🧪 Testing Guide for PyLadies Automation Presentation

This guide will help you test all the automation scripts and prepare for your 15-minute presentation.

## 📋 Pre-Presentation Checklist

### 1. Environment Setup (Do this FIRST!)

```bash
# Navigate to project directory
cd /home/joytarib/Documents/Project/pyladies

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Install Chrome/Chromium for Selenium
# Ubuntu/Debian:
sudo apt-get update
sudo apt-get install chromium-browser chromium-chromedriver

# Or use webdriver-manager (already in requirements.txt)
```

### 2. Email Configuration Setup

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your credentials
nano .env
# OR
code .env
```

**For Gmail Users:**
1. Go to https://myaccount.google.com/security
2. Enable 2-Factor Authentication
3. Generate an App Password: https://support.google.com/accounts/answer/185833
4. Use the App Password (not your regular password) in .env

## 🎯 Testing Each Module

### Test 1: File System Automation (5 minutes)

**Create Test Data:**
```bash
# Create a test directory with sample files
mkdir -p ~/test_downloads
cd ~/test_downloads

# Create various file types
touch report.pdf document.docx notes.txt
touch photo1.jpg photo2.png screenshot.png
touch script.py code.js style.css
touch song.mp3 video.mp4
touch archive.zip data.csv
```

**Run the Script:**
```bash
cd /home/joytarib/Documents/Project/pyladies
python3 file_organizer.py
# Choose option 1
# Enter path: /home/joytarib/test_downloads
```

**Expected Result:**
- Files organized into folders: images/, documents/, code/, audio/, video/, archives/, data/
- Check the log file: `file_organizer.log`

**Demo Script for Presentation:**
```
"Let's start with a common problem - a messy Downloads folder! 
Watch as Python automatically organizes these files by type in seconds..."
[Run the script]
"And just like that, everything is neatly organized! No more manual sorting."
```

---

### Test 2: Email Automation (5 minutes)

**Setup Test:**
```bash
# Make sure .env is configured
cat .env  # Should show your credentials (not in presentation!)

# Test email sending
python3 email_sender.py
```

**Test Options:**
1. **Simple Email**: Send to yourself first
2. **HTML Email**: Test formatted emails
3. **Weekly Report**: Test the automated report feature

**Expected Result:**
- Email delivered to recipient
- Check logs: `email_sender.log`
- Verify email formatting and content

**Demo Script for Presentation:**
```
"Next, let's automate those repetitive emails. 
No more copy-pasting the same message!"
[Show code for send_email function]
[Run script to send email]
"The email is sent! You can use this for reminders, reports, or any routine communication."
```

**⚠️ Presentation Tip:** Use a mock/demo mode to avoid sending real emails during live coding!

---

### Test 3: Web Automation (5 minutes)

**Test Google Search:**
```bash
python3 web_automation.py
# Choose option 1
# Enter query: "PyLadies automation"
```

**Expected Result:**
- Browser opens (or runs headless)
- Performs Google search
- Takes screenshot: `google_search_PyLadies_automation.png`
- Check logs: `web_automation.log`

**Test Form Filling:**
```bash
# You can use this test form: https://www.test-form.com/
# Or create your own simple HTML form for demo
```

**Demo Script for Presentation:**
```
"Now let's automate web interactions. 
Imagine filling out the same form repeatedly - let Python do it!"
[Show Selenium code]
[Run Google search demo]
"In seconds, Python searched, found results, and took a screenshot!"
```

---

### Test 4: Task Scheduling (5 minutes)

**Modify for Quick Demo:**
Edit `schedule_demo.py` to use shorter intervals for testing:

```python
# Change from:
interval='1'  # Every 1 minute
# To:
interval='minute'  # Every minute (better for demo)
```

**Run Scheduler:**
```bash
python3 schedule_demo.py
```

**Expected Result:**
- Jobs scheduled and listed
- Tasks run at specified intervals
- Logs show execution: `scheduler.log`
- Press Ctrl+C to stop

**Demo Script for Presentation:**
```
"The final piece - making it run automatically!
With the schedule library, your scripts become a persistent solution."
[Show scheduler code]
[Run briefly to show it working]
"Now it runs on its own - organize files daily, send reports weekly, 
or any schedule you need!"
```

---

## 🎬 Recording Your Presentation

### Option 1: OBS Studio (Recommended)
```bash
# Install OBS Studio
sudo apt-add-repository ppa:obsproject/obs-studio
sudo apt update
sudo apt install obs-studio
```

**Setup:**
1. Add "Screen Capture" source
2. Add "Audio Input Capture" (your microphone)
3. Set resolution: 1920x1080 (or 1280x720)
4. Set framerate: 30 FPS
5. Start Recording!

### Option 2: SimpleScreenRecorder
```bash
sudo apt-get install simplescreenrecorder
```

### Option 3: Kazam (Lightweight)
```bash
sudo apt-get install kazam
```

### Recording Checklist:
- ✅ Close unnecessary applications
- ✅ Set terminal font size to 14-16pt (readable on small screens)
- ✅ Use a simple, high-contrast terminal theme
- ✅ Test microphone audio levels
- ✅ Have all code files open in separate tabs
- ✅ Prepare demo data beforehand
- ✅ Do a full dry run first!

---

## 📝 15-Minute Presentation Outline

### **Intro (1 minute)**
- "Hi! I'm [your name], and I'm here to show you how Python can eliminate repetitive tasks."
- Show the problem: messy files, repetitive emails, manual web tasks

### **Demo 1: File Organization (3-4 minutes)**
- Show messy test_downloads folder
- Explain the code briefly (pathlib, file types)
- Run the script - watch it organize
- Highlight: error handling, logging

### **Demo 2: Email Automation (3-4 minutes)**
- Show email_sender.py code
- Explain smtplib basics
- Demo: send_email() function
- Show HTML email capability
- Emphasize: environment variables for security

### **Demo 3: Web Automation (3-4 minutes)**
- Show web_automation.py
- Explain Selenium setup
- Run Google search demo
- Show form filling capability
- Mention: headless mode for production

### **Demo 4: Scheduling (2-3 minutes)**
- Show schedule_demo.py
- Explain how schedule library works
- Run briefly to show automatic execution
- "Now it runs on its own!"

### **Wrap-up (1-2 minutes)**
- Best practices: error handling, logging, security
- Next steps: identify your own repetitive tasks
- Resources: point to documentation links
- Q&A

---

## 🎤 Presentation Tips

### Speaking Tips:
1. **Speak clearly and slowly** - remember, beginners are watching
2. **Explain as you code** - "Now I'm using pathlib to..."
3. **Show errors** - if something breaks, explain what happened
4. **Be enthusiastic** - your energy is contagious!

### Visual Tips:
1. **Large font** - 14-16pt minimum
2. **High contrast** - light background, dark text
3. **Zoom in** - if you're showing browser/terminal
4. **Clean workspace** - close unnecessary windows

### Technical Tips:
1. **Have backups** - if live demo fails, have a pre-recorded version
2. **Test everything** - run all scripts before recording
3. **Mock sensitive data** - use example emails, not real ones
4. **Internet connection** - web automation demo needs internet

---

## 🐛 Common Issues & Solutions

### Issue 1: Selenium WebDriver Not Found
```bash
# Solution 1: Install chromium-chromedriver
sudo apt-get install chromium-chromedriver

# Solution 2: Let webdriver-manager handle it (already in code)
# Just make sure selenium and webdriver-manager are installed
```

### Issue 2: Email Authentication Error
```bash
# Solution: Use App Password for Gmail
# Go to: https://support.google.com/accounts/answer/185833
# Generate a new App Password
# Use that in .env file, not your regular password
```

### Issue 3: Permission Denied on File Operations
```bash
# Solution: Use test directory instead of system directories
mkdir -p ~/test_downloads
# Use this path instead of actual Downloads
```

### Issue 4: Module Not Found
```bash
# Solution: Make sure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

---

## ✅ Final Pre-Recording Checklist

- [ ] Virtual environment activated
- [ ] All dependencies installed (`pip list` to verify)
- [ ] .env file configured (for email demo)
- [ ] Test data created in ~/test_downloads
- [ ] All scripts tested individually
- [ ] Chrome/Chromium installed for Selenium
- [ ] Recording software tested
- [ ] Microphone tested
- [ ] Terminal font size increased (14-16pt)
- [ ] Notes/script prepared
- [ ] Full dry run completed
- [ ] Timer set for 15 minutes
- [ ] Backup plan ready (screenshots/pre-recorded video)

---

## 🚀 Quick Test Run Script

Run this to test everything quickly:

```bash
#!/bin/bash
# quick_test.sh

echo "=== Quick Test Run ==="
echo ""

echo "1. Testing File Organizer..."
python3 file_organizer.py <<EOF
1
/home/joytarib/test_downloads
EOF

echo ""
echo "2. Testing Email Sender (dry run)..."
python3 -c "from email_sender import send_email; print('Email module loaded successfully')"

echo ""
echo "3. Testing Web Automation..."
python3 -c "from web_automation import WebAutomation; print('Selenium module loaded successfully')"

echo ""
echo "4. Testing Scheduler..."
python3 -c "from schedule_demo import TaskScheduler; print('Scheduler module loaded successfully')"

echo ""
echo "=== All modules loaded successfully! ==="
```

Make it executable and run:
```bash
chmod +x quick_test.sh
./quick_test.sh
```

---

## 📚 Additional Resources for Your Audience

Include these in your presentation closing:

1. **Python pathlib**: https://docs.python.org/3/library/pathlib.html
2. **smtplib**: https://docs.python.org/3/library/smtplib.html
3. **Selenium**: https://selenium-python.readthedocs.io/
4. **schedule library**: https://schedule.readthedocs.io/

Good luck with your presentation! You've got this! 🚀🐍
