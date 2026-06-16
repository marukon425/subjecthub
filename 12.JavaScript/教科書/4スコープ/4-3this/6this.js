const legacyObj = {
    name: '通常関数の場合',
    test: function() {
        const self = this;
        document.body.addEventListener('click', function() {
        console.log(self.name);
        });
    }
};
