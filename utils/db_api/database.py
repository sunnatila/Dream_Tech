import sqlite3



class Database:
    def __init__(self, db_path='db.sqlite3'):
        self.db_path = db_path


    @property
    async def connector(self):
        return sqlite3.connect(self.db_path)

    async def get_contact_from_id(self, user_id):
        conn = await self.connector
        cur = conn.cursor()
        query = """
        SELECT * FROM contacts WHERE id=?
        """
        cur.execute(query, (user_id, ))
        return cur.fetchone()

    async def update_contact_status(self, user_id, status):
        conn = await self.connector
        cur = conn.cursor()
        query = """
                UPDATE contacts SET status=? WHERE id=?
                """
        cur.execute(query, (status, user_id))
        conn.commit()
        if cur:
            print("User status updated")
        else:
            print("User status not updated")

    async def get_status_id(self, status_name):
        conn = await self.connector
        cur = conn.cursor()
        query = """
                SELECT status FROM contacts WHERE status=?
                """
        cur.execute(query, (status_name,))
        return cur.fetchone()

    async def get_contacts_ids(self):
        conn = await self.connector
        cur = conn.cursor()
        query = """
                SELECT id FROM contacts
                """
        res = cur.execute(query)
        ids = [set_obj[0] for set_obj in res.fetchall()]
        return ids

    async def get_order_from_id(self, user_id):
        conn = await self.connector
        cur = conn.cursor()
        query = """
        SELECT * FROM orders WHERE id=?
        """
        cur.execute(query, (user_id, ))
        return cur.fetchone()

    async def update_order_status(self, user_id, status):
        conn = await self.connector
        cur = conn.cursor()
        query = """
                UPDATE orders SET status=? WHERE id=?
                """
        cur.execute(query, (status, user_id))
        conn.commit()
        if cur:
            print("User status updated")
        else:
            print("User status not updated")

    async def get_orders_ids(self):
        conn = await self.connector
        cur = conn.cursor()
        query = """
                SELECT id FROM orders
                """
        res = cur.execute(query)
        ids = [set_obj[0] for set_obj in res.fetchall()]
        return ids

