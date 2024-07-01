import xmltodict
import json
import yaml

"""
(still in beta) The purpose of this program is to read CompanyData.xml/json/yaml, parse the data into a Python 
dictionary, then perform further operations that allow us to use our source data interchangeably. I'm not 
concerned with ux-design at this stage - rather I'm principally concerned with making these parsing operations
as simple as possible. -MPG, 7.1.24
"""

def main():    
    print(f"Welcome to FakeCompany.com's Employee Database")
    print()
    print(f"Please select a database.")
    choose_database = input(f"(type 'xml', 'json', or 'yaml'): ")
    if choose_database.lower() == "xml":
        read_xml_data()
    elif choose_database.lower() == 'json':
        read_json_data()
    elif choose_database.lower() == 'yaml':
        read_yaml_data()
    else:       
        print("Invalid entry.") 
        print()
        main() 
        
def read_xml_data():
    # read CompanyData.xml and assign an array of dictionary "Employee" objects to the variable "xml_opus"
    company_data = open("CompanyData.xml", "r")
    xml_opus = xmltodict.parse(company_data.read())["Employees"]["Employee"]
    employee_database_reader(xml_opus)

def read_json_data(): 
    # read CompanyData.json and assign an array of dictionary "Employee" objects to the variable "json_opus"
    company_data = json.load(open("CompanyData.json"))
    json_opus = company_data["Employee"]
    employee_database_reader(json_opus)

def read_yaml_data():
    # read CompanyData.yaml and assign an array of dictionary "Employee" objects to the variable "yaml_opus"
    with open("CompanyData.yaml", "r") as reader:
        company_data = yaml.safe_load(reader)
    yaml_opus = company_data["Employee"]
    employee_database_reader(yaml_opus)

def employee_database_reader(opus):
    print()
    print(f"Current employees:")
    for counter, reader in enumerate(opus, start=1):
        print(f"{counter}. {reader["FirstName"]} {reader["LastName"]}")
    print()
    employee_record = int(input(f"Please select an employee record (by number): "))
    if employee_record == 1:
        employee_info(opus[0])
    elif employee_record == 2:
        employee_info(opus[1])
    elif employee_record == 3:
        employee_info(opus[2])
    elif employee_record == 4:
        employee_info(opus[3])
    else:  
        print(f"Invalid Entry. Go back to start.")
        main() 
        
def employee_info(deets):
    # print(deets)  # this returns the dictionary object for the selected employee
    print()
    print(f"Administrator's Note: only employee display information is available at this time. Watch this space for future updates! -MPG, 6.30.24")
    print()
    print(f"Employee Name: \t{deets["FirstName"]} {deets["LastName"]}")
    print(f"Employee ID #: \t{deets["EmpID"]}")
    print(f"Employee Dept: \t{deets["Dept"]}")
    print(f"Employee Salary: ${deets["Salary"]}")
    print(f"Employee Email: {deets["Email"]}")
    print(f"Address: \t{deets["Address"]["Street"]}")   
    print(f"\t\t{deets["Address"]["City"]}, {deets["Address"]["State"]} {deets["Address"]["ZipCode"]}") 
    print()
    back_or_exit = input("Type 'b' for back or 'e' to exit: ")
    if back_or_exit.lower() == "e":
        print(f"This terminates the program.") 
    elif back_or_exit.lower() == "b":
        read_json_data()  # arbitrary - any of the read modules will effectuate the same outcome
    else:
        print(f"You mistyped that, here lemme help you out...")
        main() 
        
    
if __name__ == "__main__":
    main()
