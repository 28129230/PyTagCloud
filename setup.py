from distutils.core import setup

setup(
    name = 'pytagcloud',
    version = '0.3.0',
    description = "Create beautiful tag clouds as images or HTML",
    author = 'Reto Aebersold',
    author_email = 'aeby@atizo.com',
    url = 'https://github.com/atizo/PyTagCloud',    
    packages = ['pytagcloud', 'pytagcloud.lang'],
    package_dir = {'pytagcloud': 'src/pytagcloud'},
    package_data = {'pytagcloud': ['fonts/*.*']},
    classifiers = [
                   'Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   ],
)