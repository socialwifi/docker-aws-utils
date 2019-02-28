try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements
from setuptools import find_packages
from setuptools import setup

setup(
    name='aws_utils',
    packages=find_packages(exclude=['tests']),
    install_requires=[str(ir.req) for ir in parse_requirements('base_requirements.txt', session=False)],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'upload_tar = aws_utils.commands.upload_tar:run',
        ],
    },
)
