# Testing

## Validation Services

### Validation Services used
* [W3C Markup Validation Service](https://validator.w3.org/) - To validate html code
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - To validatate CSS code
* [JS Hint](https://jshint.com/) - To validate JavaScript code
* [PEP8 Online](http://pep8online.com/) - To validate python code

### Errors / Warnings found by W3C Markup Validation Service:
All rendered pages were ran through the W3C Markup validation Service
### Errors / Warnings found by W3C CSS Validation Service:
### Errors / Warnings found by PEP8 online:

## Testing User Stories
### Site user
1.	As a user, I want to easily browse through all products for sale.
-	From homepage, user can access the ‘Products’ page in two ways: From the ‘Products’ link in the navbar, or through the ‘Shop Now’ button on the first image of the carousel
-	User can always easily navigate to Products page through the navbar visible on all pages throughout site
-	
2.	As a user, I want to view a specific category/room of products
-	From the navbar, user has the option to ‘Shop by room’. This button provides a dropdown which allows the user to filter products by room

3.	As a user, I want to search for a product I need.
-	Navbar of site has a search bar visible on all screen sizes that allows the user to search for key words in the products title or description

4.	As a user, I want to view details of each product on the site.
-	When browsing through products, the user will see a ‘View details’ button for each product.
-	When selected user is brought to the Product Details page of that product, which has more information such as the product description

5.	As a user, I want to be able to add a product/products to my shopping cart.
-	On the product details page the user will see a button to add the product to their cart
-	The product details page also allows the user to add a quantity of the item to their cart if they are purchasing more than one

6.	As a user, I want to be able to purchase items that are in my shopping cart.
-	The user can access their shopping cart at any time through the shopping cart logo in the navbar
-	From the shopping cart page they have the ability to view what is currently in their cart, and proceed to the checkout page
-	On the checkout page the user can fill in their delivery details and card details and complete their purchase
-	If the user is logged in and has saved their delivery details, the form will be prepopulated with their details. This means they don’t have to fill in the form each time they make a purchase

7.	As a user, I want to create and sign in to my account.
-	The sites navbar has a ‘User’ icon which is a dropdown.
-	If the user is not logged in, they will have the option to Register a new account, or sign in to an existing account
-	If a user is logged in, they will have the option to view their profile page or log out
8.	As a signed in user, I want to be able to save my delivery details for my next purchase.
-	As mentioned above, user has the option to access their profile page from the navbar when logged in
-	Profile page consists of a form which the user can fill in and save their delivery details
-	The form details will pull through to the checkout page when the user is completing a purchase 

9.	As a user, I want to read news/updates on the business.
-	News section is easily accessible through the News navbar link
-	User is guided to a news/blog page where they can view posts uploaded by the store owners

10.	As a user, I want to be able to comment on news/updates uploaded by the business - to show support / ask questions.
-	After clicking to ‘Read more’ of a blog post, a logged in user will have the option to leave a comment.
-	They will need to fill out a form with their name, email address and the comment itself

### Site / business owner
1.	As a site owner, I want to be able to add/edit and delete products on the site.
- When a superuser is logged in, if they select the user icon from the navbar they will have the option to 'Add a product'. This will lead them to a form they need to fill out with the product details. On submitting this form a new product will be added to the database.
- Superusers will have the option to Edit / Delete products from the All Products page, or the individual product details page.

2.	As a site owner, I want to be able to upload news/updates about the business.
- Superusers will have the option to 'Add a blog post' from the User dropdown in the navbar. This will lead them to a form they will need to fill out with the post details. On submitting this form a blog post will be added.
- Superusers will have the option to edit / delete blog posts from the main blog page, and from the individual post detail pages.


## Manual testing of all elements and functionality 

### Navbar
- Test main site logo by clicking to ensure it leads user back to homepage
- Test search bar
    - Search for a word/words in items title and ensure it is returned to the user
    - Search for a word/words in items description and ensure it is returned to the user
    - Search for a word/words in multiple items title and ensure all products are returned to the user
    - Search for a word/words in multiple items description and ensure all products are returned to the user
- Test User icon to ensure that it reveals the correct dropdown depending on if the user is logged in/ not logged in / logged in as superuser
    - If user is not logged in the dropdown reveals two options 'Login' and 'Register'
    - If user is logged in the dropdown has two options 'Logout' and 'Profile'
    - If user is logged in as superuser dropdown has options to 'Add a product', 'Add a blog post', 'Profile' and 'Logout'
    - All dropdown items were tested to ensure the user is brought to the correct page
- Test cart icon to ensure it leads to the users Shopping Cart page
- Test navigation links
    - 'All Products' link leads to the Products page, displaying all products in all categories
    - 'Shop by Room' dropdown gives users four options, allowing them to filter products by their room (category). Each option from dropdown leads the user to a page that only shows products in that room
    - 'News' link leads the user to the news/blog page of the site
- Navbar responsiveness was tested across small, medium, large and extra large screen sizes using Google Chrome dev tools

### Registering / logging in / logging out
- Test registering for an account
    - User selects 'User' icon from navbar and selects to 'Register'. They are taken to the Sign up Page.
    - Test Register form:
        - If user doesn't enter email address / retype emaill address they get an error
        - If user doesn't enter a password / retype password they get an error
        - If password 1 doesn't match password 2 user will get an error 
        - If user doesn't enter a username they get an error
        - If user enters an email address that is already registered they get an error
        - On submitting a valid form, an email is sent to the user with a link to follow to verify their email address
        - On following the link from the email, the user is brought back to the site and asked to 'Confirm'.
        - On selecting the 'Confirm' button the user is brought to the sign in page and can sign in to their newly created account.

- Test signing in to an existing account
    - User selects the 'User' icon from navbar and selects to 'Log in'
    - User is taken to sign in page
    - If user enters an incorrect username/password match they will receive an error message
    - If user enters correct username/password match they are logged in to their account with a successfull alert message
        
- Test signing out of account
    - When a logged in user goes to the User icon of the navbar and selects to logout, they are taken to a page asking them to confirm sign out. On confirming this the user is logged out with a succesfull alert message
    

### Homepage
- Test homepage carousel
    - Test that arrows on carousel work and take the user to the next image. When 'Next' arrow is selected on the final image it takes the user back to the first image
    - Test that the button on each slide (Shop, Register, News) takes the user to the appropriate page
- Test responsiveness of homepage
    - On testing the responsiveness of the carousel across small and medium screen sizes, it was noticed that the carousel wasn't occupying the entire screen height. This was fixed by changing the height of the carousel item, and carousel item image to 100vh.


### Products Page
- Test 'View product' button to ensure that user is brought to the product details page of that particular product
- Test responsiveness of page using Google Chrome Dev Tools
    - Found that on small device sizes the navbar was covering the page heading. Fixed by using media query to add extra padding to header-container class on small and medium screen sizes.

### Product details page
- Test quantity selector input - Should only allow quantity between 1 and 6
    - If user uses 'Plus' and 'Minus' buttons to select quantity, they will only be able to select quantity between 1 and 6 - buttons will grey out if number is outside this range
    - Bug found where user is able to manually type in quantity above 6 - Fixrd by adding 'max="6"' to the input field
- Test 'Back to products' button to ensure user is brought back to the All Products page
- Test add to cart button to ensure that product is added to cart, user gets success alert message, and the cart grand total is updated accordingly

### Shopping cart
- If user selects the shopping cart logo when there are no items in their cart the cart page will tell them 'Your cart is empty' & provide button to 'Keep shopping'. Test this button to ensure it takes user back to Products page.
- Test quantity selector input - Should only allow quantity between 1 and 6
    - If user uses 'Plus' and 'Minus' buttons to select quantity, they will only be able to select quantity between 1 and 6 - buttons will grey out if number is outside this range
    - Bug found where user is able to manually type in quantity above 6
- Test Remove Item link
    - On selecting the Remove Item link item is removed from cart and user gets successful alert message
- Test 'Checkout' button
    - Only shows when user has item(s) in their cart
    - Takes user to the checkout page

### Checkout
- Ensure that Order Summary column correctly displays users current order, and adds on 20% delivery charge
- Test checkout form:
    - Test that email address is prepopulated as users email
    - Test submitting form with one required field left blank each time (Name, email, phone number, town or city, street address 1, card number, card expiry date, cvc)
        - Form will not submit without required fields
- Test 'Checkout' button
    - Slight delay in getting to checkout success page
    - On submitting the checkout form, user gets a succesful alert message with their order number, letting them know a confirmation email has been sent
    - User is directed to checkout success page
    - User receives email with the subject line 'Thank you for your order at Dulwich Interiors!'
### Checkout success
- Ensure that checkout success page shows correct details under Order Info, Order Details, Delivering to and Billing Info
- Test that 'Continue shopping' button takes user back to Products page
### Profile page
- Ensure that not logged in users are asked to sign in if they manually add '/profile' to the sites URL
- Test that Order History section displays users previous orders
- Test that the Order Number link in the Order History section directs user to the Order History page of that particular order, and gives them an alert message that this is a past order
- Test that the user can add / remove any line of information from the Default Delivery Information form, and on submitting the relevant info is added/removed from the form
- Test that after saving information to the Default Delivery Information form on the profile page, that it is pulled through to prepopulate the form on the checkout page

### Blog / News page
- Accessible through the 'News' link on navbar
- Test that all posts added by store owners are displayed, with the most recent post at the top of the page
- Test the 'Read more' button of each post to ensure it takes the user to the post details page of that post
### Post details & comments
- Test that the number of comments on that post is correctly added up and displayed to the user
- Ensure that logged in user has the option to add a comment
- Ensure that not logged in user is asked to 'Please register / sign in to leave a comment!'
- Test comments form:
    - Form cannot be submitted if any field is left blank
    - On submitting the comments form, the users comment is added to the post, and the number of comments is updated. User gets a success alert message that they've added a comment

### Add / edit / delete blog posts
- Ensure that if a logged in user who is not a store owner manually types in URL for adding a product, editing a product or deleting a product - that they cannot access the page and get an alert message that these pages are only for store owners
- Ensure that if a user who is not logged in tries to manually type the URL for adding/ editing/ deleting products that they are led to the sign in page where they either sign in as superuser / regular user
#### Add Product
- When signed in as superuser, user has the option to 'Add a product' from the User dropdown in the navbar
- 
### Add / edit / delete products


## Accessability Testing
[WAVE Web Accessability Evaluation Tool](https://wave.webaim.org/) was used to test the accessability of my site.
The following recommendations and changes were made:

