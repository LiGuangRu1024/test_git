# 时间：2023/6/12 17:43
# 人员: 莉光哈哈哈
import unittest


class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(2, 2, "判断相等")
        self.assertIn('h', 'this')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(1, 1, "判断相等")
        # self.assertIn('h', 'this')

    @unittest.skipIf(1 + 1 == 2, "跳过该条用例")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(3, 4, "判断相等")
        # self.assertIn('h', 'this')


class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print("test_demo1 case0")

    def test_demo1_case1(self):
        print("test_demo1 case1")


class demo2(unittest.TestCase):
    def test_demo2_case0(self):
        print("test_demo2 case0")

    def test_demo2_case1(self):
        print("test_demo2 case1")


if __name__ == '__main__':
    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(demo3("test_case01"))
    # suite.addTest(demo1("test_demo1_case0"))
    # unittest.TextTestRunner().run(suite)

    # suite = unittest.TestLoader().loadTestsFromTestCase(demo3)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suiteall = unittest.TestSuite([suite, suite1])
    # unittest.TextTestRunner().run(suiteall)

    discover = unittest.defaultTestLoader.discover(("./", "test*.py"))
    unittest.TextTestRunner().run(discover)
