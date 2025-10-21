import os
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]


credenciais_path = os.gentev("GOOGLE_APPLICATION_CREDENTIALS", "credenciais.json")