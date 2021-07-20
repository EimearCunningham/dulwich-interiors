# Dulwich Interiors
## An online interior design store
A website for customers / potential customers to browse products and services and potentially make a purchase.

Live website: 

# UX
### Who this website is for:
This website is for customers interested in buying home interior products.

### What they want to achieve:
They want to be able to browse through products and potentially make a purchase. 

### This project is the best way to help them achieve these things because:
The simple, clear layout of the site allows users to easily add items to their cart and make a purchase.

## User Stories:
### Site user
1. As a user, I want to easily browse through all products for sale.
2. As a user, I want to view a specific category/room of products
3. As a user, I want to search for a product I need.
4. As a user, I want to view details of each product on the site.
5. As a user, I want to be able to add a product/products to my shopping bag.
6. As a user, I want to be able to purchase items that are in my shopping bag.
7. As a user, I want to create and sign in to my account.
8. As a signed in user, I want to be able to save my delivery details for my next purchase.
9. As a user, I want to read news/updates on the business.

### Site / business owner
1. As a site owner, I want to be able to add/edit and delete products and services on the site.
2. As a site owner, I want to be able to upload news/updates about the business. 

## Design 
### Color Scheme 
The following colors were selected for use across the site:
#AD974F HUSK - This is a golden shade of yellow which gives the site a high end classy feel.
#231F20 AUBERGINE - A slighter lighter than black shade which contrasts the other colors.
#EAEAEA WHISPER - An off white shade for backgrounds. 

### Typography 
'Dancing Script' family from Google Fonts was used throughout the site. I selected this font as I thought it complimented the clean, classy feel of the site.

## Wireframes:
<details>
<summary>Home (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/home-wireframes.png)
</p>
</details>

<details>
<summary>Products (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/product-wireframes.png)
</p>
</details>

<details>
<summary>Product details (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/product-detail-wireframes.png)
</p>
</details>

<details>
<summary>Login (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/login-wireframes.png)
</p>
</details>

<details>
<summary>Register (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/register-wireframes.png)
</p>
</details>

<details>
<summary>Cart (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/cart-wireframes.png)
</p>
</details>

<details>
<summary>Checkout (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/checkout-wireframes.png)
</p>
</details>


<details>
<summary>Checkout Success (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/checkout-success-wireframes.png)
</p>
</details>

<details>
<summary>Profile (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/profile-wireframes.png)
</p>
</details>



# Features


## Features Left to Implement

# Technologies Used
## Languages, frameworks and libraries used


## Other technologies used
https://www.htmlcsscolor.com/ - Selecting colors 

# Testing


# Deployment

## Deploying to Heroku 

- Create a Heroku account and app:
    - Go to https://signup.heroku.com/login and create an account.
    - From your dashboard click 'Create app'.
    - Create a name for the app and select the region closest to you.
    - Click 'Create app'.

- Set up Postgres database on app:
    - Go to 'Resources' tab of Heroku app.
    - Search for 'Postgres'.
    - Add Postgres to the app, selecting to use the free development plan.

- Install requirements in workspace:
    - Install dj_database_url and psycopg2-binary 
    ```
        pip3 install dj_database_url
            
        pip3 install psycopg2_binary
    ```       

- Freeze new requirements to requirements.txt
    ```
        pip3 freeze > requirements.txt
    ```

- Go to settings.py file and import dj_database_url
    ```python
        import dj_database_url
    ```
    
- Add Postgres database settings to settings.py
    ``` python
        DATABASES = {
            'default': dj_database_url.parse('ENTER DATABASE URL FROM APP CONFIG SETTINGS HERE')
        }
    ```

- Comment out settings for sqlite database
- Migrate to new Postgres database
    ``` 
        python3 manage.py migrate
    ```

- Create a superuser:
    ```
        python3 manage.py createsuperuser
    ```
    
    **Here I made the error of pushing to github without removing my Postgres Database URL. I fixed this by creating a completely new app and DB URL so that it wasn't pushed to Github at any stage**

- Add the following statement to settings.py to use Postgres DB if available and sqlite DB if not:
    ``` python
        if "DATABASE_URL" in os.environ:
            DATABASES = {
                "default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
                }
        else:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
    ```
- Postgres database has now been set up.

- To complete the Heroku set up we need to install gunicorn and add it to a Procfile as shown:
    ```
        pip3 install Gunicorn
    ```
- In Procfile:
    ```
        web: gunicorn dulwich_interiors.wsgi:application
    ```

- Log into Heroku through your workspace termnial:
    ```
        heroku login -i
    ```

- Disable static file collection for now
    ```
        heroku config:set DISABLE_COLLECTSTATIC=1 --app <insert Heroku app name here>
    ```
        
- In settings.py add:
    ``` python
        ALLOWED_HOSTS = ['dulwich-interiors-ms4.herokuapp.com', 'localhost']
    ```
- Add and commit changes to github
- Push to Heroku
    ```
        heroku git:remote -a <dulwich-interiors-ms4>
        git push heroku master
    ```

- Enable automatic deploys to heroku
        - Go to setting tab of Heroku app
        - Click 'Connect to Github' and search for respository
        - Select repository
        - Click 'Enable automatic deploys'


# Credits

## Code


**This site is for educational purposes only** 