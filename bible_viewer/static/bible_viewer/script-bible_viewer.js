$(document).ready(function() {
          $("#date").datepicker({
            dateFormat: "dd-mm-yy",
            constrainInput: true,
            onClose: function (selectedDate) {
                location.href = '/NLT2013/' + selectedDate;
            }
          });
        });


var elements = document.getElementsByClassName("footnote");
for(var x=0; x < elements.length; x++)
{
	elements[x].innerHTML = '[' + String.fromCharCode(97+x) + ']';
	elements[x].style.color = "blue";
}