class Member:
    def __init__(self, name, phoneNumber, mRef, status):
        self.name = name
        self.phoneNumber = phoneNumber
        self.mRef = mRef
        self.status = status

    def memberInfo(self):
        return (self.name + " / " + self.phoneNumber + " / " + self.status) + "\n"

class MemberHashTable:
    def __init__(self, size=500):
        self.map = [None] * size
        self.size = size
        self.keys = []

    def hashId(self, key):
        hash = 0
        for c in key:
            hash = hash + ord(c)
        return (hash % self.size)

    def initializeHash(self):
        self.map = [None] * self.size
        self.keys = []

    def destroyHash(self):
        self.map.clear()
        self.keys = []


    def insertAppDetails(self, member):
        key_exists = False
        key = member.name
        hashKey = self.hashId(key)
        bucket = self.map[hashKey]
        if not bucket:
            self.map[hashKey] = []
            bucket = self.map[hashKey]

        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, member))
        else:
            bucket.append((key, member))
            self.keys.append(key)

    def print(self):
        print(self.map)
        print(self.keys)

    def getAppDetails(self, name):
        key = name
        hashKey = self.hashId(key)
        bucket = self.map[hashKey]
        if bucket:
            for i, kv in enumerate(bucket):
                k, v = kv
                if key == k:
                    return v
        return None


class ApplicationDriver:
    def __init__(self):
        self.memberMap = MemberHashTable()

    def readInputFile(self):
        inputFile = open("inputPS8.txt", "r")
        count = 0
        for line in inputFile:
            memberDataList = line.split("/")
            count += 1;
            newMember = Member(memberDataList[0].strip(), memberDataList[1].strip(), memberDataList[2].strip(),
                   memberDataList[3].strip())
            self.memberMap.insertAppDetails(newMember)

        inputFile.close()
        outputFile = open("outputPS8.txt", "w")
        outputFile.write("Successfully inserted %d applications into the system.\n" % (count));
        outputFile.close()


    def readAndProcessPromptsFile(self):
        promptsFile = open("promptsPS8.txt", "r")
        for line in promptsFile:
            if line.startswith("Update"):
                self.updateAppDetails(line)
            elif line.startswith("memberRef"):
                self.memRef(line)
            elif line.startswith("appStatus"):
                self.appStatus()
        promptsFile.close()


    def memRef(self, refString):
        memberRef = refString.replace("memberRef:", "").strip()
        outputFile = open("outputPS8.txt", "a")
        outputFile.write("---------- Member reference by " + memberRef + " ----------\n")

        for key in self.memberMap.keys:
            member = self.memberMap.getAppDetails(key)
            if member.mRef == memberRef:
                outputFile.write(member.memberInfo())

        outputFile.write("-------------------------------------\n")
        outputFile.close()


    def appStatus(self):
        applied = verified = approved = 0
        for key in self.memberMap.keys:
            member = self.memberMap.getAppDetails(key)
            if member.status == "Applied":
                applied = applied + 1;
            elif member.status == "Verified":
                verified = verified + 1
            elif member.status == "Approved":
                approved = approved + 1

        outputFile = open("outputPS8.txt", "a")
        outputFile.write("---------- Application Status ----------\n")
        outputFile.write("Applied: %d\n" % (applied))
        outputFile.write("Verified: %d\n" % (verified))
        outputFile.write("Approved: %d\n" % (approved))
        outputFile.write("-------------------------------------\n")
        outputFile.close()


    def updateAppDetails(self, updateString):
        memberDataList = updateString.replace("Update:", "").split("/")


        member = self.memberMap.getAppDetails(memberDataList[0].strip())

        newPhoneNumber = memberDataList[1].strip()
        newMRef = memberDataList[2].strip()
        newStatus = memberDataList[3].strip()

        updateString = "Updating details of " + member.name + "."

        if member.phoneNumber != newPhoneNumber:
            member.phoneNumber = newPhoneNumber
            updateString = updateString + "Phone Number has been changed.\n"

        if member.mRef != newMRef:
            member.mRef = newMRef
            updateString = updateString + "Member Reference has been changed.\n"

        if member.status != newStatus:
            member.status = newStatus
            updateString = updateString + "Status has been changed.\n"

        outputFile = open("outputPS8.txt", "a")
        outputFile.write(updateString);
        outputFile.close()

appDriver = ApplicationDriver()
appDriver.readInputFile()
appDriver.readAndProcessPromptsFile()