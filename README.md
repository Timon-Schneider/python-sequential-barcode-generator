# Python Sequential Barcode Generator

[🇬🇧 English](#english) | [🇩🇪 Deutsch](#deutsch)

<a name="english"></a>
## 🇬🇧 English

### Overview
This Python tool allows you to create custom PDF documents containing Code 128 barcodes with sequential numbers. It's designed for inventory management, event ticketing, asset labeling, and similar tasks requiring sequential barcode generation.

### Features
- Generate ascending or descending sequential barcodes
- Customize barcode width and spacing
- Add text above barcodes
- Configure leading zeros for consistent barcode length
- Add custom prefixes and suffixes to barcodes (e.g., "INV-001-2025")
- Bilingual interface (English and German)
- Full command-line interface for easy integration

### Requirements
- Python 3.6 or higher
- ReportLab library (`pip install reportlab`)

### Installation
1. Clone this repository:
   ```
   git clone https://github.com/username/barcode-generator.git
   cd barcode-generator
   ```

2. Install the required dependencies:
   ```
   pip install reportlab
   ```

### Usage
Run the script with Python:

```
python barcode_generator.py [options]
```

#### Basic Example
Generate 100 barcodes with default settings:
```
python barcode_generator.py
```

#### Command-line Options
| Option | Description | Default |
|--------|-------------|---------|
| `--output` | Output PDF filename | `barcodes.pdf` |
| `--width` | Width of the PDF in centimeters | 5.0 |
| `--start` | Starting number for barcodes | 1 |
| `--end` | Ending number for barcodes | 100 |
| `--text` | Text to display above each barcode | (none) |
| `--zeros` | Number of leading zeros | 0 |
| `--barwidth` | Width of the bars in the barcode | 1.2 |
| `--prefix` | Prefix before the number (e.g., "AB-") | (none) |
| `--suffix` | Suffix after the number (e.g., "-XYZ") | (none) |
| `--descending` | Generate barcodes in descending order | (not enabled) |
| `--lang` | Language (de/en) | en |

#### Examples

1. Generate 50 barcodes with "Inventory" as text and 4 leading zeros:
   ```
   python barcode_generator.py --start 1 --end 50 --text "Inventory" --zeros 4
   ```

2. Generate inventory barcodes with prefix and suffix:
   ```
   python barcode_generator.py --prefix "INV-" --suffix "-2025" --zeros 3
   ```

3. Generate barcodes in descending order:
   ```
   python barcode_generator.py --start 100 --end 200 --descending
   ```

4. Use German language:
   ```
   python barcode_generator.py --lang de
   ```

5. Custom output file with specific dimensions:
   ```
   python barcode_generator.py --output "warehouse_labels.pdf" --width 4.5
   ```

### Result
The script will generate a PDF file containing the requested barcodes, with each barcode showing the specified number (and optional prefix/suffix) below it and any descriptive text above it.

---

<a name="deutsch"></a>
## 🇩🇪 Deutsch

### Übersicht
Dieses Python-Tool ermöglicht die Erstellung von PDF-Dokumenten mit fortlaufenden Code-128-Barcodes. Es wurde für Bestandsverwaltung, Veranstaltungstickets, Inventarkennzeichnung und ähnliche Aufgaben entwickelt, die sequentielle Barcodes erfordern.

### Funktionen
- Generierung von auf- oder absteigenden sequentiellen Barcodes
- Anpassbare Barcode-Breite und -Abstände
- Text über den Barcodes hinzufügen
- Führende Nullen für einheitliche Barcode-Länge konfigurierbar
- Benutzerdefinierte Präfixe und Suffixe für Barcodes (z.B. "INV-001-2025")
- Zweisprachige Benutzeroberfläche (Deutsch und Englisch)
- Vollständige Befehlszeilenschnittstelle für einfache Integration

### Voraussetzungen
- Python 3.6 oder höher
- ReportLab-Bibliothek (`pip install reportlab`)

### Installation
1. Klone dieses Repository:
   ```
   git clone https://github.com/username/barcode-generator.git
   cd barcode-generator
   ```

2. Installiere die erforderlichen Abhängigkeiten:
   ```
   pip install reportlab
   ```

### Verwendung
Führe das Skript mit Python aus:

```
python barcode_generator.py [optionen]
```

#### Einfaches Beispiel
Generiere 100 Barcodes mit Standardeinstellungen:
```
python barcode_generator.py
```

#### Befehlszeilenoptionen
| Option | Beschreibung | Standard |
|--------|--------------|----------|
| `--output` | Ausgabe-PDF-Dateiname | `barcodes.pdf` |
| `--width` | Breite des PDFs in Zentimetern | 5.0 |
| `--start` | Startnummer für Barcodes | 1 |
| `--end` | Endnummer für Barcodes | 100 |
| `--text` | Text, der über jedem Barcode angezeigt wird | (keiner) |
| `--zeros` | Anzahl der führenden Nullen | 0 |
| `--barwidth` | Breite der Balken im Barcode | 1.2 |
| `--prefix` | Präfix vor der Nummer (z.B. "AB-") | (keiner) |
| `--suffix` | Suffix nach der Nummer (z.B. "-XYZ") | (keiner) |
| `--descending` | Barcodes in absteigender Reihenfolge generieren | (nicht aktiviert) |
| `--lang` | Sprache (de/en) | en |

#### Beispiele

1. Generiere 50 Barcodes mit "Inventar" als Text und 4 führenden Nullen:
   ```
   python barcode_generator.py --start 1 --end 50 --text "Inventar" --zeros 4
   ```

2. Generiere Inventar-Barcodes mit Präfix und Suffix:
   ```
   python barcode_generator.py --prefix "INV-" --suffix "-2025" --zeros 3
   ```

3. Generiere Barcodes in absteigender Reihenfolge:
   ```
   python barcode_generator.py --start 100 --end 200 --descending
   ```

4. Verwende deutsche Sprache:
   ```
   python barcode_generator.py --lang de
   ```

5. Benutzerdefinierte Ausgabedatei mit bestimmten Abmessungen:
   ```
   python barcode_generator.py --output "lager_etiketten.pdf" --width 4.5
   ```

### Ergebnis
Das Skript generiert eine PDF-Datei mit den angeforderten Barcodes, wobei jeder Barcode die angegebene Nummer (und optionalen Präfix/Suffix) darunter und einen beschreibenden Text darüber anzeigt.

---

## License / Lizenz
AGPL-3.0 license

## Contribution / Mitwirkung
Contributions are welcome! Please feel free to submit a Pull Request.  
Beiträge sind willkommen! Bitte reiche gerne einen Pull Request ein.
