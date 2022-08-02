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
    client.execute(r'''CREATE TABLE IF NOT EXISTS wb.brands (
                       query String,
                       brand_id UInt32,
                       site_brand_id Nullable(UInt32),
                       brand_name Nullable(String),
                       total_items UInt32,
                       total_pages UInt32,
                       products Nested (product_id UInt32, is_new UInt8, position UInt32),
                       bread_crumbs Nested (name String, url String),
                       is_brand_zone UInt8,
                       updated_at DateTime,
                       date Date)
                       ENGINE = ReplicatedMergeTree('/clickhouse/tables/{shard}/wb.brands', '{replica}')
                       ORDER BY (card_id);''')


#Master###########################################################################################################################3
client = Client(master[0], port=master[1],user="default", password="123")

client.execute("CREATE DATABASE IF NOT EXISTS wb")

client.execute(r'''CREATE TABLE IF NOT EXISTS wb.brands (
                       query String,
                       brand_id UInt32,
                       site_brand_id Nullable(UInt32),
                       brand_name Nullable(String),
                       total_items UInt32,
                       total_pages UInt32,
                       products Nested (product_id UInt32, is_new UInt8, position UInt32),
                       bread_crumbs Nested (name String, url String),
                       is_brand_zone UInt8,
                       updated_at DateTime,
                       date Date)
                       ENGINE = Distributed(example_cluster, wb, brands, rand());''')
