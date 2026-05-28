-- 家計簿テーブルから費目を抽出
select 費目 from 家計簿

-- 日付が2024-02-14の出金額を600円に変更
update 家計簿 
set 出金額 = 600 
where 日付 = '2024-02-14'

-- 今日の日付で任意なデータを追加
insert into 家計簿
 values('2025-04-11', '通信費', 'スマホ代', 0, 900)

-- 費目が水道光熱費の行を削除
delete from 家計簿 where 費目 = '水道光熱費'





select 口座番号, 名義, 残高 from 取引
where in(select 入金 from 取引 where 入金 >= 1000000)