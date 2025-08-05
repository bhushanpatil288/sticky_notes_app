const body = document.querySelector("body");
const themeToggle = document.getElementById("themeToggle");

function applyTheme(theme) {
    if (theme === 'light') {
        body.classList.add('light');
        body.classList.remove('bg-dark', 'text-white');
        themeToggle.innerHTML = `
            <span class="ms-5 mt-2">
                <span class="material-symbols-outlined">bedtime</span>
            </span>`;
    } else {
        body.classList.remove('light');
        body.classList.add('bg-dark', 'text-white');
        themeToggle.innerHTML = `
            <span class="ms-5 mt-2">
                <span class="material-symbols-outlined">sunny</span>
            </span>`;
    }
}


const savedTheme = localStorage.getItem('theme') || 'dark';
applyTheme(savedTheme);

themeToggle.addEventListener('click', () => {
    const isLight = body.classList.contains('light');
    const newTheme = isLight ? 'dark' : 'light';
    applyTheme(newTheme);
    localStorage.setItem('theme', newTheme);
});
