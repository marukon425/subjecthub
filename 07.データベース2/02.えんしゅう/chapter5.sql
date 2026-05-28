-- 四大命令とは
-- １.  select(抽出)
-- ２.  insert(挿入)
-- ３.  update(更新)
-- ４.  dalete(削除)



-- 四大命令の構文
-- select文
select * from テーブル
-- insert文
insert into values('データ', 1)
-- upadate文
update テーブル
SET 列名 = 値, 列名1 = 値1
-- delete文
delete テーブル
where カラム = 値



-- select文の使い方
-- 1. 重複を無くす
select distinct カラム from テーブル
-- 2.並び替え
select カラム from テーブル 
order by カラム asc(desc)
-- 3.範囲を指定
select カラム from テーブル 
where カラム between 値1 and 値2
-- 4.列名を変更して表示
select カラム1 as 列名1, カラム2 as 列名2 from テーブル
-- 5.複数の値を指定
select カラム from テーブル 
where カラム in ('値1', '値2')
-- 6.複数条件を指定 (または)
select カラム from テーブル 
where カラム = '値1' and カラム = '値2'
-- 7.複数条件を指定 (かつ)
select カラム from テーブル 
where カラム = '値1' or カラム = '値2'
-- 8.nullの指定
select カラム from テーブル 
where カラム is null 




--------------------------chapter5-------------------

-- sqlで四則演算
-- 出金額、出金額に100円を加算した値、固定値(aqlという文字)を抽出
select 出金額, 出金額+100, 'sql' 
from 家計簿

-- 出金額、税込み金額　(列名：税込み金額) を抽出 
select 出金額, 出金額*1.1 as 税込み金額 from 家計簿

-- 食費の出金額に100円を加算
update 家計簿 
set 出金額 = 出金額+100 
where 費目 = '食費'

-- 日付が2024-02-10の入金額を10000円減額
update 家計簿 
set 入金額 = 入金額-10000
where 日付 = '2024-02-10'


-- sqlで条件分岐
-- case演算子
-- 費目は、居住費と水道光熱費は「固定費」、それ以外は「変動費」で抽出して
select 費目, 出金額,
case 費目 
when '居住費' then '固定費'
when '水道光熱費' then '固定費'
else '変動費'
end as 出費の分布
from 家計簿 
where  出金額 > 0

-- 入金額が0より大きい 費目と入金額を表示
-- 入金額を500円未満の場合は「お小遣い」
-- 入金額が100000円未満の場合は「一時収入」
-- 入金額が300000円未満の場合は「給料」
-- 上記以外は、「想定外」
-- 列名は「収入の分類」
select 費目, 入金額 
case 
when 入金額 < 5000 then 'お小遣い' 
when 入金額 < 100000 then '一時収入' 
when 入金額 < 300000 then '給料' 
else '想定外' 
end as 収入の分布
from 家計簿




-- いろいろな関数の使い方
-- ※関数名や使い方はDBMSによって大きく異なる

-- 家計簿表からメモとメモの文字数 (列名：メモの長さ) を表示
select メモ, length(メモ) as メモの長さ from 家計簿 

-- 空白を除去する (trim)
select カラム, trim(メモ) as 空白除去したメモ

-- 指定文字を置換
update 家計簿 (replace)
set メモ = replace(メモ, '購入', '買った')

-- 文字列を連結する (concat)
select concat(費目, ':' || メモ) from 家計簿 

-- 一部文字を抽出する (substring)
-- 費目の1～3文字目に「費」があるものを抽出
select * from 家計簿 
where substring(費目, 1, 3) like '%費%'

-- 指定桁で四捨五入 (round)
select 出金額, round(出金額, -2) as 百円単位の出金額

-- 指定桁で切り捨てる (trunc)
select 出金額, trunc(出金額, -2) as 百円単位の出金額

-- べき乗を計算する (power)
select 数値を表す列, power(数値を表す列, 何乗するか指定)

-- 現在の時間を得る (current_timestamp. current_date, current_time)
insert into 家計簿 
values(current_date, 'しょくひ', )

-- データ型を変換する (cast)
cast (変換するカラム as 変換する型)



-- 練習問題
-- 問題5-1-1
update 試験結果
set 午後 = 平均点*4-午前-午後2-論述
where 受験者id = 'SW1046'
update 試験結果
set 論述 = 平均点*4-午前-午前1-午後2
where 受験者id = 'SW1046'
update 試験結果
set 午前 = 平均点*4-午前1-午後2-論述
where 受験者id = 'SW1046'
-- 問題5-1-2
select  
case 
when 午前 >= 60 and 午後1 + 午後2 >= 120 and 論述 >= (午前 + 午後1 + 午後2) * 0.3 then 受験者id 
end as 合格者id
from 試験結果
-- 問題5-2-1
update 回答者
set 国名 = 
































select 口座番号, 残高, 残高*0.0002 as 利息 from 口座