import unittest
import universal_translator

class UniversalTranslatorTest(unittest.TestCase):
    '''Raises file not found error if the given file route is empty'''
    def test_empty_file_route(self):
        universe = universal_translator.UnitsTranslator('')
        with self.assertRaises(FileNotFoundError):
            universe.read_file()

    '''Raises file not found error if the user is tries to use a file that does not exist'''
    def test_file_does_not_exist(self):
        universe = universal_translator.UnitsTranslator('File examples/test22345.txt')
        with self.assertRaises(FileNotFoundError):
            universe.read_file()

    '''Raises key error exception if unit is not valid'''
    def test_unit_not_valid(self):
        universe = universal_translator.UnitsTranslator('File examples/test.txt')
        with self.assertRaises(KeyError):
            universe.convert_unit(25, 'm', 'c')

    '''Raises is a directory error if the route does not point to a file but to a directory'''
    def test_is_a_directory(self):
        universe = universal_translator.UnitsTranslator('File examples')
        with self.assertRaises(IsADirectoryError):
            universe.read_file()

    '''Raises type error if the given value is not a number but another type'''
    def test_not_a_number(self):
        universe = universal_translator.UnitsTranslator('File examples/test.txt')
        with self.assertRaises(TypeError):
            universe.convert_unit('this is a test', 'm', 'cm')
    '''Raises a value error if we try to convert the given value but it's not possible'''
    def test_not_a_number2(self):
        universe = universal_translator.UnitsTranslator('File examples/test.txt')
        with self.assertRaises(ValueError):
            universe.convert_unit(float('this is a test'), 'm', 'cm')

if __name__ == '__main__':
    unittest.main()
