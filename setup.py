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
      version='0.0.24',
      description=('A docassemble package for enviromental crimes'),
      long_description='# Código da Mata\n\nPacote para [Docassemble](https://docassemble.org/) (usando Python e Markdown).\n \nAutomação da análise jurídica e montagem automatizada de documentos ("document assembly") de atos jurídicos relacionados ao desmatamento \nilegal (crimes contra a flora e correlatos previstos no art. 38 e seguintes da Lei 9.605/98)\n\nSeu objetivo é facilitar o trabalho de promotores de Justiça no âmbito do [Projeto Olhos da Mata](https://sites.google.com/view/olhosdamata)\ne, futuramente, de fiscais do Ibama, Semas, bem como de juízes com atribuição ou jurisdição em crimes relacionados ao desmatamento ilegal.\n\nO projeto foi inicialmente idealizado pelo Ministério Público do Estado de Mato Grosso, por iniciativa do Promotor Cláudio Ângelo Correa Gonzaga, que codificou as minutas das peças jurídicas (como a denúncia criminal ambiental) e os relatórios de valoração do dano ambeintal utilizados no âmbito do projeto Olhos da Mata, sob orientação do Prof. Dr. Roberto Vasconcellos Novaes, responsável pelo controle de versões, design do banco de dados, bem como adaptação do pacote para instalação e uso em máquinas físicas por meio do docker.\n\nHoje é desenvolvido em parceria com a [Faculdade de Direito da UFMG](https://www.direito.ufmg.br/) por meio do projeto de \nextensão e grupo de pesquisa [Código da Mata](https://www.robertonovaes.com.br/index.php/codigo-da-mata-the-forest-code/),\nsob coordenação do Prof. Roberto Vasconcelos Novaes. O grupo de pesquisa/extensão tem o objetivo de desenvolver e pesquisar\no direito ambiental relacionado à proteção florestal, tecnologias de automatização e geração de documentos e a robotização\ndo processo de proteção ambiental com vistas a facilitar o trabalho de órgãos de fiscalização ambiental e órgãos do sistema de Justiça (Ministério Público e, futuramente, Poder Judiciário) com vistas a contribuir para uma prestação jurisdicional mais célere.\n\n[Servidor da Aplicação](http://codigodamata.consciencia.eco.br)\n\n# Autores\n* CLAUDIO ANGELO CORREA GONZAGA, claudioacgonzaga@gmail.com\n* ROBERTO VASCONCELOS NOVAES, rnovaes@ufmg.br\n\n# Instalação em desenvolvimento\nAs instruções abaixo se aplicamo ao Ubuntu (Server ou Desktop). Foram testadas nas versões 18.04 e 20.04, mas devem funcionar\nsem maiores alterações em outras versões do Ubuntu.\n\nPara instalar o Docassemble na sua máquina:\n\n1. Clone o repositório no seu local de preferência.\n2. Se não tiver instalado na sua máquina Docker e Docker Compose, execute:\n```\n$ sudo scripts/install_docker_docker_compose.sh\n```\n3. Uma vez executado o script, digite:\n```\n$ docker-compose up -d\n```\n\nPara verificar se o container está em execução:\n\n```\n$ docker ps \n```\n\nVocê deverá ver a seguinte mensagem:\n\n```\n6c3475a13664 jhpyle/docassemble:latest "/usr/bin/supervisor…" 5 minutes ago Up About a minute 0.0.0.0:80->80/tcp, 25/tcp, 465/tcp, 514/tcp, 4369/tcp, 5432/tcp, 5671-5672/tcp, 6379/tcp, 8080-8082/tcp, 9001/tcp, 25672/tcp, 0.0.0.0:443->443/tcp docassemble\n```\n\nO container pode levar vários minutos até estar completamente configurado e disponível para uso.\n\nSe você desejar acompanhar o que está ocorrendo dentro do container digite:\n\n```\ndocker logs -f docassemble\n```\n\nVocê verá o log do container em andamento. Enquanto você não visualisar as linhas:\n\n```\n2020-08-02 19:02:17,036 INFO success: uwsgi entered RUNNING state, process has stayed up for > than 15 seconds (startsecs)\n2020-08-02 19:02:17,214 INFO spawned: \'nginx\' with pid 1380\n```\n\nO container não estará disponível.\n\nApós o término da instalação acesse localhost ou 127.0.0.1. O serviço é executado na porta 80.\n\nNo primeiro acesso, use:\n\nEmail: admin@admin.com\nPassword: password\n\nA senha deverá ser trocada no primeiro acesso. \n\nSeu servidor do Docassemble está prontinho para uso!\n\n\n\n',
      long_description_content_type='text/markdown',
      author='CLAUDIO ANGELO CORREA GONZAGA, ROBERTO VASCONCELOS NOVAES',
      author_email='claudioacgonzaga@gmail.com, rnovaes@ufmg.br',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['zipp>=3.4.1'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/codigodamata/', package='docassemble.codigodamata'),
     )

