$(document).ready(function() {
          $("#date").datepicker({
            dateFormat: "dd-mm-yy",
            constrainInput: false
          });
        });

var elements = document.getElementsByClassName("footnote");
for(var x=0; x < elements.length; x++)
{
	elements[x].innerHTML = '[' + String.fromCharCode(97+x) + ']';
	elements[x].style.color = "blue";
}