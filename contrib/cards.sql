CREATE DATABASE IF NOT EXISTS wb;


CREATE TABLE IF NOT EXISTS wb.cards (
    card_id UInt32,
    date Date,

    product_name Nullable(String),
    brand_name Nullable(String),
    brand_id Nullable(UInt32),
    site_brand_id Nullable(UInt32),
    
    supplier_name Nullable(String),
    supplier_OGRN Nullable(String),

    feedback_count Nullable(UInt64),
    question_count Nullable(UInt32),
    orders_count Nullable(UInt32),

    rating Nullable(UInt8),
    preview_image_url Nullable(String),
    quantity Nullable(UInt32),
    cards_group Array(UInt32),

    pics_count Nullable(UInt8),
    is_adult Nullable(UInt8),
    is_new Nullable(UInt8),

    warehouse_sizes Nested(warehouse_id UInt32, size String, quantity UInt32),

    napi_min_price Nullable(UInt32),
    napi_min_price_with_sale Nullable(UInt32),
    napi_sale Nullable(UInt32),

    nm_price Nullable(UInt32),
    nm_sale Nullable(UInt32),
    nm_sale_price Nullable(UInt32),

    nm_extended_basic_sale Nullable(UInt32),
    nm_extended_basic_price Nullable(UInt32),
    nm_extended_promo_sale Nullable(UInt32),
    nm_extended_promo_price Nullable(UInt32),

    updated_at DateTime

) ENGINE = ReplacingMergeTree() PARTITION BY toYYYYMM(date) ORDER BY (card_id, date);

