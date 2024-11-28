import unittest
import Простые_Юнит_Тесты, Методы_Юнит_тестирования

testTS = unittest.TestSuite()
testTS.addTest(unittest.TestLoader().loadTestsFromTestCase(Простые_Юнит_Тесты.RunnerTest))
testTS.addTest(unittest.TestLoader().loadTestsFromTestCase(Методы_Юнит_тестирования.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testTS)