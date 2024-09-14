
/* Toggles navbar if pressed while in mobile view (just make window narrow for mobile view) */
const menu = document.querySelector('#mobile-menu')
const menu_links = document.querySelector(".navbar__menu")

menu.addEventListener('click', function() {
    menu.classList.toggle('is-active');
    menu_links.classList.toggle('active');
})

