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

  //var clientHeight = document.getElementById('myDIV').clientHeight;
  //var clientWidth = document.getElementById('myDIV').clientWidth;

  var clientHeight = document.getElementById('myDIV').offsetHeight;
  var clientWidth = document.getElementById('myDIV').offsetWidth;

  if(x>(window.innerWidth-clientWidth))
      x=window.innerWidth-clientWidth;
  if(y>(window.innerHeight-clientHeight))
      y=window.innerHeight-clientHeight;
  
    document.getElementById("myDIV").style.top = y+"px";
    document.getElementById("myDIV").style.left = x + "px";
    document.getElementById("myDIV").style.display = "block";

    var p=document.getElementById("print");
    p.innerHTML=clientHeight+" "+clientWidth+" "+y+" "+x+" "+event.clientY+" "+event.clientX;
}

document.addEventListener("dblclick", doubleclick);

function ws1() {
    var clientHeight = document.getElementById('myDIV').clientHeight;
    var clientWidth = document.getElementById('myDIV').clientWidth;
    
    if(clientHeight>200){myFunction();}
    alert(clientHeight +" "+clientWidth);
}


function ws2() {
    document.getElementById("myDIV").style.display="none";
    document.getElementById("calculator").style.top=document.getElementById("myDIV").style.top;
    document.getElementById("calculator").style.left=document.getElementById("myDIV").style.left;
    document.getElementById("calculator").style.display="block";
}



function view() {
    var viewFullScreen = document.getElementById("view-fullscreen");
    if (viewFullScreen) {
        viewFullScreen.addEventListener("click", function () {
            var docElm = document.documentElement;
            if (docElm.requestFullscreen) {
                docElm.requestFullscreen();
            }
            else if (docElm.msRequestFullscreen) {
                docElm = document.body; //overwrite the element (for IE)
                docElm.msRequestFullscreen();
            }
            else if (docElm.mozRequestFullScreen) {
                docElm.mozRequestFullScreen();
            }
            else if (docElm.webkitRequestFullScreen) {
                docElm.webkitRequestFullScreen();
            }
        }, false);
    }
}
function cancel(){
    var cancelFullScreen = document.getElementById("cancel-fullscreen");
    if (cancelFullScreen) {
        cancelFullScreen.addEventListener("click", function () {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            }
            else if (document.msExitFullscreen) {
                document.msExitFullscreen();
            }
            else if (document.mozCancelFullScreen) {
                document.mozCancelFullScreen();
            }
            else if (document.webkitCancelFullScreen) {
                document.webkitCancelFullScreen();
            }
        }, false);
    }
    
}















