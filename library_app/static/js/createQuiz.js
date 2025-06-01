const createBtn = document.getElementById('createQuiz');
const quizCreate = document.getElementById('quizCreate').value;



console.log(document.cookie.split("; ")[1])
createBtn.addEventListener('click', () => {
    if (document.cookie.split("; ")[1]){
        
    }
    else {
        document.cookie =  `draft=${quizCreate}; path=/;`;
    }
});