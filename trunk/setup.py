from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='jing',
      version=version,
      description="",
      long_description="""""",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'flask',
        'flask-script',
        'WTForms',
        'blinker',
        'Flask-Assets',
        'Flask-Babel',
        'Flask-Bcrypt',
        'flask-htmlbuilder',
        'Flask-Login',
        'Flask-Principal',
        'flask-security',
        'Flask-Mail',
        'Flask-Testing',
        'Flask-Cache',
        'flask-admin',
        'flask-babelex',
        'flask-debugtoolbar',
        'flask-collect',
        'flake8',
        'passlib',
        'twill',
        'markupsafe',
        'Pillow',
        'abu.admin',
        'Mysql-python>=1.2.3',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [abu.admin]
      jing = jing.admin:Admin
      """,
      )
