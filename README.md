# 🔍 Network Log Analyzer

## What is this project? (Simple Explanation)

Imagine you're a security guard 👮 at a big building. You watch the entrance log that writes down everyone who tries to enter. Some people try to enter many times, some get rejected (401 error), some are not allowed (403 error). Your job is to find **suspicious people** and create **alerts**.

This project does the SAME THING but for websites! It analyzes **network logs** (records of people trying to access a website) and finds:
- 🚨 **People making too many requests** (like trying to get in too fast)
- ❌ **Failed login attempts** (wrong password)
- 🚫 **Forbidden access attempts** (trying to go where they're not allowed)

---

## Features (What can it do?)

✅ **Upload log files** - Upload text files with website traffic records
✅ **Analyze logs** - Automatically find suspicious activity
✅ **Show alerts** - Display dangerous IPs in a nice table
✅ **Dashboard** - See all detected IPs and their activity
✅ **User accounts** - Register and login (only you can see your logs)

---

## How to Set It Up (Installation Guide)

### Step 1: Get Python
Make sure you have Python 3.14 installed on your computer.

### Step 2: Create Virtual Environment (like a sandbox)
Think of this as creating a **special folder** for this project so it doesn't mess with your other Python stuff.

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment
This tells your computer "use Python from this folder"

**On Windows:**
```bash
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Required Packages
These are like tools/libraries the project needs to work.

```bash
pip install django
```

### Step 5: Setup Database
Think of database like a filing cabinet where we store user accounts and uploaded logs.

```bash
python manage.py migrate
```

### Step 6: Create Admin Account
Create a super user so you can login to the website.

```bash
python manage.py createsuperuser
```

### Step 7: Run the Server
Start the website!

```bash
python manage.py runserver
```

Then open your browser and go to: `http://127.0.0.1:8000/`

---

## How to Use It (Step-by-Step)

### 1. **Register Account** 📝
- Go to `/users/register/`
- Create username and password
- Click Register

### 2. **Login** 🔐
- Go to `/users/login/`
- Enter your username and password
- Click Login

### 3. **Upload Log File** 📤
- Go to the home page
- Click "Upload Log File"
- Select a `.txt` or `.log` file with network data
- Click Upload
- System automatically analyzes it! 🚀

### 4. **View Results** 📊
- See all the alerts (suspicious IPs)
- See total lines analyzed
- Shows 3 types of alerts:
  - Too many requests
  - Failed logins (401)
  - Forbidden access (403)

### 5. **Check Dashboard** 📈
- Click "Dashboard" button
- See all uploaded files
- See ALL IPs detected across all your logs
- Shows total requests per IP

---

## Project Structure (What each folder does)

```
network_log_analyzer/
│
├── core/                          # Main app that analyzes logs
│   ├── analyzer.py               # THE BRAIN - finds suspicious IPs
│   ├── views.py                  # What shows on screen
│   ├── models.py                 # Database structure
│   ├── urls.py                   # Website routes
│   └── templates/corehtml/       # HTML pages
│       ├── upload.html           # Upload page
│       ├── result.html           # Results page
│       └── dashboard.html        # Dashboard page
│
├── users/                         # Login/Register app
│   ├── views.py                  # Login/Register logic
│   ├── urls.py                   # Login routes
│   └── templates/users/          # Login pages
│       ├── login.html            # Login page
│       └── register.html         # Register page
│
├── network_log_analyzer/          # Project settings
│   ├── settings.py               # Configuration
│   ├── urls.py                   # Main routes
│   └── wsgi.py                   # Website runner
│
├── manage.py                      # Magic command runner
└── db.sqlite3                     # Database (stores users & logs)
```

---

## What Each File Does

### 📄 `analyzer.py` - The Detective 🔎
This file has the **main logic** that finds suspicious IPs. It:
1. Reads the uploaded log file line by line
2. Finds all IP addresses using regex (special pattern matching)
3. Counts how many times each IP appears
4. Marks IPs that:
   - Have more than 5 requests
   - Have failed login attempts (401)
   - Have forbidden access (403)
5. Returns the alerts

### 📄 `views.py` - The Screen Controller 🖥️
This controls what the user sees:
- `upload_log()` - Handles file uploads and shows results
- `dashboard()` - Shows all analyzed data
- Both require you to be logged in (`@login_required`)

### 📄 `models.py` - The Database Teacher 🗄️
Defines how data is stored:
```
LogFile:
  - file (the uploaded file)
  - uploaded_at (when it was uploaded)
```

---

## How Alerts Work 🚨

### Alert Type 1: Too Many Requests
- **What it means**: An IP tried to access the site more than 5 times
- **Why it's bad**: Could be a bot attacking or someone testing the site
- **Icon**: Shows count of requests

### Alert Type 2: Failed Login (401)
- **What it means**: An IP tried to login but entered wrong password
- **Why it's bad**: Could be someone trying to guess passwords
- **Icon**: ❌ (red X)

### Alert Type 3: Forbidden Access (403)
- **What it means**: An IP tried to access something they're not allowed to
- **Why it's bad**: Hacker trying to get to admin area or private files
- **Icon**: 🚫 (no entry sign)

---

## Example Log File Format

Your log file should look something like this:

```
192.168.1.1 - - [21/Apr/2026:10:15:30] "GET /index.html HTTP/1.1" 200
192.168.1.1 - - [21/Apr/2026:10:15:31] "POST /login HTTP/1.1" 401
192.168.1.2 - - [21/Apr/2026:10:15:32] "GET /admin HTTP/1.1" 403
192.168.1.1 - - [21/Apr/2026:10:15:33] "GET /index.html HTTP/1.1" 200
192.168.1.1 - - [21/Apr/2026:10:15:34] "POST /login HTTP/1.1" 401
192.168.1.1 - - [21/Apr/2026:10:15:35] "GET /index.html HTTP/1.1" 200
```

The system will:
- Find all IP addresses (192.168.1.1, 192.168.1.2, etc.)
- Count requests per IP
- Mark 192.168.1.1 as suspicious (6 requests > 5)
- Mark 192.168.1.1 for failed login (401 twice)
- Mark 192.168.1.2 for forbidden access (403)

---

## Common Problems & Solutions 🐛

### Problem: "Page shows blank"
**Solution**: Check if form template uses `{{ form }}` not `{% form %}`

### Problem: "File not found error"
**Solution**: Make sure uploaded file still exists in media folder

### Problem: "Cannot login"
**Solution**: Did you run `python manage.py migrate`? Did you create a user with `createsuperuser`?

### Problem: "Server won't start"
**Solution**: Check that you're in the right folder and virtual environment is activated

---

## Security Notes 🔒

⚠️ **This is for learning only!**
- Don't use this on a real website yet
- The SECRET_KEY in settings.py should be changed
- DEBUG mode should be False in production
- Add more validation for uploaded files

---

## Next Steps to Improve 🚀

1. Add **IP blocking** - automatically ban suspicious IPs
2. Add **email alerts** - get notified when suspicious activity detected
3. Add **charts** - show graphs of attacks over time
4. Add **export reports** - download PDF reports
5. Add **real-time monitoring** - watch live traffic

---

## Questions? 🤔

This is a Django web application. If you're stuck:
1. Check if virtual environment is activated
2. Check if you're in the right folder
3. Read the error message carefully - it usually tells you what's wrong
4. Google the error message!

Have fun analyzing! 🎉
