const input = document.getElementById('enterAnswer')
const button = document.getElementById("buttonAnswer")
input.addEventListener("input", () => {
    // Якщо є хоч один символ - кнопка активується
    if(input.value.trim() == ""){
        button.disabled = true;

    }
    else{
        button.disabled = false;
    }
    
});