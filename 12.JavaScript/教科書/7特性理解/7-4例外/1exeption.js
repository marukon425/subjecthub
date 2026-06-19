function displayName(name) {
    if(!name) {
        throw new Error('name is required');
    }

    console.log(`名前は${name}です`)
}

try {
    displayName();
}catch(e){
    console.error(`名前表示に失敗しました：${e.message}`)
}