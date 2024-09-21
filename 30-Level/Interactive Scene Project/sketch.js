import {createPallete} from 'functions/colorPallete.js';

let pencolor;
let pensize = 5;

//pallete squares size
pltsize = 30;


function setup() {
  createCanvas(1000, 1000);
}


function draw() {
  background(255);
  noCursor();
  createPallete();
  chooseColor();
  coloringPen();
  circle(200, 200, 5);

}




//Placeholder for colors in the pallete

function coloringPen() {
  circle(mouseX, mouseY,  pensize);
}

function drawPen() {
  if (mouseIsPressed()) {
    fill(pencolor);
    stroke(0);
    circle(mouseX, mouseY, pensize);
  }

}

function chooseSize() {

}

//when color from pallete is clicked on, color of pen changes
function chooseColor() {

  if (mouseIsPressed && (mouseX > 5)&&(mouseX <= 30)) {

    //blacked pressed
    if (mouseY > 5 && mouseY < 35) {
      pencolor = 'black';
    }

    //gray pressed
    if (mouseY > 40 && mouseY < 70) {
      pencolor = 'gray';
    }

    //white pressed
    if (mouseY > 75 && mouseY < 105) {
      pencolor = 'white';
    }

    //red pressed
    if (mouseY > 110 && mouseY < 140) {
      pencolor = 'red';
    }

    //orange pressed
    if (mouseY > 145 && mouseY < 175) {
      pencolor = 'orange';
    }

    //yellow pressed
    if (mouseY > 180 && mouseY < 210) {
      pencolor = 'yellow';
    }

    // lime pressed
    if (mouseY > 215 && mouseY < 245) {
      pencolor = 'lime';
    }

    //green pressed
    if (mouseY > 250 && mouseY < 280) {
      pencolor = 'green';
    }

    //turquoise pressed
    if (mouseY > 285 && mouseY < 315) {
      pencolor = 'turquoise';
  }

    //skyblue pressed
    if (mouseY > 320 && mouseY < 350) {
      pencolor = 'skyblue';
    }

    //blue pressed
    if (mouseY > 355 && mouseY < 385) {
      pencolor = 'royalblue';
    }

    //darkblue pressed
    if (mouseY > 390 && mouseY < 420) {
      pencolor = 'darkblue';
    }

    //purple pressed
    if (mouseY > 425 && mouseY < 455) {
    pencolor = 'indigo';
  }

    //lavendar pressed
    if (mouseY > 460 && mouseY < 490) {
      pencolor = '#a392cb';
    }

  //pink pressed
    if (mouseY > 495 && mouseY < 525) {
      pencolor = 'hotpink';
    }
  }
}
