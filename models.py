from datetime import datetime

ads = []

class Ad:
    def __init__(self, title, description, owner):
        self.title = title
        self.description = description
        self.owner = owner
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'owner': self.owner,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }