# Código da Mata

Pacote para [Docassemble](https://docassemble.org/) (usando Python e Markdown).
 
Automação da análise jurídica e montagem de documentos ("document assembly") de atos jurídicos relacionados ao desmatamento 
ilegal (crimes contra a flora e correlatos previstos no art. 38 e seguintes da Lei 9.605/98)

Seu objetivo é facilitar o trabalho de promotores de Justiça no âmbito do [Projeto Olhos da Mata](https://consciencia.eco.br/index.php?title=Projeto_Olhos_da_Mata)
e, futuramente, de fiscais do Ibama, Semas, bem como de juízes com atribuição ou jurisdição em crimes relacionados ao desmatamento ilegal.

O projeto foi inicialmente idealizado pelo Ministério Público do Estado de Mato Grosso, por iniciativa do Promotor Cláudio Ângelo Correa Gonzaga,
que elaborou e automatizou os primeiros documentos e é responsável pelo conteúdo jurídico-processual.

Hoje é desenvolvido em parceria com a [Faculdade de Direito da UFMG](https://www.direito.ufmg.br/) por meio do projeto de 
extensão e grupo de pesquisa [Código da Mata](https://www.robertonovaes.com.br/index.php/codigo-da-mata-the-forest-code/),
sob coordenação do Prof. Roberto Vasconcelos Novaes. O grupo de pesquisa/extensão tem o objetivo de desenvolver e pesquisar
o direito ambiental relacionado à proteção florestal, tecnologias de automatização e geração de documentos e a robotização
do processo de proteção ambiental.

[Servidor da Aplicação](http://codigodamata.consciencia.eco.br)

# Autores
* CLAUDIO ANGELO CORREA GONZAGA, gabinetepromotor@gmail.com
* ROBERTO VASCONCELOS NOVAES, rnovaes@ufmg.br

# Instalação em desenvolvimento
As instruções abaixo se aplicamo ao Ubuntu (Server ou Desktop). Foram testadas nas versões 18.04 e 20.04, mas devem funcionar
sem maiores alterações em outras versões do Ubuntu.

Para instalar o Docassemble na sua máquina:

1. Clone o repositório no seu local de preferência.
2. Se não tiver instalado na sua máquina Docker e Docker Compose, execute:
```
$ sudo scripts/install_docker_docker_compose.sh
```
3. Uma vez executado o script, digite:
```
$ docker-compose up -d
```

Para verificar se o container está em execução:

```
$ docker ps 
```

Você deverá ver a seguinte mensagem:

```
6c3475a13664 jhpyle/docassemble:latest "/usr/bin/supervisor…" 5 minutes ago Up About a minute 0.0.0.0:80->80/tcp, 25/tcp, 465/tcp, 514/tcp, 4369/tcp, 5432/tcp, 5671-5672/tcp, 6379/tcp, 8080-8082/tcp, 9001/tcp, 25672/tcp, 0.0.0.0:443->443/tcp docassemble
```

O container pode levar vários minutos até estar completamente configurado e disponível para uso.

Se você desejar acompanhar o que está ocorrendo dentro do container digite:

```
docker logs -f docassemble
```

Você verá o log do container em andamento. Enquanto você não visualisar as linhas:

```
2020-08-02 19:02:17,036 INFO success: uwsgi entered RUNNING state, process has stayed up for > than 15 seconds (startsecs)
2020-08-02 19:02:17,214 INFO spawned: 'nginx' with pid 1380
```

O container não estará disponível.

Após o término da instalação acesse localhost ou 127.0.0.1. O serviço é executado na porta 80.

No primeiro acesso, use:

Email: admin@admin.com
Password: password

A senha deverá ser trocada no primeiro acesso. 

Seu servidor do Docassemble está prontinho para uso!




