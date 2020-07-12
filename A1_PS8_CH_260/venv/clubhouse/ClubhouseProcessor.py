# Create a HashTable Class with Seperate Chaining Technique to handle Collisions
class HashTable:
    def __init__(self, entries):
        # to ensure loadfactor <= 0.5, length = 2*entries
        self.length = 2*entries

    # Initialize an empty hash table
    def initializeHash(self):
        self.array = [[] for _ in range(self.length)]

    # Generate a Hash Value of the key
    def HashId(self, key):
        ascii_val = sum([2 ** idx * ord(x) for idx, x in enumerate(key)])
        return ascii_val % len(self.array)

    # Insert/Update Key Value Pairs
    def __setitem__(self, key, val):
        hash_key = self.HashId(key)

        for idx, kv in enumerate(self.array[hash_key]):
            if key == kv[0]:
                self.array[hash_key][idx] = (key, val)
                return

        self.array[hash_key].append((key, val))

    # Get the Value from Key
    def __getitem__(self, key):
        hash_key = self.HashId(key)

        for kv in self.array[hash_key]:
            if key == kv[0]:
                return kv[1]

        return 'No Such Key Exists'


# Insert Member Details into the Hash Table
def insertAppDetails(ApplicationRecords, name, phone, memRef, status):
    ApplicationRecords[name] = [phone, memRef, status]


# Update Member Details into the Hash Table
def updateAppDetails(ApplicationRecords, name, phone, memRef, status):
    change = []

    if ApplicationRecords[name][0] != phone:
        ApplicationRecords[name][0] = phone
        change.append("Phone Number")
    if ApplicationRecords[name][1] != memRef:
        ApplicationRecords[name][1] = memref
        change.append("Member Reference")
    if ApplicationRecords[name][2] != status:
        ApplicationRecords[name][2] = status
        change.append("Status")

    return change


# Get Details of the members based on Membership ID
def memberRef(ApplicationRecords, memID):
    member = []
    for each_idx in ApplicationRecords.array:
        for kv in each_idx:
            if kv[1][1] == memID:
                name, phone, status = kv[0], kv[1][0], kv[1][2]
                member.append(name + ' / ' + phone + ' / ' + status + '\n')
    return member


# Get the Application count for each type of Status
def appStatus(ApplicationRecords):
    applied, verified, approved = 0, 0, 0
    for each_idx in ApplicationRecords.array:
        for kv in each_idx:
            if kv[1][2] == 'Applied':
                applied += 1
            elif kv[1][2] == 'Verified':
                verified += 1
            elif kv[1][2] == 'Approved':
                approved += 1

    return ['Applied: ' + str(applied) + '\n', 'Verified: ' + str(verified) + '\n',
            'Approved: ' + str(approved) + '\n']

# Empty the HashTable
def destroyHash(ApplicationRecords):
    return ApplicationRecords.initializeHash()


def processInputAndPrompt():
    # Opening text files for read/write
    input_file = open(r'inputPS8.txt', 'r+')
    output_file = open(r'outputPS8.txt', 'w+')
    prompt_file = open(r'promptsPS8.txt', 'r+')

    # Initialize the Hash Table
    entries = len(input_file.readlines())
    application_records = HashTable(entries)
    application_records.initializeHash()

    application_count = 0
    input_file.seek(0)
    # Read each line from the Input file and Call the Insert Function
    for each in input_file.readlines():
        name, phone, memRef, status = [x.strip() for x in each.strip().split('/')]
        insertAppDetails(application_records, name, phone, memRef, status)
        application_count += 1

    insert_msg = 'Successfully inserted ' + str(application_count) + ' applications into the system.'
    output_file.write(insert_msg + '\n')

    # Read each line from the Prompt file and call the appropriate functions
    for each in prompt_file.readlines():
        if each.strip() == 'appStatus':
            appstat = appStatus(application_records)
            output_file.write('---------- Application Status ----------\n')
            output_file.writelines(appstat)
            output_file.write('-------------------------------------\n')
        else:
            func, data = each.strip().split(':')
            # Update the HashTable with the given data in Prompt
            if func == 'Update':
                name, phone, memRef, status = [x.strip() for x in data.split('/')]
                field = updateAppDetails(application_records, name, phone, memRef, status)
                for each in field:
                    update_msg = 'Updated details of ' + name + '.' + ' Application ' + each + ' has been changed.\n'
                    output_file.write(update_msg)

            # Get the Member Details from the given Membership ID in Prompt
            elif func == 'memberRef':
                memID = data.strip()
                members = memberRef(application_records, memID)
                output_file.write('---------- Member reference by ' + memID + ' ----------\n')
                output_file.writelines(members)
                output_file.write('-------------------------------------\n')

if __name__ == "__main__" :
    processInputAndPrompt()