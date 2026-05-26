# Michelle's Craft Room
Michelle's Craft Room is a full-stack e-commerce website built with Django that sells digital PNG cards and art prints. The site provides a complete online shopping experience with user authentication, shopping cart functionality, secure payment processing via Stripe, and order management.

<img width="1886" height="778" alt="image" src="https://github.com/user-attachments/assets/b62464ce-a3eb-46e0-901f-530f9a76b349" />

Live Site: https://project-5-michelles-craft-room-cdc5efe9b632.herokuapp.com/

## Table of Contents
- [User Stories](#user-stories)
- [Business Model](#business-model)
- [Design & UX](#design--ux)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Database Schema](#database-schema)
- [SEO Testing](#seo-testing)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Stories
I chose to write mine out on a google sheet document laid out as a kanban board. Although this is not acceptable for larger groups as it can easily get confusing and messy. For a simple one man operation I find it best as it keeps the user stories simple and easy to follow.

<img width="1241" height="819" alt="image" src="https://github.com/user-attachments/assets/12f3aaca-78dd-4184-bbb2-3d1e6597063e" />

## Business Model

### E-Commerce Business Model

Michelle's Craft Room operates on a **B2C (Business-to-Consumer)** e-commerce model, selling digital products directly to individual customers.

**Business Type:** Product-based e-commerce  
**Revenue Model:** Single transaction payments for digital downloads

### Target Market
- Craft enthusiasts and hobbyists.
- Scrapbookers and card makers.
- Small business owners creating personalized products.
- Gift givers looking for unique digital art.
- DIY project creators.

### Value Proposition
Michelle's Craft Room provides high-quality, handcrafted digital PNG cards and art prints that customers can download instantly and use for their creative projects. Unlike physical craft supplies, our digital products offer:
- Unlimited personal use once purchased.
- High-resolution files suitable for printing.
- Unique designs created by Michelle herself.
- Affordable pricing for quality artwork.

### Revenue Streams
1. **Digital Product Sales:** Primary revenue from selling PNG cards and art prints.
2. **Future Potential:** Subscription model for regular design updates, custom commission work, or premium membership tiers.

### Marketing Strategy
- **Social Media Presence:** Facebook Business Page to showcase products and engage with the craft community.
- **Email Marketing:** Newsletter subscription system to keep customers informed about new releases and special offers.
- **SEO Optimization:** Search engine optimization to attract organic traffic from people searching for digital craft supplies.
- **Word of Mouth:** Quality products encourage customers to share and recommend to their craft communities.

### Customer Relationship
- Direct online transactions through the website.
- Email confirmations for all purchases.
- Newsletter communication for ongoing engagement.
- Profile system allowing customers to view order history.
- Responsive customer service via contact information.

### Key Resources
- Michelle's artistic talent and product creation.
- E-commerce website (Django-based).
- Cloudinary for image storage and delivery.
- Stripe payment processing infrastructure.
- Customer database and order management system.
- Facebook Page.

![IMG_0307](https://github.com/user-attachments/assets/279b7f27-9562-41f4-9f72-b2d081df3382)
![IMG_0306](https://github.com/user-attachments/assets/69f2a6e0-d6f4-4614-a270-4dc2ada7bb10)
![IMG_0305](https://github.com/user-attachments/assets/47afe648-5366-43fb-99b4-02b0d2763976)
![IMG_0304](https://github.com/user-attachments/assets/59c2a43c-131c-42fe-87f8-15a8d2a08e53)
![IMG_0302](https://github.com/user-attachments/assets/562f451e-2dc7-4ed7-ad47-14eed51663b2)
![IMG_0303](https://github.com/user-attachments/assets/09e8dd94-61be-48fa-9ca7-2241b3bf9499)

### Future Growth Opportunities
- Expand product range with seasonal collections.
- Introduce custom design services.
- Develop tutorial content to add value.
- Partner with craft influencers for promotion.
- Consider print-on-demand services for physical products.

---

## Design & UX

### Design Philosophy
The website design focuses on showcasing Michelle's artwork while providing a smooth, intuitive shopping experience. The color scheme and typography were chosen to reflect the creative, artistic nature of the products while maintaining a professional e-commerce appearance.

### Wireframes & Mockups

#### Wireframes:
products page: ![IMG_0309](https://github.com/user-attachments/assets/a7705a66-8b88-40f1-bf07-8ac04c5e3c9c)
checkout and profiles pages: ![IMG_0311](https://github.com/user-attachments/assets/e0e85595-8f90-49ad-8690-0b10a0934c27)
home page: ![IMG_0308](https://github.com/user-attachments/assets/94939dd7-4112-4707-a973-b1c923001122)

#### Design Process:
1. Started with a basic Bootstrap structure for responsive layout.
2. Customized the carousel and hero section to prominently feature artwork.
3. Implemented a clean navigation system with user account management.
4. Designed the product browsing experience with clear pricing and imagery.
5. Created a streamlined checkout flow with Stripe integration.

#### Key Design Decisions:

**Color Scheme:**
- Emerald (#1D3B28) - Professional, natural
- Mauve (#874C62) - Creative, artistic
- Chartreuse (#BA9F38) - Attention-grabbing for CTAs
- Pale Lime (#E1CC96) - Soft, elegant
- Butter Base (#FCEBD0) - Clean background

**Typography:**
- 'Playwrite NZ Guides' for headings - Adds personality and creativity.
- 'DM Serif Text' for body - Professional and readable.

**Layout Features:**
- Fixed navigation for easy access to cart and account.
- Image carousel on homepage to showcase featured artwork.
- Grid-based product display for easy browsing.
- Responsive design that works on all device sizes.
- Clear call-to-action buttons throughout.

### User Experience Considerations

**Navigation:**
- Simple, intuitive menu structure.
- Search functionality for quick product finding.
- Sorting options (price, rating, name) for product browsing.
- Shopping bag always visible with running total.

**Accessibility:**
- Semantic HTML structure.
- Descriptive alt text for all images.
- Form validation with clear error messages.
- Sufficient color contrast for readability.
- Responsive design for all screen sizes.

**User Flow:**
1. Land on homepage → Browse carousel
2. Search or browse products → View details
3. Add to cart → Review cart
4. Checkout → Enter details
5. Pay securely → Receive confirmation

### Responsive Design

The website is fully responsive across all device sizes:
- **Mobile (320px - 767px):** Stacked layout, simplified navigation, touch-friendly buttons.
- **Tablet (768px - 1023px):** Two-column layouts, adjusted image sizes.
- **Desktop (1024px+):** Full multi-column layouts, hover effects, maximum detail.

Testing was conducted using Chrome DevTools across multiple viewport sizes to ensure consistency.

---

## Features

### Existing Features

#### **User Authentication**
- Powered by Django Allauth for secure user registration, login, and logout.
- Email verification for new accounts.
- User profiles to store delivery information and view order history.

<img width="544" height="511" alt="image" src="https://github.com/user-attachments/assets/a8d8086d-7910-45eb-bc75-9830094b861d" />
<img width="1892" height="379" alt="image" src="https://github.com/user-attachments/assets/7eb040b3-8417-49da-abbc-d7d2e0426021" />

#### **Product Catalog**
- Browse all available PNG cards and art prints.
- Product details pages with images, descriptions, and pricing.
- Products organized and easily searchable.

<img width="1881" height="793" alt="image" src="https://github.com/user-attachments/assets/14ae8505-7490-43cb-936d-866eccd6aebe" />
<img width="1670" height="825" alt="image" src="https://github.com/user-attachments/assets/b8c8101f-c0d6-4c2d-9983-c71e5c9c729c" />
<img width="1810" height="734" alt="image" src="https://github.com/user-attachments/assets/73e6d1eb-4c3c-4f08-80e7-ef531f881eac" />


#### **Shopping Bag**
- Add products to shopping bag
- Adjust quantities or remove items
- Update-able total calculation
- Bag contents persist across sessions

<img width="1885" height="863" alt="image" src="https://github.com/user-attachments/assets/b79a8e33-ff51-4eb5-9b92-f0cdd07c0712" />
<img width="1846" height="844" alt="image" src="https://github.com/user-attachments/assets/6e5a9890-8f4e-4553-a53c-544b413ef567" />


#### **Secure Checkout**
- Stripe payment integration for secure card processing.
- Order form with delivery information.
- Option to save delivery details to user profile for faster future checkouts.
- Real-time payment validation.

<img width="544" height="464" alt="image" src="https://github.com/user-attachments/assets/222b2cea-52bf-4d85-9e67-132b247399ab" />
<img width="1718" height="452" alt="image" src="https://github.com/user-attachments/assets/fe3e4bab-6b37-41bd-96bb-7e4495e4fee5" />

#### **Order Management**
- Order confirmation page with order number.
- Email confirmations sent to terminal (development) showing order details.
- Order history stored in user profiles.
- Webhook handlers ensure orders are created even if user closes browser.

<img width="550" height="678" alt="image" src="https://github.com/user-attachments/assets/2078f2c9-435a-41ed-99ca-7e33129c5319" />

#### **Newsletter Subscription**
- Users can subscribe to the newsletter from their profile page.
- Email addresses stored in database with name and subscription date.
- Duplicate email protection.
- Admin interface to manage subscribers.

<img width="1210" height="540" alt="image" src="https://github.com/user-attachments/assets/ccbcb160-a0f7-4508-bd4f-c0c84e29a5e8" />

#### **Admin Panel**
- Django admin interface for managing products, orders, and users
- Upload and manage product images via Cloudinary integration

<img width="543" height="507" alt="image" src="https://github.com/user-attachments/assets/154280ad-16f9-4ab3-b5e6-1e26e40cc4b0" />

---

## Technologies Used

### Languages
- **Python** - Backend logic and Django framework.
- **JavaScript** - Stripe Elements integration and interactive features.
- **HTML5** - Structure and content.
- **CSS** - Styling and responsive design.

### Frameworks & Libraries
- **Django 6.0** - Python web framework.
- **Django Allauth** - User authentication and account management.
- **Stripe** - Payment processing.
- **Bootstrap 4** - Responsive frontend framework.
- **Crispy Forms** - Enhanced Django form rendering.
- **WhiteNoise** - Static file serving for production.

### Database
- **PostgreSQL** - Production database (via Heroku).

### Storage
- **Cloudinary** - Cloud storage for media files (product images).

### Deployment & Hosting
- **Heroku** - Application hosting.
- **Git & GitHub** - Version control.

---

## Database Schema

The application uses the following main models:

### **Product**
- Stores product information (name, description, price, image).

### **Order**
- Stores customer order details (full name, email, delivery address, order total).
- Links to UserProfile if user is authenticated.

### **OrderLineItem**
- Represents individual products within an order.
- Links to both Order and Product models.

### **UserProfile**
- Stores user's default delivery information.
- Links to Django's built-in User model.

---
## SEO Testing

| SEO Element | Status | Notes |
|-------------|--------|-------|
| Meta description tags | ✅ Pass | Present in all pages |
| Meta keywords | ✅ Pass | Relevant keywords included |
| Site title | ✅ Pass | Descriptive and SEO-friendly |
| robots.txt | ✅ Pass | Accessible at /robots.txt |
| sitemap.xml | ✅ Pass | Accessible at /sitemap.xml |
| 404 page | ✅ Pass | Custom 404 page with navigation |
| All internal links working | ✅ Pass | No broken links found |

#### SEO Engine Optimisation Strategy
Michelle's Craft Room was designed to help customers find the site when searching for digital craft products, PNG cards and art prints, the following SEO elements were implemented throughout the project.

**Meta Tags**
The following meta tags are included in base.html template and apply across all pages:
<meta name="description" content="Michelle's Craft Room - browse and instantly download unique digital PNG cards and art prints.">
This meta description summarises the site's purpose clearly for both search engines and browsing serach results. 

**Site Title**
Every page carries the base title "Michelle's Craft Room". Individual pages can extend this using the {% block extra_title %} block, allowing for page-specific titles where needed.

**robots.txt**
The robots.txt file is accessible at /robots.txt and tells search engine crawlers which parts of the site to index:
<img width="809" height="277" alt="image" src="https://github.com/user-attachments/assets/c3365ec8-7aa2-4e64-a30c-bb19ef62d3bb" />
Private and transactional pages like the admin panel, checkout, bag and profile are "disallowed" to keep them out of search results. The homepage and products pages are explicitly "allowed" as these are the most important pages for organic traffic.

**sitemap.xml**
The sitemap.xml file is accessible at /sitemap.xml and lists the key publicly accessible URLs so search engines can find and prioritise them:
<img width="893" height="698" alt="image" src="https://github.com/user-attachments/assets/47916e02-86aa-4927-b30e-0e6d515febd7" />
The homepage has the highest priority as the main entry point, with the products page ranked second as the core content of the site.


**rel Attributes**
rel="noopener noreferrer" is used on all external links, including the Facebook page link in the footer and the admin link in the navigation. This prevents external pages from accessing the window object and is also considered good SEO practice.


**404 Page**
A custom 404 page is in place and will appear whenever a user navigates to a URL that doesn't exist. It includes navigation links back to the homepage and products page so users aren't left stranded.
<img width="1845" height="844" alt="image" src="https://github.com/user-attachments/assets/60eae8ca-d91c-4250-92f7-f70a74fb94a2" />

---

## Testing

### Manual Testing

**User Authentication**
| Test | Steps | Expected Outcome | Actual Outcome | Pass/Fail | 
|------|-------|------------------|----------------|-----------|
| User Registration | 1. Navigate to /accounts/signup 2. Fill in username, email and password 3. Click Register | Account created, verification email sent, redirect to confirmation page | Works as expected | ✅ Pass | 
| Login |1. Navigate to /accounts/login 2. Enter valid credentials 3. Click Login | User logged in, redirected to homepage, account name visible in nav | Works as expected | ✅ Pass |
| Logout | 1. Click My Account in nav 2. Click Logout | User logged out, redirected to homepage | Works as expected | ✅ Pass |
| Access restricted page when logged out | 1. Log out 2. Manually type /profile/ in the URL bar | Redirected to login page | Works as expected | ✅ Pass | 
| Register with duplicate email | 1. Navigate to /accounts/signup 2. Enter an email already registered 3. Submit | Error message displayed, account not created | Works as expected | ✅ Pass| 

<img width="1046" height="606" alt="image" src="https://github.com/user-attachments/assets/33c3291f-b7ab-4b90-b3d2-851fde7d6f1e" />
<img width="1888" height="267" alt="image" src="https://github.com/user-attachments/assets/605ae742-df55-420a-856f-e62d7e098460" />
<img width="1375" height="839" alt="image" src="https://github.com/user-attachments/assets/313ef365-5630-4c6c-b480-ef5c393727e3" />


**Shopping Experience**
| Test | Steps | Expected Outcome | Actual Outcome | Pass/Fail |
|------|-------|-----------------|----------------|-----------|
| Products display correctly | 1. Navigate to /products/ | All products visible with images, names and prices | Works as expected | ✅ Pass |
| Search for a product | 1. Type a product name into the search bar 2. Click the search button | Relevant products displayed in results | Works as expected | ✅ Pass |
| Sort by price ascending | 1. Click Price ↑ in the navigation | Products reorder from lowest to highest price | Works as expected | ✅ Pass |
| Sort by price descending | 1. Click Price ↓ in the navigation | Products reorder from highest to lowest price | Works as expected | ✅ Pass |
| Sort by rating | 1. Click Rating in the navigation | Products reorder by highest rating first | Works as expected | ✅ Pass |
| Add product to bag | 1. Click on a product 2. Click Add to Bag | Product added to bag, success toast appears, bag total updates | Works as expected | ✅ Pass |
| Update quantity in bag | 1. Navigate to bag 2. Change quantity 3. Click Update | Bag total recalculates correctly | Works as expected | ✅ Pass |
| Remove item from bag | 1. Navigate to bag 2. Click Remove on an item | Item removed, bag total updates | Works as expected | ✅ Pass |
<img width="1829" height="825" alt="image" src="https://github.com/user-attachments/assets/dbf56d6b-4941-445f-b3f8-527e70bcd270" />
<img width="1736" height="527" alt="image" src="https://github.com/user-attachments/assets/7849a352-101c-45dd-b49c-1710b4a2d6d2" />

**Checkout Process**

| Test | Steps | Expected Outcome | Actual Outcome | Pass/Fail |
|------|-------|-----------------|----------------|-----------|
| Checkout form validation | 1. Navigate to checkout 2. Leave required fields empty 3. Click Complete Order | Error messages shown on empty required fields | Works as expected | ✅ Pass |
| Successful payment | 1. Fill in checkout form 2. Enter test card 4242 4242 4242 4242, expiry 12/26, CVC 123 3. Click Complete Order | Order confirmed, success page displayed with order number | Works as expected | ✅ Pass |
| Declined payment | 1. Fill in checkout form 2. Enter test card 4000 0000 0000 0002 3. Click Complete Order | Payment declined error message displayed | Works as expected | ✅ Pass |
| Order confirmation displayed | 1. Complete a successful payment | Order confirmation page shows correct order number, items and delivery details | Works as expected | ✅ Pass |
| Webhook creates order | 1. Complete payment 2. Check Stripe dashboard webhook logs | Order created in database via webhook | Works as expected | ✅ Pass |
| Save delivery info to profile | 1. Check Save delivery info box at checkout 2. Complete order 3. Navigate to profile | Delivery information pre-filled in profile | Works as expected | ✅ Pass |
<img width="1819" height="809" alt="image" src="https://github.com/user-attachments/assets/078df0b5-442f-450c-ad52-11c2df3dee97" />
<img width="1682" height="765" alt="image" src="https://github.com/user-attachments/assets/9d6de5a5-388b-44fa-b217-72ec007976d8" />

**User Profiles**
| Test | Steps | Expected Outcome | Actual Outcome | Pass/Fail |
|------|-------|-----------------|----------------|-----------|
| View profile | 1. Log in 2. Click My Account 3. Click My Profile | Profile page displays with delivery info and order history | Works as expected | ✅ Pass |
| Save default delivery info | 1. Navigate to profile 2. Fill in delivery details 3. Click Update Information | Delivery info saved, success message displayed | Works as expected | ✅ Pass |
| Delivery info pre-fills checkout | 1. Save delivery info to profile 2. Navigate to checkout | Checkout form pre-filled with saved delivery info | Works as expected | ✅ Pass |
| Order history displays | 1. Complete an order 2. Navigate to profile | Past order visible in order history with correct details | Works as expected | ✅ Pass |
<img width="1773" height="797" alt="image" src="https://github.com/user-attachments/assets/b5e20657-ad96-4fc2-93fd-843874408da4" />

**Newsletter Subscriber**
| Test | Steps | Expected Outcome | Actual Outcome | Pass/Fail |
|------|-------|-----------------|----------------|-----------|
| Subscribe to newsletter | 1. Navigate to profile 2. Enter name and email 3. Click Subscribe | Success message displayed, email saved to database | Works as expected | ✅ Pass |
| Duplicate email blocked | 1. Subscribe with an email 2. Try to subscribe again with the same email | Error message displayed, duplicate not created | Works as expected | ✅ Pass |

**Admin**
| Test | Steps | Expected Outcome | Actual Outcome | Pass/Fail |
|------|-------|-----------------|----------------|-----------|
| Add product | 1. Log in as superuser 2. Navigate to /admin/ 3. Add a new product with image | Product appears in the store | Works as expected | ✅ Pass |
| Edit product | 1. Log in as superuser 2. Navigate to /admin/ 3. Edit an existing product | Changes reflected in the store | Works as expected | ✅ Pass |
| Delete product | 1. Log in as superuser 2. Navigate to /admin/ 3. Delete a product | Product removed from store | Works as expected | ✅ Pass |
| Non-superuser cannot access admin | 1. Log in as regular user 2. Manually type /admin/ in URL bar | Redirected away, access denied | Works as expected | ✅ Pass |

**404 Page**
| Test | Steps | Expected Outcome | Actual Outcome | Pass/Fail |
|------|-------|-----------------|----------------|-----------|
| Custom 404 displays | 1. Type a non-existent URL e.g. /thispagedoesnotexist | Custom 404 page displayed with navigation links back to site | Works as expected | ✅ Pass |

### Browser Compatibility
| Browser | Result |
|---------|--------|
| Chrome | ✅ Pass |
| Firefox | ✅ Pass |
| Safari | ✅ Pass |
| Edge | ✅ Pass |

### Responsiveness
| Screen Size | Result |
|-------------|--------|
| Desktop (1920px+) | ✅ Pass |
| Laptop (1024px - 1919px) | ✅ Pass |
| Tablet (768px - 1023px) | ✅ Pass |
| Mobile (320px - 767px) | ✅ Pass |

Tested on multiple screen sizes using Chrome DevTools. Mobile-first design ensures usability on all devices.

### Validator Testing

**HTML**
- No valid errors returned when passing through the [W3C Validator](https://validator.w3.org/)
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9d16ca10-5097-4199-9ac4-d75df90f6c5d" />


**CSS**
- No errors found when passing through the [Jigsaw Validator](https://jigsaw.w3.org/css-validator/)

**JavaScript**
- No warnings returned when passing through [JSHint](https://jshint.com/)
- (there is a comment about unused variables - these have been left in for continuity and in case I ever want to update the payment system to include using username and information)
  
**Python**
- All Python code follows PEP8 standards




### Known Issues

**Resolved Bugs**
- ✅ Fixed `NoReverseMatch` error by updating allauth URL names from `'login'` to `'account_login'`.
- ✅ Resolved Stripe Elements not loading by properly configuring `STRIPE_PUBLIC_KEY` in Heroku config vars.
- ✅ Fixed media files not displaying on Heroku by implementing Cloudinary storage with Django 6.0's `STORAGES` configuration.
- ✅ Fixed missing comma in `INSTALLED_APPS` causing module import errors.
- ✅ Fixed empty profile URLs in navigation causing app crashes.

**Unfixed Bugs**
- None currently identified

---

## Deployment

### Requirements
- Python 3.12+
- PostgreSQL database
- Stripe account (for payments)
- Cloudinary account (for media storage)


### Local Development Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/michelles-craft-room.git
cd michelles-craft-room
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create an `env.py` file in the root directory:
```python
import os

os.environ['SECRET_KEY'] = 'your-secret-key-here'
os.environ['DATABASE_URL'] = 'your-database-url'
os.environ['STRIPE_PUBLIC_KEY'] = 'your-stripe-public-key'
os.environ['STRIPE_SECRET_KEY'] = 'your-stripe-secret-key'
os.environ['STRIPE_WH_SECRET'] = 'your-webhook-secret'
os.environ['CLOUDINARY_CLOUD_NAME'] = 'your-cloud-name'
os.environ['CLOUDINARY_API_KEY'] = 'your-api-key'
os.environ['CLOUDINARY_API_SECRET'] = 'your-api-secret'
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run the development server**
```bash
python manage.py runserver
```
### Heroku Deployment

1. **Create a Heroku app**
```bash
heroku create your-app-name
```

2. **Add PostgreSQL database**
```bash
heroku addons:create heroku-postgresql:mini
```

3. **Set config vars in Heroku**
Go to Settings → Config Vars and add:
- `SECRET_KEY`
- `DATABASE_URL` (automatically added with PostgreSQL)
- `STRIPE_PUBLIC_KEY`
- `STRIPE_SECRET_KEY`
- `STRIPE_WH_SECRET`
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`

4. **Deploy to Heroku**
```bash
git push heroku main
```

5. **Run migrations on Heroku**
```bash
heroku run python manage.py migrate
```

6. **Create superuser on Heroku**
```bash
heroku run python manage.py createsuperuser
```

7. **Upload product images**
- Log into the admin panel at `https://your-app-name.herokuapp.com/admin/`
- Add products and upload images - they will be stored on Cloudinary

### Stripe Webhook Setup

1. Go to Stripe Dashboard → Developers → Webhooks
2. Add endpoint: `https://your-app-name.herokuapp.com/checkout/wh/`
3. Select events: `payment_intent.succeeded` and `payment_intent.payment_failed`
4. Copy the webhook signing secret to `STRIPE_WH_SECRET` config var

### Cloudinary Setup

1. Sign up at [cloudinary.com](https://cloudinary.com)
2. Get your Cloud Name, API Key, and API Secret from the dashboard
3. Add them to Heroku config vars
4. Images uploaded through Django admin will automatically be stored on Cloudinary

**Important for Django 6.0:** The project uses Django 6.0's new `STORAGES` configuration for Cloudinary integration instead of the deprecated `DEFAULT_FILE_STORAGE` setting.

---

## Credits

### Content
- All card designs and art prints created by Michelle (the site owner's mother)
- Product descriptions written by site owner
- The Code Instutute's Boutique ado was used in the basic setup of this website.
 
### Code
- Django documentation for framework guidance
- Stripe documentation for payment integration
- Code Institute's Boutique Ado walkthrough project for e-commerce structure inspiration
- Django Allauth documentation for authentication setup
- Cloudinary documentation for media storage implementation

### Technologies
- [Django](https://www.djangoproject.com/) - Web framework
- [Stripe](https://stripe.com/) - Payment processing
- [Cloudinary](https://cloudinary.com/) - Media storage
- [Heroku](https://www.heroku.com/) - Deployment platform
- [Bootstrap](https://getbootstrap.com/) - CSS framework

### Acknowledgments
- Code Institute for the learning materials and project inspiration
- Michelle for providing the beautiful artwork and card designs

PLEASE NOTE THE README.MD WAS WRITTEDN ALL IN ONE GO AND THE GITHUB COMMITS ONLY BEGAN YESTERDAY BECAUSE AN ERROR I MADE IN DEVELOPMENT LED TO GITHUB BEING WIPED INCLUDING MY README.MD AND MOST OF MY WORK THIS PAST WEEK. FORTUNATLY I HAD SAVED A COPY OF ME README.MD ELSEWHERE BEOFRE THIS ISSUE OCCURED.
