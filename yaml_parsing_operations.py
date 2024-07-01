import yaml
from yaml import load, load_all

with open("CompanyData.yaml", "r") as meeker:
    safe_company_info = yaml.safe_load(meeker)

# print(safe_company_info)
# print()
# print(safe_company_info["Employee"])  # this is the dictionary array that gets passed to the parsing module
# print(safe_company_info["Employee"][0])  # prints dictionary of 1st object
# print() 
# mihker_salary = safe_company_info["Employee"][0]["Salary"]
# print(f"Mihker's salary is ${mihker_salary}")

# Okay, that's all fine and great, but can I get address info? 
yaml_opus = safe_company_info["Employee"]
print(yaml_opus[0]["Address"]["Street"])
print(f"{yaml_opus[0]["Address"]["City"]}, {yaml_opus[0]["Address"]["State"]}")

"""
As with our other parsing docs, I simply want to demonstrate how to get at any specified value. I haven't decided how 
exactly I want to mete out access but as long as I can pull any of my Employee objects as dictionaries then I'll save that 
for later. 
"""
