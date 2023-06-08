fetch('http://localhost:5000/api')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
