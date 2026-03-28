import pandas as pd
import sqlite3

file_path = r"3zd.xlsx"

df_operations = pd.read_excel(file_path, sheet_name='Движение_товаров')
df_goods = pd.read_excel(file_path, sheet_name='Товар')
df_shops = pd.read_excel(file_path, sheet_name='Магазин')

conn = sqlite3.connect(':memory:')


df_operations.to_sql('operations', conn, index=False, if_exists='replace')
df_goods.to_sql('goods', conn, index=False, if_exists='replace')
df_shops.to_sql('shops', conn, index=False, if_exists='replace')


query = """
SELECT 
    SUM(CASE 
        WHEN o."Тип операции" = 'Поступление' THEN o."Количество упаковок, шт."
        WHEN o."Тип операции" = 'Продажа' THEN -o."Количество упаковок, шт."
        ELSE 0
    END) AS Изменение
FROM operations o
JOIN shops s ON o."ID магазина" = s."ID магазина"
JOIN goods g ON o."Артикул" = g."Артикул"
WHERE s."Район" = 'Заречный'
  AND g."Наименование товара" = 'Яйцо диетическое'
  AND o."Дата" BETWEEN '2021-06-01' AND '2021-06-10'
"""

result = pd.read_sql_query(query, conn)
print(f"Kоличество упаковок яиц диетических, имеющихся в наличии в магазинах Заречного района за период с 1 по 10 июня увеличилось на {int(result['Изменение'].iloc[0])}")

conn.close()