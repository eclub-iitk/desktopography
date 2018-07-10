var switchBody = document.getElementById("switch");
//"hsl(238, 50%, 12%)";

switchBody.addEventListener("click", toggle);

function toggle(){
  switchBody.classList.toggle("off");
  
   document.body.style.transition="background-color 2s";
  
  if(switchBody.classList.contains("off")){
    document.body.style.backgroundColor="rgb(10, 11, 31)";
    
  }
  else{
    document.body.style.backgroundColor="rgb(135, 206, 250)";
  }
  // rgb(31, 31, 31)
  // rgb(255, 255, 255)
}