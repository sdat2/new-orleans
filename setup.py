from setuptools import find_packages, setup


REQUIRED = [
    "typeguard",
    "pylint",
    "sithom",
    "cdsapi",
    "xarray",
    "uncertainties",
]

setup(
    name="src",
    version="0.0.1",
    author="sdat2",
    author_email="sdat2@cam.ac.uk",
    description="Scripts to run emulation of ADCIRC/SWAN in the vacinity of New Orleans",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    include_package_data=True,
    install_requires=REQUIRED,
    dependency_links=["https://github.com/sdat2/noaa_coops.git@bbox"],
    license="MIT",
    tests_require=["flake8", "pytest"],
    url="https://github.com/sdat2/new-orleans",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    python_requires=">=3.8",
)
