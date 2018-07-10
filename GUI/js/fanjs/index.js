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