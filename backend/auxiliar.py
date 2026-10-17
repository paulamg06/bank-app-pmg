import sqlite3

conn = sqlite3.connect("db.sqlite3")

cursor = conn.cursor()

cursor.execute("UPDATE movimientos_movimiento SET fecha='2026-09-05T00:00:00Z' WHERE id=188")
# cursor.execute("UPDATE cuentas_cuenta SET saldo=297.5 WHERE id=1")
# cursor.execute("DROP TABLE saldos_saldo")

conn.commit()

conn.close()