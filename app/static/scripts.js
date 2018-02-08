// scripts.js

var counter = 'Unknown';

var xhr = new XMLHttpRequest();

xhr.onload = function (e) {
  if (xhr.readyState === 4) {
    if (xhr.status === 200) {
      counter = xhr.responseText;
    } else {
      console.error(xhr.statusText);
      counter = 'Unknown'
    }
  }
};

xhr.onerror = function (e) {
  console.error(xhr.statusText);
};

setInterval(function () {  

  xhr.open("GET", "http://127.0.0.1:5000/testendpoint", true);
  xhr.send(null);
  document.getElementById('demo').innerHTML = counter

}, 2000);
