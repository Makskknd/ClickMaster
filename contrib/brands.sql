CREATE DATABASE IF NOT EXISTS wb;


CREATE TABLE IF NOT EXISTS wb.brands (
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
    date Date
) ENGINE = ReplacingMergeTree() PARTITION BY toYYYYMM(date) ORDER BY (query, date);

