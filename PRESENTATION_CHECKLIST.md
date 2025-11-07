# 📋 Presentation Day Checklist

Use this checklist on the day of your presentation/recording!

## ⏰ 30 Minutes Before

- [ ] Close ALL unnecessary applications and browser tabs
- [ ] Silence notifications (phone and computer)
- [ ] Clear desktop of clutter
- [ ] Set "Do Not Disturb" mode

## 🖥️ Terminal Setup

- [ ] Terminal font size: 14-16pt (for readability)
- [ ] Terminal theme: High contrast (light background recommended)
- [ ] Terminal size: Full screen or large enough to see clearly
- [ ] Navigate to project directory: `cd /home/joytarib/Documents/Project/pyladies`
- [ ] Activate virtual environment: `source venv/bin/activate`

## 📁 Files & Tabs Ready

- [ ] Open VS Code / text editor
- [ ] Have these files in separate tabs:
  - [ ] `file_organizer.py` 
  - [ ] `email_sender.py`
  - [ ] `web_automation.py`
  - [ ] `schedule_demo.py`
- [ ] Terminal window ready
- [ ] Browser window ready (for Selenium demo)

## 📂 Test Data Prepared

- [ ] Test directory exists: `~/test_downloads`
- [ ] Test directory has sample files (at least 10-15 files of different types)
- [ ] Test directory is MESSY (not organized yet!)
- [ ] Know the path: `/home/joytarib/test_downloads`

## 📧 Email Setup

- [ ] `.env` file configured with valid credentials
- [ ] Test email address ready (use your own email for demo)
- [ ] Know what email you'll send in demo
- [ ] Email app/browser tab open to show received email

## 🌐 Web Automation

- [ ] Internet connection verified
- [ ] Chrome/Chromium installed and working
- [ ] Know what search query you'll use (e.g., "PyLadies automation")
- [ ] Decide: headless=True or headless=False for demo

## 🎬 Recording Setup

- [ ] Recording software open (OBS/SimpleScreenRecorder/Kazam)
- [ ] Screen capture configured
- [ ] Microphone tested and working
- [ ] Audio levels checked (not too loud, not too quiet)
- [ ] Resolution set (1920x1080 or 1280x720)
- [ ] Frame rate: 30 FPS
- [ ] Know where recording will be saved
- [ ] Test recording: 10-second test run

## 📝 Presentation Materials

- [ ] Script/notes ready (but not on screen)
- [ ] Timer visible (for 15-minute limit)
- [ ] Water nearby
- [ ] Resources list ready to show at end
- [ ] GitHub repo link ready (if applicable)

## 🧪 Final Technical Checks

Run these commands to verify everything works:

```bash
# Activate environment
source venv/bin/activate

# Quick module checks
python3 -c "import file_organizer; print('✓ file_organizer')"
python3 -c "import email_sender; print('✓ email_sender')"  
python3 -c "from web_automation import WebAutomation; print('✓ web_automation')"
python3 -c "import schedule_demo; print('✓ schedule_demo')"

# Check test directory
ls ~/test_downloads

# Verify .env
cat .env | grep "SENDER_EMAIL"
```

## 🎤 Right Before Recording

- [ ] Take a deep breath! 
- [ ] Water nearby
- [ ] Good posture
- [ ] Smile (it affects your voice!)
- [ ] Start timer
- [ ] Hit RECORD ▶️

## 📊 Presentation Flow (15 minutes)

### **0:00-1:00 - Introduction**
- [ ] Introduce yourself
- [ ] State the problem: repetitive tasks
- [ ] Preview what you'll cover

### **1:00-4:30 - Demo 1: File Organization**
- [ ] Show messy test directory: `ls ~/test_downloads`
- [ ] Briefly explain code (pathlib, FILE_TYPES dict)
- [ ] Run: `python3 file_organizer.py`
- [ ] Choose option 1
- [ ] Enter path: `/home/joytarib/test_downloads`
- [ ] Show organized result: `ls ~/test_downloads/`
- [ ] Mention: logging, error handling

### **4:30-8:00 - Demo 2: Email Automation**
- [ ] Show `email_sender.py` code
- [ ] Explain: smtplib, MIME types
- [ ] Mention: environment variables for security (.env)
- [ ] Run: `python3 email_sender.py`
- [ ] Send test email to yourself
- [ ] Check email inbox (show received email)

### **8:00-11:30 - Demo 3: Web Automation**
- [ ] Show `web_automation.py` code
- [ ] Explain: Selenium, WebDriver, locators
- [ ] Run: `python3 web_automation.py`
- [ ] Choose Google search option
- [ ] Enter query: "PyLadies automation"
- [ ] Watch browser (or show headless logs)
- [ ] Show screenshot generated

### **11:30-13:30 - Demo 4: Scheduling**
- [ ] Show `schedule_demo.py` code
- [ ] Explain: schedule library, job intervals
- [ ] Run: `python3 schedule_demo.py` (briefly)
- [ ] Show scheduled jobs list
- [ ] Let it run for 30 seconds
- [ ] Ctrl+C to stop
- [ ] Emphasize: "Now it runs on its own!"

### **13:30-14:30 - Best Practices & Wrap-up**
- [ ] Error handling (try/except, logging)
- [ ] Security (environment variables, never hardcode passwords)
- [ ] Code readability (clear variable names, docstrings)
- [ ] Testing before deploying

### **14:30-15:00 - Next Steps & Q&A**
- [ ] Identify your own repetitive tasks
- [ ] Start small, then expand
- [ ] Resources:
  - [ ] Python pathlib docs
  - [ ] smtplib docs
  - [ ] Selenium Python docs
- [ ] Thank you!
- [ ] Questions?

## ⚠️ Backup Plans

### If file_organizer.py fails:
- [ ] Have pre-organized screenshots ready
- [ ] Explain what WOULD happen

### If email_sender.py fails:
- [ ] Show the code and explain the logic
- [ ] Show pre-sent email screenshot

### If web_automation.py fails:
- [ ] Use headless=False to show browser
- [ ] Or have pre-recorded video clip
- [ ] Show screenshot instead

### If schedule_demo.py fails:
- [ ] Explain the concept with code walkthrough
- [ ] Show log files from previous runs

## 🎉 After Recording

- [ ] Stop recording
- [ ] Save file immediately
- [ ] Watch recording (check audio, video, pace)
- [ ] Edit if needed (trim start/end)
- [ ] Export in required format
- [ ] Verify file size (check submission requirements)
- [ ] Upload to required platform
- [ ] Backup copy saved

## 📊 Self-Evaluation

After watching your recording:

- [ ] Was audio clear?
- [ ] Was video clear (no pixelation)?
- [ ] Was pacing good (not too fast)?
- [ ] Did all demos work?
- [ ] Was timing under 15 minutes?
- [ ] Did I explain concepts clearly?
- [ ] Was I enthusiastic and engaging?
- [ ] Would a beginner understand?

## 💡 Pro Tips

1. **If something fails during live coding**: 
   - Stay calm
   - Explain what should happen
   - Move to next demo
   - Come back if time allows

2. **Time management**:
   - Keep an eye on timer
   - If running long, skip to conclusion
   - Better to end early than go over

3. **Engagement**:
   - Speak to the audience, not the screen
   - Use "you" and "we" (inclusive language)
   - Show enthusiasm!

4. **Beginner-friendly**:
   - Define technical terms
   - Explain WHY, not just WHAT
   - Use real-world examples

## ✅ Final Go/No-Go Check

Everything green? → **GO FOR LAUNCH! 🚀**

Any red? → **Fix before recording!**

- [ ] ✅ Virtual environment activated
- [ ] ✅ All modules import successfully
- [ ] ✅ Test data ready
- [ ] ✅ Email configured (or demo mode ready)
- [ ] ✅ Recording software ready
- [ ] ✅ Microphone working
- [ ] ✅ Timer ready
- [ ] ✅ Notes prepared
- [ ] ✅ Confidence level: HIGH! 💪

---

**Remember**: You've got this! The PyLadies community will love your practical, hands-on approach. Show them how Python can change their daily workflow! 🐍✨

**Good luck! 🍀**
