from setuptools import setup
from textwrap import dedent

setup(
      name="ApiFK_frekassa",
      version='0.1',
      packages=['ApiFK_frekassa'],
      description='FreeKassa API. Check Balance + check status',
      long_description=dedent("""
        pip install ApiFK_frekassa
        Docs: https://github.com/DeveloperrEva/api-freekassa-py
        """),
      url='https://freekassa.ru/',
      download_url='https://github.com/DeveloperrEva/api-freekassa-py',
      install_requires=['requests>=2.27.1'],
      requires='requests',
      license='BSD License',
      classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      include_package_data=True,
)
