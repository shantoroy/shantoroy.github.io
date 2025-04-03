// Global variables
let currentCertification = null;
let currentQuestionIndex = 0;
let selectedAnswers = [];
let answersChecked = false;
let currentQuestions = [];

// Application states
const APP_STATE = {
    HOME: 'home',
    EXAM: 'exam'
};
let currentState = APP_STATE.HOME;

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    initializeCertGrid();
    setupEventListeners();
});

// Initialize the certification grid for the homepage
function initializeCertGrid() {
    const certGrid = document.getElementById('cert-grid');
    
    // Create a card for each certification
    Object.keys(certifications).forEach(certId => {
        const cert = certifications[certId];
        
        const cardDiv = document.createElement('div');
        cardDiv.classList.add('cert-card');
        cardDiv.setAttribute('data-cert-id', certId);
        
        cardDiv.innerHTML = `
            <h4>${cert.name}</h4>
            <p>Practice exam questions to help you prepare for the ${cert.name} certification.</p>
            <div class="cert-card-footer">
                <button class="btn btn-primary start-exam-btn">Start Practice</button>
            </div>
        `;
        
        cardDiv.addEventListener('click', () => selectCertification(certId));
        certGrid.appendChild(cardDiv);
    });
}

// Set up event listeners for buttons
function setupEventListeners() {
    document.getElementById('check-btn').addEventListener('click', checkAnswer);
    document.getElementById('next-btn').addEventListener('click', nextQuestion);
    document.getElementById('prev-btn').addEventListener('click', prevQuestion);
}

// Go back to the home page
function goToHome() {
    // Reset state
    currentState = APP_STATE.HOME;
    currentCertification = null;
    currentQuestionIndex = 0;
    currentQuestions = [];
    selectedAnswers = [];
    answersChecked = false;
    
    // Update UI
    document.getElementById('question-nav').style.display = 'none';
    document.getElementById('home-container').style.display = 'block';
    document.getElementById('question-container').style.display = 'none';
    document.getElementById('nav-buttons').style.display = 'none';
    document.getElementById('progress-container').style.display = 'none';
    
    // Update titles
    document.getElementById('main-title').textContent = 'Certification Exam Practice';
    document.getElementById('cert-title').textContent = '';
}

// Select a certification and load its questions
async function selectCertification(certId) {
    // Update state
    currentState = APP_STATE.EXAM;
    currentCertification = certId;
    
    // Show loading state
    document.getElementById('question-container').innerHTML = '<div class="text-center p-5"><div class="spinner-border" role="status"></div><p class="mt-3">Loading questions...</p></div>';
    document.getElementById('question-container').style.display = 'block';
    document.getElementById('home-container').style.display = 'none';
    document.getElementById('nav-buttons').style.display = 'flex';
    document.getElementById('progress-container').style.display = 'block';
    
    // Update UI for exam mode
    document.getElementById('question-nav').style.display = 'block';
    
    // Clear previous question list
    document.getElementById('question-list').innerHTML = '';
    
    // Update titles
    document.getElementById('main-title').textContent = 'Exam Practice';
    document.getElementById('cert-title').textContent = certifications[certId].name;
    
    try {
        // Load questions for this certification
        currentQuestions = await loadCertificationQuestions(certId);
        
        // Build question navigation
        buildQuestionNav(currentQuestions);
        
        // Reset question index and render first question
        currentQuestionIndex = 0;
        selectedAnswers = [];
        answersChecked = false;
        
        // Enable check button
        document.getElementById('check-btn').disabled = false;
        
        // Render the first question
        renderQuestion(currentQuestionIndex);
    } catch (error) {
        document.getElementById('question-container').innerHTML = `
            <div class="alert alert-danger" role="alert">
                <h4 class="alert-heading">Error Loading Questions</h4>
                <p>Failed to load questions for this certification. Please try again later.</p>
                <hr>
                <p class="mb-0">Error details: ${error.message}</p>
            </div>
        `;
    }
}

// Build the question navigation in the left panel
function buildQuestionNav(questions) {
    const questionList = document.getElementById('question-list');
    questionList.innerHTML = '';
    
    questions.forEach((question, index) => {
        const listItem = document.createElement('a');
        listItem.classList.add('list-group-item', 'list-group-item-action');
        listItem.setAttribute('data-question-index', index);
        
        // Create a preview of the question with ellipsis
        const questionPreview = question.text.length > 30 
            ? question.text.substring(0, 30) + '...' 
            : question.text;
            
        listItem.innerHTML = `
            <div class="question-num">Q${index + 1}.</div>
            <div class="question-preview">${questionPreview}</div>
        `;
        
        listItem.addEventListener('click', () => {
            // if (answersChecked || confirm('You haven\'t checked your answer. Are you sure you want to move to another question?')) {
                jumpToQuestion(index);
            // }
        });
        
        questionList.appendChild(listItem);
    });
}

// Jump to a specific question by index
function jumpToQuestion(index) {
    if (index >= 0 && index < currentQuestions.length) {
        currentQuestionIndex = index;
        selectedAnswers = [];
        answersChecked = false;
        renderQuestion(currentQuestionIndex);
        
        // Update active state in question nav
        const questionItems = document.querySelectorAll('#question-list .list-group-item');
        questionItems.forEach(item => {
            item.classList.remove('active');
        });
        const activeItem = document.querySelector(`#question-list [data-question-index="${index}"]`);
        if (activeItem) {
            activeItem.classList.add('active');
        }
    }
}

// Function to convert plain text URLs into clickable links
function makeUrlsClickable(text) {
    // Regular expression to match URLs starting with https
    const urlRegex = /(https:\/\/[^\s]+)/g;
    
    // Replace URLs with anchor tags
    return text.replace(urlRegex, function(url) {
        return `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>`;
    });
}

// Modified renderQuestion function with URL conversion
function renderQuestion(index) {
    if (!currentCertification || currentQuestions.length === 0) return;
    
    const question = currentQuestions[index];
    const questionContainer = document.getElementById('question-container');
    
    // Reset for new question
    selectedAnswers = [];
    answersChecked = false;
    
    // Generate HTML for the question
    let questionHTML = `
        <h4 class="mb-3">Question ${index + 1}/${currentQuestions.length}</h4>
        <p class="mb-4">${question.text}</p>
    `;
    
    if (question.multipleSelect) {
        questionHTML += `<p class="text-muted mb-3"><em>Select all that apply</em></p>`;
    }
    
    questionHTML += `<div class="options-container">`;
    
    question.options.forEach(option => {
        const inputType = question.multipleSelect ? 'checkbox' : 'radio';
        questionHTML += `
            <label class="option-label" data-option-id="${option.id}">
                <input type="${inputType}" name="question${question.id}" value="${option.id}" class="me-2">
                ${option.text}
            </label>
        `;
    });
    
    // Convert URLs in explanation to clickable links
    const explanationWithLinks = makeUrlsClickable(question.explanation);
    
    questionHTML += `</div>
        <div id="explanation" class="explanation">${explanationWithLinks}</div>
    `;
    
    questionContainer.innerHTML = questionHTML;
    
    // Update progress bar
    const progressBar = document.getElementById('progress-bar');
    const progress = ((index + 1) / currentQuestions.length) * 100;
    progressBar.style.width = `${progress}%`;
    progressBar.setAttribute('aria-valuenow', progress);
    
    // Add option selection handlers
    const optionLabels = document.querySelectorAll('.option-label');
    optionLabels.forEach(label => {
        label.addEventListener('click', function() {
            const optionId = this.getAttribute('data-option-id');
            const input = this.querySelector('input');
            
            if (question.multipleSelect) {
                // For checkboxes
                if (input.checked) {
                    selectedAnswers = selectedAnswers.filter(id => id !== optionId);
                    input.checked = false;
                    this.classList.remove('selected');
                } else {
                    selectedAnswers.push(optionId);
                    input.checked = true;
                    this.classList.add('selected');
                }
            } else {
                // For radio buttons
                selectedAnswers = [optionId];
                document.querySelectorAll('.option-label').forEach(l => {
                    l.classList.remove('selected');
                });
                this.classList.add('selected');
                input.checked = true;
            }
        });
    });
    
    // Enable/disable navigation buttons
    document.getElementById('prev-btn').disabled = index === 0;
    document.getElementById('next-btn').disabled = index === currentQuestions.length - 1 || !answersChecked;
    document.getElementById('check-btn').disabled = false;
    
    // Update active question in left panel
    const questionItems = document.querySelectorAll('#question-list .list-group-item');
    questionItems.forEach(item => {
        item.classList.remove('active');
    });
    const activeItem = document.querySelector(`#question-list [data-question-index="${index}"]`);
    if (activeItem) {
        activeItem.classList.add('active');
        // Ensure the active question is visible by scrolling to it
        activeItem.scrollIntoView({ block: 'nearest' });
    }
}

// Check if the selected answers are correct
function checkAnswer() {
    if (!currentCertification || currentQuestions.length === 0) return;
    
    if (selectedAnswers.length === 0) {
        alert('Please select an answer first.');
        return;
    }
    
    const question = currentQuestions[currentQuestionIndex];
    const correctAnswers = question.correctAnswers;
    const explanation = document.getElementById('explanation');
    
    // // Check if answers are correct
    // const optionLabels = document.querySelectorAll('.option-label');
    // optionLabels.forEach(label => {
    //     const optionId = label.getAttribute('data-option-id');
    //     const isSelected = selectedAnswers.includes(optionId);
    //     const isCorrect = correctAnswers.includes(optionId);
        
    //     if (isSelected && isCorrect) {
    //         label.classList.add('correct');
    //     } else if (isSelected && !isCorrect) {
    //         label.classList.add('incorrect');
    //     } else if (!isSelected && isCorrect) {
    //         label.classList.add('correct');
    //     }
    // });

    // Check if answers are correct
    const optionLabels = document.querySelectorAll('.option-label');
    let allCorrect = true; // Flag to track if all selections are correct

    optionLabels.forEach(label => {
        const optionId = label.getAttribute('data-option-id');
        const isSelected = selectedAnswers.includes(optionId);
        const isCorrect = correctAnswers.includes(optionId);
        
        if (isSelected && isCorrect) {
            label.classList.add('correct');
        } else if (isSelected && !isCorrect) {
            label.classList.add('incorrect');
            allCorrect = false; // User selected a wrong answer
        } else if (!isSelected && isCorrect) {
            label.classList.add('correct');
            allCorrect = false; // User missed a correct answer
        }
    });
    
    // Show explanation
    explanation.style.display = 'block';
    
    // Disable options and check button
    optionLabels.forEach(label => {
        const input = label.querySelector('input');
        input.disabled = true;
    });
    
    document.getElementById('check-btn').disabled = true;
    document.getElementById('next-btn').disabled = currentQuestionIndex === currentQuestions.length - 1;
    answersChecked = true;
    
    // // Update visual indicator in question list to show this question was answered
    // const questionItem = document.querySelector(`#question-list [data-question-index="${currentQuestionIndex}"]`);
    // if (questionItem) {
    //     questionItem.style.borderLeft = '4px solid #28a745';
    // }

    // Update visual indicator in question list to show this question was answered correctly/incorrectly
    const questionItem = document.querySelector(`#question-list [data-question-index="${currentQuestionIndex}"]`);
    if (questionItem) {
        const borderColor = allCorrect ? '#28a745' : '#dc3545'; // Green for correct, red for incorrect
        questionItem.style.borderLeft = `4px solid ${borderColor}`;
    }
}


// Function to check if the user's answer is correct
function checkIfAnswerIsCorrect() {
    const currentQuestion = currentQuestions[currentQuestionIndex];
    
    // Get user's selected answers
    let userAnswers = [];
    
    if (currentQuestion.multipleSelect) {
        // For multiple select questions, gather all checked options
        const checkboxes = document.querySelectorAll('.correct-multi:checked');
        userAnswers = Array.from(checkboxes).map(checkbox => checkbox.value);
    } else {
        // For single select questions, get the selected radio value
        const selectedRadio = document.querySelector('input[name="option"]:checked');
        if (selectedRadio) {
            userAnswers = [selectedRadio.value];
        }
    }
    
    // No answer selected
    if (userAnswers.length === 0) {
        return false;
    }
    
    // Check if arrays have the same elements (regardless of order)
    if (userAnswers.length !== currentQuestion.correctAnswers.length) {
        return false;
    }
    
    // Sort both arrays to compare them easily
    const sortedUserAnswers = [...userAnswers].sort();
    const sortedCorrectAnswers = [...currentQuestion.correctAnswers].sort();
    
    // Compare each element
    for (let i = 0; i < sortedUserAnswers.length; i++) {
        if (sortedUserAnswers[i] !== sortedCorrectAnswers[i]) {
            return false;
        }
    }
    
    return true;
}


// Move to the next question
function nextQuestion() {
    if (!currentCertification || currentQuestions.length === 0) return;
    
    if (currentQuestionIndex < currentQuestions.length - 1 && answersChecked) {
        currentQuestionIndex++;
        renderQuestion(currentQuestionIndex);
    }
}

// Move to the previous question
function prevQuestion() {
    if (!currentCertification || currentQuestions.length === 0) return;
    
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        renderQuestion(currentQuestionIndex);
    }
}