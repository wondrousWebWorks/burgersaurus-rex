/*jshint esversion: 6 */

const toggleNavbarBackground = () => {
    const nav = document.querySelector('#navbar');
    const deliveryBanner = document.querySelector('#delivery-banner');
    nav.classList.toggle('add-navbar-background', window.scrollY > 300);
    deliveryBanner.classList.toggle('add-delivery-banner-background', window.scrollY > 300);
};

window.addEventListener('scroll', toggleNavbarBackground);

// document.documentElement.style.setProperty('--colour-1', '7, 59, 76');
// document.documentElement.style.setProperty('--colour-2', '6, 214, 160');
// document.documentElement.style.setProperty('--colour-3', '239, 71, 111');
// document.documentElement.style.setProperty('--colour-4', '255, 209, 102');
// document.documentElement.style.setProperty('--colour-5', '17, 138, 178');
// document.documentElement.style.setProperty('--body-colour', '10, 10, 10');