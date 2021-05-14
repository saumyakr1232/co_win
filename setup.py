import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="co_win vaccine availablity checker",
    version="1.0.0",
    description='A little tool to check for vaccine availability in a LOCATION of your choice.',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/saumyakr1232/vaccine_availability_cowin',
    author='saumya kumar',
    packages=['cowin', "models"],
    install_requires=["click",'termcolor', 'webbrowswer'],
    entry_points={"console_script":["availability=cowin.co_win:main"]},

)