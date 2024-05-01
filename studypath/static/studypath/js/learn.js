const learnCards = document.querySelectorAll(".learn-card")
const loc = window.location.href
const stage = Object.values(loc.split("/")).slice(-1)
// const url = `../learn-data/${stage[0]}`
// const url = `/studypath/learn-data1/1/vocab/3?stage=1`
const params = new URLSearchParams(window.location.search)
const qt_stage = params.get('stage')
const qt_gt = params.get('grammar_type')
console.log(qt_stage, qt_gt);
const url = `/studypath/learn-data?stage=${qt_stage}&grammar_type=${qt_gt}`


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
    const freWord = document.getElementById("freWord")
    const engWord = document.getElementById("engWord")
    const submitBtn = document.getElementById("userSubmit")
    let index = 0
   
    freWord.innerText = dataArr[index]['fre_word']
    engWord.innerText = dataArr[index]["eng_word"]
    
    submitBtn.addEventListener("click", () => {
        if (index < dataArr.length -1) {
            index++
            freWord.innerText = dataArr[index]['fre_word']
            engWord.innerText = dataArr[index]["eng_word"]     
        }
    })
}


initialize()