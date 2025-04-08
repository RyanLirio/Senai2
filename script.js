const dropdown = document.querySelector('.dropdown');
const submenu = document.querySelector('.submenu');

dropdown.addEventListener('mouseenter', () => {
    submenu.style.display = 'block';
    setTimeout(() => {
        submenu.style.opacity = '1';
        submenu.style.transform = 'translateY(0)';
    }, 10);
})
dropdown.addEventListener('mouseleave', () => {
    submenu.style.opacity = '0';
    submenu.style.transform = 'translateY(-10px)';
    setTimeout(() => {
        submenu.style.display ='none';
    }, 300);
});