-- 学生テーブルから
-- 年齢が20または21または22の氏名と住所を抽出
select 氏名, 住所 from 学生
where 年齢 in (20, 21, 22)


-- 商品テーブルから
-- 住所に小倉北区が含まれる行を抽出
select * from 商品
where 住所 like '%小倉北区%'


-- 商品テーブルから
-- カテゴリがチョコ　かつ　在庫数が１００以上の行を抽出
select * from 商品
where カテゴリ = 'チョコ' and 在庫数 >= 100



------------------------------------------------------------
--講義範囲
------------------------------------------------------------

-- 重複を取り除いてデータを抽出
-- sekect distinct 列名

-- 家計簿テーブルから入金額を重複なく抽出
select distinct 入金額 from 家計簿


-- 家計簿アーカイブ表から費目を重複なく抽出
-- distinctあり → 5行
select distinct 費目 from 家計簿アーカイブ

-- distinctなし → 8行
select 費目 from 家計簿アーカイブ


-- 並び替え (oder by 列名 並び順)
-- 並び順  asc → 昇順    desc → 降順
-- 家計簿テーブルから出金額の昇順
select * from 家計簿 
order by 出金額 asc

-- 家計簿表から日付の降順
select * from 家計簿 
order by 日付 desc


-- 家計簿テーブルから
-- 入金額が同じ場合は昇順、出金額を降順で
-- * を使用せず全行
select 費目, メモ, 入金額, 出金額 from 家計簿
order by 入金額 asc, 出金額 desc 

-- order byの後の列名の番号で記載することもできる
-- select句で指定した列名を1, 2, 3・・・
-- 入金額 = ４行目     出金額 = ５行目
select 費目, メモ, 入金額, 出金額 from 家計簿
order by 4 asc, 5 desc 


-- 並び替え後に特定の行のみを取得する
-- 例. トップ３、１０番目～１５番目　など
-- 家計簿表から出金額が高いトップ３の費目と金額
select * from 家計簿 アーカイブ 
order by 出金額 desc 
offset 0 rows -- 先頭から除外したい行数 ０行
fetch next 3 rows only -- 取得したい行数 ３行

-- vscodeはmySQLベース → offset, onlyが使えない

-- ３番目に高い出金額と費目
select * from 家計簿アーカイブ 
order by 出金額 desc 
offset 2 rows -- 先頭から除外したい行数 2行
fetch next 1 rows only -- 取得したい行数 1行


-- ５番目から７番目に高い出金額と費目
select * from 家計簿アーカイブ 
order by 出金額 desc 
offset 4 rows -- 先頭から除外したい行数 ０行
fetch next 2 rows only -- 取得したい行数 ３行






--------------------------------- 集合演算 ---------------------------------
-- 和集合 (nunion)：２つを足し合わせる
-- 差集合 (except)：最初の結果から次の結果の重複を取り除く
-- 席集合 (intersect)：２つの重複　(共通)　を取り出す

-- 家計簿テーブルと家計簿アーカイブテーブルを足し合わせて表示
select * from 家計簿
    union -- 集合演算
select * from 家計簿


-- 家計簿テーブルにあって、家計簿アーカイブにない費目を表示
select 費目 from 家計簿 
except 
select 費目 from 家計簿アーカイブ 

-- 家計簿テーブルと家計簿アーカイブに重複する(共通)費目
select 費目 from 家計簿 
intersect 
select 費目 from 家計簿アーカイブ






------------------------問題
-- 問題4-1-1
select * from 注文履歴
order by 注文番号 asc

-- 問題4-1-2
select 商品名 from 注文履歴
where 日付 = 2024-01
order by 商品名 asc


-- 問題4-1-3
select 注文番号, 注文枝番, 注文金額 from 注文履歴
order by 注文金額 desc
offset 1 rows
fetch next 2 rows only

-- 問題4-1-4  ?
select 日付, 商品名, 単価, 数量, 注文金額 from 注文履歴 
order by 

-- 問題4-1-5
select 分類, 商品名, 単価 from 注文履歴 
order by 分類 asc, 商品名 asc



-- 問題4-2-1
select * from 整数
union 
select * from 奇数
union
select * from 偶数

-- 問題4-2-2
select * from 整数
except 
select * from 奇数
except
select * from 偶数

-- 問題4-2-3
select * from 整数
intersect 
select * from 奇数
intersect
select * from 偶数

-- 問題4-2-4
SELECT * FROM 奇数
INTERSECT
SELECT * FROM 偶数;









