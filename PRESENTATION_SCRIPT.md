# 🎤 Presentation Script - 15 Minutes
## "Python for Automation: Getting Rid of Repetitive Tasks"

---

## 🎬 INTRO (0:00 - 1:00) - 1 minute

**[Slide: Title slide visible]**

> "Hi everyone! I'm Joy Tari-Bagshaw, and I'm so excited to be here today!
> 
> Can I get a show of hands - who here has ever spent hours organizing files on their computer? What about sending the same email over and over? Or filling out the same form multiple times?
> 
> **[Pause for response]**
> 
> Yeah, me too! And that's exactly why I'm here today - to show you how Python can turn those tedious tasks into a few lines of code that run themselves.
> 
> In the next 15 minutes, we're going to automate four common tasks: organizing files, sending emails, interacting with websites, and making it all run on a schedule. And the best part? You can do all of this with beginner-level Python!
> 
> So let's dive in!"

**[Switch to terminal/code view]**

---

## 📁 DEMO 1: File Organization (1:00 - 4:30) - 3.5 minutes

### Show the Problem (1:00 - 1:30)

**[Terminal: Show messy directory]**
```bash
ls ~/test_downloads
```

> "Okay, so here's my Downloads folder. Sound familiar? We've got PDFs mixed with photos, code files everywhere, videos... it's a mess! 
> 
> Normally, I'd spend 10-15 minutes manually sorting these. But watch what happens when I let Python do it..."

### Show the Code (1:30 - 2:30)

**[Open file_organizer.py]**

> "Here's the code. Let me break it down quickly:
> 
> **[Point to FILE_TYPES dictionary]**
> First, we define what types of files we want to organize - images, documents, code, audio, video. Python's `pathlib` module makes working with files really elegant.
> 
> **[Point to organize_downloads function]**
> Then our main function does three things:
> 1. Creates folders for each file type
> 2. Looks at each file's extension
> 3. Moves it to the right folder
> 
> **[Point to safe_move and logging]**
> We've also got error handling - if there's a naming conflict, we add a timestamp. And we log everything so we know what happened.
> 
> Pretty straightforward, right? Let's run it!"

### Run the Demo (2:30 - 3:30)

**[Terminal: Run the script]**
```bash
python3 file_organizer.py
# Choose option 1
# Enter: /home/joytarib/test_downloads
```

> "I'll choose option 1 to organize the Downloads folder...
> 
> **[While it's running]**
> Watch the output - it's showing us each file being moved... and...
> 
> **[Show results]**
> Done! In just a few seconds, everything is organized!"

```bash
ls ~/test_downloads
```

> "Look at that! We now have folders for images, documents, code, audio, video - everything in its place. What would have taken me 15 minutes now takes 2 seconds!
> 
> And here's the powerful part - you can customize this. Maybe you want to organize by date instead of type, or add new categories. The code is yours to adapt to YOUR needs."

### Transition (3:30 - 4:00)

> "But file organization is just the beginning. Let's talk about communication..."

---

## 📧 DEMO 2: Email Automation (4:30 - 8:00) - 3.5 minutes

### Show the Code (4:30 - 5:30)

**[Open email_sender.py]**

> "Sending emails programmatically might sound complicated, but Python makes it surprisingly easy with the `smtplib` library - it's built right into Python!
> 
> **[Point to send_email function]**
> Here's our main function. It takes a recipient, subject, and body - just like composing an email normally. But now we can call this function from anywhere in our code.
> 
> **[Point to SMTP connection]**
> Behind the scenes, we're connecting to an email server - I'm using Gmail here - authenticating with our credentials, and sending the message. All with just a few lines of code!
> 
> **[Point to environment variables]**
> Now, **super important** - we NEVER hardcode passwords in our scripts! See how we're using environment variables? We store sensitive info in a `.env` file that never gets shared.
> 
> **[Show .env.example]**
> Here's what that looks like. For Gmail, you'd use an App Password, not your regular password. Links to set that up are in the README."

### Show Enhanced Features (5:30 - 6:30)

**[Scroll to send_html_email and create_weekly_report_email]**

> "But we can do more than just plain text! 
> 
> Here's a function that sends HTML emails - formatted text, colors, images, whatever you need.
> 
> And here's a practical example: an automated weekly report. Imagine every Friday, your computer automatically sends you a summary of what you accomplished that week. Pretty cool, right?
> 
> You could use this for:
> - Sending reminders to yourself
> - Notifying team members when something happens
> - Sending birthday wishes automatically
> - Monthly newsletter... the possibilities are endless!"

### Run the Demo (6:30 - 7:30)

**[Terminal: Run email script]**
```bash
python3 email_sender.py
# Choose option 1 (simple email)
# Enter your email
# Enter subject and message
```

> "Let's send a quick test email to myself...
> 
> **[While sending]**
> The script is connecting to Gmail, authenticating, and sending...
> 
> **[Check email in browser]**
> And there it is! Email received!
> 
> What took several clicks and typing in my email client now happens instantly from code. And because it's code, I can trigger this from other scripts, on a schedule, or based on events."

### Transition (7:30 - 8:00)

> "So we can organize files, we can send emails. But what about the web?"

---

## 🌐 DEMO 3: Web Automation (8:00 - 11:30) - 3.5 minutes

### Show the Code (8:00 - 9:00)

**[Open web_automation.py]**

> "This is where things get really powerful. Selenium lets us control a web browser programmatically.
> 
> **[Point to WebAutomation class]**
> I've created a class that wraps common web tasks. Think of it as a robot that can:
> - Open websites
> - Click buttons
> - Fill out forms
> - Take screenshots
> - Extract information
> 
> **[Point to find_element and click_element methods]**
> These methods let us locate elements on a page - by ID, by name, by CSS selector - and interact with them.
> 
> **[Point to search_google function]**
> Here's a practical example: automated Google searching. Maybe you want to monitor how often certain topics appear, or check search rankings for your website."

### Show Form Example (9:00 - 9:30)

**[Scroll to fill_contact_form]**

> "And here's form filling. Ever had to fill out the same form repeatedly? Maybe for testing, or data entry?
> 
> With Selenium, you write the script once, and it can fill out forms hundreds of times without error. Way faster and more accurate than doing it manually!"

### Run the Demo (9:30 - 11:00)

**[Terminal: Run web automation]**
```bash
python3 web_automation.py
# Choose option 1
# Enter: "PyLadies automation"
```

> "Let's search Google for 'PyLadies automation'...
> 
> **[Browser opens or show headless mode]**
> Watch - the browser opens automatically, navigates to Google, types our query, and clicks search...
> 
> **[Show screenshot]**
> And it captured a screenshot! This is the result.
> 
> All of this happened without me touching the browser. I could run this on a schedule to monitor search results, or set it up to notify me when certain content appears.
> 
> **[Show first result text in terminal if available]**
> The script even extracted the first result title. We could save this data, analyze trends, whatever we need!"

### Practical Applications (11:00 - 11:30)

> "Real-world uses for this:
> - Automating form submissions
> - Data collection from websites
> - Testing web applications
> - Monitoring price changes
> - Filling out repetitive paperwork
> 
> Any repetitive web task can be automated!"

### Transition (11:30 - 11:45)

> "Now, running these scripts manually is already powerful. But what if they could run themselves?"

---

## ⏰ DEMO 4: Task Scheduling (11:45 - 13:30) - 1.75 minutes

### Show the Code (11:45 - 12:30)

**[Open schedule_demo.py]**

> "This is where everything comes together. The `schedule` library lets us make any Python function run automatically.
> 
> **[Point to TaskScheduler class]**
> I've built a scheduler that can run jobs:
> - Every minute, hour, day, week
> - At specific times
> - On specific days
> 
> **[Point to example jobs in main function]**
> Look at these examples:
> - Organize downloads folder every minute (or daily in real use)
> - Send a daily report at 6 PM
> - Run backups every Monday at 2 AM
> 
> **[Point to the while loop]**
> Once started, the scheduler just keeps running, checking for jobs to execute. Set it and forget it!"

### Run the Demo (12:30 - 13:15)

**[Terminal: Run scheduler]**
```bash
python3 schedule_demo.py
```

> "Let me start the scheduler...
> 
> **[Show job list]**
> Here are our scheduled jobs. For this demo, I've set it to run frequently so we can see it work...
> 
> **[Let it run for 20-30 seconds]**
> Watch - it's checking for jobs... there! The file organizer just ran automatically!
> 
> **[Ctrl+C to stop]**
> In a real scenario, you'd run this as a background service, and it would just keep working 24/7.
> 
> Imagine: every night, your computer automatically organizes files, backs up important documents, sends reports, checks websites... all while you sleep!"

### Transition (13:15 - 13:30)

> "So that's automation! But before we wrap up, let's talk about doing this right..."

---

## 📝 BEST PRACTICES (13:30 - 14:30) - 1 minute

**[Can show code examples or just talk]**

> "A few quick best practices to make your automation reliable:
> 
> **1. Error Handling**
> Things will go wrong - networks fail, files move, websites change. Use try-except blocks and logging so you know what happened.
> 
> **[Point to logging examples in code if visible]**
> Notice how all our scripts log what they're doing? This is crucial for debugging.
> 
> **2. Security**
> Never hardcode passwords! Use environment variables or config files. Keep your `.env` file out of version control.
> 
> **3. Start Small**
> Don't try to automate everything at once. Start with one annoying task, get that working, then move to the next.
> 
> **4. Test First**
> Always test your automation with sample data before running on real stuff. Create a test folder, test email address, etc.
> 
> **5. Document Your Code**
> Future you will thank present you! Write docstrings, add comments, make it clear what each part does."

---

## 🚀 CONCLUSION & NEXT STEPS (14:30 - 15:00) - 0.5 minutes

**[Can show resource slide or just speak]**

> "So, to wrap up:
> 
> We've seen how to automate file organization, emails, web interactions, and scheduling. All with beginner-friendly Python!
> 
> **Your homework:**
> 1. Identify ONE repetitive task in your workflow
> 2. Start small - maybe just organizing one folder
> 3. Build from there!
> 
> **Resources** - all links are in the README:
> - Python pathlib documentation
> - smtplib documentation  
> - Selenium Python docs
> - The GitHub repo with all this code
> 
> Remember: every expert was once a beginner. Start small, be patient with yourself, and soon you'll have your computer working for you instead of the other way around!
> 
> Thank you so much! Questions?"

---

## 🎯 BACKUP CONTENT (If You Have Extra Time)

### If you finish early (use remaining time for Q&A or show these):

**Additional Examples to Mention:**
- "You could combine these! Organize files AND email yourself a summary!"
- "Monitor a website for changes and get notified immediately!"
- "Batch process hundreds of images with just one script!"
- "Automatically back up your work to cloud storage!"

**Common Questions to Anticipate:**

**Q: "What if I don't know Python?"**
> "Great question! This is actually a perfect starting point. The automation libraries are very beginner-friendly. Start with the file organizer - it's the simplest. The PyLadies community has tons of resources for learning Python basics!"

**Q: "Is this safe? Won't automation mess things up?"**
> "Excellent question! That's why we test first with sample data. Start with a test folder, not your important files. Once you're confident, then use it on real data. And always, always keep backups!"

**Q: "Can I do this on Windows/Mac?"**
> "Yes! Python works the same way on all platforms. The file paths might look different (C:\ vs /home/), but the logic is identical. All these scripts work cross-platform!"

**Q: "What if a website changes and breaks my Selenium script?"**
> "That's a real issue! Websites do change. That's why we use logging and error handling. Your script will tell you what broke, and you can update the selectors. It's also why starting with stable APIs (when available) is often better than web scraping."

---

## ⏱️ TIME MANAGEMENT TIPS

**If running LONG:**
- Skip detailed code walkthrough, show results instead
- Skip one of the demos (maybe web automation, as it's most complex)
- Skip the "practical applications" sections
- Go straight to conclusion

**If running SHORT:**
- Add more code explanation
- Show more error handling examples
- Demo the HTML email or bulk emails
- Show the testing process
- Take more questions

**If something BREAKS:**
- Stay calm!
- Explain what SHOULD happen
- Have screenshots ready as backup
- Move to next demo
- "And that's why testing is important!" (turn it into a teaching moment)

---

## 📋 PRESENTATION DAY REMINDERS

**Before you start recording:**
- [ ] Glass of water nearby
- [ ] Timer visible (or phone timer)
- [ ] All files open in tabs
- [ ] Test directory ready
- [ ] Deep breath!
- [ ] SMILE - it shows in your voice!

**While presenting:**
- Speak clearly and at a moderate pace
- Make eye contact (look at camera if recording)
- Use hand gestures (if on camera)
- Show enthusiasm!
- It's okay to say "um" occasionally - you're human!

**If you mess up:**
- Pause
- Take a breath
- "Let me try that again..."
- Keep going!

---

**You've got this! Go automate the world! 🚀🐍✨**
