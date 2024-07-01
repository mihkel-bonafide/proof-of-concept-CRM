import xmltodict

"""
This module is for accessing CompanyData.xml via the "XmlToDict" library. -MPG, 6/28/24
"""

# Get the XML file data
# stream = open("CompanyData.xml", "r") 
company_data = open("CompanyData.xml", "r")

# Parse the data into an 'OrderedDict'
# xml = xmltodict.parse(company_data.read())
"""
If you append "["Employees"]" to this variable assignment, it bring you down one level, 
such that the print-statement below produces the "Employee" tag instead of "Employees".
This is demonstrated further down. 
"""

# for goatsex in xml:
#     print(goatsex)  # Output: Employees

# for goatsex in xml["Employees"]:
#     print(goatsex)  # Output: Employee 

# for goatsex in xml["Employees"][0]:
#     print(goatsex)  # Output: Employee  # This doesn't/won't work

# for goatsex in xml["Employees"]["Employee"]:
#     print(goatsex)  # Output: python dictionary with all of the Employee sub-elements
"""
IMPORTANT! 
The output from the print-statement above produces a Python dictionary with all of the
Employee sub-elements (its format/syntax is identical to what you'd get from a JSON object,
which means you should be able to write Python code that parses both. -MPG)
"""

# for goatsex in xml["Employees"]["Employee"][0]:
#     print(goatsex)  
"""
Output: 
@email
FirstName
LastName
EmpID
Salary
Dept
Address
"""
"""
Now we're going to try this by parsing down a level.
"""
xml = xmltodict.parse(company_data.read())["Employees"]["Employee"]
# for opus in xml:
#     print(opus["FirstName"])
"""
This above produces the python dictionary with all sub-elements and much simpler code.
"""

# This produces each sub-element value in a reasonableish format. 
# for opus in xml:
#     print(f"Name: \t\t{opus["FirstName"]} {opus["LastName"]}")
#     print(f"Employee ID: \t{opus["EmpID"]}")
#     print(f"Salary: \t{opus["Salary"]}")
#     print(f"Department: \t{opus["Dept"]}")
#     print(f"Email: \t\t{opus["@email"]}")
#     print(f"Address: \t{opus["Address"]["Street"]}")
#     print(f"\t\t{opus["Address"]["City"]}, {opus["Address"]["State"]} {opus["Address"]["ZipCode"]}")
#     print()

"""
An easy way to work with specific elements/fields is to create variables with their values, as 
demonstrated below: 
"""
employee_1 = xml[0]  # this assigns a Python dictionary value specific to the Mihker object
employee_1_firstName = employee_1["FirstName"]
employee_1_lastName = employee_1["LastName"]
employee_1_id = employee_1["EmpID"]
employee_1_email = employee_1["Email"]
employee_1_dept = employee_1["Dept"]
employee_1_salary = employee_1["Salary"]
employee_1_firstName = employee_1["FirstName"]

print(f"{employee_1_firstName} {employee_1_lastName}'s department is {employee_1_dept}")
# output: "Mihker Gardner's department is IT"

