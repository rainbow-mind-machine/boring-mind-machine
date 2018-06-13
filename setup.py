from setuptools import setup

version = "2.0"

setup(  name='boringmindmachine',
        version=version,
        description='Boring base classes for awesome bot flocks.',
        url='https://pages.charlesreid1.com/boring-mind-machine',
        author='charlesreid1',
        author_email='charles@charlesreid1.com',
        test_suite='nose.collector',
        tests_require=['nose'],
        license='MIT',
        packages=['boringmindmachine'],
        install_requires=[
            'oauth2>=1.5',
            'simplejson>=3.13',
            'python-twitter>=3.4.1',
            'oauth2client>=3.0.0',
            'requests>=1.0.0'],
        zip_safe=False)

