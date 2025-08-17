# AstroWorld
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/SaiManoharDamerla/AstroWorld)

AstroWorld is a dynamic web application built with Django that provides users with personalized astrological insights. The platform offers a range of services, including Rashi chart generation, Zodiac sign determination, and daily horoscopes, all accessible through a user-friendly interface.

## Features

*   **User Authentication**: Secure sign-up, sign-in, and logout functionality. Includes a "Forgot Password" feature with OTP verification sent via email.
*   **User Profile**: After signing up, users can fill out their personal details which are then displayed on a dedicated profile page.
*   **Rashi Chart Generation**: Users can input their birth date and time to generate a detailed Rashi (Vedic astrology moon sign) chart, visualized as an SVG.
*   **Zodiac Sign Finder**: A simple tool for users to find their Western zodiac sign based on their birth date.
*   **Daily Horoscope**: Provides daily horoscope predictions for different zodiac signs.
*   **Feedback System**: Users can submit feedback and ratings about the application.
*   **Contact Form**: A functional contact form for users to send messages to the administrators.

## Technologies Used

*   **Backend**: Python, Django
*   **Frontend**: HTML, Tailwind CSS, JavaScript
*   **Database**: SQLite 3
*   **API**: [Free Astrology API](https://www.freeastrologyapi.com/) for generating horoscopes and Rashi charts.

## Local Setup and Installation

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/SaiManoharDamerla/AstroWorld.git
    cd AstroWorld/SDP
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```sh
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```sh
    pip install django requests
    ```

4.  **Configure Email and API Keys:**
    *   For the "Forgot Password" feature to work, you need to configure your email settings in `SDP/SDP/settings.py`. Replace the placeholder `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` with your own SMTP credentials.
    *   The project uses a hardcoded API key for `freeastrologyapi.com` in `SDP/app/views.py`. It is recommended to replace this with your own key.

5.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```

7.  Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Application Flow

1.  **Sign Up/Sign In**: New users can create an account. Existing users can sign in.
2.  **Enter User Details**: On the first login, users are prompted to provide their personal and contact information.
3.  **Homepage**: After login, users are directed to the homepage, where they can explore the application's features.
4.  **Services**:
    *   **Rashi Chart**: Navigate to Services -> Rashi Chart. Enter your birth details (date, month, year, time) to generate and view your Rashi chart and moon sign.
    *   **Zodiac Sign**: Navigate to Services -> Zodiac Sign. Enter your birth day and month to find out your corresponding zodiac sign.
    *   **Daily Horoscope**: Navigate to Services -> Daily Horoscope. Select your sign to read your daily horoscope.
5.  **Profile**: View your saved user information on the Profile page.
6.  **Feedback & Contact**: Use the "Feedback" and "Contact Us" pages to communicate with the site administrators.