from setuptools import setup
from boringmindmachine import __version__

setup(  name='boringmindmachine',
        version=__version__,
        description='Boring base classes for awesome bot flocks.',
        url='https://pages.charlesreid1.com/boring-mind-machine',
        author='charlesreid1',
        author_email='charles@charlesreid1.com',
        test_suite='nose.collector',
        tests_require=['nose'],
        license='MIT',
        packages=['boringmindmachine'],
        install_requires=[],
        zip_safe=False)

