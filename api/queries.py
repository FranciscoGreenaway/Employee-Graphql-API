from .models import Employee
from ariadne import convert_kwargs_to_snake_case


def get_employees_resolver(obj, info):
    try:
        employees = [employee.to_dict() for employee in Employee.query.all()]
        print(employees)
        payload = {
            "success": True,
            "employees": employees
        }

    except Exception as error:

        payload = {
            "success": False,
            "errors": [str(error)],
        }

    return payload


@convert_kwargs_to_snake_case
def get_employee_by_id_resolver(obj, info, id):
    try:
        employee = Employee.query.get(id)
        print(employee)
        payload = {
            "success": True,
            "employee": employee
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f'An employee with id "{id}" not found']
        }
    return payload
