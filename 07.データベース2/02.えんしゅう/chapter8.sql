-- sql構文
select 列 from 表
    group by 列名
            having 列名 = 条件
    where 列 = 条件, 列 in(列, 列), 列 like "%条件%"
        order by 列名 asc


-- 家計簿集計表の「費目が食費」の平均を更新したい
-- 家計簿アーカイブ表の「出金額が0より大きく費目が食品」の「平均」に更新
update 家計簿集計
set 平均 = (select avg(出金額) from 家計簿 where 費目 = '食費')
where 費目 = '食費'

-- 家計簿集計表から、すべての列を表示
-- 費目が家計簿テーブルにある費目(重複なく取り出し)
select * from 家計簿集計
-- 複数行でかえって来るからinを使う
where 費目 in (select 費目 from 家計簿 group by 費目)




---------------------- chapter8 ----------------------

-- リレーション(複数のテーブルを接続する) ⇒ join文
-- 家計簿テーブルと費目テーブルを(費目テーブルの費目ID)の外部キーで接続
-- 表示する列は、日付、名前(費目)、メモを表示

-- 家計簿 → 費目がid管理だから費目テーブルの外部キーから名前で表示する
select 日付, 名前 as 費目, メモ
    from -- 家計簿と費目 (結合が必要)
        家計簿 join 費目 on 家計簿.費目ID = 費目ID


-- 名前、入社日、部署を表示
-- 二つのテーブルにnameカラムが存在してるからemployee.nameで書く
select employee.name as 名前,
        hire_date as 入社日,
        department as 部署
    -- 接続するテーブル名
    from employee join department
    -- 接続するカラム名
    on employee.department_id = department.id

-- 給料が30万以上の人のカナ、入社日、部署を給料の降順で表示
select employee.name as 名前,
        hire_date as 入社日,
        department as 部署
    from employee join department
    on employee.department_id = department.id
        where salary >= 300000 
            order by salary desc


-- 練習問題
-- 問題8-1.1
select a1, a2, b1, b2 
from a join b on a.a1 = b.b2


-- 問題8-2.1
select 社員番号, 社員.名前 as 名前, 部署.名前 as 部署名
from 社員 join 部署
    on 社員.部署ID = 部署.部署ID


-- 問題8-2.2
select 
    社員番号,
    社員.名前 as 名前,
    社員.上司ID as 上司名
-- 同じ表を参照するときは必ず別名を付けないといけない
from 社員 as s1 join 社員 as s2
    on s1.上司ID = s2.社員番号

select 
    s.社員番号,
    s.名前 as 名前,
    j.名前 as 上司名
from 社員 s
left join 社員 j
    on s.上司ID = j.社員番号;


-- 問題8-2.3
select 
    社員.社員番号,
    社員.名前,
    部署.名前,
    支店.名前
from
社員
join 部署 on 部署.部署ID = 社員.部署ID
join 支店 on 支店.支店ID = 社員.勤務地ID

-- 問題8-2.4
select 支店.支店コード, 支店.名前, 社員.社員名 as 支店長名, --ここに社員数
from 支店 --メインテーブル
join 





