function myFunction() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

var x1;
var y1;

function doubleclick(event) {

  x=event.clientX;
  y=event.clientY;

    document.getElementById("myDIV").style.top = y+"px";
    document.getElementById("myDIV").style.left = x + "px";
    document.getElementById("myDIV").style.display = "block";
}

document.addEventListener("click", doubleclick);
