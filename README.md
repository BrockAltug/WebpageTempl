# Project Overview

This project consists of several files contributing to a Flask-based web application designed for user authentication and management.

## Files Overview

### 1. `app.py`

- **Purpose**: Contains the Flask application with routes managing user authentication, registration, dashboard display, user information, and logout.
- **Key Functionalities**:
    - **Routes**:
        - `/`: Renders the login page.
        - `/login`: Handles user login and authentication.
        - `/register`: Manages user registration.
        - `/delete_user`: Deletes a user from the database.
        - `/info`: Displays user information and allows user deletion.
        - `/dashboard`: Renders the dashboard page.
        - `/logout`: Logs out the user.
    - **Integration**:
        - Utilizes SQLite database for user data storage.

### 2. `make_db.py`

- **Purpose**: Creates an SQLite database file (`user_database.db`) and defines a table structure (`users`) for user registration.
- **Functionality**:
    - Establishes the database schema with columns for user ID, username, and password.

### 3. `dashboard.html`

- **Purpose**: Represents the dashboard view for authenticated users.
- **Content**:
    - Welcomes the user.
    - Provides links to logout and view user information.
    - Contains placeholders for dashboard content.

### 4. `index.html`

- **Purpose**: Serves as the login page.
- **Content**:
    - Login form with username and password fields.
    - Redirects to the dashboard upon successful login.

### 5. `info.html`

- **Purpose**: Displays user information and allows deletion of user accounts.
- **Content**:
    - Total registered accounts count.
    - Table listing usernames with delete options.
    - Link to navigate back to the dashboard.

### 6. `registration.html`

- **Purpose**: Provides a registration form for new users.
- **Content**:
    - Form to input username and password.
    - Validation for password matching and existing usernames.
    - Link to navigate to the login page.
