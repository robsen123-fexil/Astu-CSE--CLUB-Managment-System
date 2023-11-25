

# Database Configuration for Your Project

## Overview

This repository contains the source code for a project that involves user management, event tracking, and contests. It uses a simple authentication system with an admin account having privileged access to manage users, events, and user information. The database is configured with the following credentials:

- **Database Admin:**
  - Username: `admin`
  - Password: `12345`

## Admin Authority

The admin account is the primary authority for database management. Admins can perform the following actions:

### Registering New Users

Admins have the ability to register new users by providing the necessary information, including:

- First Name
- Last Name
- Email
- Username
- Temporary Password

#### Temporary Password

When an admin registers a new user, a temporary password is assigned to the user. This temporary password is a security measure to ensure initial access. Upon first login, users are required to change their temporary password to a secure one.

### User Registration Workflow

1. **Admin Registration:**
   - Admins navigate to the registration page to add a new user.
   - They input the user's first name, last name, email, username, and assign a temporary password.
   - A unique temporary password is generated for added security.

2. **User First Login:**
   - Users receive their temporary password and log in for the first time.
   - The system prompts users to change their temporary password immediately.

3. **Password Update:**
   - Users set their own secure password during the initial login.
   - This step ensures that users have control over their account security.

