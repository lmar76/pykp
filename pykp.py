import datetime
import numpy


__version__ = '1.0'


def get_values(filename, begin_date=None, end_date=None):
    """Extract timestamps, Kp and ap indices from `filename`.

    Parameters
    ----------
    filename : str
        Kp indices filename.
    begin_date : date, datetime or None
        get values having timestamps greater than or equal to `begin_date`.
    end_date : date, datetime or None
        get values having timestamps lower than or equal to `end_date`.

    Returns
    -------
    dict of numpy.array
        timestamps and Dst indices extracted from `filename`.

    Raises
    ------
    OSError
        if `filename` is not readable.
    TypeError
        if type of `begin_date` or `end_date` is wrong.
    ValueError
        if `filename` is not valid.
    """
    # Check filename
    if not isinstance(filename, str):
        raise TypeError('filename must be str, not %s' % type(str))

    # Check dates
    if begin_date is None:
        begin_date = datetime.datetime(datetime.MINYEAR, 1, 1)
    elif isinstance(begin_date, datetime.date):
        if isinstance(begin_date, datetime.datetime):
            pass
        else:
            begin_date = datetime.datetime.combine(begin_date, datetime.time())
    else:
        raise TypeError('begin_date must be date, datetime or None, not %s' % type(begin_date))
    if end_date is None:
        end_date = datetime.datetime(datetime.MAXYEAR, 12, 31, 23, 59, 59, 999999)
    elif isinstance(end_date, datetime.date):
        if isinstance(end_date, datetime.datetime):
            pass
        else:
            end_date = datetime.datetime.combine(end_date, datetime.time())
    else:
        raise TypeError('end_date must be date, datetime or None, not %s' % type(begin_date))

    # Fetch data
    params = {
        'timestamp': [],
        'Kp': [],
        'ap': []
    }
    with open(filename) as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip()
            try:
                # Parse year (columns 0-1)
                year = int(line[0:2]) + 2000
                # Parse month (columns 2-3)
                month = int(line[2:4])
                # Parse day (columns 4-5)
                day = int(line[4:6])
                ts = datetime.datetime(year, month, day)
                for group in range(0, 8):
                    # Parse Kp indices (columns 12-27), 8 groups of 2 chars.
                    kpvalue = line[12:28][group * 2:group * 2 + 2]
                    # Parse ap indices (columns 31-54), 8 groups of 3 chars.
                    apvalue = line[31:55][group * 3:group * 3 + 3]
                    if kpvalue != '99' and apvalue != '   ':
                        ts += datetime.timedelta(hours=3)
                        if begin_date <= ts <= end_date:
                            params['timestamp'].append(ts)
                            params['Kp'].append(int(kpvalue))
                            params['ap'].append(int(apvalue))
                    else:
                        break
            except ValueError as err:
                raise ValueError('line %d not valid: %s' % (n, err))

        # Convert lists to arrays and return values
        return {p: numpy.array(params[p]) for p in params}
