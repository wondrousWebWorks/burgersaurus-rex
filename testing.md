# Testing & Bugs

## Behaviour of site components

### Navbar

- 

## Behaviour of indivudual pages

### Home page

## Bugs

### Development Bugs

#### Checkout Issue for Non-Authenticated Users

- **Bug**

    Non-authenticated users couldn't complete the checkout process. A misconfiguration in `stripe-elements.js` resulted in the *save_info* checkbox in the checkout form's value was required as `true` or `false` when creating the Stripe payment intent. The was targeting the checkbox element and trying to determine it's value regardless of whether it was being displayed for authenticated users or not. This resulted in a value of `undefined` instead of the expected `true` or `false`.

- **Fix**

    I added an if statement in `stripe-elements.js` to determine whether the checkbox element exists before trying to check its status and to set the value explicitely as `false` if no checkbox is found.

- **Verdict**

    This bug was squashed and the checkout process now works for authenticated and non-authenticated users.
