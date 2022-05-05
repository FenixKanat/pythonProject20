import unittest
from unittest import mock
import mysql.connector

def insert_rows(rows, table_name, dbc):
    field_names = rows[0].keys()
    field_names_str = ', '.join(field_names)
    placeholder_str = ','.join('?'*len(field_names))
    insert_sql = f'INSERT INTO {table_name}({field_names_str}) VALUES ({placeholder_str})'
    saved_autocommit = dbc.autocommit
    with dbc.cursor() as cursor:
        try:
            dbc.autocommit = False
            tuples = [ tuple((row[field_name] for field_name in field_names)) for row in rows ]
            cursor.executemany(insert_sql, tuples)
            cursor.commit()
        except Exception as exc:
            cursor.rollback()
            raise exc
        finally:
            dbc.autocommit = saved_autocommit

class TestConnection(unittest.TestCase):
    """Database Connection tests."""

    connection = None
    
    def setUp(self):
        self.connection = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='org'
            )
        
    def tearDown(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

    def test_connection(self):        
        self.assertTrue(self.connection.is_connected())
    


class Test_insert_rows(unittest.TestCase):
    """Database Insert Row Test"""

    def fix_dbc(self):
        dbc = mock.MagicMock(spec=['cursor'])
        dbc.autocommit = True
        return dbc

    def fix_rows(self):
        rows = [{'id':1, 'name':'John'}, 
                {'id':2, 'name':'Jane'},]
        return rows

    def test_insert_rows_calls_cursor_method(self):
        dbc = self.fix_dbc()
        rows = self.fix_rows()
        insert_rows(rows, 'users', dbc)
        self.assertTrue(dbc.cursor.called)

if __name__ == '__main__':
    unittest.main(argv=['', '-v'])