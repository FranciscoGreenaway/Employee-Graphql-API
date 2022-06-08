from datetime import date
from .models import Employee
from api import db
from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def create_employee_resolver(obj, info, department, first_name,
                             last_name, birth_date):
    try:
        today = date.today()
        employee = Employee(department=department, first_name=first_name,
                            last_name=last_name,
                            created_at=today.strftime("%m/%d/%Y"),
                            birth_date=birth_date)
        db.session.add(employee)
        db.session.commit()
        payload = {
            "success": True,
            "employee": employee.to_dict()
        }

    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"mm/dd/yyyy"]
        }

    return payload

