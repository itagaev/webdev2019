window.onload = function(){

var toDoList = [];

document.getElementById('btn').addEventListener('click', function(){
  var input = document.getElementById("myInput").value;
  var obj = {};
  obj.task = input;
  obj.check = false;
  var i = toDoList.length;
  toDoList[i] = obj;
  console.log(obj);
  out();
});

function out(){
  var out = "";
  for(var key in toDoList){
    if(toDoList[key].chech == true){
      out += '<input type="checkbox" checked>';
    }else {
      out += '<input type="checkbox">';
    }
    out += toDoList[key].task + '<br>';
  }
  document.getElementById('out').innerHTML = out;
}

}



var timer = setInterval(tick, 1000);


function tick(){
  var date = new Date();
  var h = date.getHours();
  var m = date.getMinutes();
  var s = date.getSeconds();

  document.getElementById('clock').innerHTML = "<h1>" + h + ":" + m + ":" + s + "</h1>";
}
