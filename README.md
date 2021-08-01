# pykt #

### Overview ###

`pykt` is a Python module containing tools to read Kp and ap index files in WDC format.

### Installation ###

To install the module:

```sh
$ cd INSTALLDIR
$ pip install ARCHIVE
```

### Usage ###

To extract data from kp index file:

```python
import pykp

data = pykp.get_values(filename, begin_date, end_date)
```

where `begin_date` (optional) and `end_date` (optional) are the lower/upper bound of the
query interval.

The function returns a dictionary with three fields: `timestamp`, `Kp`, `ap`.

### WDC format ###

The following documentation is adapted from [1] and [2]:

Columns |  Format  | Description
--------|----------|:---------------------------------------------------------------
 1-2    |  I2      | Year.
 3-4    |  I2      | Month.
 5-6    |  I2      | Day.
 7-10   |  I4      | Bartels Solar Rotation Number - a sequence of 27-day intervals
        |          | counted continuously from February 8, 1832.
11-12   |  I2      | Number of day within the Bartels 27-day cycle.
13-14   |  I2      | Kp or planetary 3-hour range index for 0000 - 0300 UT.
15-16   |  I2      | Kp or planetary 3-hour range index for 0300 - 0600 UT.
17-18   |  I2      | Kp or planetary 3-hour range index for 0600 - 0900 UT.
19-20   |  I2      | Kp or planetary 3-hour range index for 0900 - 1200 UT.
21-22   |  I2      | Kp or planetary 3-hour range index for 1200 - 1500 UT.
23-24   |  I2      | Kp or planetary 3-hour range index for 1500 - 1800 UT.
25-26   |  I2      | Kp or planetary 3-hour range index for 1800 - 2100 UT.
27-28   |  I2      | Kp or planetary 3-hour range index for 2100 - 2400 UT.
29-31   |  I3      | Sum of the eight Kp indices for the day expressed to the nearest
        |          | third of a unit.
32-34   |  I3      | ap or planetary equivalent amplitude for 0000 - 0300 UT.
35-37   |  I3      | ap or planetary equivalent amplitude for 0300 - 0600 UT.
38-40   |  I3      | ap or planetary equivalent amplitude for 0600 - 0900 UT.
41-43   |  I3      | ap or planetary equivalent amplitude for 0900 - 1200 UT.
44-46   |  I3      | ap or planetary equivalent amplitude for 1200 - 1500 UT.
47-49   |  I3      | ap or planetary equivalent amplitude for 1500 - 1800 UT.
50-52   |  I3      | ap or planetary equivalent amplitude for 1800 - 2100 UT.
53-55   |  I3      | ap or planetary equivalent amplitude for 2100 - 2400 UT.
56-58   |  I3      | Ap or planetary equivalent amplitude - the arithmetic mean
        |          | of the day's eight ap values.
59-61   |  F3.1    | Cp or planetary daily character figure - a qualitative estimate
        |          | of overall level of magnetic activity for the day determined
        |          | from the sum of the eight ap amplitudes.  Cp ranges, in steps
        |          | of one-tenth, from 0 (quiet) to 2.5 (highly disturbed).
62-62   |  I1      | C9 - a conversion of the 0-to-2.5 range of the Cp index to one
        |          | digit between 0 and 9.
63-65   |  I3      | International Sunspot Number. Records contain the Zurich
        |          | number through December 31, 1980, and the International
        |          | Brussels number thereafter.
        |          | **Not any more reported from 2015 onwards**
66-70   | F5.1     | Ottawa 10.7 cm solar radio flux adjusted TO 1 AU - measured at
        |          | 1700 UT daily and expressed in units of 10^-22 Watts/
        |          | meter sq/hertz.  Observations began on February 14, 1947. 
        |          | From that date through December 31, 1973, the fluxes given
        |          | here don't reflect the revisions Ottawa made in 1966. NOTE: 
        |          | If a solar radio burst is in progress during the observation
        |          | the pre-noon or afternoon value is used (as indicated by a
        |          | flux qualifier value of 1 in column 71.
        |          | **Not any more reported from 2007 onwards**
71-71   | I1       | Flux qualifier. "0" indicates flux required no adjustment; 
        |          | "1" indicates flux required adjustment for burst in progress
        |          | at time of measurement; "2" indicates a flux approximated by
        |          | either interpolation or extrapolation; and "3" indicates no
        |          | observation.
        |          | **Not any more reported from 2007 onwards**

[1]: ftp://ftp.ngdc.noaa.gov/STP/GEOMAGNETIC_DATA/INDICES/KP_AP/kp_ap.fmt
[2]: ftp://ftp.gfz-potsdam.de/pub/home/obs/kp-ap/wdc/wdc_fmt.txt

### Availability ###

Recent data:
- http://www-app3.gfz-potsdam.de/kp_index/pqlyymm.wdc
- http://www-app3.gfz-potsdam.de/kp_index/kpyymm.wdc
- http://www-app3.gfz-potsdam.de/kp_index/qlyymm.wdc

Archive:
- ftp://ftp.gfz-potsdam.de/pub/home/obs/kp-ap/
