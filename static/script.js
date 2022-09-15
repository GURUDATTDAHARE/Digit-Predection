var canvas = document.getElementById("draw");
var ctx = canvas.getContext("2d");
const answer = document.getElementById("answer");
resize();
function resize() {
  canvas.width = 300;
  canvas.height = 300;
}

// last known position
var pos = { x: 0, y: 0 };

// new position from mouse events
function setPosition(e) {
  var rect = canvas.getBoundingClientRect();
  pos.x = e.clientX - rect.left;
  pos.y = e.clientY - rect.top;
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
    answer.innerHTML = content.img;
  } catch (error) {
    console.log("Fetch error: ", error);
  }
}

function draw(e) {
  if (e.buttons !== 1) return; // if mouse is not clicked, do not go further

  ctx.beginPath(); // begin the drawing path

  // line properties
  ctx.lineWidth = 25; // width of line
  ctx.lineCap = "round"; // rounded end cap
  ctx.strokeStyle = "#3E60F9"; // hex color of line

  // draw line
  ctx.moveTo(pos.x, pos.y); // from position
  setPosition(e);
  ctx.lineTo(pos.x, pos.y); // to position

  ctx.stroke(); // draw it!
}

canvas.addEventListener("resize", resize);
document.addEventListener("mousemove", draw);
document.addEventListener("mousedown", setPosition);
document.addEventListener("mouseenter", setPosition);
