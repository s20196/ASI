import setuptools

setuptools.setup(
    name="app",
    version="0.0.1",
    author="Illia Shkroba",
    author_email="is@pjwstk.edu.pl",
    description="My app",
    packages=setuptools.find_packages(),
    install_requires=["pandas==1.5.0"],
    python_requires=">=3.6",
)
