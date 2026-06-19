function fetchHello() {
    const promise = fetch('./hello.json');
    
    // jsonファイルが読み込めたら
    const onFulfilled = (data) => {
        console.log('通信成功しました')
    }

    // jsonファイルの読み込みに失敗したら
    const onRejected = (err) => {
        console.log('通信失敗しました');
    }

    // 成功ならこっち、失敗ならあっち を実行するよう「約束」
    return promise.then(onFulfilled, onRejected)
}