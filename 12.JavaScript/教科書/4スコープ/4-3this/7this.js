const arrowObj = {
    name: 'アロー関数の場合',
    test: function() {
        document.body.addEventListener('click', () => {
        console.log(this.name); // これで親側にアクセスできます
        });
    }
};
