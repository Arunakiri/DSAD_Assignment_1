class HashTable:
    def __init__(self):
        self.length = 13
        self.array = [[] for _ in range(self.length)]

    def HashId(self, key):
        ascii_val = sum([2 ** idx * ord(x) for idx, x in enumerate(key)])
        return ascii_val % self.length

    def __setitem__(self, key, val):
        hash_key = self.HashId(key)
        flag = False

        for idx, kv in enumerate(self.array[hash_key]):
            if key == kv[0]:
                self.array[hash_key][idx] = (key, val)
                flag = True
                break

        if flag == False:
            self.array[hash_key].append((key, val))

    def __getitem__(self, key):
        hash_key = self.HashId(key)

        for kv in self.array[hash_key]:
            if key == kv[0]:
                return kv[1]

        return 'No Such Key Exists'

    def __delitem__(self, key):
        hash_key = self.HashId | (key)

        for idx, kv in enumerate(self.array[hash_key]):
            if key == kv[0]:
                del self.array[hash_key][idx]
                break


def insertAppDetails(ApplicationRecords, name, phone, memRef, status):
    ApplicationRecords[name] = [phone, memRef, status]


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


def memberRef(ApplicationRecords, memID):
    member = []
    for each_idx in ApplicationRecords.array:
        for kv in each_idx:
            if kv[1][1] == memID:
                member.append(kv[0] + ' / ' + kv[1][0] + ' / ' + kv[1][2] + '\n')
    return member


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

    return ['Applied: ' + str(applied) + '\n', 'Verified: ' + str(verified) + '\n', 'Approved: ' + str(approved) + '\n']


def destroyHash(ApplicationRecords):
    ApplicationRecords = HashTable()
    return ApplicationRecords.array


input_file = open(r'inputPS8.txt', 'r+')
output_file = open(r'outputPS8_kiri.txt', 'w+')
prompt_file = open(r'promptsPS8.txt', 'r+')

# output_file.seek(0)
# output_file.truncate()

ApplicationRecords = HashTable()

application_count = 0

for each in input_file.readlines():
    name, phone, memRef, status = [x.strip() for x in each.strip().split('/')]
    insertAppDetails(ApplicationRecords, name, phone, memRef, status)
    application_count += 1

print(application_count)
insert_msg = 'Successfully inserted ' + str(application_count) + ' applications into the system.'
output_file.write(insert_msg + '\n')

for each in prompt_file.readlines():
    try:
        func, data = each.strip().split(':')
        if func == 'Update':
            name, phone, memRef, status = [x.strip() for x in data.split('/')]
            field = updateAppDetails(ApplicationRecords, name, phone, memRef, status)
            for each in field:
                update_msg = 'Updated details of ' + name + '.' + ' Application ' + each + ' has been changed.\n'
                output_file.write(update_msg)

        elif func == 'memberRef':
            memID = data.strip()
            members = memberRef(ApplicationRecords, memID)
            output_file.write('---------- Member reference by ' + memID + ' ----------\n')
            output_file.writelines(members)
            output_file.write('-------------------------------------\n')

    except:
        if each.strip() == 'appStatus':
            appstat = appStatus(ApplicationRecords)
            output_file.write('---------- Application Status ----------\n')
            output_file.writelines(appstat)
            output_file.write('-------------------------------------\n')

