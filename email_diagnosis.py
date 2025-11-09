"""
Email Diagnosis Tool

Quick script to help diagnose email connection issues.
"""

import smtplib
import ssl
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def test_gmail_connection():
    """Test Gmail SMTP connection step by step."""
    
    email = os.getenv('SENDER_EMAIL', '')
    password = os.getenv('SENDER_PASSWORD', '')
    
    print("🔍 Gmail SMTP Connection Test")
    print("=" * 40)
    
    print(f"📧 Email: {email}")
    print(f"🔐 Password: {'*' * len(password) if password else 'NOT SET'}")
    
    if not email or not password:
        print("❌ Email or password not set in .env file")
        return False
    
    # Test different approaches
    approaches = [
        ("Standard Gmail SMTP (Port 587, TLS)", "smtp.gmail.com", 587, "TLS"),
        ("Gmail SMTP SSL (Port 465, SSL)", "smtp.gmail.com", 465, "SSL"),
    ]
    
    for name, server, port, security in approaches:
        print(f"\n🧪 Testing: {name}")
        try:
            if security == "SSL":
                # SSL connection
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(server, port, context=context) as smtp:
                    smtp.login(email, password)
                    print(f"✅ {name} - SUCCESS!")
                    return True
            else:
                # TLS connection
                with smtplib.SMTP(server, port) as smtp:
                    smtp.starttls()
                    smtp.login(email, password)
                    print(f"✅ {name} - SUCCESS!")
                    return True
                    
        except smtplib.SMTPAuthenticationError as e:
            print(f"❌ Authentication failed: {e}")
            print("   💡 Check your App Password or enable 2FA")
            
        except smtplib.SMTPConnectError as e:
            print(f"❌ Connection failed: {e}")
            print("   💡 Check network/firewall settings")
            
        except smtplib.SMTPException as e:
            print(f"❌ SMTP error: {e}")
            
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    return False

def check_account_settings():
    """Check account settings recommendations."""
    print("\n📋 Account Settings Checklist:")
    print("=" * 40)
    print("1. ✅ 2-Factor Authentication enabled?")
    print("   Go to: https://myaccount.google.com/security")
    print()
    print("2. ✅ App Password generated?") 
    print("   Go to: https://myaccount.google.com/apppasswords")
    print("   - Select 'Mail' and your device")
    print("   - Copy the 16-character password")
    print()
    print("3. ✅ Less secure app access (if needed)?")
    print("   Go to: https://myaccount.google.com/lesssecureapps")
    print("   Note: This is less secure, App Passwords are better!")

if __name__ == "__main__":
    success = test_gmail_connection()
    
    if not success:
        check_account_settings()
        print("\n💡 Common Solutions:")
        print("   1. Generate a NEW App Password")
        print("   2. Make sure 2FA is enabled first")
        print("   3. Use the App Password, not your regular password")
        print("   4. Check your network connection")
    else:
        print("\n🎉 Connection successful! Your email setup is working.")