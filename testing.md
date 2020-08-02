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
  - [Behaviour of Individual Pages](#behaviour-of-individual-pages)
    - [Home Page](#home-page)
      - [Carousel](#carousel)
      - [Delivery Information](#delivery-information)
      - [Information Section](#information-section)
    - [Menu Page](#menu-page)
    - [Add Product Page](#add-product-page)
    - [Edit Product Page](#edit-product-page)
    - [Cart Page](#cart-page)
    - [Checkout Page](#checkout-page)
      - [Payment Form](#payment-form)
      - [Order Summary](#order-summary)
      - [Stripe](#stripe)
    - [Checkout Success Page](#checkout-success-page)
      - [Order Info](#order-info)
      - [Order Details](#order-details)
      - [Delivery Details](#delivery-details)
      - [Billing Info](#billing-info)
    - [Image Management Page](#image-management-page)
    - [Edit Image Page](#edit-image-page)
    - [Allauth Pages (Authentication)](#allauth-pages-authentication)
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

## Behaviour of Individual Pages

### Home Page

#### Carousel

- Verify that the expected background images are displayed in carousel slides :heavy_check_mark:
- Verify that the expected text is displayed on carousel slides :heavy_check_mark:
- Confirm that the CTA (Call to Action) buttons animate correctly on hover :heavy_check_mark:
- Confirm that the CTA buttons link to the expected pages :heavy_check_mark:
- Confirm that the *carousel indicators* and *carousel selectors* display correctly :heavy_check_mark:
- Verify that the carousel animations work as expected when navigating to new slides :heavy_check_mark:
- Verify that the background shadow effect is visibly to improve legibility of carousel text :heavy_check_mark:

#### Delivery Information

- Verify that the correct images are displayed for each step of the ordering process :heavy_check_mark:
- Verify that the expected Animate On Scroll (AOS) effects are shown when scrolling to the **Delivery Information** section :heavy_check_mark:
- Confirm that ordering of the images and text change when viewed on mobile devices in portrait orientation :heavy_check_mark:
- Confirm that the link *Browse* for the first image's text direct the user to the **Menu** page :heavy_check_mark:

#### Information Section

This section provides information on sources from Irish suppliers and winning awards

- Confirm that the correct images are displayed for each of the two sections :heavy_check_mark:
- Verify that the correct background gradient colours are displayed for each image wrapper :heavy_check_mark:
- Verify that the the correct text is displayed for each section :heavy_check_mark:
- Confirm that the font colour for the text changes when **dark mode** is selected :heavy_check_mark:

### Menu Page

- Verify that the expected background image is displayed in the header depending on **category** selected :heavy_check_mark:
- Verify that the default image is displayed if no category is selected :heavy_check_mark:
- Confirm that a message is displayed informing the user when a non-existent category is entered as a parameter in the URL :heavy_check_mark:
- Verify that the **Menu** category icons are displayed as expected :heavy_check_mark:
- Verify that clicking on a **Menu** category icon displays the correct filtered menu items :heavy_check_mark:
- Confirm that the appropriate heading is displayed for the selected category :heavy_check_mark:
- Confirm that all expected menu items are displayed for each category :heavy_check_mark:
- Verify that every other menu item has a background colour matching the currently selected theme :heavy_check_mark:
- Verify that the correct **name** is displayed for each menu item :heavy_check_mark:
- Confirm that the correct **description** is displayed for each menu item :heavy_check_mark:
- Confirm that the correct **allergens** are displayed for each menu item :heavy_check_mark:
- Verify that clicking on an allergen directs the user to a page with more information on it :heavy_check_mark:
- Verify that the **price** for each menu item is displayed correctly :heavy_check_mark:
- Confirm that the quantity input works as expected :heavy_check_mark:
- Confirm that the **Add To Order** button is displayed correctly :heavy_check_mark:
- Verify that clicking the **Add To Order** buttons adds the menu item and quantity to the cart, the cart amount is updated and a success toast is displayed to inform the user that an item has been successfully added to their order :heavy_check_mark:
- Verify that the **Edit** and **Delete** buttons are displayed for authenticated superusers :heavy_check_mark:
- Verify that clicking the **Edit** button for a given menu item redirects the user to the **Edit Product** page with the form pre-filled with data :heavy_check_mark:
- Confirm that clicking the **Delete** button for a given menu item removes it from the menu :heavy_check_mark:

### Add Product Page

- Verify that the page heading displays correctly :heavy_check_mark:
- Verify that the page heading's colour changes when **dark mode** is selected :heavy_check_mark:
- Confirm that the **Add Product** form has a background colour matching that of the theme :heavy_check_mark:
- Confirm that the **Category** dropdown features all categories :heavy_check_mark:
- Verify that all input fields are displayed :heavy_check_mark:
- Verify that required fields need an input for the form to be validated :heavy_check_mark:
- Confirm that all **Allergens** are displayed in the allergen multiple select dropdown :heavy_check_mark:
- Verify that the **Back To Menu** button redirects the user back to the menu :heavy_check_mark:
- Verify that clicking the **Add Product** button with a valid form add the product to the menu :heavy_check_mark:
- Confirm that a success message is displayed notifying the user that product was added successfully :heavy_check_mark:
- Confirm that the user is redirected to the **Menu** page :heavy_check_mark:

### Edit Product Page

- Verify that the page heading displays correctly :heavy_check_mark:
- Verify that the page heading's colour changes when **dark mode** is selected :heavy_check_mark:
- Confirm that the **Edit Product** form has a background colour matching that of the theme :heavy_check_mark:
- Confirm that an alert message is displayed notifying the user of which product is being edited :heavy_check_mark:
- Confirm that the **Category** dropdown features all categories and that the product's existing category is selected :heavy_check_mark:
- Verify that the product's existing *name* is displayed in the **Name** input :heavy_check_mark:
- Verify that the product's existing *description* is displayed in the **Description** input :heavy_check_mark:
- Confirm that the product's existing price is listed in the **Price** input :heavy_check_mark:
- Confirm that the **Is vegetarian** checkbox is selected or not depending on the product :heavy_check_mark:
- Confirm that the **Allergen** dropdown features all allergens and tha the product's existing allergens are selected :heavy_check_mark:
- Verify that the **Back To Menu** button redirects the user back to the menu :heavy_check_mark: :heavy_check_mark:
- Verify that clicking the **Edit Product** button with a valid form edits the product's values :heavy_check_mark: :heavy_check_mark:
- Confirm that the user is then redirected to the **Menu** page :heavy_check_mark:
- Confirm that a **success** message is displayed notifying the user that the product has been edited successfully :heavy_check_mark:

### Cart Page

- Verify that the page heading displays correctly :heavy_check_mark:
- Verify that the page heading's colour changes when **dark mode** is selected :heavy_check_mark:
- Confirm that the cart table's header content is displayed correctly :heavy_check_mark:
- Confirm that the **Product Info**, **Price**, **Quantity** and **Subtotal** are displayed correctly for each cart item :heavy_check_mark:
- Confirm that every other cart item has a background colour matching that of the theme :heavy_check_mark:
- Verify that cart items with a background colour matching the page background change font colour when **dark mode** is selected :heavy_check_mark:
- Verify that the **quantity** for each cart item can be updated :heavy_check_mark:
- Verify that cart items can be removed from the cart :heavy_check_mark:
- Confirm that the **Order Sub-total**, **Delivery Charge** and **Order Total** are displayed correctly :heavy_check_mark:
- Confirm that the **Order Sub-total**, **Delivery Charge** and **Order Total** font colour changes when **dark mode** is active :heavy_check_mark:
- Verify that the **Go To Menu** button directs the user back to the menu :heavy_check_mark:
- Verify that the **Checkout** button directs the user to the **Checkout** page :heavy_check_mark:

### Checkout Page

#### Payment Form

- Verify that the page heading displays correctly :heavy_check_mark:
- Verify that font colour changes when **dark mode** is selected for targeted text :heavy_check_mark:
- Confirm that the Details section of the payment form displays correctly with all inputs present and placeholders displaying :heavy_check_mark:
- Confirm that the Delivery section of the payment form displays correctly with all inputs present and placeholders displaying :heavy_check_mark:
- Confirm that the Payment section of the payment form displays correctly with all inputs present and placeholders displaying :heavy_check_mark:
- Verify that a checkbox is displayed for logged-in users to save their information to their profile :heavy_check_mark:
- Verify that the form data is saved to a logged-in user's profile if the checkbox is checked :heavy_check_mark:
- Confirm that buttons to **register** or **sign in** are displayed instead of the checkbox for users not logged into the site :heavy_check_mark:
- Confirm that the **register** and **sign in** buttons direct the user to the appropriate page when clicked :heavy_check_mark:
- Verify that an error message is displayed below the **Payment** section when invalid card details are entered :heavy_check_mark:
- Verify that an *loading spinner* is displayed when the **Checkout** button is clicked :heavy_check_mark:
- Verify that the **Checkout** button is *disabled* when the **Checkout** button is clicked :heavy_check_mark:

#### Order Summary

- Verify that the **Order Summary** heading is displayed :heavy_check_mark:
- Verify that the **Order Summary** table headers (Product Info, Price, Qty, Subtotal) are displayed :heavy_check_mark:
- Confirm that all items in the order are displayed in the **Order Summary** table :heavy_check_mark:
- Confirm that every other item in the **Order Summary** has a background colour matching that of the theme :heavy_check_mark:
- Confirm that the **Order Sub-total**, **Delivery Charge** and **Order Total** are displayed correctly :heavy_check_mark:

#### Stripe

- Verify in **Stripe** account that the payment was successful and that the webhooks were handled successfully :heavy_check_mark:

### Checkout Success Page

- Verify that the page heading displays correctly :heavy_check_mark:
- Verify that the confirmation email notification displays below the page heading with the correct email address listed :heavy_check_mark:
- Verify that font colour changes when **dark mode** is selected for targeted text :heavy_check_mark:
- Confirm that a **Success Toast** is displayed at the top right of the screen with the order number and email address for the confirmation email :heavy_check_mark:
- Confirm that the **Check out the menu for next time** button is displayed and directs the user to the *menu* page :heavy_check_mark:

#### Order Info

- Confirm that that the section heading displays correctly :heavy_check_mark:
- Confirm that the section has a background colour matching the currently selected theme :heavy_check_mark:
- Verify that the correct **Order Number** and **Order Date** are displayed :heavy_check_mark:

#### Order Details

- Confirm that that the section heading displays correctly :heavy_check_mark:
- Confirm that the section has a background colour matching the currently selected theme :heavy_check_mark:
- Verify that the correct **Menu Item**, **quantity** and **price** are displayed for each order item :heavy_check_mark:

#### Delivery Details

- Confirm that that the section heading displays correctly :heavy_check_mark:
- Confirm that the section has a background colour matching the currently selected theme :heavy_check_mark:
- Verify that the correct delivery details (**Full Name**, **Address 1**, **Address 2 if present**, **Town or City**, **Postal Code** and **phone number**) are displayed :heavy_check_mark:

#### Billing Info

- Confirm that that the section heading displays correctly :heavy_check_mark:
- Confirm that the section has a background colour matching the currently selected theme :heavy_check_mark:
- Verify that the correct **Order Sub-Total**, **Delivery** charge and **Order Total** are displayed :heavy_check_mark:

### Image Management Page

- Verify that the page heading displays correctly :heavy_check_mark:
- Verify that font colour changes when **dark mode** is selected for targeted text :heavy_check_mark:
- Confirm that the correct background colour is displayed for each image card as determined by the selected theme :heavy_check_mark:
- Confirm that all the images for the **Home**, **About** and **Menu** pages are displayed for editing :heavy_check_mark:
- Verify that the correct **friendly name** is displayed for each image :heavy_check_mark:
- Confirm that an **Edit** button is displayed for each image :heavy_check_mark:
- Confirm that clicking on an image's **Edit** redirects the user to the **Edit Image** for the selected image :heavy_check_mark:

### Edit Image Page

- Verify that the page heading displays correctly :heavy_check_mark:
- Verify that the correct **friendly name** is displayed for the image to be edited :heavy_check_mark:
- Confirm that an alert message is displayed letting the user know which image they're about to edit :heavy_check_mark:
- Confirm that the correct image which is currently saved is displayed to let the user know what they're going to change :heavy_check_mark:
- Verify that the *current* image URL is displayed :heavy_check_mark:
- Verify that clicking on the **Choose File** button opens and explorer to select an image to upload :heavy_check_mark:
- Confirm that the **Back To Images** button is displayed and redirects the user to the **Image Management** page when clicked :heavy_check_mark:
- Confirm that the **Change Image** button is displayed and redirects the user to the **Image Management** page when clicked :heavy_check_mark:
- Verify that the image in question has been changed by inspecting the image displayed in the relevant section on the **Image Management** page :heavy_check_mark:
- Confirm that a **success** notification is displayed :heavy_check_mark:

### Allauth Pages (Authentication)

There are simply too many pages here to list individually within my time constraints. A summary is provided below which is true for all **allauth** pages where applicable.

- Verify that the page heading displays correctly :heavy_check_mark:
- Verify that all inputs are displayed as expected :heavy_check_mark:
- Confirm that **buttons** for returning to the **Home** page redirect the user as expected :heavy_check_mark:
- Confirm that forms require validation to be submitted :heavy_check_mark:
- Verify that **buttons** for submitting forms do so and redirect the user back the **Home** page :heavy_check_mark:
- Verify that the correct background image is displayed on all **authentication** pages :heavy_check_mark:
- Verify that the **Confirm Email** page displays as expected and allows the user to confirm their email address :heavy_check_mark:

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
