# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os
from typing import cast

import dotenv
import pymysql
import pymysql.cursors

CURRENT_CURSOR = pymysql.cursors.SSDictCursor
CURRENT_CURSOR2 = pymysql.cursors.DictCursor

TABLE_NAME = 'users'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=CURRENT_CURSOR2,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )

        # CUIDADO: ISSO LIMPA A TABELA
        # cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')

    connection.commit()

# Manipulação de Dados

    with connection.cursor() as cursor:
        cursor = cast(CURRENT_CURSOR2, cursor)
        '''
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Luiz", 25) '
        )
        '''
       # Inserindo um valor usando placeholder e um iterável
        '''
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)'
        )
        data = ('Rian', 18)
        result = cursor.execute(sql, data)
        '''
        # Inserindo um valor usando placeholder e um dicionário
        '''
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%(name)s, %(age)s)'
        )
        data = {
            "age": 37,
            "name": 'Leticia'
        }
        result = cursor.execute(sql, data)
        '''
       # Inserindo vários valores usando placeholder e um tupla de dicionários
        """
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%(name)s, %(age)s)'

        )
        data = (
            {"name": 'Iago Pultz', "age": 90},
            {"name": 'Vinicius', "age": 20},
            {"name": 'Emily', "age": 30},
        )
        result = cursor.executemany(sql, data)
        """
       # Inserindo vários valores usando placeholder e um tupla de tuplas
        """
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = (
            ("Siri", 22, ),
            ("Helena", 15, ),
        )
        result = cursor.executemany(sql, data)
        """

    # connection.commit()

    # Lendo os valores com SELECT
        # menor_id = int(input('Digite o menor ID: '))
        # maior_id = int(input('Digite o maior ID: '))

        menor_id = 2
        maior_id = 4

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )

        sql2 = (f'SELECT * FROM {TABLE_NAME} WHERE id BETWEEN %s AND %s')
        
        # cursor.execute(sql)
        cursor.execute(sql2, (menor_id, maior_id))
        print(cursor.mogrify(sql2, (menor_id, maior_id)))

        data = cursor.fetchall()
      
   
      # Editando com UPDATE, WHERE e placeholders no PyMySQ

        sql3 = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id=%s'
        )
        cursor.execute(sql3, ('Eleonor', 102, 4)) 
        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        cursor.execute(
            f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        )
        lastIdFromSelect = cursor.fetchone()

        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        print('resultFromSelect', resultFromSelect)
        print('len(data6)', len(data))
        print('rowcount', cursor.rowcount)
        print('lastrowid', cursor.lastrowid)
        print('lastrowid na mão', lastIdFromSelect)

        cursor.scroll(0, 'absolute')
        print('rownumber', cursor.rownumber)
        """  
        # Fetch com SSDICTCURSOR       
        for row in data:
            print(row)

        print('For 1: ')
        for row in cursor.fetchall_unbuffered():
            print(row)

            if row['id'] >= 5:
                break

        print()
        print('For 2: ')
             # cursor.scroll(-1)
        for row in cursor.fetchall_unbuffered():
            print(row)

    connection.commit()
    """
    """
    # Apagando com DELETE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql3 = (
            f'DELETE FROM {TABLE_NAME} WHERE id = %s'
        )
        print(cursor.execute(sql3, (8,)))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        for row in cursor.fetchall():
            print(row)    
    """

