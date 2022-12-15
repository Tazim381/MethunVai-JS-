document.getElementById("tablee").hidden = true;
var list1 = [];
var list2 = [];
var list3 = [];
var list4 = [];
var list5 = [];
var n = 1;
var x = 0;
function tazim() {
  document.getElementById("tablee").hidden = false;
  document.getElementById("form").hidden = true;
  var addrw = document.getElementById("table");
  var newrw = addrw.insertRow(n);
  list1[x] = document.getElementById("id");
  list2[x] = document.getElementById("name").value;
  list3[x] = document.getElementById("textarea").value;
  list4[x] = document.getElementById("date").value;
  list5[x] = document.getElementById("myfile").value;

  var cel1 = newrw.insertCell(0);
  var cel2 = newrw.insertCell(1);
  var cel3 = newrw.insertCell(2);
  var cel4 = newrw.insertCell(3);
  var cel5 = newrw.insertCell(4);

  cel1.innerHTML = list1[x].value;
  cel2.innerHTML = list2[x];
  cel3.innerHTML = list3[x];
  cel4.innerHTML = list4[x];
  var z = list5[x].split("fakepath\\").pop();
  cel5.innerHTML =
    '<img src="image/' + z + '"style="width:150px;height:150px;"/>';
  x++;
  n++;
  document.getElementById("output").innerHTML = "Output Form";
}

function myFunction() {
  document.getElementById("tabl").reset();
}

function back() {
  document.getElementById("tablee").hidden = true;
  document.getElementById("form").hidden = false;
}
