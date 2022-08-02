CREATE DATABASE IF NOT EXISTS wb;


CREATE TABLE IF NOT EXISTS wb.sales (
    card_id UInt32,
    sum_sales UInt32,
    count_sales UInt32,
    updated_at DateTime,
    date Date
) ENGINE = ReplacingMergeTree() PARTITION BY toYYYYMM(date) ORDER BY (card_id, date);