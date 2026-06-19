function fetchHello() {
    return fetch('./hello.json').then((data) => {
        console.log('通信が成功しました');
    }, (err) => {
        console.log('通信が失敗しました')
    });
}


// 1promise.jsを短くしたやつ