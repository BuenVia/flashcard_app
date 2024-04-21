const learnCards = document.querySelectorAll(".learn-card")

learnCards.forEach(card => {
    card.addEventListener("click", () => {

        if (card.querySelector("#spaWord")) {
            // card.querySelector("#spaWord").classList.remove("hide")
            // card.querySelector("#spaWord").classList.add("show")
        } else {
            // card.querySelector("#spaWord").classList.remove("show")
            // card.querySelector("#spaWord").classList.add("hide")
        }
    })
})
