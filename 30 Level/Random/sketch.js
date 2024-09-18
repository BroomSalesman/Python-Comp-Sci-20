let color = 'white';
let black  = false;

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  let cellSize = width / 8;
  for (y = 0; y <= 8; y+= height / 8) {
    for (x = 0; x <= 8; x+= width/8) {
      fill(color);

      square(x, y, cellSize);

      black = !black;
      if (black) {
        color = 'black';
      }

      if (!black)
        color = 'white';
      }
      square(x, y, 50);
    }
    black = !black;
  }

}
