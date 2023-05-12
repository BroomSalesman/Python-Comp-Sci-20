//function scroll_credits(duration) {

    //var endCredits= document.getElementById("doneCredits");
    //All this code was copied from Bito (GPT 4 code assistant) response, but after thoroughly digging into what I didn't understand.
    //I have snips of proof that I used this in my code after asking Bito how it works, why it works like that, and verifiying if I understood how it worked.
    //See "Bito Screenshots".
    //I wrote this before it worked though, so I may be getting a little too confident.
    //Didn't work. Just jumped right to the id.
    //Going to comment all of this and try something else (this is me starting again a day later)
    //endCredits.scrollIntoView({
        //behaviour: 'smooth',
        //block: 'start',
        //inline: 'nearest',
        //duration: duration
    //})
//}

function  scroll_to_element(elementId, scrollSpeed) {
    //Const is used to definesa variable that cannot be changed after assignment, and
    //document.getElementByID(elementID) takes the argument elementId, and uses the element ID to determine what
    //element from the document is used as the stop auto scroll marker.
    const stop_scrolling_mark = document.getElementById(elementId);
    const ScrollHeight = element.scrollHeight;

}
