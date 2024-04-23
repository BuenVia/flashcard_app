const learnCards = document.querySelectorAll(".learn-card")
const loc = window.location.href
const stage = Object.values(loc.split("/")).slice(-1)
const url = `../learn-data/${stage[0]}`
console.log(url);

let dataArr = []


const initialize = async () => {
    await getData()
    addCard(dataArr)
}

const getData = async () => {
    await fetch(url)
    .then(res => res.json())
    .then(data => dataArr = data)
    console.log(dataArr);
}

const addCard = (dataArr) => {
    const card = document.getElementById("card")
    card.innerText = dataArr[0]['eng_word']
}


initialize()