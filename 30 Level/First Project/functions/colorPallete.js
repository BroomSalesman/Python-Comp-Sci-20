let pltsize = 30;

export function pltBlock(x, y, size, color) {
    fill(color);
    square(x, y, size);
  }

export function createPallete() {

    //pallete area
    line (40, 0 , 40, 1000);
    fill('lightgray');
    rect(0, 0, 40, 1000);

    //black
    pltBlock(5, 5, pltsize, 'black');

    //gray
    pltBlock(5, 40, pltsize, 'gray');

    //white
    pltBlock(5, 75, pltsize, 'white');

    //red
    pltBlock(5, 110, pltsize, 'red');

    //orange
    pltBlock(5, 145, pltsize, 'orange');

    //yellow
    pltBlock(5, 180, pltsize, 'yellow');

    //lime
    pltBlock(5, 215, pltsize, 'lime');

    //green
    pltBlock(5, 250, pltsize, 'green');

    //turquoise
    pltBlock(5, 285, pltsize, 'turquoise');

    //sky blue
    pltBlock(5, 320, pltsize, 'skyblue');

    //blue
    pltBlock(5, 355, pltsize, 'royalblue');

    //darkblue
    pltBlock(5, 390, pltsize, 'darkblue');

    //violet
    pltBlock(5, 425, pltsize, 'indigo');

    //lavendar
    pltBlock(5, 460, pltsize, '#a392cb');

    //pink
    pltBlock(5, 495, pltsize, 'hotpink');
  }
