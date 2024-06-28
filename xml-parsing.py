from lxml import etree 

"""
This module is for accessing CompanyData.xml. -MPG, 6/26/24
"""

# Get the XML file data
# stream = open("CompanyData.xml", "r") 
company_data = open("CompanyData.xml", "r")

# Parse the data into an ETree object
# xml = etree.parse(company_data)
mihker_etree = etree.parse(company_data)

# Get the "root element object" (this would be the "Employees" object here)
root = mihker_etree.getroot()

# Iterate through each child of the root element
for iterator in root:
    # print the stringified version of the element
    # print(etree.tostring(iterator))
    # print() 

    # this syntax only works for XML attributes
    print(iterator.get("email"))
  
