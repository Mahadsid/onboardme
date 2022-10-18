from setuptools import setup


def readme():
    """
    grab and return contents of README.md for use in long description
    """
    with open('README.md') as f:
        return f.read()


setup(name='onboardme',
      description='An onboarding tool to install dot files and packages',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha'
          'Programming Language :: Python :: 3.10'
          'Topic :: Image Processing :: Display',
      ],
      classifiers=[
          'Development Status :: 3 - Alpha'
          'Programming Language :: Python :: 3.10'
          'Topic :: Environment Setup',
      ],
      keywords='onboardme onboarding desktop-setup',
      version='0.1',
      url='http://github.com/jessebot/onboardme',
      author='Jesse Hitch',
      author_email='jessebot@linux.com',
      license='GPL version 3 or later',
      packages=['onboardme'],
      install_requires=['wget', 'GitPython', 'PyYAML', 'rich', 'click'],
      scripts=['bin/onboardme'],
      include_package_data=True,
      zip_safe=False)
