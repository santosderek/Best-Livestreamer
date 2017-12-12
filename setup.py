from setuptools import setup, find_packages

setup(name='Best Quality Livestream Downloader',
      version='0.1',
      description='Use livestreamer at best quality.',
      author='Derek Santos',
      license='The MIT License (MIT)',
      packages=['bestlivestreamer'],
      scripts=['bestlivestreamer/__main__.py'],
      entry_points={
          'console_scripts':
              ['bls = bestlivestreamer.__main__:main']  # bdl = best download
      },
      )
