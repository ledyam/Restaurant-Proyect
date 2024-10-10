document.getElementById('book-a-table-form').addEventListener('submit', function(event) {
event.preventDefault();

const formData = new FormData(this);
const formObject = Object.fromEntries(formData.entries());

fetch('/Restaurant-Proyect/index.html#book-a-table', {
method: 'POST',
headers: {
'Content-Type': 'application/json'
},
body: JSON.stringify(formObject)
})
.then(response => response.json())
.then(data => {
document.getElementById('form-response').innerText = 'Reserva realizada con éxito';
})
.catch(error => {


});
});
