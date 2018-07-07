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

$( function() {
  $("button").on('click', function() {
  	  $("button").removeClass("current");
      $(this).addClass("current");
      
      var speed = $(this).data("speed");
      
      if(speed === "paused") {
          $(".circle").css("animation-play-state", "paused");
      } else {
          $(".circle").css({ 
              animationPlayState: "running",
              animationDuration: speed
          });
      }
  });
});
