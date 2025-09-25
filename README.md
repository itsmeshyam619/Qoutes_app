# "Qoutes" App

A simple web application to view, add, edit, and delete motivational quotes. Built with Python (Flask), HTML, CSS, and Prometheus metrics for monitoring.

## Features

- **View all quotes**
- **Get a random quote**
- **Add new quotes**
- **Edit existing quotes**
- **Delete quotes**
- **Responsive UI** with a modern design
- **Prometheus metrics** integration for monitoring

## Technologies Used

- Python 3
- Flask
- HTML/CSS (custom styles)
- Prometheus Flask Exporter

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository:
    ```shell
    git clone https://github.com/itsmeshyam619/Qoutes_app.git
    cd Qoutes_app
    ```

2. Install dependencies:
    ```shell
    pip install -r requirements.txt
    ```

3. Run the app:
    ```shell
    python app.py
    ```

4. Open your browser and go to [http://localhost:5000](http://localhost:5000)

## API Endpoints
initially these endpoints are used for generating random jokes , so read the code once before you modify it..

- `GET /jokes` — Get all quotes
- `GET /jokes/random` — Get a random quote
- `GET /jokes/<id>` — Get quote by ID
- `POST /jokes` — Add a new quote (`{"text": "Your quote"}`)
- `PUT /jokes/<id>` — Update a quote (`{"text": "Updated quote"}`)
- `DELETE /jokes/<id>` — Delete a quote

## Monitoring

Prometheus metrics are available for integration and monitoring Flask endpoints.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)

---

**Enjoy sharing DevOps wisdom and humor!**
