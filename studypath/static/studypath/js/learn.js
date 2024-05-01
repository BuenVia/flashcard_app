const learnCards = document.querySelectorAll(".learn-card")
const loc = window.location.href
const stage = Object.values(loc.split("/")).slice(-1)
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
    const audioBtn = document.getElementById("audioBtn")
    const submitBtn = document.getElementById("userSubmit")
    let index = 0
   
    freWord.innerText = dataArr[index]['fre_word']
    engWord.innerText = dataArr[index]["eng_word"]
    
    audioBtn.addEventListener("click", () => {
        playAudio(dataArr[index]['fre_word'], .1, 1)
    })

    submitBtn.addEventListener("click", () => {
        if (index < dataArr.length -1) {
            index++
            freWord.innerText = dataArr[index]['fre_word']
            engWord.innerText = dataArr[index]["eng_word"]     
        }
    })
}


const playAudio = (text, pitch, speed) => {
    const speech = new SpeechSynthesisUtterance()

    if (speechSynthesis.speaking) return
    speech.lang = "fr-FR"
    speech.text = text
    speech.pitch = pitch
    speech.rate = speed || 1
    speechSynthesis.speak(speech)
}


initialize()