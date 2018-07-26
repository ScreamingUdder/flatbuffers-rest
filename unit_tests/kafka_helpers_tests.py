import unittest
from App.kafka_helpers import num_of_messages_int_check, parameter_empty, default_port


class KafkaHelperTests(unittest.TestCase):

    def test_int_check_with_int_input(self):
        self.assertEqual(num_of_messages_int_check('12'), 12)

    def test_parameter_empty_when_not_empty(self):
        self.assertEqual(parameter_empty('Topic', 'Broker'), None)

    def test_parameter_empty_when_empty(self):
        with self.assertRaises(Exception):
            parameter_empty('', '')

    def test_default_port_has_port(self):
        self.assertEqual(default_port('hinata.isis.cclrc.ac.uk:9092'), 'hinata.isis.cclrc.ac.uk:9092')

    def test_default_port_has_no_port(self):
        self.assertEqual(default_port('hinata.isis.cclrc.ac.uk'), 'hinata.isis.cclrc.ac.uk:9092')


class KafkaHelperTestExpectedFails(unittest.TestCase):
    @unittest.expectedFailure  # On test raises expected error but shows as failed test
    def test_int_check_with_char_input(self):
        self.assertRaises(ValueError, num_of_messages_int_check('A'))

    @unittest.expectedFailure  # On test raises expected error but shows as failed test
    def test_int_check_with_char_and_int_input(self):
        self.assertRaises(ValueError, num_of_messages_int_check('23A'))


if __name__ == '__main__':
    unittest.main()
