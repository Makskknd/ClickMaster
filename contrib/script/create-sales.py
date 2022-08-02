from email.policy import default
from clickhouse_driver import Client

subs = [
    ("ch-sub-1", "92"),
    ("ch-sub-2", "92"),
]
master = ("ch_master", "91")

#SLave###########################################################################################################################3
for sub in subs:
    client = Client(sub[0], port=sub[1])

    client.execute(r"CREATE DATABASE IF NOT EXISTS wb")

    client.execute(r'''CREATE TABLE IF NOT EXISTS wb.sales (
                        card_id UInt32,
                        sum_sales UInt32,
                        count_sales UInt32,
                        updated_at DateTime,
                        date Date )
                        ENGINE = ReplicatedMergeTree('/clickhouse/tables/{shard}/wb.sales', '{replica}') 
                        PARTITION BY toYYYYMM(date) ORDER BY (card_id, date);''')
 

#Master###########################################################################################################################3
client = Client(master[0], port=master[1],user="default", password="123")

client.execute("CREATE DATABASE IF NOT EXISTS wb")

client.execute(r'''CREATE TABLE IF NOT EXISTS wb.sales (
                        card_id UInt32,
                        sum_sales UInt32,
                        count_sales UInt32,
                        updated_at DateTime,
                        date Date ) 
                        ENGINE = Distributed(example_cluster, wb, sales, rand());''')


