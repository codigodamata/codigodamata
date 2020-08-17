import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.codigodamata',
      version='0.0.17',
      description=('A docassemble package for enviromental crimes'),
      long_description='# Código da Mata\r\n\r\nPacote para Docassemble (usando Python e Markdown) visando a automação da análise jurídica e montagem de documentos ("document assembly") de atos jurídicos relacionados ao desmatamento ilegal (crimes contra a flora e correlatos previstos no art. 38 e seguintes da Lei 9.605/98), visando facilitar o trabalho de promotores de Justiça no âmbito do Projeto Olhos da Mata (https://consciencia.eco.br/index.php?title=Projeto_Olhos_da_Mata) e, futuramente, de fiscais do Ibama, Semas, bem como de juízes com atribuição ou jurisdição em crimes relacionados ao desmatamento ilegal.\r\nhttp://codigodamata.consciencia.eco.br\r\n\r\n## Author\r\n\r\nCLAUDIO ANGELO CORREA GONZAGA, gabinetepromotor@gmail.com\r\n\r\n',
      long_description_content_type='text/markdown',
      author='CLAUDIO ANGELO CORREA GONZAGA',
      author_email='claudioacgonzaga@gmail.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['zipp'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/codigodamata/', package='docassemble.codigodamata'),
     )

