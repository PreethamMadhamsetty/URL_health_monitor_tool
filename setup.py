# setup.py
from setuptools import setup, find_packages

setup(
    name="url-monitor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "urlmonitor=monitor.__main__:main"
        ]
    },
    author="Preetham Madhamsetty",
    description="A URL health monitor that logs status, sends email alerts, and runs on schedule",
    include_package_data=True,
)
