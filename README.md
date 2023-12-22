# Sqlalchemy Basics 

## Project Overview
Sqlalchemy Basics is a Python application designed to explore the capabilities and strengths of SQLAlchemy when interfacing with a PostgreSQL database. The project sets up a virtual environment with a PostgreSQL server and utilizes SQLAlchemy for ORM. It includes models for actors, movies, contact details, and stuntmen, with defined relationships between them.

### Features
- **Database Setup and Connection**: Set up a PostgreSQL database in a VirtualBox VM with bridged networking by using Vagrantfile.
- **Model Definition**: Define SQLAlchemy ORM models for actors, movies, contact details, and stuntmen.
- **Relationships**: Establish relationships between models to reflect real-world connections between data entities.
- **Logging**: Implement logging to track the application's behavior and any errors.

## Prerequisites
- Python 3.10
- VirtualBox
- Vagrant
- A PostgreSQL server running on a VM
- `sqlalchemy` library
- Other Python libraries as required by the project

## Installation

### Setting up the Virtual Environment
1. **Clone the repository**:
git clone https://github.com/mucahitkls/sqlalchemy_basics.git

2. **Navigate to the project directory**:
cd project_directory


### Setting up the Database
1. **Create a PostgreSQL VM**: Ensure you have a running PostgreSQL database in a VirtualBox VM with bridged networking.
2. **Create a database and user**: Set up your PostgreSQL database and user with the necessary permissions.

### Installing Dependencies
1. **Install Python dependencies**:
pip install -r requirements.txt

- This will start the application and perform any predefined tasks or scripts.

## Usage
- **Creating Models**: Use the provided model classes to create new instances of actors, movies, etc., and commit them to the database.
- **Querying**: Utilize SQLAlchemy sessions to query the database for information on the stored entities.
- **Relationship Management**: Explore how relationships between entities (like actors and their stuntmen) are managed and queried.

## Contributing
- If you'd like to contribute to this project, please fork the repository and submit a pull request.

## Acknowledgements
- auth0 SQLAlchemy ORM Tutorial: https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

## Contact Information
- Your Name - kelessmucahit@gmail.com
- Project Link: https://github.com/mucahitkls/sqlalchemy_basics

