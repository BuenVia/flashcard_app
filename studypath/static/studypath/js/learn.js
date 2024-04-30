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
    const spaWord = document.getElementById("spaWord")
    const engWord = document.getElementById("engWord")
    const userAns = document.getElementById("userAns")
    const submitBtn = document.getElementById("userSubmit")
    let index = 0

    spaWord.innerText = dataArr[index]['fre_word']
    engWord.innerText = dataArr[index]["eng_word"]

    submitBtn.addEventListener("click", () => {
        index++
        spaWord.innerText = dataArr[index]['fre_word']
        engWord.innerText = dataArr[index]["eng_word"]
    })
}


initialize()