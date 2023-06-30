from deta import Deta
import os
from dotenv import load_dotenv

# load env var
load_dotenv(".env")

DETA_KEY = os.getenv("DETA_KEY")


#enter key
deta = Deta(DETA_KEY)

# connect db
db = deta.Base("mcc")

def insert_period(period, incomes, expenses, note):
    """Return report if success, raise error if not"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "note":note})

def fetch_all_periods():
    """Return a dict of all period"""
    res = db.fetch()
    return res.items

def get_period(period):
    """none if not found"""
    return db.get(period)