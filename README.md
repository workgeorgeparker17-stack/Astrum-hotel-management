# 🏨 Astrum Hotel Management System

A simple command-line application for managing hotel guests, built with Python and JSON for data persistence. This project was developed as a hands-on exercise in file I/O, data validation, and CRUD (Create, Read, Update, Delete) operations — core concepts for backend development.

## 📋 Features

- **Add a guest** — register a new guest with name, room number, and phone number
- **Remove a guest** — delete a guest from the system by ID
- **List all guests** — view every currently registered guest
- **Duplicate room prevention** — the system checks that a room isn't already occupied before adding a new guest
- **Phone number validation** — ensures phone numbers follow the Uzbekistan format (`+998...`)
- **Persistent storage** — all data is saved to a local JSON file, so guest records survive between program runs
- **Input safety** — handles invalid input (e.g. entering text instead of a number) without crashing

## 🛠️ Built With

- **Python 3** — core application logic
- **JSON** — lightweight data storage (no external database required)
- Built-in modules: `json`, `os`

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher installed on your machine

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/workgeorgeparker17-stack/Astrum-hotel-management.git
   ```
2. Navigate into the project folder:
   ```bash
   cd Astrum-hotel-management
   ```
3. Run the program:
   ```bash
   python Mehmonhona_astronum.py
   ```

No external dependencies needed — the project runs with Python's standard library only.

## 💻 Usage

When you run the program, you'll see a simple menu:

```
Welcome to Astronum plaza hotel

    1 - Add a guest
    2 - Remove a guest
    3 - Guests list 
    
    0 - Leave the app
```

| Option | Action |
|--------|--------|
| `1` | Add a new guest (name, room number, phone number) |
| `2` | Remove an existing guest by ID |
| `3` | Display the full list of registered guests |
| `0` | Exit the program |

All guest data is automatically saved to `guests.json` after every change — there's no separate "save" step required.

## 📂 Project Structure

```
Astrum-hotel-management/
├── Mehmonhona_astronum.py   # Main application logic
├── guests.json              # Auto-generated data file (ignored by Git)
├── .gitignore
├── LICENSE
└── README.md
```

> **Note:** `guests.json` is excluded from version control via `.gitignore`, since it contains local runtime data rather than source code.

## 🗂️ Data Format

Each guest is stored as a JSON object with the following structure:

```json
{
    "id": 1,
    "name": "Aziz",
    "room_number": 101,
    "phone": "+998901234567"
}
```

## 🔮 Planned Improvements

This project is a work in progress as I continue building my backend development skills. Upcoming improvements include:

- [ ] Stricter phone number validation (length and digit-only checks)
- [ ] Preventing empty or whitespace-only guest names
- [ ] Preventing negative or zero room numbers
- [ ] Checking for duplicate phone numbers across guests
- [ ] Migrating storage from JSON to a MySQL database
- [ ] Adding unit tests

## 👤 Author

**George**
Backend Development Student | Python & SQL
📍 Karshi, Uzbekistan
🔗 [GitHub](https://github.com/workgeorgeparker17-stack)

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.