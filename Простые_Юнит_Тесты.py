import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name
    
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, f'Тесты в этом кейсе заморожены. is_frozen = {str(is_frozen)}')
    def test_walk(self):
        runner = Runner('Гриша')

        for _ in range(10):
            runner.walk()

        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, f'Тесты в этом кейсе заморожены. is_frozen = {str(is_frozen)}')
    def test_run(self):
        runner = Runner('Гриша')

        for _ in range(10):
            runner.run()

        self.assertEqual(runner.distance, 100)
    
    @unittest.skipIf(is_frozen, f'Тесты в этом кейсе заморожены. is_frozen = {str(is_frozen)}')
    def test_challenge(self):
        runner1 = Runner('Гриша')
        runner2 = Runner('Петя')

        for _ in range(10):
            runner1.walk()

        for _ in range(10):
            runner2.run()

        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()