/*jshint esversion: 6 */

const nav = document.querySelector('#navbar');
const deliveryBanner = document.querySelector('#delivery-banner');
const themesWrapper = document.querySelector('#theme-options');
const themeSelectors = document.querySelectorAll('.theme-option');

/* Set default theme colours */
let colour1 = '6, 214, 160';
let colour2 = '239, 71, 111';
let colour3 = '255, 209, 102';
let colour4 = '17, 138, 178';
let colour5 = '7, 59, 76';
let darkModeColour = '28, 28, 28';
let lightModeColour = '247, 247, 247';
let darkModeBoxShadowColour = '0, 0, 0';
let lightModeBoxShadowColour = '51, 51, 51';
let theme = "1";
let darkMode = 'false';

/**
 * Toggles the navbar animation when scrolling past a certain screen height
 */
const toggleNavbarBackground = () => {
    nav.classList.toggle('add-navbar-background', window.scrollY > 100);
    deliveryBanner.classList.toggle('add-delivery-banner-background', window.scrollY > 100);
};

window.addEventListener('scroll', toggleNavbarBackground);

document.querySelector('#theme-selector-trigger').addEventListener('click', () => {
    themesWrapper.classList.toggle('translate-left');
});

themeSelectors.forEach(themeSelector => {
    themeSelector.addEventListener('click', () => {
        const themeSelectorClassList = themeSelector.classList;

        if (themeSelectorClassList.contains('theme-1')) {
            sessionStorage.setItem('theme', '1');
            setCSSColour('--colour-1', colour1);
            setCSSColour('--colour-2', colour2);
            setCSSColour('--colour-3', colour3);
            setCSSColour('--colour-4', colour4);
            setCSSColour('--colour-5', colour5);
        } else if (themeSelectorClassList.contains('theme-2')) {
            sessionStorage.setItem("theme", '2');
            setCSSColour('--colour-1', colour2);
            setCSSColour('--colour-2', colour3);
            setCSSColour('--colour-3', colour4);
            setCSSColour('--colour-4', colour5);
            setCSSColour('--colour-5', colour1);
        } else if (themeSelectorClassList.contains('theme-3')) {
            sessionStorage.setItem('theme', '3');
            setCSSColour('--colour-1', colour3);
            setCSSColour('--colour-2', colour4);
            setCSSColour('--colour-3', colour5);
            setCSSColour('--colour-4', colour1);
            setCSSColour('--colour-5', colour2);
        } else if (themeSelectorClassList.contains('theme-4')) {
            sessionStorage.setItem('theme', '4');
            setCSSColour('--colour-1', colour4);
            setCSSColour('--colour-2', colour5);
            setCSSColour('--colour-3', colour1);
            setCSSColour('--colour-4', colour2);
            setCSSColour('--colour-5', colour3);
        } else if (themeSelectorClassList.contains('dark-mode')) {
            let darkModeCheck = sessionStorage.getItem('dark-mode');
            
            if (darkModeCheck === 'false') {
                sessionStorage.setItem('dark-mode', 'true');
                setCSSColour('--body-colour', darkModeColour);
                setCSSColour('--heading-colour', lightModeColour);
                setCSSColour('--box-shadow-colour', darkModeBoxShadowColour);
                document.querySelector('.dark-mode').style.backgroundColor = '#f7f7f7';
            } else {
                sessionStorage.setItem('dark-mode', 'false');
                setCSSColour('--body-colour', lightModeColour);
                setCSSColour('--heading-colour', darkModeColour);
                setCSSColour('--box-shadow-colour', lightModeBoxShadowColour);
                document.querySelector('.dark-mode').style.backgroundColor = '#1c1c1c';
            }
        }
    });
});

/**
 * Sets the colour value as an RGB triplet for a specified
 * CSS variable
 * @param {String} target The CSS variable to be targeted
 * @param {String} colour The RGB values for the CSS variable's value
 */
const setCSSColour = (target, colour) => {
    document.documentElement.style.setProperty(target, colour);
};

/**
 * Gets the current theme and whether dark mode is enabled
 * from session storage
 */
const getTheme = () => {
    theme = sessionStorage.getItem('theme');
    darkMode = sessionStorage.getItem('dark-mode');
};

/**
 * Sets the CSS colour variables to the relevant values
 * depending on theme and dark or light mode
 */
const setTheme = () => {
    switch(theme) {
        case '1':
            setCSSColour('--colour-1', colour1);
            setCSSColour('--colour-2', colour2);
            setCSSColour('--colour-3', colour3);
            setCSSColour('--colour-4', colour4);
            setCSSColour('--colour-5', colour5);
            break;
        case '2':
            setCSSColour('--colour-1', colour2);
            setCSSColour('--colour-2', colour3);
            setCSSColour('--colour-3', colour4);
            setCSSColour('--colour-4', colour5);
            setCSSColour('--colour-5', colour1);
            break;
        case '3':
            setCSSColour('--colour-1', colour3);
            setCSSColour('--colour-2', colour4);
            setCSSColour('--colour-3', colour5);
            setCSSColour('--colour-4', colour1);
            setCSSColour('--colour-5', colour2);
            break;
        case '4':
            setCSSColour('--colour-1', colour4);
            setCSSColour('--colour-2', colour5);
            setCSSColour('--colour-3', colour1);
            setCSSColour('--colour-4', colour2);
            setCSSColour('--colour-5', colour3);
            break;
        default:
            setCSSColour('--colour-1', colour1);
            setCSSColour('--colour-2', colour2);
            setCSSColour('--colour-3', colour3);
            setCSSColour('--colour-4', colour4);
            setCSSColour('--colour-5', colour5);
    }

    if (darkMode === 'true') {
        setCSSColour('--body-colour', darkModeColour);
        setCSSColour('--heading-colour', lightModeColour);
        setCSSColour('--box-shadow-colour', darkModeBoxShadowColour);
    } else {
        setCSSColour('--body-colour', lightModeColour);
        setCSSColour('--heading-colour', darkModeColour);
        setCSSColour('--box-shadow-colour', lightModeBoxShadowColour);
    }
};

window.addEventListener('DOMContentLoaded', () => {
    getTheme();
    setTheme();
});