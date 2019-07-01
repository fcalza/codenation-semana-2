# Validador de e-mails

Os e-mails seguem sempre um padrão como este: username@websitename.extension, quando inserimos um e-mail num cadastro, o sistema pode verificar se o este é válido.
O objetivo desse desafio é fazer uma validador de e-mails.

Você receberá uma lista de e-mails e deverá validá-los, retornando uma lista com os e-mails válidos.

## Observações

- Deve ter o tipo de formato username@websitename.extension
- O nome de usuário só pode conter letras, dígitos e os caracteres -, . e _
- O nome do site só pode ter letras e dígitos
- O comprimento máximo da extensão é 1, 2, 3 caracteres

Ex:

    Entrada:
        emails = ['matt23@@india.in', 'lara@codenation.com']

    Saida:
        emails = ['lara@codenation.com']

## Tópicos

Neste desafio você vai aprender:

- Python
    - Expressões Regulares
    - Filter
- Testes unitários

## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`




Dicas:
- Comece lendo o arquivo README.md, que possui a descrição do seu desafio e os requisitos que você precisa cumprir antes de começar a programar
- Lembre-se que na página do desafio você pode encontrar links com conteúdo para ajudar na solução
- Você pode tirar dúvidas e conversar com outros desenvolvedores realizando este desafio no forum: https://forum.codenation.com.br

Próximos passos:
- Entre no diretório do desafio com o comando cd /home/lipe/codenation/validador-emails-python
- Execute o comando "codenation test -c nome-do-desafio" para validar sua aplicação
- Execute o comando "codenation submit -c nome-do-desafio" para enviar sua aplicação

