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

  var clientHeight = document.getElementById('myDIV').clientHeight;
  var clientWidth = document.getElementById('myDIV').clientWidth;

  if(x>(window.innerWidth-clientWidth))
      x=window.innerWidth-clientWidth;
  if(y>(window.innerHeight-clientHeight))
      y=window.innerHeight-clientHeight;
  
    document.getElementById("myDIV").style.top = y+"px";
    document.getElementById("myDIV").style.left = x + "px";
    document.getElementById("myDIV").style.display = "block";

    
}

document.addEventListener("dblclick", doubleclick);

function ws() {
    var clientHeight = document.getElementById('myDIV').clientHeight;
    var clientWidth = document.getElementById('myDIV').clientWidth;
    
    if(clientHeight>200){myFunction();}
    alert(clientHeight +" "+clientWidth);
}