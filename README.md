# Burgersaurus Rex

Welcome to my project! I really hope you enjoy it, and that it provides a good user experience. Burgersaurus Rex is takeway site which allows users to order and pay for food online. It provides all the functionality one would expect to see in such a site, such as the ability to view the menu and add items to your order, modify your order before payment and paying securely. It also offers the user the opportunity to create an account o make future checkouts easier as well as allowing users to view their full order history and select a past order to speed up the ordering process if they order the same on a regular basis. The site owner is provided with the ability to add, update or remove products from the site, as well as viewing the full order customer order history. A lot of love went into making this app, and I hope that comes across to you, the user.

- [Burgersaurus Rex](#burgersaurus-rex)
  - [User Experience](#user-experience)
    - [User Stories](#user-stories)
    - [Site Owner Stories](#site-owner-stories)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Site Layout](#site-layout)
      - [Home Page](#home-page)
      - [Menu Page](#menu-page)
      - [About Page](#about-page)
      - [Order Summary Page](#order-summary-page)
      - [Checkout Page](#checkout-page)
  - [Wireframes](#wireframes)
  - [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Data Models](#data-models)
      - [User Model](#user-model)
      - [Menu App](#menu-app)
        - [Category Model](#category-model)
        - [Allergen Model](#allergen-model)
        - [Product Model](#product-model)
      - [Checkout App](#checkout-app)
        - [Order Model](#order-model)
        - [OrderItem Model](#orderitem-model)
      - [Profiles App](#profiles-app)
        - [UserProfile](#userprofile)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries, Frameworks & Tools](#libraries-frameworks--tools)
  - [Deployment](#deployment)
  - [Running the project locally](#running-the-project-locally)
    - [Credits](#credits)
  - [Disclaimer](#disclaimer)

## User Experience

### User Stories

- As a first-time visitor fo the site, I want to be able to navigate the site with ease to find what I'm looking for without any hassle.
- As someone who is concerned about the sourcing of animal products, I wish to see information about where the meat is sourced form so that I can order with confidence.
- As a hungry user, I want the menu to be easily accessible with easy navigation so I can put together my order with ease.
- As a site user, I want to be able to view and modify my order before completing it so that I can last minute changes before committing my payment details.
- As someone concerned about online security, I want to be able to pay securely so that I don't have to concern myself with unfulfilled orders or being wrongfully charged for an order.
- As a regular visitor to the site, I want to be able to store my details and previous orders to speed up the completion of future orders.

### Site Owner Stories

- As the site owner, I want to offer a visually striking site so that shoppers will have confidence in my business' quality.
- As the site owner, I want an admin interface so that I modify site content when the menu changes.
- As the site owner, I want to be able to view a history of all orders on the site so that I can track the performance of the business over time.

### Colours

While I was looking for a suitable colour palette for Burgersaurus Rex, I noticed that a lot of take away businesses have very vibrant colour schemes on their sites. Since this seemed to be prevalent in the industry, I decided to follow suit for this project. the following colour palette was ultimately selected and can be viewed on [coolors.co](https://coolors.co/ef476f-ffd166-06d6a0-118ab2-073b4c). There is a strong contrast between all the colours, and the selection of colours should make different areas of the site distinct and easy to notice.

![alt text](https://res.cloudinary.com/wondrouswebworks/image/upload/v1592252012/burgersaurus/colour-palette_xyvt0u.png "Colour Palette")

### Fonts

I took inpiration from Nandos, my favourite restaurant, and looked for a font equally cartoony and unique for my project. I finally settled on [Miltonian Tattoo](https://fonts.google.com/specimen/Miltonian+Tattoo?sidebar.open&selection.family=Miltonian+Tattoo&preview.text_type=custom&query=miltonian#standard-styles). Coupled with this is [Open Sans](https://fonts.google.com/specimen/Open+Sans?sidebar.open&selection.family=Miltonian+Tattoo&preview.text_type=custom&query=open#standard-styles), commonly used with the cartoony Miltonian Tattoo to provide a more regular font to balance site text. Both fonts were imported from [Google Fonts](https://fonts.google.com/?preview.text_type=custom&query=open#standard-styles).

### Site Layout

Due to Django's ability to effortlessly render multi-page sites, Burgersaurus rex was designed to feature multiple pages.

#### Home Page

#### Menu Page

#### About Page

#### Order Summary Page

#### Checkout Page

## Wireframes

All wireframes were created using [Balsamiq](https://balsamiq.com/) and can be viewed [here](https://github.com/wondrousWebWorks/burgersaurus-rex/tree/master/wireframes).

## Information Architecture

### Database Choice

- By default, Django works with SQL databases. During development on my local machine I worked with the standard **sqlite3** database installed with Django.
- Heroku provies a **PostgreSQL** database for deployment.

### Data Models

#### User Model

The standard Djando user model, `django.contrib.auth.models`, was used for this project.

#### Menu App

##### Category Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Name | name | max_length=254 | CharField
Friendly Name | friendly_name | max_length=254, blank=True, null=True | CharField
Menu Header URL | menu_header_url | max_length=254, blank=True, null=True | CharField

##### Allergen Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Name | name | max_length=254 | CharField
Friendly Name | friendly_name | max_length=254, blank=True, null=True | CharField
Info URL | info_url | max_length=254, null=True | CharField

##### Product Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Category | category | null=True, blank=True, on_delete=models.SET_NULL | ForeignKey to Category model
Shop category | category | choices=CATEGORY_CHOICES | CharField
Name | name | max_length=254, blank=True, null=True | CharField
Description | description |  | TextField
Price | price | max_digits=4, decimal_places=2 | DecimalField
Is Vegetarian | is_vegetarian | default=False | BooleanField
Allergens | allergens |  | ManyToManyfield

#### Checkout App

##### Order Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order Number | order_number | max_length=32, null=False, editable=False | CharField
User Profile | user_profile | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' | ForeignKey to UserProfile
Full Name | full_name | max_length=50, null=False, blank=False | CharField
Email | email | max_length=254, null=False, blank=False | EmailField
Phone Number | phone_number | max_length=20, null=False, blank=False | CharField
Postcode | postcode | max_length=20, null=True, blank=False | CharField
Town Or City | town_or_city | max_length=40, null=True, blank=False | CharField
Street Address 1 | street_address1 | max_length=80, null=False, blank=False | CharField
Street Address 2 | street_address2 | max_length=80, null=True, blank=True | CharField
Date | date | auto_now_add=True | DateTimefield
Delivery Cost | delivery_cost | max_digits=6, decimal_places=2, null=False, default=0 | DecimalField
Order Sub Total | order_sub_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
Order Total | order_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
Original Cart | original_cart | null=False, blank=False, default='' | TextField
Stripe PID | stripe_pid | max_length=254, null=False, blank=False, default='' | CharField

##### OrderItem Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order | order | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='orderitems' | ForeignKey to Order
Product | product | Product, null=False, blank=False, on_delete=models.CASCADE | ForeignKey to Product
Quantity | quantity | null=False, blank=False, default=0 | IntegerField
Order Item Total | order_item_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | Decimalfield

#### Profiles App

##### UserProfile

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
User | user | User, on_delete=models.CASCADE | OneToOneField
Default Phone Number | default_phone_number | max_length=20, null=True, blank=True | CharField
Default Street Address 1 | deafult_street_address_1 | max_length=80, null=True, blank=True | CharField
Default Street Address 2 | deafult_street_address_2 | max_length=80, null=True, blank=True | CharField
Default Town Or City | default_town_or_city | max_length=40, null=True, blank=True | CharField
Postcode | postcode | max_length=20, null=True, blank=True | CharField

## Technologies Used

### Languages

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)
- [Python](https://www.python.org/about/)

### Libraries, Frameworks & Tools

- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [Cloudinary](https://cloudinary.com/about)
- [Balsamiq](https://balsamiq.com/)
- [mockDrop](https://mockdrop.io/)
- [Git](https://git-scm.com/about)
- [GitHub](https://github.com/)

## Deployment

## Running the project locally

Follow the instructions below to run this project in your own Interactive Development Environment (IDE):

Ensure that you have an IDE of your choice installed:

- An example is [Visual Studio Code](https://code.visualstudio.com/), a free and powerful IDE which was used for the development of this project

Ensure that the following is installed on your machine. **This is a must!**:

- [Python 3](https://www.python.org/downloads/) as the site's backend is written in Python
- [PIP](https://pip.pypa.io/en/stable/installing/) for installing Python packages
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) for version control

You will also need to create free accounts with the following services:

- [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- [Stripe](https://dashboard.stripe.com/register)

### Credits

- [AOS](https://github.com/michalsnik/aos) (Animate On Scroll)

## Disclaimer

This site is intended for **educational purposes** only, and is not intended for use in any other capacity.
