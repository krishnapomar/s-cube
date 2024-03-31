function saveAnswer(index) {
    const answer = document.getElementById(`answer-${index}`).value;

    // Send answer to backend to save into MongoDB
    fetch('/save-answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            questionNumber: index + 1,
            answer: answer,
        }),
    }).then(response => {
        if (response.ok) {
            console.log('Answer saved successfully.');
        } else {
            console.error('Failed to save answer.');
        }
    }).catch(error => {
        console.error('Error:', error);
    });
}