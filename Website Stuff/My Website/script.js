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
    const stop_scroll_element = document.getElementById(elementId);

    // Gives the height of the stop_scroll_element
    const ScrollHeight = stop_scroll_element.scrollHeight;

    //So if I understood correctly, this should y axis value of stop_scroll_element.  Wait no. Okay I do not get this.
    // After a lot of ChatGPT prompts and a google search, I understand! It gets the distance from the scroll bar and the top of the element.
    let scrollTop = stop_scroll_element.scrollTop;

    // So apaprently dividing the scrollSpeed by 10 to create more consistent and smooth scrolling.
    //  It makes the scrolling increment equal in each 10 milisecond interval.
    const scrollIncrement = scrollSpeed /10;


    //setInterval() is used to repeatedly calls a function or code snippet repeatedly, at a specificed interval.
    //So in this code, it is more like a"if True: [lines of code]... if this: break" in Pyhon, instead of a for loop.
    //Also => is used to create anonymous functions, so it's kind of like lambda I guess, except it can be more than one line.
    const scrollInterval = setInterval(() => {

    //Increases scrollTop by increment, and then scrolls to the new scrollTop value.
      scrollTop += scrollIncrement;
      stop_scroll_element.scrollTo(0, scrollTop);

    // once the scrollTop value is greater than or equal to the height of the page, and the height at which the element is at,
    //it clears the interval, which is like a break statement in Python
      if (element.scrollTop >= scrollHeight - stop_scroll_element.clientHeight) {
        clearInterval(scrollInterval)
      }
      }, 10); //The 10 creates a 10 milisecond delay between each iteration.
  }
