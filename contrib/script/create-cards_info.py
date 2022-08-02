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

    client.execute(r''' CREATE TABLE IF NOT  EXISTS wb.cards_info(
                        card_id UInt32,

                        brand_id Nullable(UInt32),
                        brand_name Nullable(String),
                        site_brand_id Nullable(UInt32),

                        brand_url Nullable(String),
                        brand_query Nullable(String),

                        brands Nested (name Nullable(String), url Nullable(String), pos Nullable(UInt32), level Nullable(UInt8), query Nullable(String), full_name Nullable(String)),
                        catalogs Nested (id Nullable(UUID), name Nullable(String), url Nullable(String), level Nullable(UInt8), pos Nullable(UInt32), query Nullable(String), full_name Nullable(String)),

                        product_name Nullable(String),

                        supplier_name Nullable(String),
                        supplier_OGRN Nullable(String),

                        feedback_count Nullable(UInt64),
                        question_count Nullable(UInt32),
                        orders_count Nullable(UInt32),
                        rating Nullable(UInt8),

                        preview_image_url Nullable(String),

                        is_adult Nullable(UInt8),

                        price Nullable(UInt32),
                        sale_price Nullable(UInt32),
                        sale Nullable(UInt32),

                        founded_at Date,
                        updated_at DateTime,
                        date Date,
                        pics_count Nullable(UInt8))

                        ENGINE = ReplicatedMergeTree('/clickhouse/tables/{shard}/wb.cards_info', '{replica}')
                        PARTITION BY toYYYYMM(date)
                        ORDER BY  (card_id, date);''')

#Master###########################################################################################################################3
client = Client(master[0], port=master[1],user="default", password="123")

client.execute("CREATE DATABASE IF NOT EXISTS wb")

client.execute(r'''CREATE TABLE IF NOT  EXISTS wb.cards_info(
                        card_id UInt32,

                        brand_id Nullable(UInt32),
                        brand_name Nullable(String),
                        site_brand_id Nullable(UInt32),

                        brand_url Nullable(String),
                        brand_query Nullable(String),

                        brands Nested (name Nullable(String), url Nullable(String), pos Nullable(UInt32), level Nullable(UInt8), query Nullable(String), full_name Nullable(String)),
                        catalogs Nested (id Nullable(UUID), name Nullable(String), url Nullable(String), level Nullable(UInt8), pos Nullable(UInt32), query Nullable(String), full_name Nullable(String)),

                        product_name Nullable(String),

                        supplier_name Nullable(String),
                        supplier_OGRN Nullable(String),

                        feedback_count Nullable(UInt64),
                        question_count Nullable(UInt32),
                        orders_count Nullable(UInt32),
                        rating Nullable(UInt8),

                        preview_image_url Nullable(String),

                        is_adult Nullable(UInt8),

                        price Nullable(UInt32),
                        sale_price Nullable(UInt32),
                        sale Nullable(UInt32),

                        founded_at Date,
                        updated_at DateTime,
                        date Date,
                        pics_count Nullable(UInt8))
                        ENGINE = Distributed(example_cluster, wb, cards_info, rand());''')
