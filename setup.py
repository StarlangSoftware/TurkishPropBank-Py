from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='NlpToolkit-PropBank',
    version='1.0.21',
    packages=['PropBank', 'PropBank.data'],
    package_data={'PropBank.data': ['*.xml']},
    url='https://github.com/StarlangSoftware/TurkishPropbank-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Turkish PropBank',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
