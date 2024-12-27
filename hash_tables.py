import pandas as pd

my_dict = {'Dave': '001', 'Ava': '002', 'Joe': '003'}
# print(my_dict) -> {'Dave': '001', 'Ava': '002', 'Joe': '003'}
# type(my_dict) -> dict'
# my_dict['Dave'] -> 001

# Functions
# print(my_dict.keys()) -> ['Dave', 'Ava', 'Joe']
# print(my_dict.values()) -> ['001', '002', '003']
# print(my_dict.get('Dave')) -> 001

# Nested Dictionary
emp_details = {'Employee': {'Dave': {'ID': '001',
                                     'Salary': 2000,
                                     'Designation': 'Python Developer'},
                            'Ava': {'ID': '002',
                                    'Salary': 2300,
                                    'Designation': 'Java Developer'},
                            'Joe': {'ID': '003',
                                    'Salary': 1843,
                                    'Designation': 'Hadoop Developer'}}}

# In the loop
print("All keys")
for x in my_dict:
    print(x)  # prints the keys
print("All values")
for x in my_dict.values():
    print(x)  # prints values
print("All keys and values")
for x, y in my_dict.items():
    print(x, ":", y)  # prints keys and values

# Updating dictionary
my_dict['Dave'] = '004'  # updating the value of Dave
my_dict['Chris'] = '005'  # adding a key-value pair
print(my_dict)

# Deleting from dictionary
my_dict = {'Dave': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}
del my_dict['Dave']  # removes key-value pair of 'Dave'
my_dict.pop('Ava')  # removes the value of 'Ava'
my_dict.popitem()  # removes the last inserted item
print(my_dict)

print("")
# Converting Dictionary into a dataframe
emp_details = {'Employee': {'Dave': {'ID': '001',
                                     'Salary': 2000,
                                     'Designation': 'Python Developer'},
                            'Ava': {'ID': '002',
                                    'Salary': 2300,
                                    'Designation': 'Java Developer'},
                            'Joe': {'ID': '003',
                                    'Salary': 1843,
                                    'Designation': 'Hadoop Developer'}}}
df = pd.DataFrame(emp_details['Employee'])
print(df)
