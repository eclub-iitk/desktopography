
function calc(){
    var a = parseInt(document.querySelector("#value1").value);
    var b = parseInt(document.querySelector("#value1").value);
    var op = document.querySelector("#operator").value;
    var calculate;

    if(op=="add"){
        calculate = a+b;
    }
    else if(op=="min"){
        calculate = a-b;
    }
    else if(op=="div"){
        calculate = a/b;
    }
    else if(op=="mul"){
        calculate = a*b;
    }
document.querySelector("#result").innerHTML = calculate;

}

function insert(num){
    document.form.textview.value=document.form.textview.value+ num;
}