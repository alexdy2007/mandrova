from setuptools import setup, find_packages

#python setup.py clean --all bdist_wheel
setup(
    #this will be the package name you will see, e.g. the output of 'conda list' in anaconda prompt
    name = 'mandrova',
    #some version number you may wish to add - increment this after every update
    version='0.1',
    packages=find_packages(exclude=["tutorials"]),
    setup_requires=["wheel"],
    include_package_data=True,
    install_requires=["numpy", "sympy", "pandas", "scikit-learn", "matplotlib"],
    license_files = ('LICENSE',)
)



