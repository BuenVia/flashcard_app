const learnCards = document.querySelectorAll(".learn-card")
const engSpans = document.querySelectorAll("learn-word-eng")
const spaSpans = document.querySelectorAll("learn-word-spa")

learnCards.forEach(card => {
    card.addEventListener("click", () => {
        console.log(card.innerHTML);
    })
})
