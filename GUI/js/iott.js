function Fan() {
    document.getElementById('Fan').style.display = "block";
    
 }
 function Cooler() {
    document.getElementById('Cooler').style.display = "block";
 }

 function Lights() {
    document.getElementById('Lights').style.display = "block";
 }
 function Lock() {
    document.getElementById('Lock').style.display = "block";
 }
 function Music() {
    document.getElementById('Music').style.display = "block";
 }
 function Home() {
    document.getElementById('Home').style.display = "block";
 }
var x;
function changeText(x){
    if(document.getElementById(x).value=="ON")
        {
            document.getElementById(x).value="OFF";
            document.getElementById(x).backgroundImage=url(idea.svg);
        }
    else 
        document.getElementById(x).value="ON";
}
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    output.innerHTML = this.value;
}

function showTime(){
    var date = new Date();
    var h = date.getHours(); // 0 - 23
    var m = date.getMinutes(); // 0 - 59
    var s = date.getSeconds(); // 0 - 59
    var session = "AM";
    
    if(h == 0){
        h = 12;
    }
    
    if(h > 12){
        h = h - 12;
        session = "PM";
    }
    
    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;
    
    var time = h + ":" + m + ":" + s + " " + session;
    document.getElementById("MyClockDisplay").innerText = time;
    document.getElementById("MyClockDisplay").textContent = time;
    
    setTimeout(showTime, 1000);
    
}
