async function getContents() {
    const response = await fetch('https://exampleB.com');
    const contents = await response.json();
    console.log(contents);
}

getContents();