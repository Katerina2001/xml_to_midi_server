# XML to MIDI Server

This server converts **MusicXML** files to **MIDI**, enabling recognition and playback of musical notes using **Audiveris**.

## Installation Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/Katerina2001/xml_to_midi_server.git
cd xml_to_midi_server
```

### 2. Install **Audiveris**
Audiveris must be installed manually.  
Download it from the **[official GitHub repository](https://github.com/Audiveris/audiveris)** and follow the installation instructions.

After installation, ensure that **Audiveris.jar** is in the correct path and that **Java** is installed.

### 3. Create and Activate a **Virtual Environment** (Optional)
```sh
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 4. Install Dependencies
```sh
pip install -r requirements.txt
```

## Running the Server
```sh
python app.py
```
The server will run at:  
🌍 **http://127.0.0.1:5000/**

## Required Dependencies
The `requirements.txt` file includes:
```
Flask
Werkzeug
pydub
requests
```
Additionally, you will need:
- **Java (JDK 11 or later)**
- **Audiveris 5.3+**

## Technologies Used
- **Python**
- **Flask**
- **Audiveris**
- **MIDI Processing Libraries**

## API Endpoints

| Method | Endpoint | Description |
|----------|---------|------------|
| `POST` | `/convert` | Send XML and receive MIDI |
| `GET`  | `/status` | Check if the server is running |

## Notes
If you encounter issues with `Audiveris`, check `audiveris_error.log`.

