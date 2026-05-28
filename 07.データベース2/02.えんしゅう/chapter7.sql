-- sqlの基本構文
-- select文
-- inset文
-- update文
-- delet文


-- chapter7

-- ☆ 副問い合わせ ☆

-- 最も大きな出費の費目と金額を求める
select 費目, 出金額 from 家計簿
    -- where 出金額 = max(出金額) ← ✕ 
    where 出金額 = (select max(出金額) from 家計簿)
-- where 出金額 = 7560

-- selectをネスト (selectの中にselectを記述) する
-- sql(select)では、「副問い合わせ」という

-- 単一の値と比較 (一つと比較) : = 
-- 複数値と比較 (複数と比較) : in
-- 表形式の複数値と比較 (いずれかと...) : any  や  all

-- 単一行副問い合わせの演習
-- 家計簿集計表の食費の費目の平均を更新したい
-- 家計簿アーカイブ表の出金額が0より大きく費目が食品の平均額
update 家計簿集計
set 費目 = (select avg(出金額) from 家計簿アーカイブ where 費目 = '食費' and 出金額 > 0 )
where 費目 = '食費'

update 家計簿集計
set = (
    select avg(出金額) from アーカイブ
    where 出金額 > 0 and 費目 = '食費'
)
where 費目

-- 家計簿アーカイブから「費目が食費」の行を取り出したい
-- 表示する列は、費目・メモ・出金額・家計簿集計の費目が食費の合計金額を「過去の合計額」
select 日付, メモ, 出金額, 
    (select sum(出金額) from 家計簿集計
    where 費目 = '食費'
    ) as 過去の合計額 
    from 家計簿アーカイブ
where 費目 = '食費'



-- 複数と比較
-- 復習
-- 家計簿集計から、費目から「食費」「水道光熱費」・「給料」のすべての列を表示
select * from 家計簿集計
where 費目 in('食費', '水道光熱費', '給料')


-- 家計簿集計から、すべての列を表示
-- 費目が家計簿にある費目(重複なく費目を取り出し)
select * from 家計簿集計
where 費目 in (select distinct 費目 from 家計簿)

-- where 〇〇 = (select 〇〇)
-- where 〇〇 in (select 〇〇)
-- 外の〇〇と内側の〇〇を比較するため、同じになる


-- any演算子

-- 家計簿テーブルからすべての列を取り出す
-- 抽出条件は 費目が食費の列 と 出金額が「家計簿アーカイブ」の「費目」が「食費」の列 よりも 小さい
select * from 家計簿
--                         出金額(家計簿) < 出金額(家計簿アーカイブの費目が食費)
where 費目 = '食費' and 出金額 < any(select 出金額 from 家計簿アーカイブ where 費目 = '食費')







----------------------- 練習問題 ------------------------
-- 問題7-1
-- (A)

-- (B)
select
-- (C)
set


-- 問題7-2
-- 問題7-3-1

-- 回答
insert into 頭数集計
values (select 飼育県 from 個体識別 group by 飼育県,
        select count(*) from 個体識別 group by 飼育県)

-- 答え
insert into 頭数集計 
select 飼育県, count(*) from 個体識別 
group by 飼育県

-- 問題7-3-2

-- 回答
select 都道府県, 個体識別番号, 
case 雄雌コード
when '1' then '雄'
when '2' then '雌'
end as 雄雌
from 頭数集計 
where 都道府県 = 
select 飼育県 from 頭数集計 
order by 頭数 desc
offset 0 rows
fetch next 3 rows only

-- 問題7-3-3

-- 回答
-- 個体識別テーブルには母牛についてデータ登録されてる
-- 母牛が乳用種である牛の一覧を個体識別テーブルから抽出したい
select 個体識別番号, 
case 品種コード
when '01' then '乳用種'
when '02' then '肉用種'
when '03' then '交雑種'
end as 品種,
出生日, 母牛番号 from 個体識別
where 母牛番号 in
    (select 個体識別番号 from 個体識別
    where 品種コード = '01')



select title, Authors, name, publication_date from Books





