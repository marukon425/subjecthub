select * from 商品
where 単価 >= 50000



select * from 注文
where 注文日 < '2024-01-01'



select * from 注文
where 注文日 < '2023-11-01'



select * from 商品
where not 商品区分 = '1'



select * from 注文
where クーポン割引料 is not null



delete 商品
where 商品コード like 'N%'



select 商品コード, 商品名, 単価 from 商品
where 商品名 like '%コート%'



select * from 商品
where 商品区分 in('2', '3', '9')



select * from 商品
where 商品コード >= 'A0100' and 商品コード <= 'A0500'



select * from 注文 
where 商品コード in('N0501', 'N1021', 'N0223')



select * from 商品
where 商品区分 = '3' and 商品名 like '%水玉%'



select * from 商品
where 商品名 like '%軽い%' or 商品名 like '%ゆるふわ%'




update 廃番商品
set 廃番日 = current_date
where 商品コード = 'S1990'



select 商品コード, 商品名, cast(integer, 単価 - (単価*0.3)) as 単価
where 単価 >= 10000



select 商品区分, min(単価) as 最少額, max(単価) as 最高額 from 商品
group by 商品区分   



select 商品コード, sum(数量) as 注文合計 from 注文
group by 商品コード
order by 商品コード


-- ①
create table 口座 (
    口座 char(7)  not null,
    名義 varchar(40) not null,
    種別 char(1) not null,
    残高 integer(10) not null,
    更新日 date(13) not null,
    primary key (口座)
)

-- ②
update 口座
set 口座番号 = '388000'
where 口座番号 = '0351333'

-- ③
delete 口座
where 口座番号 = '0887132'

-- ④
select avg(残高) as 残高の平均 from 口座
where 種別 = '1'
group by 種別

-- ⑤
select 名義, 残高 from 口座
order by 残高 asc

-- ⑥
select 口座番号, 名義, 残高 from



select 商品コード from 注文
where (注文日 >= '2022-03-01' and 注文日 < '2022-04-01' ) and 数量 >= 3


select * from 注文
where 数量 >= 10 or not クーポン割引料 is null


select 商品コード, sum(数量) as 数量 from 注文
group by 商品コード
having sum(数量) > 5



select count(*), sum(割引額) from 注文