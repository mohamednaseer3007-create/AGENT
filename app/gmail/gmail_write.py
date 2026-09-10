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
