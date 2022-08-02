CREATE DATABASE IF NOT EXISTS wb;


CREATE TABLE IF NOT EXISTS wb.catalogs (
    id UUID,
    url String,
    total_items UInt32,
    total_pages UInt32,
    breadcrumbs Nested (name String, url String),
    children Nested (id UUID, url String),
    products Nested (product_id UInt32, is_new UInt8, position UInt32),
    is_root UInt8,
    updated_at DateTime,
    date Date
) ENGINE = ReplacingMergeTree() PARTITION BY toYYYYMM(date) ORDER BY (url, date);

