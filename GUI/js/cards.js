function myFunction() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}



function fun1() {

    var targLink = document.getElementById ("body1");
    var clickEvent  = document.createEvent ('MouseEvents');
    clickEvent.initEvent ('dblclick', true, true);
    targLink.dispatchEvent (clickEvent);

    /*var x2 = document.getElementById("x").value;
    var y2 = document.getElementById("y").value;
    //var output = document.getElementById("output");
    var p3=document.getElementById("cursor");
    p3.style.top=y2+"px";
    p3.style.left=x2+"px";
    var elements = document.elementsFromPoint(x2,y2);
    elements[1].dblclick();*/
    //document.write(elements[1].id);
    /*for(var i = 0; i < elements.length; i++) {
    output.textContent += elements[i].localName;
    if (i < elements.length - 1) {
      output.textContent += " < ";
    }
  }*/
    //document.write(elems[0].id);
}
function fun2() {	
    var x4 = document.getElementById("x").value;
    var y4 = document.getElementById("y").value;
    //var output = document.getElementById("output");
    var p4=document.getElementById("cursor");
    p4.style.top=y4+"px";
    p4.style.left=x4+"px";
    var elements = document.elementsFromPoint(x4,y4);
    elements[1].click();
    //document.write(elements[1].id);
    /*for(var i = 0; i < elements.length; i++) {
    output.textContent += elements[i].localName;
    if (i < elements.length - 1) {
      output.textContent += " < ";
    }
  }*/
    //document.write(elems[0].id);
}
function mymove() {

  var x3=document.getElementById("x").value;
  var y3=document.getElementById("y").value;
  var p2=document.getElementById("cursor");
  p2.style.top=y3+"px";
  p2.style.left=x3+"px";
}



var x1;
var y1;

function doubleclick() {

  //x=event.clientX;
  //y=event.clientY;
  //document.write("koojhg");
  var x=document.getElementById("x").value;
  var y=document.getElementById("y").value;

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

    /*var p=document.getElementById("print");
    p.innerHTML=clientHeight+" "+clientWidth+" "+y+" "+x+" "+event.clientY+" "+event.clientX;*/
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

function ws3() {
    document.getElementById("myDIV").style.display="none";
    document.getElementById("calendar").style.top=document.getElementById("myDIV").style.top;
    document.getElementById("calendar").style.left=document.getElementById("myDIV").style.left;
    document.getElementById("calendar").style.display="block";
}

function ws4() {
    document.getElementById("myDIV").style.display="none";
    document.getElementById("mainmap").style.top=document.getElementById("myDIV").style.top;
    document.getElementById("mainmap").style.left=document.getElementById("myDIV").style.left;
    document.getElementById("mainmap").style.display="block";
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















