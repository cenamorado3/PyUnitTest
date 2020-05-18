import unittest
from AngularWeb.src.app.WebServer.BinomaticDisconfigurationTool import BinomaticDisconfigurationTool
class TestBinomaticDisconfigurationTool(unittest.TestCase):
    def test_Conversion(self):
        a = BinomaticDisconfigurationTool()
        x = a.ConvertToBinaryArray(20900000)
        self.assertEqual(['000010', '000000', '001001', '000000', '000000', '000000', '000000', '000000'], x)

    def test_Prime(self):
        a = BinomaticDisconfigurationTool()
        primes = [2, 3, 5, 199]
        for i in primes:
            self.assertTrue(a.Prime(i))

    def test_LeftShift(self):
        a = BinomaticDisconfigurationTool()
        #b     1    110001           00000001 = 1
        #b<<1  2 '  110010           00000010 = 2
        b = 123415
        bN = b << 1

        self.assertEqual(bN, a.LeftShift(b))
        self.assertEqual(a.ConvertToBinaryArray(bN), a.ConvertToBinaryArray(a.LeftShift(b)))

    def test_Unpack(self):
        a = BinomaticDisconfigurationTool()
        x = ['000010', '000000', '001001', '000000', '000000', '000000', '000000', '000000']
        self.assertEqual(a.Unpack(x), 20900000)
        
if __name__ == '__main__':
    unittest.main()