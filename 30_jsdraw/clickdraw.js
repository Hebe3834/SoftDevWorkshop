// retrieve node in DOM via ID
var c = document.getElementById("slate");

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

// init global state var
var mode = "rect";

// var toggleMode = function(e) {}
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode=="rect") {
        mode = "circle";
    } else {
        mode = "rect";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);

    ctx.beginPath();
    ctx.rect(mouseX, mouseY, 100, 150);
    ctx.fillStyle = "red";
    ctx.fill();
}

var drawCircle = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);

    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, 360);
    ctx.fillStyle = "red";
    ctx.fill();
}

var draw = (e) => {
    if (mode=="rect") drawRect(e);
    if (mode=="circle") drawCircle(e);
}

var wipeCanvas = (e) => {
    console.log("wiping canvas...");
    ctx.clearRect(0,0,c.clientWidth,c.clientHeight);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode); 
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
