from lxml import etree 

"""
The purpose of this file is to demonstrate basic XML/Python parsing operations using the LXML library. 
I'm leaning in the direction of using the XMLtoDict library for this program, but in case I change my
mind, the steps below should indicate how we'll extract data from 'CompanyData.xml'. -MPG, 6.30.24
"""

# Get the XML file data
company_data = open("CompanyData.xml", "r")

# Parse the data into an ETree object
mihker_etree = etree.parse(company_data)

# Get the "root element object" (this would be the "Employees" object here)
root = mihker_etree.getroot()

# How to navigate:
print(root.tag)   # output: Employees (root tag)
print(len(root))  # output: 4
print(root[0].tag)  # output: Employee
print(root[1].tag)  # output: Employee (this is where the Employee tags reside)
print(root[0])   # output: 'Element Employee at 0x213b...'
# print(root[0]["Employee"])  # "TypeError: 'str' object cannot be interpreted as an integer"
print(root[0][0])  # output: 'Element FirstName at 0x...' 
print(root[0][0].text)  # output: Mihker
print(f"{root[0][0].text}'s salary is ${root[0][4].text} and his email is {root[0][2].text}")
# output: Mihker's salary is $169000 and his email is mihker.gardner@fakecompany.com 
print(len(root[0])) # output: 7 
salary = (len(root[0])) - 3  # assigned "4" to the salary variable
print(type(salary))  # output: <class 'int'>
print(salary)  # output: 4
print(f"Jill's salary is ${root[2][salary].text}")  # Jill's salary is $200000
print(f"Lily's salary is ${root[1][salary].text}")  # Lily's salary is $100000

##################################################################################

"""
Extracting an attribute value.
Note: I removed the 'email' attribute from CompanyData.xml and added it as a tag instead (made no sense to 
store it that way). Below is how you would extract that attribute value if it was still there. 
"""
# for child in root:
#     print(child.get("@email"))

##################################################################################

"""
for loops: useful for iterating through our source data
"""

for child in root:
    print(f"Name: {child[0].text} {child[1].text}:")
    print(f"{child[2].tag}: {child[2].text}")
    print(f"{child[3].tag}: {child[3].text}")
    print(f"{child[4].tag}: ${child[4].text}")
    print(f"{child[5].tag}: {child[5].text}")
    print(child[6][0].text)
    print(f"{child[6][2].text}, {child[6][3].text} {child[6][4].text}")
    print() 

# output: produces (very lightly) formatted employee info including address

##################################################################################

"""
We might want to iterate through the values of tags that appear in multiple elements
This is an example of the 'iter' function:
"""
 
for salary in root.iter('Salary'):
    print(salary.text)  # output: each salary value prints to one line

for dept in root.iter('Dept'):
    print(dept.text)  # output: each dept value prints to one line

# The 'find all' function finds all the children with a specific tag name. When you use the find all 
# function on a node, it only looks at the children, not the grandchildren. 

print(len(root[0].findall('FirstName')))  # output: 1 
print(root[0].findall('FirstName')[0].text)  # output: Mihker
print(root[1].findall('FirstName')[0].text)  # output: Lily

##################################################################################

"""
This is how you WRITE to and REMOVE DATA FROM CompanyData.xml:
"""

# root[0][0].text = "Bihker" 
# mihker_etree.write('CompanyData.xml')  # holy hell IT WORKS!! 

# this is how you REMOVE A TAG from CompanyData.xml
# root[3].remove(root[3][3])  # I didn't execute - this would remove the dog's salary lol

##################################################################################


"""
Note to future self: you can use XPATH query within LXML to reference tags by name instead of index 
value. I'm leaning in the direciton of using xmltodict instead, but if you need to use lxml 
down the road and reference tags by name, the format/syntax (on a general level) is:
description = data.xpath('tagname//tagname)(just look this up later if you need or want to)
"""







  
