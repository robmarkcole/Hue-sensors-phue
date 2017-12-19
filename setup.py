from setuptools import setup

setup(
    name='hue-sensors-phue',
    version='1.0',
    py_modules=['hue_sensors_phue'],
    url='https://github.com/robmarkcole/Hue-sensors-phue',
    keywords='phillips hue',
    author='Robin Cole',
    author_email='robmarkcole@gmail.com',
    description='Tools for reading the state of Philips Hue sensors',
    install_requires=['phue'],
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"]
)
