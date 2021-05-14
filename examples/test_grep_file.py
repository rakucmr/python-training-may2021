import os
import unittest

from examples.files import grep


class GrepTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filename = 'testfile'
        with open(cls.filename, 'w') as f:
            f.write('hello\nhello again\nhi\nbye\nhell')

    def test_grep_lines_found(self):
        lines = grep(self.filename, 'hell')
        self.assertEqual(lines, ['hello', 'hello again', 'hell'])

    def test_grep_lines_not_found(self):
        lines = grep(self.filename, 'bla')
        self.assertEqual(lines, [])

    def test_grep_empty_string(self):
        lines = grep(self.filename, '')
        self.assertEqual(lines, ['hello', 'hello again', 'hi', 'bye', 'hell'])

    def test_file_does_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            grep('inexistent_file', '')

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.filename)
