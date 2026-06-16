// JSONの文字列は **必ずダブルクオーテーション""で囲む**
const jsonStr = JSON.stringify({
    name:"田中太郎",
    age:25,
    interest:["プログラミング", "料理", "読書"]
});
console.log(jsonStr);

// parse：引数で与えられたjsonをオブジェクトにして返す(プログラムとして操作できるようにしたもの)
const obj = JSON.parse(jsonStr);
console.log(obj)

//代入してる「name」キーを表示してる
console.log(obj.name)

//JSON (送るよう)：ただのテキスト
//object：JSONをプログラム上で使えるようにしたもの(操作できるようにしたもの)