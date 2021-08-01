from setuptools import setup


def get_version(filename):
    """Read version info from file without importing it."""
    for line in open(filename):
        if '__version__' in line:
            if '"' in line:
                # __version__ = "0.9"
                return line.split('"')[1]
            elif "'" in line:
                # __version__ = '0.9'
                return line.split("'")[1]


setup(
    name='pykp',
    version = get_version('pykp.py'),
    py_modules=['pykp'],
    description='Python library for reading Kp and ap values.',
    author='Luca Mariani',
    author_email='lmar76@gmail.com',
    url='https://bitbucket.org/lmar76/pykp/overview',
    keywords=['kp', 'ap'],
    setup_requires=['numpy'],
)
