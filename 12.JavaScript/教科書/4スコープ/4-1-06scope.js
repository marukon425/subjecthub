function funcHoisting(){
    let  myHoistingVar1 = 'myHoistingVar1';
    console.log(myHoistingVar1);

    if(true){
        let myHoistingVar1 = '変更！';
        console.log(myHoistingVar1);
    }

    console.log(myHoistingVar1); // => "変更！"
}