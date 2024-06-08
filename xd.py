import oracledb

# Asegúrate de tener el cliente Oracle configurado correctamente.
dsn = oracledb.makedsn('adb.sa-santiago-1.oraclecloud.com', '1522', service_name='test_high')
connection = oracledb.connect(
    user='Admin',
    password='Diamanco2313',
    dsn=dsn,
    config_dir=r"C:\Users\basti\Dropbox\Duoc Uc\1° Semestre\Programación Web\Libros_web\wallet",
    wallet_location=r"C:\Users\basti\Dropbox\Duoc Uc\1° Semestre\Programación Web\Libros_web\wallet",
   # wallet_password='Casa2313'
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM dual")
result = cursor.fetchone()
print(result)