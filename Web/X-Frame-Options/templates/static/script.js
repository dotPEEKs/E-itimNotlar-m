document.addEventListener("DOMContentLoaded", () => {
    const image = document.getElementById('center-image');
    image.addEventListener('click', () => {
        alert('X-Frame-Options ile ilgili güzel bir örnek');
    });
});