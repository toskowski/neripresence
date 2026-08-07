from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'neripresence',         
  packages = ['neripresence'],   
  version = '0.4.5',      
  license='MIT',        
  description = 'Small and simple nerimity presence wrapper :3',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Tosiek',     
  url = 'https://github.com/toskowski/neripresence',   
  download_url = 'https://github.com/toskowski/neripresence/archive/refs/tags/v_045.tar.gz',    
  keywords = ['nerimity', 'presence' ],   
  install_requires=[            
          'websockets',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      

    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',   

    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13',
    'Programming Language :: Python :: 3.14'
  ],
)
