from clickhouse_driver import Client

subs = [
    ("127.0.0.1", "92"),
    ("127.0.0.1", "93"),
]
master = ("127.0.0.1", "91")

#SLave###########################################################################################################################3
for sub in subs:
    client = Client(sub[0], port=sub[1])

    client.execute("CREATE DATABASE IF NOT EXISTS wb")

    client.execute(r''' CREATE TABLE IF NOT EXISTS wb.catalogs (
                        id UUID,
                        url String,
                        total_items UInt32,
                        total_pages UInt32,
                        breadcrumbs Nested (name String, url String),
                        children Nested (id UUID, url String),
                        products Nested (product_id UInt32, is_new UInt8, position UInt32),
                        is_root UInt8,
                        updated_at DateTime,
                        date Date)
                        ENGINE = ReplicatedMergeTree('/clickhouse/tables/{shard}/wb.catalogs', '{replica}')
                        PARTITION BY toYYYYMM(date)
                        ORDER BY (url, date);''')

#Master###########################################################################################################################3
client = Client(master[0], port=master[1],user="default", password="123")

client.execute("CREATE DATABASE IF NOT EXISTS wb")

client.execute(r'''CREATE TABLE IF NOT EXISTS wb.catalogs (
                        id UUID,
                        url String,
                        total_items UInt32,
                        total_pages UInt32,
                        breadcrumbs Nested (name String, url String),
                        children Nested (id UUID, url String),
                        products Nested (product_id UInt32, is_new UInt8, position UInt32),
                        is_root UInt8,
                        updated_at DateTime,
                        date Date)
                        ENGINE = Distributed(example_cluster, wb, catalogs, rand());''')
