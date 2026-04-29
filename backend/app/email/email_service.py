import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
from app.core.config import SMTP_SERVER, SMTP_PORT
EMAIL_USER, EMAIL_PASS="a9a310001@smtp-brevo.com","xsmtpsib-39d69c1f5a33b9e395e56a7caddd1bfdd6f10ee46cfb416009c9ccd4f050f330-xuEOV2lobQ1UwVma"


# -------------------------
# SEND OTP EMAIL
def send_email(to_email: str, otp: str):

    try:
        print("📧 Sending OTP via Brevo to:", to_email)
        print("SMTP_SERVER:", SMTP_SERVER)
        print("SMTP_PORT:", SMTP_PORT)
        print("EMAIL_USER:", EMAIL_USER)

        msg = MIMEText(f"Your OTP is {otp}. Valid for 5 minutes.")
        msg["Subject"] = "OTP Verification - SeniorGuide"
        msg["From"] = EMAIL_USER
        msg["To"] = to_email

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)

        print("✅ OTP Email sent successfully")
        return True

    except Exception as e:
        print("❌ Email error:", str(e))
        return False

# -------------------------
# SEND REPORT EMAIL (PDF)
# -------------------------
def send_report_email(to_email: str, file_path: str):

    try:
        print("📧 Sending report email to:", to_email)

        msg = EmailMessage()

        msg["Subject"] = "Your College Consultation Report"
        msg["From"] = EMAIL_USER
        msg["To"] = to_email

        msg.set_content(
            "Your consultation report is attached. Please review carefully."
        )

        with open(file_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="pdf",
                filename="report.pdf"
            )

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)

        print("✅ Report email sent successfully")
        return True

    except Exception as e:
        print("❌ Report email error:", str(e))
        return False


# -------------------------
# SEND CALENDAR INVITE
# -------------------------
def send_calendar_invite(to_email: str, ics_file: str):

    try:
        print("📧 Sending calendar invite to:", to_email)

        msg = EmailMessage()

        msg["Subject"] = "Consultation Call Reminder"
        msg["From"] = EMAIL_USER
        msg["To"] = to_email

        msg.set_content(
            "Your consultation session is scheduled. Calendar invite attached."
        )

        with open(ics_file, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="text",
                subtype="calendar",
                filename="invite.ics"
            )

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)

        print("✅ Calendar invite sent successfully")
        return True

    except Exception as e:
        print("❌ Calendar email error:", str(e))
        return False
