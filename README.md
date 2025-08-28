# CookShelf
#### Video Demo:

#### Description:

CookShelf is a personal digital recipe manager built using Python(Flask), HTMl, CSS, JavaScript, and SQLite. It allows users to securely register, log in, and create, view, and organize their favorite recipes in a clean and intuitive interface. Insprired by the simplicity and warmth of Scandinavian design, CookShelf is both functionally and visually tailored to make recipe saving feel personal and cozy.

## Overview

CookShelf is designed for users who want to build their own curated collection of recipes, whether they are daily go-to meals or special-occasion treats. Users can store details such as title, ingredients, instruction, category, cooking time, and difficulty. This website also includes user authentication, session management, flash messaging, and responsive layout.

## Features

- User registration and login with hashed password storage
- Flash message for feedback (errors and success)
- Recipe creation form with required fields
- Viewing all personal recipes on the main page
- View a full single-recipe page
- Delete recipe functionality with confirmation prompt
- Responsive design that works across screen sizes
- A welcoming homepage for guests

## File Descriptions

### app.py
This is the core backend file that contains all routing logic and business logic. It uses Flask to define endpoint for:
- /: Displays recipes for the logged-in user or a welcome page for guests
- /register: Handles new user registration
- /login: Authenticates existing users
- /logout: Clears session and logs user out
- /create: Allows users to add a new recipe
- /recipe/<id>: Displays the full recipe content
- /delete/<id>: Deletes a user-owned recipe

It also includes logic to check if a user is logged in (session management), flash message handling, and redirects based on authentication state.

### schema.sql
This file defines the structure of the SQLite database used by the application. It includes two tables:
- users: Stores id, username, and hashed password
- recipe: Stores recipe data with fields like title, ingredients, instructions, etc., linked by a user_id foreign key

### recipe.db
This is the SQLite database generated from schema.sql, containing persistent user and recipe data.

### templates/layout.html
A base template that defines the HTML structure used across the site. It includes the <head>, navigation bar, flash message display, and footer. All other pages extend this layout.

### templates/welcome.html
A friendly landing page that appears for guests (not logged in). It inroduces the app's functionality and encourages users to register or log in.

### templates/index.html
Displays a list of the user's personal recipes, each in a card format. Includes a link to view or delete individual recipes.

### templates/create.html
Contains the form for creating a new recipe. Fields include title, ingredients, instructions, category, cooking time, and difficulty.

### templates/recipe.html
Displays the full details of a single recipe, rendered when clicking "View Recipe."

### templates/login.html and register.html
Forms for logging in and creating an account, respectively. These use Bootstrap classes and inherit from layout.html.

### static/style.css
Custom CSS that implements a warm, Scandinavian-inspired color palette and layout styling. The CSS uses soft browns, beige, and light grays to support a calming visual experience. It includes styles for:
- body, form, recipe-card
- Buttons, alerts, input fields
- Layout elements such as sticky footers using Flexbox

### static/script.js
Currently minimal, reserved for future JavaScript enhancements like client-side validation or interactivity (e.g., favorite recipes)

## Design Decisions

### Scandinavian Theme
The color palette was chosen to fell homey and neutral, prioritizing simplicity and a light visual experience over sharp contrast. This theme is inspired by Scandinavian interior design: natural, calming, and user-friendly.

### Session Security
Flask's session management is used with a manually set secret_key to protect user sessions. Passwords are hashed using Werkzeug's security methods.

### Authentication FLow
Routes like /create, /, and /recipe/<id> are protected by session checks. If a user is not logged in, they are redirected to /login.

### Separation of Templates
Templates are modular and reusable. Layout inheritance reduces duplication, and each user-facing page has a dedicated file, making it easy to maintain.

### Flash Messages
Flask's flash() functionality is used extensively to give users feddbacj, especially during login, registration, and recipe creation.

### Flexbox for Footer
A sticky footer implementation was done using Flexbox to ensure the footer stays as the bottom on short pages like welcome.html.

### Future Improvements
- edit recipe functionality
- recipe tags or filtering
- uploading images per recipe
- favorite sysyem (e.g. ♥ for quick access)
- light/dark theme toggle
- export/import recipe collection

## Summary
CookShelf. is a CS50 final project designed with care to deliver a smooth and cozy digital recipe management experience. It focuses on clean design, useful core functionality, and thoughtful user interaction. The project showcases a blend of backend logic with front-end visual quality and makes room for future enhancements.


---

**Project Metadata**

-**Name:** Fazi Atabaeva
-**GitHub Username:** [a-fazi](https://github.com/a-fazi)
-**edX Username:** afazi_
-**Location:** Nuremberg, Germany
