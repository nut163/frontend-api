```python
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from api.models import User

class Authentication(UserMixin):

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def authenticate_user(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return user
        else:
            return None

    def get_id(self):
        return self.username
```