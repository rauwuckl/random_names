from setuptools import setup, find_packages

setup(
    name="RandomNames",
    packages=find_packages(),
    package_data = {
        'data': ['*'],
    }
    # entry_points = {
    #     'console_scripts': [
    #         'run_experiments = InSilicoModel.cli:main'
    #     ]
    # }
)