import unittest


class CandlePipelineTestCase(unittest.TestCase):
    def test_import(self):
        # Act
        import candle_pipeline

        # Assert
        self.assertIsNotNone(candle_pipeline)


if __name__ == "__main__":
    unittest.main()
