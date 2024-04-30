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
    const submitBtn = document.getElementById("userSubmit")
    let index = 0
<<<<<<< HEAD

    spaWord.innerText = dataArr[index]['fre_word']
=======
    
    spaWord.innerText = dataArr[index]['spa_word']
>>>>>>> 3aef2881d68bcaf874f5cde1c30a732e79bed055
    engWord.innerText = dataArr[index]["eng_word"]
    
    submitBtn.addEventListener("click", () => {
<<<<<<< HEAD
        index++
        spaWord.innerText = dataArr[index]['fre_word']
        engWord.innerText = dataArr[index]["eng_word"]
=======
        const userAns = document.getElementById("userAns")
        if (userAns.value.toLowerCase() === dataArr[index]['spa_word'].toLowerCase() && index < dataArr.length - 1) {
            index++
            spaWord.innerText = dataArr[index]['spa_word']
            engWord.innerText = dataArr[index]["eng_word"]
        } else {
            console.log(userAns.value, dataArr[index]['spa_word']);
            addStyle("incorrect-answer")
            setTimeout(removeStyle("incorrect-answer"), 2000)
        }
        
>>>>>>> 3aef2881d68bcaf874f5cde1c30a732e79bed055
    })
}

const addStyle = (element) => {
    userAns.classList.add(element)
}

const removeStyle = (element) => {
    userAns.classList.remove(element)
}


initialize()