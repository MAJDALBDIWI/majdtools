fetch('/translate', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        text: document.getElementById('text').value,
        target_language: document.getElementById('target_language').value
    })
})
.then(response => response.json())
.then(data => {
    document.getElementById('translation').innerHTML = data.translation;
})
.catch(error => console.error(error));
