import psycopg2


class DBHandler(object):
    def __init__(self):
        self.conn = psycopg2.connect(database='odoo_9', user='admin', password='admin', host='127.0.0.1', port='5432')
        self.cur = self.conn.cursor()

    def create(self, table):
        self.cur.execute('''SELECT COUNT(*) FROM pg_class WHERE relname = 'test1';''')
        data = self.cur.fetchall()
        if data[0][0]==0:
            self.cur.execute('''CREATE TABLE %s
           (ID INT PRIMARY KEY     NOT NULL,
           NAME            TEXT   NOT NULL,
           METHOD       TEXT   NOT NULL,
           ACCEPT         TEXT,
           ADDRESS      TEXT,
           COOKIE         TEXT,
           SALARY          REAL);''' % table)
            print "Table created successfully"
        self.conn.commit()

    def write(self, vals):
        self.cur.execute(
            '''INSERT INTO test1 (ID,NAME,METHOD,ACCEPT,ADDRESS,COOKIE) VALUES (%d, '%s', '%s', '%s', '%s' ,'%s');''' % (
                vals['id'], vals['name'], vals['method'], vals['accept'], vals['address'], vals['cookie']))
        self.conn.commit()

