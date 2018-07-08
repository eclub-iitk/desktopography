$(document).ready(function(){
	var weekdays=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
	var months=["January","Februray","March","April","May","June","July","August","September","October","November","December"];
		setInterval(function(){
		var d=new Date();
		var day=d.getDay();
		var day_name=weekdays[day];
		var num=d.getDate();
		var mo=d.getMonth();
		var name=months[mo];
				$(".month-name").html(name.substring(0,3));
		$(".number").html(num);
		//$(".day").html(day_name);
		$(".monthtwo").html(name+" "+num);
		$(".daytwo").html(day_name);
		var minute=d.getMinutes();
		var hour=d.getHours();
		var sec=d.getSeconds();
		var secMinMeter=300/60;
		$(".hours").css("width",hour*12.5+"px");
		if(hour<10){
			$(".hour").html("0"+hour+":")
		}
		else if(hour>12){
			hour=hour-12;
			if(hour<10){
				$(".hour").html("0"+hour+":");
			}
		}
		else{
			$(".hour").html(hour+":");
		}
		if(minute<10){
			$(".min").html("0"+minute+":");
			$(".minutes").css("width",minute*5+"px");
		}
		else{
			$(".min").html(minute+":");
			$(".minutes").css("width",minute*5+"px");
		}
		if(sec<10){
			$(".sec").html("0"+sec);
			$(".seconds").css("width",sec*5+"px");
		}
		else{
			$(".sec").html(sec);
			$(".seconds").css("width",sec*5+"px");
		}
	},1000)
})