// ブロックスコープ

// ブロック：{}で囲まれたコード群を指す

if(true){
    const myBlockVar1 = 'myBlockVar1-true'; // これがブロックスコープです
    console.log(myBlockVar1)
}else{
    const myBlockVar1 = 'myBlockVar1-false'; // これがブロックスコープです
    console.log(myBlockVar1)
}