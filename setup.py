from distutils.core import setup
setup(
  name = 'neripresence',         
  packages = ['neripresence'],   
  version = '0.1',      
  license='MIT',        
  description = 'Small and simple nerimity presence wrapper',   
  author = 'Tosiek',                   
  author_email = 'orzechowymastermind@proton.me',      
  url = 'https://github.com/toskowski/neripresence',   
  download_url = 'https://github.com/toskowski/neripresence/archive/refs/tags/v_01.tar.gz',    
  keywords = ['nerimity', 'presence' ],   
  install_requires=[            
          'websockets',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      

    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   

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
