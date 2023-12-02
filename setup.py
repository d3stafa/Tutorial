from setuptools import setup

setup(
    name='clean_folder',
    version='1.0.0',
    description='This code can clean ur folder',
    url='https://github.com/d3stafa/clean_folder',
    author='Hripich Tymofii',
    author_email='hripich.tymofii@outlook.com',
    license='MIT',
    packages=['clean_folder'],
    entry_points={
        'console_scrips': [
            'clean-folder = clean_folder.clean:main'
        ]
    }

)
