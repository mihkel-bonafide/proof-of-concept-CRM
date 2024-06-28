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

# How to navigate:
# print(root.tag)
# print(len(root))
# print(root[0].tag)
# print(root[1].tag)
# print(root[0]) 
for child in root:
    # print(child[0].tag)
    # print(child[0].text)
    # print(child[1].tag)
    # print(f"{child[0].tag}: {child[0].text}")
    # print(f"{child[1].tag}: {child[1].text}")
    # print(f"{child[0-2].tag}: {child[0-2].text}")  # this? [0:2]
    # print(f"{child[0-3].tag}: {child[0-3].text}")

    # this output is passable (without doing the address portion)
    # print(f"{child[0].text} {child[1].text}:")
    # print(f"{child[2].tag}: {child[2].text}")
    # print(f"{child[3].tag}: ${child[3].text}")
    # print(f"{child[4].tag}: {child[4].text}")
    # print() 

    # stepping through grandchild objects for the address! 
    # print(child[5][0].text)
    # print(f"{child[5][2].text}, {child[5][3].text} {child[5][4].text}")

    # Presentable(ish) employee data via LXML
    # note: this code may be simplified by using LEN
    print(f"{child[0].text} {child[1].text}:")
    print(f"{child[2].tag}: {child[2].text}")
    print(f"{child[3].tag}: ${child[3].text}")
    print(f"{child[4].tag}: {child[4].text}")
    print(child[5][0].text)
    print(f"{child[5][2].text}, {child[5][3].text} {child[5][4].text}")
    print(child.get("email"))  # attribute syntax 
    print()












  
