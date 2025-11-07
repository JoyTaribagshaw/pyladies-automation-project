````markdown
# Python for Automation: Reclaim Your Time! 🚀

**PyLadies Presentation Project** - A hands-on guide to automating repetitive tasks using Python.

> *"Work smarter, not harder. Let Python be your personal assistant!"*

## 📚 About This Project

This project was created for a **PyLadies conference talk** aimed at **beginners** who want to learn how to automate common, tedious tasks. Whether it's organizing messy folders, sending routine emails, or interacting with websites, this project shows you how to turn hours of manual work into seconds of automated magic!

## 🎯 What You'll Learn

Through **four practical examples**, you'll discover how to:

1. 📁 **File System Automation** - Automatically organize messy folders by file type
2. 📧 **Email Automation** - Send emails programmatically (no more copy-paste!)
3. 🌐 **Web Automation** - Interact with websites automatically using Selenium
4. ⏰ **Task Scheduling** - Make your scripts run automatically on a schedule

## 🛠️ Prerequisites

- **Python 3.8+** (Python 3.10+ recommended)
- Basic Python knowledge (variables, functions, imports)
- A computer running Linux, macOS, or Windows
- Enthusiasm to automate! ⚡

## ⚡ Quick Start

### 1. Clone or Download This Repository
```bash
cd /home/joytarib/Documents/Project/pyladies
```

### 2. Run the Quick Test Script
```bash
./quick_test.sh
```
This will check your environment, install dependencies, and verify everything works!

### 3. Set Up Email Configuration (Optional)
```bash
cp .env.example .env
# Edit .env with your email credentials (see TESTING_GUIDE.md)
```

### 4. Try It Out!
```bash
# Activate the virtual environment
source venv/bin/activate

# Try organizing files
python3 file_organizer.py

# Try sending an email (configure .env first!)
python3 email_sender.py

# Try web automation
python3 web_automation.py

# Try scheduling tasks
python3 schedule_demo.py
```

## 📂 Project Structure

```
pyladies/
├── file_organizer.py           # 📁 File organization automation
├── email_sender.py             # 📧 Email automation
├── web_automation.py           # 🌐 Web automation with Selenium
├── schedule_demo.py            # ⏰ Task scheduling
├── requirements.txt            # 📦 Python dependencies
├── .env.example                # 🔐 Example environment config
├── README.md                   # 📖 This file
├── TESTING_GUIDE.md            # 🧪 Complete testing instructions
├── PRESENTATION_CHECKLIST.md   # 📋 Day-of presentation checklist
└── quick_test.sh               # ✅ Quick setup verification script
```

## 🎯 Quick Examples

### 1️⃣ File System Automation
```python
from file_organizer import organize_downloads

# Organize your messy Downloads folder in seconds!
organize_downloads()
# Files are now sorted into: images/, documents/, code/, audio/, video/, etc.
```

**Real-world use case**: Never manually sort files again. Run this daily!

---

### 2️⃣ Email Automation
```python
from email_sender import send_email

# Send automated emails without opening your email client
send_email(
    to_email="recipient@example.com",
    subject="Weekly Report",
    body="Here's your automated weekly summary!"
)
```

**Real-world use case**: Weekly reports, reminders, notifications - all automated!

---

### 3️⃣ Web Automation
```python
from web_automation import search_google

# Automate web interactions - searching, form filling, data extraction
search_google("Python automation PyLadies")
# Browser opens, searches, takes screenshot - all automatically!
```

**Real-world use case**: Data collection, form submissions, web monitoring.

---

### 4️⃣ Task Scheduling
```python
from schedule_demo import TaskScheduler

scheduler = TaskScheduler()

# Make any function run automatically on a schedule
scheduler.add_job(
    organize_downloads,
    interval='daily',
    at='18:00',  # Run every day at 6 PM
    job_name='organize_files'
)

scheduler.start()  # Now it runs on its own!
```

**Real-world use case**: Set it and forget it. Your scripts become persistent solutions.

---

## 📖 Learning Resources

**Recommended for Beginners:**

1. 📚 [Python pathlib Documentation](https://docs.python.org/3/library/pathlib.html) - Modern file path handling
2. 📧 [smtplib Documentation](https://docs.python.org/3/library/smtplib.html) - Sending emails with Python
3. 🌐 [Selenium Python Docs](https://selenium-python.readthedocs.io/) - Web automation guide
4. ⏰ [schedule Library Docs](https://schedule.readthedocs.io/) - Simple task scheduling

## 🎬 For Presenters

If you're using this project for a presentation:

1. **Read**: `TESTING_GUIDE.md` - Complete instructions for testing all components
2. **Use**: `PRESENTATION_CHECKLIST.md` - Day-of checklist to ensure smooth delivery
3. **Run**: `./quick_test.sh` - Verify everything works before showtime!

## 🐛 Troubleshooting

### Common Issues:

**"Module not found"**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**"Email authentication failed"**
- For Gmail: Use an [App Password](https://support.google.com/accounts/answer/185833), not your regular password
- Configure `.env` file with your credentials

**"Selenium WebDriver error"**
```bash
# Install Chrome/Chromium
sudo apt-get install chromium-browser chromium-chromedriver
```

**"Permission denied"**
- Use a test directory: `~/test_downloads` instead of system directories
- Make script executable: `chmod +x quick_test.sh`

See `TESTING_GUIDE.md` for detailed solutions.

## 🚀 Next Steps

**After completing this workshop:**

1. ✅ Identify repetitive tasks in YOUR workflow
2. ✅ Start small - automate one task at a time
3. ✅ Share your automation scripts with others
4. ✅ Join the PyLadies community and keep learning!

**Ideas to automate:**
- Daily backups of important files
- Downloading and organizing reports
- Monitoring websites for changes
- Sending birthday reminders
- Cleaning up old files
- Batch renaming photos
- ...and so much more!

## 🤝 Contributing

Found a bug? Have an improvement? Contributions welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - feel free to use it for your own learning and teaching!

## 🙏 Acknowledgments

- **PyLadies** - For creating an inclusive space for women in tech
- **Python Software Foundation** - For the amazing language and libraries
- **Open Source Community** - For the tools that make automation possible
- **You!** - For taking the time to learn automation

---

**Questions? Found this helpful? Let me know!**

Happy automating! 🐍✨
