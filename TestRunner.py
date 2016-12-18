from unittest import TestLoader, TextTestRunner, TestSuite
from day01.TaxicabTest import TaxicabTest
from day02.KeypadTest import KeypadTest
from day03.ThreeSidesTest import ThreeSidesTest
from day04.DecoyTest import DecoyTest
from day05.ChessTest import ChessTest
from day06.NoiseTest import NoiseTest
from day07.IpTest import IpTest

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
                loader.loadTestsFromTestCase(TaxicabTest),
                loader.loadTestsFromTestCase(KeypadTest),
                loader.loadTestsFromTestCase(ThreeSidesTest),
                loader.loadTestsFromTestCase(DecoyTest),
                loader.loadTestsFromTestCase(ChessTest),
                loader.loadTestsFromTestCase(NoiseTest),
                loader.loadTestsFromTestCase(IpTest)
                ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
