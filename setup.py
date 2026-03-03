from setuptools import setup, find_packages

setup(
    name="chaty_proto",
    version="0.1.25",
    packages=find_packages(where="gen/python"),
    package_dir={"": "gen/python"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "grpcio",
        "protobuf",
    ],
)
