-- 出金額が1円でもある行を削除
delete from 家計簿 
where 出金額 > 0

-- 家計簿表から○○を取り出す
-- 取り出される行はなし
select * 
from 家計簿 
where 出金額 is null


-- like = あいまい検索
-- %1月% ⇒　１月を含む (１番使用率が多い)
-- %1月 ⇒　１月で終わる
-- _1月 ⇒ 〇１月の三文字
select * 
from 家計簿 
where メモ like '%1月%'
-- ↑メモから「１月」を含む行を抽出

-- 費目が「費」で終わる行を抽出
select * 
from 家計簿 
where 費目 like '%費'

-- 家計簿テーブルから出金額が500円～900円の行を抽出
-- between
select * from 家計簿 
where 出金額 between 500 and 900

-- IN (○○, ○○)→ 複数選択
-- 費目が「食費」または「交際費」の行を取り出す
select * from 家計簿 
where 費目 in ('食費', '交際費')

-- 費目が「食費」または「交際費」以外の行を取り出す
select * from 家計簿 
where 費目 not in ('食費', '交際費')

-- 名称が「スッキリ勇者クエスト」'かつ' 販売店が「B」の価格カラムを6200円に変更
UPDATE 湊くんの買い物リスト 
SET 価格 = 6200 
WHERE 名称 = 'スッキリ勇者クエスト' AND 販売店 = 'B'

-- 
select * from 湊くんの買い物リスト 
where   (販売店 = 'A' or 販売店 = 'B') and (カテゴリ = 'ゲーム' or カテゴリ = 'DVD')

-- 3.7練習問題
-- 問題3-1 1
select * from 気象観測 
where 月 = '６月'

-- 問題3-1 2
select * from 気象観測
where 月 not '６月'

-- 問題3-1 3
select * from 気象観測 
where 降水量 < 100

-- 問題3-1 4
select * from 気象観測
where 降水量 > 200

-- 問題3-1 5
select * from 気象観測 
where 最高気温 >= 30
select * from 気象観測 
where 月 in ('３月', '５月', '７月')

-- 問題3-1-6
select * from 気象観測
where 最低気温 =< 0

-- 問題3-1 7
select * from 気象観測
where 月 in ('３月', '５月', '７月')

-- 問題3-1 8
select * from 気象観測
where 月 not in ('３月', '５月', '７月')

-- 問題3-1 9
select * from 気象観測
where 降水量 =< 100 and 湿度 < 50

-- 問題3-1 10
select * from 気象観測
where 最低気温 =< 5 or 最高気温 > 35

-- 問題3-1 11
select * from 気象観測
where 湿度 between 60 and 79

-- 問題3-1 12
select * from 気象観測
where 降水量 is null or 最高気温 is null or 最低気温 is null or 湿度 is null or




-- 問題3-2 1 
select * from 都道府県
where 都道府県名 like '%川'

-- 門災3-2 2
select * from 都道府県
where 都道府県名 like '%島%'

-- 問題3-2 3
select * from 都道府県
where 都道府県名 like '愛%'

-- 問題3-2 4
select * from 都道府県
where 都道府県名 = 県庁所在地

-- 問題3-2 5
select * from 都道府県
where not 都道府県名 = 県庁所在地




-- 問題3-3 1
select * from 成績表

-- 問題3-3 2
insert into 成績表 values ( 'S001', '織田信長', 77, 55, 80, 93, null  )
insert into 成績表 values ( 'A002', '豊臣秀吉', 64, 69, 0, 59, null  )
insert into 成績表 values ( 'E003', '徳川家康', 80, 85, 90, 79, null  )

-- 問題3-3 3
update 成績表 
set 法学 = 85, 哲学 = 67 
where 学籍番号 = 'S001'

-- 問題3-3 4
update 成績表 
set 外国語 = 81 
where 学籍番号 = 'A002' or 学籍番号 = 'E003'

-- 問題3-3 5-1
update 成績表
set 総合成績 = 'A'
where 法学 >= 50 and 経済学 >= 80 and 哲学 >= 80 and 情報理論 >= 80 and 外国語 >= 80 and

-- 問題3-3 5-2
update 成績表
set 総合成績 = 'B'
where ( 法学 >=80 or 外国語 >= 80 ) and ( 経済学 >=80 or 哲学 >= 80 )

-- 問題3-3 5-3
update 成績表
set 総合成績 = 'D'
where 法学 >= 50 and 経済学 >= 50 and 哲学 >= 50 and 情報理論 >= 50 and 外国語 >= 50    

-- 問題3-3 5-4
update 成績表
set 総合成績 = 'D'
where (法学 between 79 and 50) and (経済学 between 79 and 50) and (哲学 between 79 and 50) and (情報理論 between 79 and 50) and (外国語 between 79 and 50) 














select * from 商品
where 単価 >= 50000