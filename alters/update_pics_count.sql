-- Обновление поля pics_count таблицы cards_info из таблицы cards

alter table cards_info
update pics_count = (SELECT argMax(pics_count, date) from cards where cards.card_id = card_id)
where card_id in (select cc.card_id from cards_info as cc order by cc.card_id)

OPTIMIZE TABLE wb.cards_info FINAL