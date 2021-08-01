import datetime
import numpy
import os
import unittest
import pykp


class TestGetValues(unittest.TestCase):
    """Test the `get_values` function."""
    def setUp(self):
        self.data = os.path.join(os.path.dirname(__file__), "data")

    def test_not_existent(self):
        """Test with not existent file."""
        self.assertRaises(OSError, pykp.get_values, "xxx")

    def test_wdc(self):
        """Test with correct AUX_KP__2F file."""
        testfile = os.path.join(
            self.data,
            "SW_OPER_AUX_KP__2F_20160701T000000_20160704T030000_0001.DBL"
        )
        r_t = numpy.array([datetime.datetime(2016, 7, 1, 3, 0),
                           datetime.datetime(2016, 7, 1, 6, 0),
                           datetime.datetime(2016, 7, 1, 9, 0),
                           datetime.datetime(2016, 7, 1, 12, 0),
                           datetime.datetime(2016, 7, 1, 15, 0),
                           datetime.datetime(2016, 7, 1, 18, 0),
                           datetime.datetime(2016, 7, 1, 21, 0),
                           datetime.datetime(2016, 7, 2, 0, 0),
                           datetime.datetime(2016, 7, 2, 3, 0),
                           datetime.datetime(2016, 7, 2, 6, 0),
                           datetime.datetime(2016, 7, 2, 9, 0),
                           datetime.datetime(2016, 7, 2, 12, 0),
                           datetime.datetime(2016, 7, 2, 15, 0),
                           datetime.datetime(2016, 7, 2, 18, 0),
                           datetime.datetime(2016, 7, 2, 21, 0),
                           datetime.datetime(2016, 7, 3, 0, 0),
                           datetime.datetime(2016, 7, 3, 3, 0),
                           datetime.datetime(2016, 7, 3, 6, 0),
                           datetime.datetime(2016, 7, 3, 9, 0),
                           datetime.datetime(2016, 7, 3, 12, 0),
                           datetime.datetime(2016, 7, 3, 15, 0),
                           datetime.datetime(2016, 7, 3, 18, 0),
                           datetime.datetime(2016, 7, 3, 21, 0),
                           datetime.datetime(2016, 7, 4, 0, 0),
                           datetime.datetime(2016, 7, 4, 3, 0)], dtype=datetime.datetime)
        r_kp = numpy.array([27, 17, 20, 20, 13, 7, 0, 3, 3, 10, 7, 7, 13, 7, 27,
                            37, 30, 17, 13, 13, 10, 23, 20, 27, 13])
        r_ap = numpy.array([12, 6, 7, 7, 5, 3, 0, 2, 2, 4, 3, 3, 5, 3, 12, 22,
                            15, 6, 5, 5, 4, 9, 7, 12, 5])
        result = pykp.get_values(testfile)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result['timestamp'], numpy.ndarray)
        numpy.testing.assert_array_equal(result['timestamp'], r_t)
        self.assertIsInstance(result['Kp'], numpy.ndarray)
        numpy.testing.assert_array_equal(result['Kp'], r_kp)
        self.assertIsInstance(result['ap'], numpy.ndarray)
        numpy.testing.assert_array_equal(result['ap'], r_ap)

    def test_wdc_time_filter(self):
        """Test with AUX_KP__2F file (wdc format) and time filter:
        2016-07-01 04:00:00 <= t <= 2016-07-01 14:00:00.
        """
        testfile = os.path.join(
            self.data,
            "SW_OPER_AUX_KP__2F_20160701T000000_20160704T030000_0001.DBL"
        )
        r_t = numpy.array([datetime.datetime(2016, 7, 1, 6, 0),
                           datetime.datetime(2016, 7, 1, 9, 0),
                           datetime.datetime(2016, 7, 1, 12, 0)], dtype=datetime.datetime)
        r_kp = numpy.array([17, 20, 20])
        r_ap = numpy.array([6, 7, 7])
        result = pykp.get_values(
            testfile,
            begin_date=datetime.datetime(2016, 7, 1, 4, 0),
            end_date=datetime.datetime(2016, 7, 1, 14, 0)
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result['timestamp'], numpy.ndarray)
        numpy.testing.assert_array_equal(result['timestamp'], r_t)
        self.assertIsInstance(result['Kp'], numpy.ndarray)
        numpy.testing.assert_array_equal(result['Kp'], r_kp)
        self.assertIsInstance(result['ap'], numpy.ndarray)
        numpy.testing.assert_array_equal(result['ap'], r_ap)

    def test_wdc_old_file(self):
        """Test with an old file containing also International Sunspot Number
        (columns 63-65).
        """
        testfile = os.path.join(self.data, 'kp0101.wdc')
        result = pykp.get_values(testfile)
        r_t = numpy.arange(
            '2001-01-01T03:00:00',
            '2001-01-05T03:00:00',
            numpy.timedelta64(3, 'h'),
            dtype='datetime64[s]'
        ).astype(datetime.datetime)
        r_kp = numpy.array(
            [
                0, 3, 10, 10, 3, 3, 7, 7,
                13, 3, 0, 0, 7, 3, 10, 27,
                23, 37, 23, 23, 23, 7, 7, 10,
                23, 13, 30, 23, 30, 30, 23, 23
            ]
        )
        r_ap = numpy.array(
            [
                0, 2, 4, 4, 2, 2, 3, 3,
                5, 2, 0, 0, 3, 2, 4, 12,
                9, 22, 9, 9, 9, 3, 3, 4,
                9, 5, 15, 9, 15, 15, 9, 9
            ]
        )
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result['timestamp'], numpy.ndarray)
        numpy.testing.assert_array_equal(result['timestamp'], r_t)
        self.assertIsInstance(result['Kp'], numpy.ndarray)
        numpy.testing.assert_array_equal(result['Kp'], r_kp)
        self.assertIsInstance(result['ap'], numpy.ndarray)
        numpy.testing.assert_array_equal(result['ap'], r_ap)


if __name__ == "__main__":
    unittest.main()
