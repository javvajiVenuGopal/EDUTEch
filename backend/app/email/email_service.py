import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
from app.core.config import SMTP_SERVER, SMTP_PORT,EMAIL_USER, EMAIL_PASS,BREVO_API_KEY
import  requests



def send_email(to_email: str, otp: str):

    try:
        print("📧 Sending OTP via Brevo API to:", to_email)

        url = "https://api.brevo.com/v3/smtp/email"

        payload = {
            "sender": {
                "name": "SeniorGuide",
                "email": EMAIL_USER
            },
            "to": [
                {"email": to_email}
            ],
            "subject": "OTP Verification - SeniorGuide",
            "htmlContent": f"<p>Your OTP is <b>{otp}</b>. Valid for 5 minutes.</p>"
        }

        headers = {
            "accept": "application/json",
            "api-key": BREVO_API_KEY,
            "content-type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        print("Brevo response:", response.status_code)

        if response.status_code == 201:
            print("✅ OTP Email sent successfully")
            return True
        else:
            print("❌ Brevo error:", response.text)
            return False

    except Exception as e:
        print("❌ Email API error:", e)
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
