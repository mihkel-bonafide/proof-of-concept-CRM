import yaml
from yaml import load, load_all

with open("CompanyData.yaml", "r") as meeker:
    safe_company_info = yaml.safe_load(meeker)

print(safe_company_info)
print()
print(safe_company_info["Employee"][0])  # prints dictionary of 1st object
print() 
mihker_salary = safe_company_info["Employee"][0]["Salary"]
print(f"Mihker's salary is ${mihker_salary}")

"""
As with our other parsing docs, I simply want to demonstrate how to get at any specified value. I haven't decided how 
exactly I want to mete out access but as long as I can pull any of my Employee objects as dictionaries then I'll save that 
for later. 
"""




# salary = company_info["Salary"]
# print(salary)

# stream = open("CompanyData.yaml", "r")
# yaml_parser = load_all(stream, Loader=yaml.FullLoader)

# print(type(yaml_parser))

# for iterator in yaml_parser:
#     print(iterator["Employee"][0])
# output: dictionary of the Mihker object

"""
It's unclear how I access
"""