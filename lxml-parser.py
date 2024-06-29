from lxml import etree 

"""
This module is for accessing CompanyData.xml via the lxml library. -MPG, 6/28/24
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

# basic parsing by index number
# for child in root:
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
    # print(f"{child[0].text} {child[1].text}:")
    # print(f"{child[2].tag}: {child[2].text}")
    # print(f"{child[3].tag}: ${child[3].text}")
    # print(f"{child[4].tag}: {child[4].text}")
    # print(child[5][0].text)
    # print(f"{child[5][2].text}, {child[5][3].text} {child[5][4].text}")
    # print(child.get("email"))  # attribute syntax 
    # print()
  
#######################################################

# We might want to iterate through the values of tags that appear in multiple elements
# This is an example of the 'iter' function: 
# for salary in root.iter('Salary'):
#     print(salary.text)

# for dept in root.iter('Dept'):
#     print(dept.text)

# The 'find all' function finds all the children with a specific tag name. When you use the find all 
# function on a node, it only looks at the children, not the grandchildren. 

# print(len(root[0].findall('FirstName')))
# print(root[0].findall('FirstName')[0].text)
"""
Output:
1
Mihkel
* because we indexed from root[0], there was only 1 iteration of the FirstName tag, hence 1.
* the 2nd print statement simply prints the value of the specified tag
"""

# this is how you WRITE to CompanyData.xml:
# root[0][0].text = "Bihker" 
# mihker_etree.write('CompanyData.xml')  # holy hell IT WORKS!! 

# this is how you REMOVE A TAG from CompanyData.xml
# root[3].remove(root[3][3])  # didn't execute - this would remove the dog's salary lol

"""
Note to future self: you can use XPATH query within LXML to reference tags by name instead of index 
value. I'm leaning in the direciton of using xmltodict instead, but if you need to use lxml 
down the road and reference tags by name, the format/syntax (on a general level) is:
description = data.xpath('tagname//tagname)(just look this up later if you need to)
"""







  
