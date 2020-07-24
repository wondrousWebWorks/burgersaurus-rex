/*jshint esversion: 6 */

const themesWrapper = document.querySelector('#theme-options');
const themeSelectors = document.querySelectorAll('.theme-option');

/* Set default theme colours */
let colour1 = '6, 214, 160';
let colour2 = '239, 71, 111';
let colour3 = '255, 209, 102';
let colour4 = '17, 138, 178';
let colour5 = '7, 59, 76';
let darkModeColor = '28, 28, 28';

/**
 * Toggles the navbar animation when scrolling past a certain screen height
 */
const toggleNavbarBackground = () => {
    const nav = document.querySelector('#navbar');
    const deliveryBanner = document.querySelector('#delivery-banner');
    nav.classList.toggle('add-navbar-background', window.scrollY > 300);
    deliveryBanner.classList.toggle('add-delivery-banner-background', window.scrollY > 300);
};

window.addEventListener('scroll', toggleNavbarBackground);


document.querySelector('#theme-selector-trigger').addEventListener('click', () => {
    themesWrapper.classList.toggle('translate-left');
});

themeSelectors.forEach(themeSelector => {
    themeSelector.addEventListener('click', () => {
        const themeSelectorClassList = themeSelector.classList;

        if (themeSelectorClassList.contains('theme-1')) {
            sessionStorage.setItem("theme", "1");
            document.documentElement.style.setProperty('--colour-1', '6, 214, 160');
            document.documentElement.style.setProperty('--colour-2', '239, 71, 111');
            document.documentElement.style.setProperty('--colour-3', '255, 209, 102');
            document.documentElement.style.setProperty('--colour-4', '17, 138, 178');
            document.documentElement.style.setProperty('--colour-5', '7, 59, 76');
        } else if (themeSelectorClassList.contains('theme-2')) {
            sessionStorage.setItem("theme", "2");
            document.documentElement.style.setProperty('--colour-2', '6, 214, 160');
            document.documentElement.style.setProperty('--colour-3', '239, 71, 111');
            document.documentElement.style.setProperty('--colour-4', '255, 209, 102');
            document.documentElement.style.setProperty('--colour-5', '17, 138, 178');
            document.documentElement.style.setProperty('--colour-1', '7, 59, 76');
        } else if (themeSelectorClassList.contains('theme-3')) {
            sessionStorage.setItem("theme", "3");
            document.documentElement.style.setProperty('--colour-3', '6, 214, 160');
            document.documentElement.style.setProperty('--colour-4', '239, 71, 111');
            document.documentElement.style.setProperty('--colour-5', '255, 209, 102');
            document.documentElement.style.setProperty('--colour-1', '17, 138, 178');
            document.documentElement.style.setProperty('--colour-2', '7, 59, 76');
        } else if (themeSelectorClassList.contains('theme-4')) {
            sessionStorage.setItem("theme", "4");
            document.documentElement.style.setProperty('--colour-4', '6, 214, 160');
            document.documentElement.style.setProperty('--colour-5', '239, 71, 111');
            document.documentElement.style.setProperty('--colour-1', '255, 209, 102');
            document.documentElement.style.setProperty('--colour-2', '17, 138, 178');
            document.documentElement.style.setProperty('--colour-3', '7, 59, 76');
        } else if (themeSelectorClassList.contains('dark-mode')) {
            sessionStorage.setItem("dark-mode", "true");
            document.documentElement.style.setProperty('--body-colour', darkModeColor);
        }
    });
});

const getTheme = () => {
    const targetUrl = `/content/get-theme/`;
    const csrfToken = "{{ csrf_token }}";

    fetch(targetUrl, {
        method: "get",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": csrfToken,
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
    }).then(response => {
        return response.json();
    }).then(data => {
        colour1 = hexToRgb(data.colour_1);
        colour2 = hexToRgb(data.colour_2);
        colour3 = hexToRgb(data.colour_3);
        colour4 = hexToRgb(data.colour_4);
        colour5 = hexToRgb(data.colour_5);
        darkModeColor = hexToRgb(data.dark_mode_colour);
    }).catch(error => {
        console.log("Something went wrong!", error);
    });
};

const checkTheme = () => {
    const darkMode = sessionStorage.getItem('dark-mode');

    if (darkMode === 'true') {
        document.documentElement.style.setProperty('--body-colour', '10, 10, 10');
    }
};

/**
 * Converts a hex colour value to RGB
 * @param {String} hex A hexidecimal colour value
 */
const hexToRgb = hex =>{
    const bigint = parseInt(hex, 16);
    const r = (bigint >> 16) & 255;
    const g = (bigint >> 8) & 255;
    const b = bigint & 255;

    return `${r}, ${g}, ${b}`;
};

document.addEventListener("DOMContentLoaded", () => {
    getTheme();
    checkTheme();
});