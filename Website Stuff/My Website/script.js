function scroll_credits(duration) {

    var endCredits= document.getElementById("doneCredits");
    // All this code was copied from Bito (GPT 4 code assistant) response, but after thoroughly digging into what I didn't understand.
    // I have snips of proof that I used this in my code after asking Bito how it works, why it works like that, and verifiying if I understood how it worked.
    // See "Bito Screenshots".
    // I wrote this before it worked though, so I may be getting a little too confident.
    //Didn't work. Just jumped right to the id.
    endCredits.scrollIntoView({
        behaviour: 'smooth',
        block: 'start',
        inline: 'nearest',
        duration: duration
    })
}






