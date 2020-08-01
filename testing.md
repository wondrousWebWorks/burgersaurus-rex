# Testing & Bugs

- [Testing & Bugs](#testing--bugs)
  - [Testing](#testing)
    - [HTML Validation](#html-validation)
    - [Responsiveness](#responsiveness)
      - [Desired Result](#desired-result)
      - [Steps Taken to Ensure Result](#steps-taken-to-ensure-result)
      - [Verdict](#verdict)
  - [Behaviour of site components](#behaviour-of-site-components)
    - [Navbar](#navbar)
  - [Behaviour of individual pages](#behaviour-of-individual-pages)
    - [Home page](#home-page)
  - [Bugs](#bugs)
    - [Development Bugs](#development-bugs)
      - [Checkout Issue for Non-Authenticated Users](#checkout-issue-for-non-authenticated-users)
      - [Navbar Displayed Wider Than Screen Width on Mobile Devices](#navbar-displayed-wider-than-screen-width-on-mobile-devices)
      - [Dark and Light Mode Text Colour Change in Menu App](#dark-and-light-mode-text-colour-change-in-menu-app)

## Testing

Manual testing was performed for this project due to time constraints.

### HTML Validation

The deployed site was run through an online [HTML validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fburgersaurus-rex.herokuapp.com%2F), and though warnings were returned for content within `article` and `section` tags not having headings, it was considered not to be important as these sections were designed not to have them.

### Responsiveness

#### Desired Result

The site is displayed on any screen size without compromising legibility and eliminating screen and element overflow.

#### Steps Taken to Ensure Result

Bootstrap was used as a library to create Burgersaurus Rex. In particular, its grid system was used extensively to ensure responsiveness on any screen size. It proved necessary to use CSS media queries to display the content as intended on mobile and tablet devices.

In addition to testing using responsiveness using Chrome Developer Tools Microsoft Edge Developer Tools and Firefox Developer Tools, these physical devices were also used for testing:

- Sony Xperia Xa2
- Samsung J5, Galaxy S10 Lite
- Apple iPhone X, iPad Pro
- Amazon Fire HD 7 Inch tablet
- Dell Inspiron 5490 Laptop

#### Verdict

The app adapts to all tested screen sizes and devices and displays as expected. :heavy_check_mark:

## Behaviour of site components

### Navbar

- 

## Behaviour of individual pages

### Home page

## Bugs

### Development Bugs

#### Checkout Issue for Non-Authenticated Users

- **Bug**

    Non-authenticated users couldn't complete the checkout process. A misconfiguration in `stripe-elements.js` resulted in the *save_info* checkbox in the checkout form's value was required as `true` or `false` when creating the Stripe payment intent. The was targeting the checkbox element and trying to determine it's value regardless of whether it was being displayed for authenticated users or not. This resulted in a value of `undefined` instead of the expected `true` or `false`.

- **Fix**

    I added an if statement in `stripe-elements.js` to determine whether the checkbox element exists before trying to check its status and to set the value explicitly as `false` if no checkbox is found.

- **Verdict**

    This bug was squashed and the checkout process now works for authenticated and non-authenticated users.

#### Navbar Displayed Wider Than Screen Width on Mobile Devices

- **Bug**

    The position of the **Burger** icon to toggle the navigation dropdown on mobile screens caused it to be displayed off screen. This in turn resulted in a fair amount of horizontal scroll needed to view the **Cart** and **Burger** icons.

- **Fix**

    Absolute positioning was used for both icons on mobile devices in portrait orientation.

- **Verdict**

    This bug was squashed and the icons in the navbar are now displayed as expected with zero horizontal scrolling required to view them.

#### Dark and Light Mode Text Colour Change in Menu App

- **Bug**

    When viewing the **full menu**, the ordering of the individual menu items did not behave as expected causing the CSS `nth-child` rule I created to be misapplied. This in turn caused the font colour to be changed in menu items that did not require it which resulted in the text being illegible. This was strange, as this behaviour only manifested when viewing the **full menu** and with none of the other menu categories.

- **Fix**

    I removed the CSS styling, and used the `divisibleby` template tag to add the appropriate class to menu items where the font colour requires changing in dark mode.

- **Verdict**

    This bug was squashed, and the light and dark mode font colours display as expected.

