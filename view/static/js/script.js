document.getElementById('routine-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    fetch('/generate', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('routine-result').innerText = data.routine;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('routine-result').innerText = 'Error al generar la rutina.';
    });
});
