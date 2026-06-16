// インストールした picocolors ライブラリを読み込む  

const pc = require('picocolors');  

// ターミナルから引数（名前）を受け取る  

const name = process.argv[2] || "ゲスト";  

// 文字を緑色（green）、黄色（yellow）、太字（bold）にして出力する 
console.log(pc.green(`🎉 こんにちは、${pc.bold(pc.yellow(name))}さん！ 🎉`)); 