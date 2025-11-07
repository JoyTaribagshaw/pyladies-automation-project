"""
Email Automation Module

This module provides functions to automate email sending using Python's built-in
smtplib library. It includes support for plain text and HTML emails.

SECURITY NOTE: Never hardcode credentials in your scripts!
Use environment variables or a .env file to store sensitive information.
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from typing import List, Optional
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('email_sender.log')
    ]
)
logger = logging.getLogger(__name__)

# Email configuration from environment variables
DEFAULT_SENDER_EMAIL = os.getenv('SENDER_EMAIL', '')
DEFAULT_SENDER_PASSWORD = os.getenv('SENDER_PASSWORD', '')
DEFAULT_SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
DEFAULT_SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))

def send_email(
    to_email: str,
    subject: str,
    body: str,
    from_email: str = None,
    from_password: str = None,
    smtp_server: str = None,
    smtp_port: int = None,
    attachments: Optional[List[str]] = None,
    html: bool = False
) -> bool:
    """
    Send an email using SMTP.
    
    Args:
        to_email: Recipient's email address
        subject: Email subject line
        body: Email body content
        from_email: Sender's email address (uses env var if not provided)
        from_password: Sender's email password (uses env var if not provided)
        smtp_server: SMTP server address (defaults to Gmail)
        smtp_port: SMTP port (defaults to 587 for TLS)
        attachments: List of file paths to attach
        html: Whether the body is HTML (default: False for plain text)
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    # Use defaults if not provided
    from_email = from_email or DEFAULT_SENDER_EMAIL
    from_password = from_password or DEFAULT_SENDER_PASSWORD
    smtp_server = smtp_server or DEFAULT_SMTP_SERVER
    smtp_port = smtp_port or DEFAULT_SMTP_PORT
    
    # Validate required fields
    if not from_email or not from_password:
        logger.error("Email credentials not provided. Set SENDER_EMAIL and SENDER_PASSWORD in .env file.")
        return False
    
    if not to_email:
        logger.error("Recipient email address is required.")
        return False
    
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject
        
        # Add the email body
        if html:
            message.attach(MIMEText(body, 'html'))
        else:
            message.attach(MIMEText(body, 'plain'))
        
        # Add attachments if any
        if attachments:
            for file_path in attachments:
                if not Path(file_path).exists():
                    logger.warning(f"Attachment not found: {file_path}")
                    continue
                
                with open(file_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {Path(file_path).name}'
                )
                message.attach(part)
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(from_email, from_password)
            server.send_message(message)
        
        logger.info(f"Email sent successfully to {to_email}")
        return True
        
    except smtplib.SMTPAuthenticationError:
        logger.error("Authentication failed. Check your email and password.")
        return False
    except smtplib.SMTPException as e:
        logger.error(f"SMTP error occurred: {e}")
        return False
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        return False

def send_bulk_emails(
    recipients: List[str],
    subject: str,
    body: str,
    **kwargs
) -> dict:
    """
    Send the same email to multiple recipients.
    
    Args:
        recipients: List of recipient email addresses
        subject: Email subject line
        body: Email body content
        **kwargs: Additional arguments to pass to send_email()
    
    Returns:
        dict: Summary of sent/failed emails
    """
    results = {
        'sent': [],
        'failed': []
    }
    
    for recipient in recipients:
        logger.info(f"Sending email to {recipient}...")
        if send_email(to_email=recipient, subject=subject, body=body, **kwargs):
            results['sent'].append(recipient)
        else:
            results['failed'].append(recipient)
    
    logger.info(f"Bulk email complete. Sent: {len(results['sent'])}, Failed: {len(results['failed'])}")
    return results

def send_html_email(
    to_email: str,
    subject: str,
    html_content: str,
    **kwargs
) -> bool:
    """
    Send an HTML formatted email.
    
    Args:
        to_email: Recipient's email address
        subject: Email subject line
        html_content: HTML content for the email body
        **kwargs: Additional arguments to pass to send_email()
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    return send_email(
        to_email=to_email,
        subject=subject,
        body=html_content,
        html=True,
        **kwargs
    )

def create_weekly_report_email(recipient: str, stats: dict) -> bool:
    """
    Example function: Send a weekly report email with statistics.
    
    Args:
        recipient: Email address to send the report to
        stats: Dictionary containing report statistics
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    html_body = f"""
    <html>
        <body>
            <h2>📊 Weekly Automation Report</h2>
            <p>Hello!</p>
            <p>Here's your weekly automation summary:</p>
            <ul>
                <li><strong>Files Organized:</strong> {stats.get('files_organized', 0)}</li>
                <li><strong>Emails Sent:</strong> {stats.get('emails_sent', 0)}</li>
                <li><strong>Tasks Completed:</strong> {stats.get('tasks_completed', 0)}</li>
            </ul>
            <p>Keep up the great work! 🚀</p>
            <p><em>This is an automated message from your Python automation system.</em></p>
        </body>
    </html>
    """
    
    return send_html_email(
        to_email=recipient,
        subject="📊 Weekly Automation Report",
        html_content=html_body
    )

if __name__ == "__main__":
    print("=== Email Sender Demo ===")
    print("\nIMPORTANT: This is a demonstration. To actually send emails:")
    print("1. Create a .env file in the project root")
    print("2. Add your email credentials:")
    print("   SENDER_EMAIL=your.email@gmail.com")
    print("   SENDER_PASSWORD=your_app_password")
    print("\nFor Gmail, use an App Password (not your regular password):")
    print("https://support.google.com/accounts/answer/185833")
    print("\n" + "="*50 + "\n")
    
    # Check if credentials are configured
    if not DEFAULT_SENDER_EMAIL or not DEFAULT_SENDER_PASSWORD:
        print("⚠️  Email credentials not configured.")
        print("Please set up your .env file before running this script.")
        print("\nFor demo purposes, here's what the code would do:\n")
        
        demo_email = "recipient@example.com"
        demo_subject = "Hello from Python!"
        demo_body = "This is an automated email sent using Python's smtplib library."
        
        print(f"To: {demo_email}")
        print(f"Subject: {demo_subject}")
        print(f"Body: {demo_body}")
        print("\n✅ In a real scenario, this email would be sent!")
    else:
        # Interactive demo
        print("Email credentials found! Let's send a test email.")
        
        choice = input("\n1. Send simple email\n2. Send HTML email\n3. Send weekly report\n\nChoose an option (1-3): ").strip()
        
        if choice == "1":
            to = input("Recipient email: ").strip()
            subject = input("Subject: ").strip()
            body = input("Message: ").strip()
            
            if send_email(to, subject, body):
                print("\n✅ Email sent successfully!")
            else:
                print("\n❌ Failed to send email. Check the logs for details.")
        
        elif choice == "2":
            to = input("Recipient email: ").strip()
            html = """
            <html>
                <body>
                    <h1>Hello from Python! 🐍</h1>
                    <p>This is an <strong>HTML</strong> email sent automatically.</p>
                    <p style="color: blue;">Pretty cool, right?</p>
                </body>
            </html>
            """
            
            if send_html_email(to, "HTML Email Demo", html):
                print("\n✅ HTML email sent successfully!")
            else:
                print("\n❌ Failed to send email. Check the logs for details.")
        
        elif choice == "3":
            to = input("Recipient email: ").strip()
            stats = {
                'files_organized': 42,
                'emails_sent': 15,
                'tasks_completed': 8
            }
            
            if create_weekly_report_email(to, stats):
                print("\n✅ Weekly report sent successfully!")
            else:
                print("\n❌ Failed to send report. Check the logs for details.")
        
        else:
            print("Invalid choice.")
