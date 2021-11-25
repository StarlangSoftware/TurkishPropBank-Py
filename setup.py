from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NlpToolkit-PropBank',
    version='1.0.18',
    packages=['PropBank', 'PropBank.Frames', 'PropBank.Predicates'],
    package_data={'PropBank.Frames': ['*.xml'],
                  'PropBank.Predicates': ['*.xml']},
    url='https://github.com/StarlangSoftware/TurkishPropbank-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Turkish PropBank',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
