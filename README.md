# Flask Superheroes API

This project is a RESTful API built with Flask and SQLAlchemy that allows users to manage a database of superheroes and their powers.

## Owner

- **Name:** [JOSEPH MBURU]

## Project Description

The Flask Superheroes API provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on heroes, powers, and their associations. It features data validation, nested JSON responses, and email notifications.

## Features

-   **RESTful API:** Follows REST conventions for predictable and easy-to-use endpoints.
-   **View Heroes:** Get a list of all heroes or a single hero by their ID.
-   **View Powers:** Get a list of all powers or a single power by its ID.
-   **Update Powers:** Modify the description of an existing power.
-   **Assign Powers:** Create an association between a hero and a power, specifying the strength (`Weak`, `Average`, `Strong`).
-   **Data Validation:**
    -   A power's `description` must be at least 20 characters long.
    -   A hero-power `strength` must be one of 'Weak', 'Average', or 'Strong'.

## Project Setup and Installation

### Prerequisites

-   Python 3.8+
-   `pipenv` for managing packages.

### Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/J-JMN/Phase-4-superheroes-lab](https://github.com/J-JMN/Phase-4-superheroes-lab)
    cd Phase-4-superheroes-lab
    ```

3.  **Install Dependencies:**
    Use `pipenv` to create a virtual environment and install the required packages from the `Pipfile`.
    ```bash
    pipenv install
    ```

4.  **Activate the Virtual Environment:**
    ```bash
    pipenv shell
    ```

5.  **Seed the Database:**
    Run the seed script to populate the database with initial sample data.
    ```bash
    python app/seed.py
    ```

6.  **Run the Application:**
    Start the Flask development server.
    ```bash
    flask run
    ```
    The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

-   `GET /heroes`: Get all heroes.
-   `GET /heroes/<id>`: Get a specific hero and their powers.
-   `GET /powers`: Get all powers.
-   `GET /powers/<id>`: Get a specific power.
-   `PATCH /powers/<id>`: Update a power's description.
-   `POST /hero_powers`: Assign a power to a hero.

## Support and Contact

For questions or support, please open an issue in the GitHub repository or contact [Joseph Mburu] at [joseph.mburu3@student.moringaschool.com].



## License

This project is licensed under the MIT License.