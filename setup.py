import setuptools

setuptools.setup(
    name="progress_timer",
    version="0.1.0",
    license='MIT',
    author="Yonghee Cheon",
    author_email="yonghee.cheon@gmail.com",
    description="A Python module which prints elapsed time and estimated time left with accordance to percentage",
    long_description=open('README.md').read(),
    url="https://github.com/yonghee12/progress_timer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.4',
    install_requires=['numpy>=1.11']
)
