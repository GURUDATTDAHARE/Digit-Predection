var canvas = document.getElementById("draw");
var ctx = canvas.getContext("2d");

resize();
function resize() {
  ctx.canvas.width = window.innerWidth;
  ctx.canvas.height = window.innerHeight;
}

// last known position
var pos = { x: 0, y: 0 };

// new position from mouse events
function setPosition(e) {
  pos.x = e.clientX;
  pos.y = e.clientY;
}

async function onSubmit() {
  var dataURL = canvas.toDataURL();
  try {
    const res = await fetch("/predict", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ imageURL: dataURL }),
    });
    const content = await res.json();
    console.log(content);
  } catch (error) {
    console.log("Fetch error: ", error);
  }
}

function draw(e) {
  if (e.buttons !== 1) return; // if mouse is not clicked, do not go further

  ctx.beginPath(); // begin the drawing path

  // line properties
  ctx.lineWidth = 40; // width of line
  ctx.lineCap = "round"; // rounded end cap
  ctx.strokeStyle = "#00ffff"; // hex color of line

  // draw line
  ctx.moveTo(pos.x, pos.y); // from position
  setPosition(e);
  ctx.lineTo(pos.x, pos.y); // to position

  ctx.stroke(); // draw it!
}

window.addEventListener("resize", resize);
document.addEventListener("mousemove", draw);
document.addEventListener("mousedown", setPosition);
document.addEventListener("mouseenter", setPosition);
