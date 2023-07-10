```python
from models import User

def calculateBill(user_id):
    user = User.query.get(user_id)
    if user is None:
        return {"error": "User not found"}

    usage = user.usage
    bill = 0

    # Define your billing rules here
    if usage <= 1000:
        bill = usage * 0.01
    elif usage <= 10000:
        bill = usage * 0.005
    else:
        bill = usage * 0.001

    return {"bill": bill}
```