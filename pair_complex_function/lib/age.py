from datetime import datetime
from dateutil.relativedelta import relativedelta


def age_check_over_18(str):
    dob = datetime.strptime(str, '%Y-%m-%d')

    today = datetime.today()
    age = relativedelta(today,dob).years

    if age < 18:
        return "Access granted"
    return "Access denied"
