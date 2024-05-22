from setuptools import setup, find_packages

setup(
    name='YOLOv8App',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'kivy',
        'numpy',
        'opencv-python',
        'torch',
        'torchvision',
        'ultralytics',
        'certifi'
    ],
)
