fetch('http://localhost:5000/api')
    .then(response => response.json())
    .then(data => {
        document.getElementById('apiMessage').innerText = data.message;
    })
    .catch(error => console.error('Error:', error));
