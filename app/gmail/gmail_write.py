import os 
import re 
import urllib.parse

CLIENT_EMAIL = os.getenv("CLIENT_EMAIL","")

KEYWORDS = (
  "gmail","email","e-mail","mail",
  "write an email","send an email","draft an email0",
  "compose an email","write maill","send mail","draft mail",
  "compose mail"
)

def is_email_command(test):
  text = text.lower()
  return any(k in text for k in KEYWORDS)

def exact_email(text):
  match = re.search(r"[\w.+-]+@[\w.-]+\.\w+",text)
  if match :
    return match.group(0)

match = re.search(
  r"([\w.+-]+)\s+at\s+([\w.-]+)\s+dot\s+(\w+)"
  text.lower()
)
if match:
  return f"{match.group(1)}@{match.group(2)}.{match.group(3)}"

  return CLIENT_EMAIL
  return ""

def create_gmail_url(subject ="", body="", recipient="")
  params = urllib.parse.urlencode({
    "view": "cm",
    "fs":"1"
    "to":recipient,
    "su":subject,
    "body":body
  })
  return f"https://mail.goole.com/mail/u/0/?{params}"
