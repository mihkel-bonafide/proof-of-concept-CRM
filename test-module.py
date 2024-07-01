import xmltodict

"""
WIP -MPG, 6.30
"""

def read_xml_data():
    # read and parse CompanyData.xml
    company_data = open("CompanyData.xml", "r")
    xml_opus = xmltodict.parse(company_data.read())["Employees"]["Employee"]
    return xml_opus

def employee_database_xml():
    # xml database exists as a python dictionary called xml_dictionary
    xml_dictionary = read_xml_data()
    # print(xml_dictionary[0])  # 1st employee object as dictionary
    for counter, beaker in enumerate(xml_dictionary, start=1):
        print(f"{counter}. {beaker["FirstName"]} {beaker["LastName"]}")
    while True:
        employee_record = int(input(f"Please select an employee record (by number): "))
        if employee_record == 1:
            employee_info(xml_dictionary[0])
        elif employee_record == 2:
            employee_info(xml_dictionary[1])
        elif employee_record == 3:
            employee_info(xml_dictionary[2])
        elif employee_record == 4:
            employee_info(xml_dictionary[3])
        else:  
            return False 
        
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
        return False 
    elif back_or_exit.lower() == "b":
        main()
    else:
        print(f"You mistyped that, here lemme help you out...")
        main() 
        
def main():    
    print(f"Welcome to FakeCompany.com's Employee Database")
    print()
    employee_database_xml()

main()
