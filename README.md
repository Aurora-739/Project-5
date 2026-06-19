# Michelle's Craft Room
Michelle's Craft Room is a full-stack e-commerce website built with Django that sells digital PNG cards and art prints. The site provides a complete online shopping experience with user authentication, shopping cart functionality, secure payment processing via Stripe, order management, product reviews, a wishlist system, and category-based browsing.

<img width="1920" height="877" alt="image" src="https://github.com/user-attachments/assets/fa8beeb3-f0e7-43e2-bb17-ca5a92b3757a" />
<img width="1920" height="868" alt="image" src="https://github.com/user-attachments/assets/00efb5a8-5196-4898-b39d-f1edbc7223a1" />

[Live Site](https://project-5-michelles-craft-room-cdc5efe9b632.herokuapp.com/)

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
I chose to document my user stories using two Agile tools. The user stories themselves are written out on a Google Sheet laid out as a kanban-style board, which works well for a solo developer as it keeps things simple and easy to follow. I also used GitHub Projects to track progress throughout development, moving issues through columns as they were worked on and completed.
[View User Stories Google Sheet](https://docs.google.com/spreadsheets/d/1tD8bA1ClfzmBbyvkxD35EFTUJaqyDd4cXXsyrhJOCPY/edit?usp=sharing)
[View GitHub Project Board](https://github.com/users/Aurora-739/projects/14/views/1)

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
- Collections dropdown in the top navigation for quick category browsing.
- Search functionality supporting product name, description and category name.
- Sorting options (price, rating, name) for product browsing.
- Shopping bag always visible with running total.
- My Account dropdown with links to profile, wishlist and logout.

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

<img width="1875" height="861" alt="image" src="https://github.com/user-attachments/assets/f703d2ed-3e92-487c-b9ec-2d4790abd649" />
<img width="1883" height="216" alt="image" src="https://github.com/user-attachments/assets/ac748a95-b591-4afd-bf14-ca847802d756" />

#### **Product Catalogue**
- Browse all available PNG cards and art prints.
- Product details pages with images, descriptions, and pricing.
- Filter products by category using the Collections dropdown or category filter on the products page.
- Search by product name, description or category.
- Sort by price, rating or name.
- Products display live average rating calculated from customer reviews.

<img width="1920" height="877" alt="image" src="https://github.com/user-attachments/assets/b6388476-af2c-407c-aafb-c3eedcc64b1b" />
<img width="1920" height="874" alt="image" src="https://github.com/user-attachments/assets/fa1369e0-98fd-4480-ae75-7f7e18931151" />
<img width="1920" height="871" alt="image" src="https://github.com/user-attachments/assets/acb0e8b3-cd27-475e-80a1-70a3795e9af9" />
<img width="1920" height="877" alt="image" src="https://github.com/user-attachments/assets/db60e302-20ae-42c4-ad09-45e5c7f2044f" />

#### **Product Reviews**
- Authenticated users can post a review with a star rating (1-5) and written comment.
- Reviews display on the product detail page with username, star rating and date.
- Users can edit or delete only their own reviews.
- Defensive design prevents users from editing other users' reviews via URL manipulation.
- Products display a live calculated average rating based on submitted reviews.
- Users who have not yet reviewed a product see the review form; existing reviewers see their review with edit/delete options.

<img width="1920" height="855" alt="image" src="https://github.com/user-attachments/assets/3afd0963-5158-4b58-bace-575b8ef4dace" />

#### **Wishlist**
- Authenticated users can add products to a personal wishlist from the product detail page.
- The wishlist is accessible via My Account → My Wishlist in the navigation.
- Users can remove products from their wishlist.
- Duplicate detection prevents the same product being added twice, with an informative message displayed instead.
- Unauthenticated users are redirected to the login page if they attempt to access wishlist functionality.

<img width="1905" height="241" alt="image" src="https://github.com/user-attachments/assets/632793e4-2531-417a-b249-68331a87e474" />
<img width="1920" height="860" alt="image" src="https://github.com/user-attachments/assets/a727ee50-c8d2-4b9a-8e86-aab9327460b0" />
<img width="1920" height="870" alt="image" src="https://github.com/user-attachments/assets/3a07b080-ddd9-40da-ba3f-8a0aa51aae61" />

#### **Shopping Bag**
- Add products to shopping bag
- Adjust quantities or remove items
- Update-able total calculation
- Bag contents persist across sessions

<img width="1898" height="884" alt="image" src="https://github.com/user-attachments/assets/c908de6a-39a6-4dc7-9941-6db125630bca" />
<img width="1893" height="681" alt="image" src="https://github.com/user-attachments/assets/dbd9e15e-8c32-400d-bc84-9e1bfa24a68d" />


#### **Secure Checkout**
- Stripe payment integration for secure card processing.
- Order form with delivery information.
- Option to save delivery details to user profile for faster future checkouts.
- Real-time payment validation.

<img width="1883" height="878" alt="image" src="https://github.com/user-attachments/assets/8d389acd-c638-44b8-af1b-e91aba71614e" />
<img width="1874" height="740" alt="image" src="https://github.com/user-attachments/assets/c522d992-c9a1-4c08-973f-debc68a6b9a4" />
<img width="1751" height="702" alt="image" src="https://github.com/user-attachments/assets/a5fbba90-fc7f-4f75-9d49-7c3d2a647dce" />
<img width="1903" height="645" alt="image" src="https://github.com/user-attachments/assets/995eb84e-f201-486e-90d6-6eea76f817df" />

#### **Order Management**
- Order confirmation page with order number.
- Confirmation emails sent to the customer's email address after a successful payment, including product download links via Cloudinary URLs.
- Order history stored in user profiles.
- Webhook handlers ensure orders are created even if user closes browser.

<img width="550" height="678" alt="image" src="https://github.com/user-attachments/assets/2078f2c9-435a-41ed-99ca-7e33129c5319" />

#### **Newsletter Subscription**
- Users can subscribe to the newsletter via the Newsletter Signup link in the footer or from their profile page.
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
- Stores product information (name, description, price, image, SKU).
- ManyToManyField relationship with Category.
- Custom `average_rating()` method calculates live rating from related Reviews.

### **Category**
- Stores product categories (name and friendly_name).
- ManyToMany relationship with Product allows products to belong to multiple categories.

### **Order**
- Stores customer order details (full name, email, delivery address, order total).
- Links to UserProfile if user is authenticated.

### **OrderLineItem**
- Represents individual products within an order.
- Links to both Order and Product models.

### **UserProfile**
- Stores user's default delivery information.
- Links to Django's built-in User model.

### **Review** *(Custom Model)*
- Stores customer reviews for products.
- ForeignKey to both Product and User.
- Rating (1-5), comment, and timestamps.
- Unique together constraint prevents duplicate reviews per user per product.
- Powers the `average_rating()` method on Product.

### **Wishlist** *(Custom Model)*
- One-to-one relationship with User (each user has one wishlist).
- ManyToManyField to Product allowing multiple saved products.
- Add/remove functionality with duplicate detection.

### **NewsletterSubscriber** *(Custom Model)*
- Stores newsletter signups (name, email, date subscribed).
- Unique email constraint prevents duplicate subscriptions.

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
This meta description summarises the site's purpose clearly for both search engines and browsing search results. 

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
<img width="1890" height="894" alt="image" src="https://github.com/user-attachments/assets/ecad65ae-02be-42d7-811a-8a96390d484c" />

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
| Filter by category via nav | 1. Click Collections in nav 2. Select a category | Only products in that category displayed | Works as expected | ✅ Pass |
| Search by category name | 1. Type a category name e.g. "floral" in the search bar 2. Click search | Products in that category displayed in results | Works as expected | ✅ Pass |
| Category filter dropdown | 1. Navigate to /products/ 2. Select a category from the All Categories dropdown | Products filtered to selected category | Works as expected | ✅ Pass |
<img width="1920" height="806" alt="image" src="https://github.com/user-attachments/assets/a9731ae9-7289-440f-8b79-10b4ac42bb24" />
<img width="1920" height="873" alt="image" src="https://github.com/user-attachments/assets/d7020cc5-9330-474f-bb0a-5e4a8474dfbc" />

**Checkout Process**

| Test | Steps | Expected Outcome | Actual Outcome | Pass/Fail |
|------|-------|-----------------|----------------|-----------|
| Checkout form validation | 1. Navigate to checkout 2. Leave required fields empty 3. Click Complete Order | Error messages shown on empty required fields | Works as expected | ✅ Pass |
| Successful payment | 1. Fill in checkout form 2. Enter test card 4242 4242 4242 4242, expiry 12/26, CVC 123 3. Click Complete Order | Order confirmed, success page displayed with order number | Works as expected | ✅ Pass |
| Declined payment | 1. Fill in checkout form 2. Enter test card 4000 0000 0000 0002 3. Click Complete Order | Payment declined error message displayed | Works as expected | ✅ Pass |
| Order confirmation displayed | 1. Complete a successful payment | Order confirmation page shows correct order number, items and delivery details | Works as expected | ✅ Pass |
| Webhook creates order | 1. Complete payment 2. Check Stripe dashboard webhook logs | Order created in database via webhook | Works as expected | ✅ Pass |
| Save delivery info to profile | 1. Check Save delivery info box at checkout 2. Complete order 3. Navigate to profile | Delivery information pre-filled in profile | Works as expected | ✅ Pass |
| Confirmation email sent | 1. Complete a successful payment 2. Check email inbox | Email received containing order details and product download links | Works as expected | ✅ Pass |
<img width="1905" height="641" alt="image" src="https://github.com/user-attachments/assets/5b598d85-d987-481c-899a-3aa381976ffe" />
<img width="1894" height="710" alt="image" src="https://github.com/user-attachments/assets/ba988b76-01f7-4ef1-b7bb-be9c9bad1ead" />


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

**Product Reviews**
| Test | Steps | Expected Outcome | Actual Outcome | Pass/Fail |
|------|-------|-----------------|----------------|-----------|
| Post a review | 1. Log in 2. Navigate to a product 3. Fill in rating and comment 4. Click Post Review | Review appears on product page with username, stars and date | Works as expected | ✅ Pass |
| Edit own review | 1. Log in 2. Navigate to a product with your review 3. Update the form 4. Click Update Review | Review updated with new content | Works as expected | ✅ Pass |
| Delete own review | 1. Log in 2. Navigate to a product with your review 3. Click Delete Review 4. Confirm deletion | Review removed from product page | Works as expected | ✅ Pass |
| Cannot edit another user's review | 1. Log in as a different user 2. Manually type the edit URL for another user's review | Redirected or 404 error, review not editable | Works as expected | ✅ Pass |
| Average rating updates after review | 1. Post a review with a rating 2. Return to products page | Product card shows updated average rating | Works as expected | ✅ Pass |
| Duplicate review blocked | 1. Post a review 2. Try to post another review on the same product | Error message shown, duplicate not created | Works as expected | ✅ Pass |

<img width="1325" height="380" alt="image" src="https://github.com/user-attachments/assets/8aa7aaf0-9e96-4f34-9974-d4a50e53322a" />


**Wishlist**
| Test | Steps | Expected Outcome | Actual Outcome | Pass/Fail |
|------|-------|-----------------|----------------|-----------|
| Add to wishlist | 1. Log in 2. Navigate to a product 3. Click Add to Wishlist | Product added to wishlist, success message shown | Works as expected | ✅ Pass |
| View wishlist | 1. Log in 2. Click My Account → My Wishlist | Wishlist page displays all saved products | Works as expected | ✅ Pass |
| Remove from wishlist | 1. Navigate to wishlist 2. Click Remove on a product | Product removed, wishlist updates | Works as expected | ✅ Pass |
| Duplicate detection | 1. Add a product to wishlist 2. Try to add the same product again | "Already in your wishlist" message shown, no duplicate added | Works as expected | ✅ Pass |
| Wishlist requires login | 1. Log out 2. Try to access /products/wishlist/ | Redirected to login page | Works as expected | ✅ Pass |

<img width="1925" height="911" alt="image" src="https://github.com/user-attachments/assets/e36e718a-af48-4aed-95af-3a570b83eaae" />

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
<img width="1563" height="718" alt="image" src="https://github.com/user-attachments/assets/91d58319-7ada-4b1c-ad72-17e4fd51f38b" />

**CSS**
- No errors found when passing through the [Jigsaw Validator](https://jigsaw.w3.org/css-validator/)
<img width="1535" height="679" alt="image" src="https://github.com/user-attachments/assets/1d2f600d-b291-43a5-8f91-7a12db6d9308" />

**JavaScript**
- No warnings returned when passing through [JSHint](https://jshint.com/)
<img width="1514" height="695" alt="image" src="https://github.com/user-attachments/assets/223e886f-bad4-467c-8631-ec18144fd2ba" />
  
**Python**
- All Python code follows PEP8 standards

Bag:

admin.py (no errors found):
<img width="1535" height="656" alt="image" src="https://github.com/user-attachments/assets/d29a876b-bb58-4910-b960-8eef60f59d03" />
apps.py (no errors found);
<img width="1464" height="690" alt="image" src="https://github.com/user-attachments/assets/4f792414-5d61-4697-9956-0bee62244b52" />
contexts.py (no errors found):
<img width="1498" height="670" alt="image" src="https://github.com/user-attachments/assets/7c077b16-68a2-4de1-83d3-7b8bb8c69a56" />
models.py (no errors found):
<img width="1514" height="697" alt="image" src="https://github.com/user-attachments/assets/46f7acb6-11c5-4e7c-82a7-ddcd7d23acd9" />
tests.py (no errors found):
<img width="1377" height="655" alt="image" src="https://github.com/user-attachments/assets/7b2e38c7-721a-4687-8039-ace6015f2f3c" />
urls.py (no errors found):
<img width="1392" height="657" alt="image" src="https://github.com/user-attachments/assets/c690d2bd-a5d0-48dd-ad32-eba221abf292" />
views.py (1 issue found: E501 line too long (109 > 79 characters) on line 63. This is due to long string expressions, complex function calls, or Stripe API calls which have been left as single lines for readability.):
<img width="1432" height="680" alt="image" src="https://github.com/user-attachments/assets/1bdb0ecd-f06d-4e7d-b41b-cb60eb618934" />

Checkout:

views.py (no errors found):
<img width="1772" height="831" alt="image" src="https://github.com/user-attachments/assets/8370d730-f6b0-4cc1-9f42-7e8e53a2be36" />
apps.py (no errors found):
<img width="1364" height="641" alt="image" src="https://github.com/user-attachments/assets/fd48fa5b-99c1-4462-b6da-614b49034bcf" />
forms.py (1 issue found: E501 line too long (95 > 79 characters) on line 7. This is due to long string expressions, complex function calls, or Stripe API calls which have been left as single lines for readability.):
<img width="1343" height="654" alt="image" src="https://github.com/user-attachments/assets/d3128de2-789d-4d45-9fd8-ddd54bf8d991" />
models.py (6 issues found: all E501 line too long errors on lines 10, 21, 32, 45, 46 and 48. These are due to long model field definitions which have been left as single lines for readability.):
<img width="1454" height="653" alt="image" src="https://github.com/user-attachments/assets/9ebf61b5-09be-4e4e-8eb6-76e6f7772421" />
signals.py (no errors found):
<img width="1364" height="652" alt="image" src="https://github.com/user-attachments/assets/285daad2-4fc5-43ff-99ac-4011cd6b692f" />
tests.py (no errors found):
<img width="1389" height="675" alt="image" src="https://github.com/user-attachments/assets/f0710ad0-7d13-4e4f-b983-8b2ac983fe2f" />
urls.py (2 issues found: E501 line too long errors on lines 10 and 12. These are due to long URL path definitions which have been left as single lines for readability.):
<img width="1443" height="653" alt="image" src="https://github.com/user-attachments/assets/b916c765-84fd-467f-80b4-7e7ab6ea7eea" />
views.py ( 8 issues found, all E501 line too long errors on lines 2, 7, 83, 110, 117, 119, 123 and 138. These are due to long import statements, Stripe API calls and string expressions which have been left as single lines for readability.):
<img width="1323" height="630" alt="image" src="https://github.com/user-attachments/assets/887fe20e-556a-4aa3-b3e0-e6c54d82d62f" />


Home:

admin.py (no errors found):
<img width="1368" height="651" alt="image" src="https://github.com/user-attachments/assets/18a06b82-3e9e-4e3a-bcb7-8a4c578a334b" />
apps.py (no errors found):
<img width="1404" height="663" alt="image" src="https://github.com/user-attachments/assets/8098066e-3964-42a7-9c5b-4f846f604e91" />
models.py (no errors found):
<img width="1417" height="652" alt="image" src="https://github.com/user-attachments/assets/9e347492-0226-431c-abe6-146fa23ed5f5" />
tests.py (no errors found):
<img width="1420" height="659" alt="image" src="https://github.com/user-attachments/assets/32796a9a-705d-4536-809c-a0ae64491865" />
views.py (no errors found):
<img width="1430" height="643" alt="image" src="https://github.com/user-attachments/assets/4f773cdd-eec0-4a57-b359-ae9f78352023" />

Pdf_shop:

asgi.py (no errors found):
<img width="1408" height="673" alt="image" src="https://github.com/user-attachments/assets/dcf0abcc-8178-4284-8c1e-9ae27c7b20fa" />
settings.py (8 issues found, all E501 line too long errors on lines 37, 107, 142, 144, 145, 197, 199 and 213. These are due to long configuration strings and environment variable definitions which have been left as single lines for readability.):
<img width="1402" height="643" alt="image" src="https://github.com/user-attachments/assets/44507094-786c-4cc1-b815-5d13726b040f" />
urls.py (4 issues found, all E501 line too long errors on lines 28, 29, 31 and 41. These are due to long URL path definitions and inline comments which have been left as single lines for readability.):
<img width="1374" height="652" alt="image" src="https://github.com/user-attachments/assets/bd3426f7-a60d-434e-acf7-8f65262c1e49" />
views.py (2 issues found, both E501 line too long errors on lines 20 and 36. These are due to long authentication function calls which have been left as single lines for readability.):
<img width="1420" height="653" alt="image" src="https://github.com/user-attachments/assets/8029a50a-0553-40a6-b4ff-e5e47fae0f45" />
wsgi.py (no errors found):
<img width="1357" height="639" alt="image" src="https://github.com/user-attachments/assets/b2fdd2fb-75c9-4fd6-9b14-31f6dc86b13d" />

Products:

admin.py (no errors found):
<img width="1393" height="651" alt="image" src="https://github.com/user-attachments/assets/6d340aa0-8609-46f7-8f92-52dd0d74d670" />
apps.py (no errors found):
<img width="1417" height="639" alt="image" src="https://github.com/user-attachments/assets/a5f5b4eb-d0a9-4f5a-8cee-3fdc407a2013" />
forms.py (2 issues found, both E501 line too long errors on lines 13 and 16. These are due to a long widget choice definition with an inline comment which have been left as single lines for readability.):
<img width="1358" height="646" alt="image" src="https://github.com/user-attachments/assets/0c06b238-5445-4f4c-8806-cf3134b15009" />
models.py (6 issues found, all E501 line too long errors on lines 28, 39, 47, 48, 63 and 64. These are due to long model field definitions which have been left as single lines for readability.):
<img width="1383" height="653" alt="image" src="https://github.com/user-attachments/assets/836ab0ec-2a8c-4ad9-abb9-2197a9e51748" />
tests.py (no errors found):
<img width="1366" height="622" alt="image" src="https://github.com/user-attachments/assets/50a81692-1b53-4857-a0b9-d5359f7dacde" />
urls.py (4 issues found, all E501 line too long errors on lines 12, 13, 14 and 15. These are due to long URL path definitions with view names which have been left as single lines for readability.):
<img width="1330" height="648" alt="image" src="https://github.com/user-attachments/assets/0fa5dbe4-c575-42c9-b838-0d7cf23bd0e3" />
views.py (4 issues found, all E501 line too long errors on lines 13, 22, 30 and 52. These are due to long database query annotations, complex Q object filter expressions and category filter queries which have been left as single lines for readability.):
<img width="1342" height="632" alt="image" src="https://github.com/user-attachments/assets/8f7aaef2-bd2b-41f2-b0ed-b4ab7d25c6cb" />


Store:

admin.py (no errors found):
<img width="1336" height="649" alt="image" src="https://github.com/user-attachments/assets/d6f1da4a-1a42-4a69-ab89-c4691a0b3379" />
apps.py (no errors found):
<img width="1374" height="630" alt="image" src="https://github.com/user-attachments/assets/6ca7520e-6d25-4842-b3c1-416d8bdd8483" />
models.py (no errors found):
<img width="1359" height="625" alt="image" src="https://github.com/user-attachments/assets/68b9fd5b-6685-4244-a916-a961a8f51d67" />
tests.py (no errors found):
<img width="1327" height="637" alt="image" src="https://github.com/user-attachments/assets/52332797-29d5-47be-9bba-260547aa6889" />
views.py (no errors found):
<img width="1313" height="622" alt="image" src="https://github.com/user-attachments/assets/556190fc-b3ec-4155-af42-19642b2cca36" />

Profiles:

admin.py (no errors found):
<img width="1321" height="653" alt="image" src="https://github.com/user-attachments/assets/37e76745-316e-4fe8-a7aa-f64963ca1c2b" />
forms.py (3 issues found, all E501 line too long errors on lines 35, 44 and 45. These are due to long widget attribute definitions which have been left as single lines for readability.):
<img width="1362" height="640" alt="image" src="https://github.com/user-attachments/assets/9c29cbe9-639c-48b6-b45a-914f9b22780e" />
models.py (5 issues found, all E501 line too long errors on lines 11, 12, 13, 14 and 17. These are due to long model field definitions which have been left as single lines for readability.):
<img width="1347" height="636" alt="image" src="https://github.com/user-attachments/assets/2cc44ead-34a8-4b2b-a1e7-3bd2f0f80313" />
urls.py (1  issue found: E501 line too long (89 > 79 characters) on line 11. This is due to a long URL path definition which has been left as a single line for readability.):
<img width="1347" height="637" alt="image" src="https://github.com/user-attachments/assets/faecdc4d-64eb-4690-a922-07f026d7b3a6" />
views.py (3 issues found, all E501 line too long errors on lines 27, 44 and 60. These are due to long string expressions and function calls which have been left as single lines for readability.):
<img width="1352" height="621" alt="image" src="https://github.com/user-attachments/assets/eb45dde6-e088-4ba9-96ee-c247c5dc59f9" />

All Python files were passed through the CI Python Linter. Some E501 line too long warnings are present due to long string expressions and Stripe API calls that cannot be shortened without breaking functionality.

### Known Issues

**Resolved Bugs**
- ✅ Fixed `NoReverseMatch` error by updating allauth URL names from `'login'` to `'account_login'`.
- ✅ Resolved Stripe Elements not loading by properly configuring `STRIPE_PUBLIC_KEY` in Heroku config vars.
- ✅ Fixed media files not displaying on Heroku by implementing Cloudinary storage with Django 6.0's `STORAGES` configuration.
- ✅ Fixed missing comma in `INSTALLED_APPS` causing module import errors.
- ✅ Fixed empty profile URLs in navigation causing app crashes.
- ✅ Fixed site-wide 500 error caused by `CompressedManifestStaticFilesStorage` missing manifest file — switched to `CompressedStaticFilesStorage`.
- ✅ Fixed `NoReverseMatch` error in `checkout_success.html` caused by deprecated `products:products` URL name — updated to `products:all_products`.
- ✅ Fixed profile page 500 error caused by incorrect `order.grand_total` field reference — updated to `order.order_total`.
- ✅ Fixed newsletter redirect loop — corrected success redirect in the `newsletter_signup` view.
- ✅ Fixed duplicate `products.html` template in the `home` app being loaded instead of the correct `products` app template.
- ✅ Fixed wishlist add URL routing conflict with product detail URL pattern — moved `wishlist/` path above `<str:sku>/` in `products/urls.py`.

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
