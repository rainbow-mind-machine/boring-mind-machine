from setuptools import setup

version = "2"

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
            'PyGithub>=1.39',
            'google-api-python-client>=1.7.3',
            'pyasn1-modules>=0.2.1',
            'apiclient',
            'httplib2>=0.10.3',
            'requests>=1.0.0'],
        zip_safe=False)

