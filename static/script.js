
var canvas = document.getElementById("draw");
var but = document.getElementById("predict")
var input=document.getElementById("inp")
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


function draw(e) {
    if (e.buttons !== 1) return; // if mouse is not clicked, do not go further
 
    var color = document.getElementById("hex").value;

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
but.addEventListener("click",()=>{
   
  var dataURL = canvas.toDataURL();
  // but.value=dataURL
 // console.log(dataURL)
    // var highQuality = canvas.toDataURL("image/jpeg", 1.0);
    input.value=""+dataURL
    //location.href="/predict"
});
window.addEventListener("resize", resize);
document.addEventListener("mousemove", draw);
document.addEventListener("mousedown", setPosition);
document.addEventListener("mouseenter", setPosition);