import imp
from flask import request, json, Response, Blueprint, jsonify
from flasgger import swag_from

from src.models.employee import EmployeeModel, db
# from src.app import db

emp_api = Blueprint('employee', __name__)

@emp_api.route('/api/add_employee', methods=['POST'])
@swag_from('../docs/emp_add.yaml')
def add():
    """
    example endpoint
    """
    entry = EmployeeModel(request.json['id'],request.json['name'], request.json['email'],request.json['salary'],request.json['designation'])
    db.session.add(entry)
    db.session.commit()
    return 'Congratulations... Emtry is added in database !!!' 


@emp_api.route('/api/employee_get', methods=['GET'])
@swag_from('../docs/emp_get.yaml')
def get():
    """
    example endpoint
    """
    print('id')
    data = db.session.query(EmployeeModel).all()
    #data = db.session.query(EmployeeModel).filter(EmployeeModel.id == id).first()
    all_emp = []
    for emp in data:
        emp_dict = {
            "Id": emp.id,
            "Name": emp.name,
            "Email" : emp.email,
            "Salary" : emp.salary,
            "Designation" : emp.designation
        }
        all_emp.append(emp_dict)
    return jsonify(all_emp)

@emp_api.route('/api/employee_update/<id>', methods=['PUT'])
@swag_from('../docs/emp_update.yaml')
def update(id):
    """
    example endpoint
    """
    print(request.json['name'])
    data = db.session.query(EmployeeModel).filter(EmployeeModel.id == id).first()
    data.name = request.json['name']
    data.email = request.json['email']
    data.salary = request.json['salary']
    data.designation = request.json['designation']
    db.session.commit()
    return 'data update successfully'


@emp_api.route('/api/employee_delete/<id>', methods=['DELETE'])
@swag_from('../docs/emp_delete.yaml')
def delete(id):
    """
    example endpoint
    """
    db.session.query(EmployeeModel).filter(EmployeeModel.id == id).delete()
    db.session.commit()
    return 'data deleted successfully'

@emp_api.route('/login')
def login():
    return 'successs'
