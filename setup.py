from setuptools import setup

version = "13"

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
            'oauth2client>=3.0.0',
            'apiclient',
            'httplib2>=0.10.3',
            'requests>=1.0.0'],
        zip_safe=False)

