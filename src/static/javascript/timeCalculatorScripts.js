document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', async function (event) {
        event.preventDefault();
        const formData = new FormData(form);
        const response = await fetch('/calculate-time', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        const resultDiv = document.getElementById('result');
        resultDiv.textContent = 'Clock-Off Time: ' + data.result;
    });
});
