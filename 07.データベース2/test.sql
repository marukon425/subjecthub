create table 口座 (口座番号 char(7) primary key, 名義 )







select 商品コード, 商品名, 単価, sum(数量) as これまでに販売した数量 
where 



-- 問11
select 注文日, 注文番号, 商品コード, 数量 from 注文
where not クーポン割引料 is null
order by 注文日 asc,  商品コード asc


-- 問12
select 商品コード, 商品名, 商品区分 from 商品
where 商品名 like '%水玉%'


-- 問13
insert into 廃番商品 
(商品コード, 商品名, 単価, 商品区分, 廃番日, 売上個数)
values ('A0052', '裏起毛パーカー', 2900, '2025-07-05', 0)

-- 問題14
delete from 商品
where 商品コード = 'A0052'

-- 問題15
select 商品区分, cast(avg(単価) as int) as 平均単価 from 商品
group by 商品区分

-- 問題16
select 注文番号, 商品名, 単価*sum(数量) as 販売金額 from 商品
union
select 注文番号, 商品名, 単価*sum(数量) as 販売金額 from 注文
group by 注文番号
having 注文番号 = '2023310300045'


select 注文番号, 商品名, 
(select 単価 from 商品)*sum(数量) from 注文
group by 注文番号
having 注文番号 = '2023310300045'


select 注文番号, 商品.商品名, 商品.単価*数量 as 販売金額
from 注文 join 商品
on 商品.商品コード = 注文.商品コード
where 注文番号 = '2023310300045'
-- 問題17
select 注文日, 注文番号, 商品.単価*数量 as 販売金額合計
from 注文 join 商品
on 注文.商品コード = 商品.商品コード
where 商品.単価*数量 >= 10000


-- 問題18
select 商品コード, 商品名 from 商品
except
select 商品コード, 商品名 from 廃番商品
where 商品区分 = '9'