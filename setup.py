from setuptools import setup, find_packages

setup(
    name="Kidney_Disease_Classification_Deep_Learning_Project",
    version="0.0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="Deep Learning Project for Kidney Disease Classification",
    long_description=open("Readme.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/kidney-disease-classification",  # optional
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/kidney-disease-classification/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=[
        "tensorflow==2.12.0",
        "pandas",
        "dvc",
        "mlflow==2.2.2",
        "notebook",
        "numpy",
        "matplotlib",
        "seaborn",
        "python-box==6.0.2",
        "pyYAML",
        "tqdm",
        "ensure==1.0.2",
        "joblib",
        "types-PyYAML",
        "scipy",
        "Flask",
        "Flask-Cors",
        "gdown"
    ],
    python_requires=">=3.10",
)
