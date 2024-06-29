import json

json_string = """{
"Employee":[{"FirstName":"Mihker","LastName":"Gardner","Email":"mihkel.gardner@fakecompany.com","EmpID":"44210","Salary":169000,"Dept":"IT","Address":{"Street":"2734 NE 49th Ave","Unit":"none","City":"Portland","State":"OR","Zip":"97213"}},{"FirstName":"Lily","LastName":"Gardner-Butts","Email":"lily.gardner-butts@fakecompany.com","EmpID":"44211","Salary":100000,"Dept":"CEO","Address":{"Street":"2734 NE 49th Ave","Unit":"none","City": "Portland","State":"OR","Zip":"97213"}},{"FirstName":"Jill","LastName":"Helmberger","Email":"jill.helmberger@fakecompany.com","EmpID":"44212","Salary":200000,"Dept":"CTO","Address":{"Street":"15900 NE 18th St","Unit":"none","City": "Vancouver","State":"WA","Zip": "98003"}},{"FirstName":"Charles","LastName":"Helmberger","Email":"charles.helmberger@fakecompany.com","EmpID":"44213","Salary": 150,"Dept": "dog","Address":{"Street": "15900 NE 18th St","Unit":"none","City":"Vancouver","State":"WA","Zip":"98003"}}]}"""

json_object = json.loads(json_string)

# this is how you get a Python dictionary object for the first entry, Mihker Gardner.
print(json_object["Employee"][0])
print() 

json_object_two = json.load(open("CompanyData.json"))
# same output as above but as a read operation
print(json_object_two["Employee"][0])

"""
The operations here are identical to the "XMLtoDICT-parsing" module. This is the same code 
minus the email field, which is stored as an attribute on CompanyData.xml(may want to change that, eh?))
"""
employee_1 = json_object_two["Employee"][0]
print(employee_1)  # same output as above
employee_1_firstName = employee_1["FirstName"]
employee_1_lastName = employee_1["LastName"]
employee_1_id = employee_1["EmpID"]
employee_1_email = employee_1["Email"]  # this field is DIFFERENT, changed from "@email" 
employee_1_dept = employee_1["Dept"]
employee_1_salary = employee_1["Salary"]
employee_1_firstName = employee_1["FirstName"]

print(f"{employee_1_firstName} {employee_1_lastName}'s department is {employee_1_dept}")
# output: "Mihker Gardner's department is IT"

"""
Parting thought: from a design standpoint, I don't think it makes sense to assign variables 
in the above fashion. It's a neat proof-of-concept, but I think it makes more sense to keep the 
values as dictionaries and extract values only as needed. 
"""
