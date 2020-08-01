# Testing & Bugs

- [Testing & Bugs](#testing--bugs)
  - [Testing](#testing)
    - [HTML Validation](#html-validation)
    - [Responsiveness](#responsiveness)
      - [Desired Result](#desired-result)
      - [Steps Taken to Ensure Result](#steps-taken-to-ensure-result)
      - [Verdict](#verdict)
    - [Cross-browser Compatibility](#cross-browser-compatibility)
      - [Desired Result](#desired-result-1)
      - [Steps Taken to Ensure Result](#steps-taken-to-ensure-result-1)
      - [Verdict](#verdict-1)
  - [Authentication](#authentication)
    - [Menu App](#menu-app)
    - [Images App](#images-app)
  - [Behaviour of Shared Site Components](#behaviour-of-shared-site-components)
    - [Navbar (Navigation Bar)](#navbar-navigation-bar)
    - [Theme Selector](#theme-selector)
    - [Footer](#footer)
  - [Behaviour of Site Components](#behaviour-of-site-components)
    - [Navbar](#navbar)
  - [Behaviour of Individual Pages](#behaviour-of-individual-pages)
    - [Home Page](#home-page)
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

### Cross-browser Compatibility

#### Desired Result

Display correctly in any browser users are likely to use, except for older versions of Internet Explorer.

#### Steps Taken to Ensure Result

A a range of browsers were used to test the site, and where I did not have access to it - such as Safari - I borrowed Apple devices to test for potential bugs.

As Firefox does not support the WebKit browser rendering engine, steps were taken to ensure an approximation of the same functionality and styling in the Firefox browser. An example of this would be custom scrollbar styling, where Firefox uses the more modern CSS scrollbar styling tool. Including this not only makes the scrollbars display correctly in Firefox, but also makes the site future proof as the WebKit specification has been abandoned by W3C (World Wide Web Consortium) and will be deprecated eventually.

Browsers tested include:

- [Chrome](https://www.google.com/chrome/) - desktop and mobile
- [Firefox](https://www.mozilla.org/en-US/firefox/new/) - desktop and mobile
- [Opera](https://www.opera.com/computer/opera) - desktop
- [Opera Mini](https://www.opera.com/mobile/mini) - mobile
- [DuckDuckGo](https://duckduckgo.com/app) - mobile

#### Verdict

No obvious bugs were detected in any of the tested browsers. :heavy_check_mark:

## Authentication

Every attempt has been made to secure the app by only allowing authenticated super users to access pages where CUD (create, update, delete) functionality needs to be performed.

### Menu App

A user has be logged in as a super user in order to Add, Update or Delete a product. Should they try to access the related URLs by typing them directly in the browser, they're informed of the need to be logged in with the proper credentials and redirected to the **Home** page. Furthermore, the buttons to **Update** and **Delete** products are only displayed on the **Menu** screen when a user is logged in as a super user.

### Images App

As the images in the Burgersaurus Rex app aren't linked to products or any other apps which can expand the site, users don't have the ability to **add** images.  Instead, they're only allowed to update the images already present within the Image app. A user needs to be logged in as a super user to Update images. Should they try to access the related URLs by typing them directly in the browser, they're informed of the need to be logged in with the proper credentials and redirected to the **Home** page.

## Behaviour of Shared Site Components

### Navbar (Navigation Bar)

- Click on navigation links to confirm correct redirection to the appropriate pages :heavy_check_mark:
- Verify correct colour transition of navigation links on hover :heavy_check_mark:
- Verify that the so-called **'burger'** menu icon displays on smaller screens :heavy_check_mark:
- Verify that on clicking of the **'burger** icon triggers visibility of the vertical navigation menu for smaller screens :heavy_check_mark:
- Verify that using the search input redirects the user to the **Menu** app which displays the relevant results or a message stating that no results were found :heavy_check_mark:
- Confirm that the navbar's height and background colour changes when scrolling past a specified height on screen :heavy_check_mark:
- Confirm that the navbar stays fixed at the top of the screen and is displayed on top of all other site content :heavy_check_mark:

### Theme Selector

- Verify that the **Theme Selector** is displayed as a fixed circle on the bottom right of the screen :heavy_check_mark:
- Click on **Theme Selector** to confirm the animation of *theme options* works by translating them from off-screen to on-screen :heavy_check_mark:
- Confirm that each *theme option* is displayed with the correct border and background colours :heavy_check_mark:
- Verify that hovering over a *theme option* triggers a vertical translation animation :heavy_check_mark:
- Verify that clicking on a theme sets the colours across the site to the selected theme's colours :heavy_check_mark:
- Verify that clicking on the *dark mode* option triggers the dark background on all pages and adjust font colour where necessary to make it legible :heavy_check_mark:
- Confirm that the selected theme and dark mode selections persists across different app pages :heavy_check_mark:

### Footer

As no actual social media accounts exist for this fictional company, links were added to the home pages for each social media service.

- Verify that background colour gradient displays correctly :heavy_check_mark:
- Confirm that copyright information displays correctly :heavy_check_mark:
- Verify that **Opening Times** display correctly :heavy_check_mark:
- Verify that navigation links redirect the user to the expected destination :heavy_check_mark:
- Confirm that the social media icons redirect the user to the relevant social media site upon clicking it :heavy_check_mark:
- Confirm that the order of footer components change when viewed on mobile devices in portrait mode :heavy_check_mark:

## Behaviour of Site Components

### Navbar

- 

## Behaviour of Individual Pages

### Home Page

## Bugs

### Development Bugs

#### Checkout Issue for Non-Authenticated Users

- **Bug**

    Non-authenticated users couldn't complete the checkout process. A misconfiguration in `stripe-elements.js` resulted in the *save_info* checkbox in the checkout form's value was required as `true` or `false` when creating the Stripe payment intent. The was targeting the checkbox element and trying to determine it's value regardless of whether it was being displayed for authenticated users or not. This resulted in a value of `undefined` instead of the expected `true` or `false`.

- **Fix**

    I added an if statement in `stripe-elements.js` to determine whether the checkbox element exists before trying to check its status and to set the value explicitly as `false` if no checkbox is found.

- **Verdict**

    This bug was squashed and the checkout process now works for authenticated and non-authenticated users. :heavy_check_mark:

#### Navbar Displayed Wider Than Screen Width on Mobile Devices

- **Bug**

    The position of the **Burger** icon to toggle the navigation dropdown on mobile screens caused it to be displayed off screen. This in turn resulted in a fair amount of horizontal scroll needed to view the **Cart** and **Burger** icons.

- **Fix**

    Absolute positioning was used for both icons on mobile devices in portrait orientation.

- **Verdict**

    This bug was squashed and the icons in the navbar are now displayed as expected with zero horizontal scrolling required to view them. :heavy_check_mark:

#### Dark and Light Mode Text Colour Change in Menu App

- **Bug**

    When viewing the **full menu**, the ordering of the individual menu items did not behave as expected causing the CSS `nth-child` rule I created to be misapplied. This in turn caused the font colour to be changed in menu items that did not require it which resulted in the text being illegible. This was strange, as this behaviour only manifested when viewing the **full menu** and with none of the other menu categories.

- **Fix**

    I removed the CSS styling, and used the `divisibleby` template tag to add the appropriate class to menu items where the font colour requires changing in dark mode.

- **Verdict**

    This bug was squashed, and the light and dark mode font colours display as expected. :heavy_check_mark:
