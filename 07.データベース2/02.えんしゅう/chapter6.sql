-- selectの使い方
select 列名, 列名・・・
    from テーブル名
        where 抽出条件
            order by テーブル名 asc か desc

------------------ chapter6 ------------------

-- 様々な集計
-- 1.合計値
select sum(出金額) as 出金額の合計値 from 家計簿
-- 2.最大値
select max(出金額) as 出金額の最大値 from 家計簿
-- 3.最小値
select min(出金額) as 出金額の最小値 from 家計簿
-- 4.平均値
select avg(出金額) as 出金額の平均値 from 家計簿


-- 列名を書く集計関数
sum(列名) : 合計
avg(列名) : 平均
max(列名) : 最大
min(列名) : 最小

-- 「基本的な構文」は列名を書かない集計関数
count(*) : 行数をカウント
-- ※()の中に列名を記述をするとnullをカウントしない

-- 費目が食費の行数をカウント
-- 列名を食費の行数
select count(*) as 食費の行数 from 家計簿
    where 費目 = "食費"

-- 重複しない費目をカウント
select count(distinct count) as  from 家計簿

-- 日付と出金額の合計を表示する
select 日付, sum(出金額) from 家計簿アーカイブ
-- 表示される行数(日付)：全行
-- 表示される行数(合計)：1行
-- だからエラーが起きる


-- 複数のデータが取り出されるわけじゃない。1つのデータだけが取り出される



-- 費目別(費目ごと、費目をグループとして)の集計をする
-- 表示される列名は自分で判断できるようにしておく
select 費目, sum(出金額)
    from 家計簿
        group by 費目 -- グループ化したい列名 (○○別)　

-- 家計簿アーカイブから
-- 出金額が5000以上のデータを
-- 費目別の平均を表示
select 費目, avg(出金額) from 家計簿アーカイブ 
where 出金額 >= 5000 
group by 費目 


-- 家計簿アーカイブかあ
-- 費目別(group by)に出金額の合計を表示
-- 平均が0より大きい費目のみ表示
-- ※ グループ化後にデータを絞る
select 費目, sum(出金額) from 家計簿アーカイブ 
group by 費目 
having sum(出金額) > 0-- having : グループ化後の条件 ※ group byがないと使用不可



-- 練習問題
-- 問題6-1-1
select sum(降水量), avg(最高気温), avg(最低気温) from 都市別気象観測

-- 問題6-1-2
select sum(降水量), avg(最高気温), avg(最低気温) from 都市別気象観測
where 都市名 = '東京'

-- 問題6-1-3
select avg(降水量), max(最高気温), min(最高気温), max(最低気温), min(最低気温) 

-- 問題6-1-4
select 

-- 問題6-1-5
select 都市名, 最高気温 from 都市別気象観測
where 最高気温 >= 38

-- 問題6-1-6
select 都市名, 最低気 from 都市別気象観測
where 最低気温 <= -10

-- 問題6-2-1
select count(*) from 入退出
where 退出 is null

-- 問題6-2-2
select 社員名, sum(社員名) as 入室回数 from 入退室管理
group by 社員名
order by 入退室回数

-- 問題6-2-3
select 社員, count(*) as 入出回数 from 入退室管理 
group by 事由区分

-- 問題6-2-4
select 社員名, sum(社員名) as 入室回数 from 入退出管理
group by 社員名
having sum(社員名) > 10

-- 問題6-2-5
select 日付, count(*) as 社員数 from 入退室管理 
having 事由区分 = '3'
group by 日付

-- 問題6-3
-- 答え：2, 


-- 1
SELECT COUNT(*) AS 社員数
FROM 入退室管理
WHERE 退室 IS NULL;
-- 2
SELECT 社員名, COUNT(*) AS 入室回数
FROM 入退室管理
GROUP BY 社員名
ORDER BY 2 DESC;
-- 3
SELECT CASE 事由区分 WHEN '1' THEN 'メンテナンス'
                    WHEN '2' THEN 'リリース作業'
                    WHEN '3' THEN '障害対応'
                    WHEN '9' THEN 'その他'
    END AS 事由,
    COUNT(*) AS 入室回数
FROM 入退室管理
GROUP BY 事由区分;
-- 4
SELECT 社員名, COUNT(*) AS 入室回数
FROM 入退室管理
GROUP BY 社員名
HAVING COUNT(*) > 10;
-- 5
SELECT 日付, COUNT(社員名) AS 対応社員数
FROM 入退室管理
WHERE 事由区分 = '3'
GROUP BY 日付;







select 口座番号, 名義 from 口座
union
select 口座番号, 名義 from 廃止口座
