import unittest


class Emproyee:
    def __init__(self, first_name, second_name, salary) -> None:
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary

    def give_raise(self, amount=5_000):
        self.salary += amount


class EmproyeeTest(unittest.TestCase):
    def setUp(self):
        self.emproyee = Emproyee("John", "Billington", 10_000)

    def test_default_raise(self):
        self.emproyee.give_raise()
        self.assertEqual(self.emproyee.salary, 15_000)

    def test_custom_raise(self):
        self.emproyee.give_raise(10_000)
        self.assertEqual(self.emproyee.salary, 20_000)
        pass


if __name__ == "__main__":
    unittest.main()
