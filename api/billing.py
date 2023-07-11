import os
import datetime

BILLING_INFO = os.getenv("BILLING_INFO")

def bill_user(user_id, usage):
    """
    Function to bill the user based on their usage
    """
    rate_per_usage = BILLING_INFO['rate_per_usage']
    bill_amount = usage * rate_per_usage

    billing_details = {
        'user_id': user_id,
        'bill_date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'usage': usage,
        'bill_amount': bill_amount
    }

    # Here, you can add code to update the billing details in your database

    return billing_details