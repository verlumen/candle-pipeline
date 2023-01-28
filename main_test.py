import unittest


class MainTestCase(unittest.TestCase):
    def test_import(self):
        # Act
        import main

        # Assert
        self.assertIsNotNone(main)


if __name__ == "__main__":
    unittest.main()
