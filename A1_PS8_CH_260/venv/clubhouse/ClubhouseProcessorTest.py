import ClubhouseProcessor
import unittest


class MyTestCase(unittest.TestCase):
    def testHasTableLoadFactorIs2x(self):
        hash_table = ClubhouseProcessor.HashTable(10)
        hash_table.initializeHash()
        self.assertEqual(len(hash_table.array), 20)

        hash_table = ClubhouseProcessor.HashTable(1000)
        hash_table.initializeHash()
        self.assertEqual(len(hash_table.array), 2000)

        hash_table = ClubhouseProcessor.HashTable(0)
        hash_table.initializeHash()
        self.assertEqual(len(hash_table.array), 0)

        hash_table = ClubhouseProcessor.HashTable(-1)
        hash_table.initializeHash()
        self.assertEqual(len(hash_table.array), 0)

    def testHashIdIsUnique(self):
        hash_table = ClubhouseProcessor.HashTable(10)
        hash_table.initializeHash()
        self.assertNotEqual(hash_table.HashId("RAM"), hash_table.HashId("MAR"))
        self.assertNotEqual(hash_table.HashId("RAM"), hash_table.HashId("ARM"))
        self.assertNotEqual(hash_table.HashId("SPOT"), hash_table.HashId("POTS"))


if __name__ == "__main__" :
    unittest.main()