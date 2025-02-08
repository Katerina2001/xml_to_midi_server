# XML to MIDI Server

Αυτός ο server μετατρέπει αρχεία **MusicXML** σε **MIDI**, επιτρέποντας την αναγνώριση και αναπαραγωγή μουσικών σημειώσεων μέσω του **Audiveris**.

## Οδηγίες εγκατάστασης

### 1. Κλωνοποίηση του αποθετηρίου

git clone https://github.com/Katerina2001/xml_to_midi_server.git
cd xml_to_midi_server

### 2. Εγκατάσταση του **Audiveris**
Το Audiveris πρέπει να εγκατασταθεί χειροκίνητα.  
Κατεβάστε το από το **[επίσημο αποθετήριο στο GitHub](https://github.com/Audiveris/audiveris)** και ακολουθήστε τις οδηγίες εγκατάστασης.

Μετά την εγκατάσταση, βεβαιωθείτε ότι το **Audiveris.jar** βρίσκεται στη σωστή διαδρομή και ότι το **Java** είναι εγκατεστημένο.

### 3. Δημιουργία και ενεργοποίηση **virtual environment** (προαιρετικό)

python -m venv venv
source venv/bin/activate  # Για Linux/macOS
venv\Scripts\activate     # Για Windows

### 4. Εγκατάσταση εξαρτήσεων

pip install -r requirements.txt

## Τρόπος εκτέλεσης

python app.py

Ο server θα τρέξει στη διεύθυνση:  
🌍 **http://127.0.0.1:5000/**

## Απαιτούμενα Dependencies
Το αρχείο `requirements.txt` περιλαμβάνει:

Flask
Werkzeug
pydub
requests

Επιπλέον, θα χρειαστείτε:
- **Java (JDK 11 ή νεότερο)**
- **Audiveris 5.3+**

## Τεχνολογίες
- **Python**
- **Flask**
- **Audiveris**
- **MIDI Processing Libraries**

## API Endpoints

| Μέθοδος | Διαδρομή | Περιγραφή |
|----------|---------|------------|
| `POST` | `/convert` | Αποστολή XML και λήψη MIDI |
| `GET`  | `/status` | Έλεγχος αν ο server είναι ενεργός |

## Σημειώσεις
Αν υπάρχει πρόβλημα με το `Audiveris`, ελέγξτε το `audiveris_error.log`.

