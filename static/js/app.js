/*jshint esversion: 6 */

const toggleNavbarBackground = () => {
    const nav = document.querySelector('#navbar');
    const deliveryBanner = document.querySelector('#delivery-banner');
    nav.classList.toggle('add-navbar-background', window.scrollY > 300);
    deliveryBanner.classList.toggle('add-delivery-banner-background', window.scrollY > 300);
};

window.addEventListener('scroll', toggleNavbarBackground);