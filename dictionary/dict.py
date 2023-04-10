fullDetails = {'name': 'Abdullah', 'address': 'Nagbari',
               'job': 'Software Engineer', 'location': 'remote'}

# check datatype
print(type(fullDetails))

# check output my data store
print(fullDetails)

# check my results

fullDetails['job'] = 'Full-stack Developer'

print(fullDetails['job'])

# new add item for data store

fullDetails['hometown'] = 'Tangail'

print(fullDetails)

fullDetails.values()

print(f'check ', fullDetails)
