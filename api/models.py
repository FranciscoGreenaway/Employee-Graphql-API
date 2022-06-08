from app import db


class Employee(db.Model):
    # Instantiating columns, types, and keys.
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    created_at = db.Column(db.Date)
    birth_date = db.Column(db.Date)

    def to_dict(self):
        return {
            "id": self.id,
            "department": self.department,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": str(self.created_at.strftime('%m/%d/%Y')),
            "birth_date": str(self.birth_date.strftime('%m/%d/%Y'))
        }
