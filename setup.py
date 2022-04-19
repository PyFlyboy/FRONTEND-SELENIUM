from setuptools import setup, find_packages


setup(name='FrontTests',
      version='1.0',
      description="Selenium",
      author='Tomasz Kraczka',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "pytest==7.1.1",
          "pytest-html==3.1.1",
          "requests==2.27.1",
          "requests-oauthlib==1.3.0",
          "selenium==4.1.2",
          "pytest-xdist==2.5.0"
          "pymysql"

      ]
      )