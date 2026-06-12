//ブロックは意図的に書くこともできる
{
    const myBlockVar2 = 'myBlockVar2' //これがブロックスコープ変数
    console.log(myBlockVar2);
}

// console.log(myBlockVar2); // エラー：ブロックの外なので利用できません