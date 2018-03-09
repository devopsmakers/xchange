from setuptools import setup

setup(name='xchange',
      version='0.1',
      description='Flexible file transfers',
      long_description='Highly configurable file transfers with monitoring, encryption, backups....',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: File Sharing',
        'Intended Audience :: System Administrators',
      ],
      keywords='file transfer sftp ftp s3 gpg backup',
      url='http://github.com/devopsmakers/xchange',
      author='Tim Birkett',
      author_email='tim.birkett@devopsmakers.com',
      license='MIT',
      packages=['xchange'],
      install_requires=[
          'boto3',
          'gpg',
      ],
      include_package_data=True,
      zip_safe=False)
