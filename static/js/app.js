/*jshint esversion: 6 */

/* Grabbing elements and storing them in variables */
const nav = document.querySelector('#navbar');
const deliveryBanner = document.querySelector('#delivery-banner');
const themesWrapper = document.querySelector('#theme-options');
const themeSelectors = document.querySelectorAll('.theme-option');

/* Set default theme colours */
let green = '6, 214, 160';
let pink = '239, 71, 111';
let yellow = '255, 209, 102';
let lightBlue = '17, 138, 178';
let darkBlue = '7, 59, 76';
let darkModeColour = '28, 28, 28';
let lightModeColour = '247, 247, 247';
let darkModeBoxShadowColour = '0, 0, 0';
let lightModeBoxShadowColour = '51, 51, 51';

/* Set default theme and whether dark mode is enabled */
let theme = "1";
let darkMode = 'false';

/**
 * Toggles the navbar animation when scrolling past a certain screen height
 */
const toggleNavbarBackground = () => {
    nav.classList.toggle('add-navbar-background', window.scrollY > 100);
    deliveryBanner.classList.toggle('add-delivery-banner-background', window.scrollY > 100);
};

/* Event listener which calls toggleNavbarBackground to change the navbar background on scroll */
window.addEventListener('scroll', toggleNavbarBackground);

/* Event listener which toggles the theme options animation when the themes button is clicked */
document.querySelector('#theme-selector-trigger').addEventListener('click', () => {
    themesWrapper.classList.toggle('translate-left');
});

/**
 * Listens for click event on theme buttons 
 * and sets the selected theme accordingly. 
 * This includes setting dark mode.
 */
themeSelectors.forEach(themeSelector => {
    themeSelector.addEventListener('click', () => {
        const themeSelectorClassList = themeSelector.classList;

        if (themeSelectorClassList.contains('theme-1')) {
            sessionStorage.setItem('theme', '1');
            setThemeColours(green, pink, yellow, lightBlue, darkBlue);
        } else if (themeSelectorClassList.contains('theme-2')) {
            sessionStorage.setItem("theme", '2');
            setThemeColours(pink, yellow, lightBlue, darkBlue, green);
        } else if (themeSelectorClassList.contains('theme-3')) {
            sessionStorage.setItem('theme', '3');
            setThemeColours(yellow, lightBlue, darkBlue, green, pink);
        } else if (themeSelectorClassList.contains('theme-4')) {
            sessionStorage.setItem('theme', '4');
            setThemeColours(lightBlue, darkBlue, green, pink, yellow);
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
 * Sets the CSS colour variable values to the supplied
 * RGB triplet values to set the theme colours
 * @param {String} colour1 the RGB triplet values for the primary colour
 * @param {String} colour2 the RGB triplet values for the secondary colour
 * @param {String} colour3 the RGB triplet values for the tertiary colour
 * @param {String} colour4 the RGB triplet values for the quarternary colour
 * @param {String} colour5 the RGB triplet values for the quinary colour
 */
const setThemeColours = (colour1, colour2, colour3, colour4, colour5) => {
    setCSSColour('--colour-1', colour1);
    setCSSColour('--colour-2', colour2);
    setCSSColour('--colour-3', colour3);
    setCSSColour('--colour-4', colour4);
    setCSSColour('--colour-5', colour5);
};

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
            setThemeColours(green, pink, yellow, lightBlue, darkBlue);
            break;
        case '2':
            setThemeColours(pink, yellow, lightBlue, darkBlue, green);
            break;
        case '3':
            setThemeColours(yellow, lightBlue, darkBlue, green, pink);
            break;
        case '4':
            setThemeColours(lightBlue, darkBlue, green, pink, yellow);
            break;
        default:
            setThemeColours(green, pink, yellow, lightBlue, darkBlue);
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

/**
 * Checks which theme is loaded whenever a page refreshes 
 * and ensures the theme selection persists by setting the 
 * theme again on page reload.
 */
window.addEventListener('DOMContentLoaded', () => {
    getTheme();
    setTheme();
});