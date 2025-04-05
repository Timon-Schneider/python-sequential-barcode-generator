import argparse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from reportlab.lib.units import cm, mm

# Translations / Übersetzungen
translations = {
    "de": {
        "desc": "Erstelle eine PDF mit aufsteigenden oder absteigenden Barcodes.",
        "output_desc": "Ausgabedatei (PDF)",
        "width_desc": "Breite des PDFs in Zentimetern",
        "start_desc": "Startnummer für Barcodes",
        "end_desc": "Endnummer für Barcodes",
        "text_desc": "Text über den Barcodes",
        "zeros_desc": "Anzahl der führenden Nullen",
        "barwidth_desc": "Breite der Balken im Barcode (Standard: 1.2)",
        "prefix_desc": "Präfix vor der Nummer im Barcode (z.B. \"AB-\")",
        "suffix_desc": "Suffix nach der Nummer im Barcode (z.B. \"-XYZ\")",
        "descending_desc": "Barcodes in absteigender Reihenfolge generieren",
        "success_msg": "PDF mit {} Barcodes wurde erfolgreich erstellt: {}"
    },
    "en": {
        "desc": "Create a PDF with ascending or descending barcodes.",
        "output_desc": "Output file (PDF)",
        "width_desc": "Width of the PDF in centimeters",
        "start_desc": "Starting number for barcodes",
        "end_desc": "Ending number for barcodes",
        "text_desc": "Text above the barcodes",
        "zeros_desc": "Number of leading zeros",
        "barwidth_desc": "Width of the bars in the barcode (default: 1.2)",
        "prefix_desc": "Prefix before the number in the barcode (e.g. \"AB-\")",
        "suffix_desc": "Suffix after the number in the barcode (e.g. \"-XYZ\")",
        "descending_desc": "Generate barcodes in descending order",
        "success_msg": "PDF with {} barcodes has been successfully created: {}"
    }
}


def create_barcode_pdf(output_file, width_cm, start_number, end_number, text_above, leading_zeros=0,
                       bar_width=1.2, prefix="", suffix="", descending=False, language="en"):
    # EN: Page width in points (1 point = 1/72 inch)
    # DE: Seitenbreite in Punkten (1 Punkt = 1/72 Zoll)
    page_width = width_cm * cm

    # EN: Lower barcode height to save paper
    # DE: Niedrigere Barcode-Höhe um Papier zu sparen
    barcode_height = 0.5 * cm

    # EN: Spacing between barcodes
    # DE: Abstand zwischen Barcodes
    spacing = 0.4 * cm

    # EN: Text size
    # DE: Textgröße
    text_size = 8

    # EN: Page length is dynamically adjusted
    # DE: Seitenlänge wird dynamisch angepasst
    total_items = end_number - start_number + 1

    # EN: Compact spacing for text and number
    # DE: Kompakterer Abstand für Text und Nummer
    item_height = barcode_height + spacing + 4 * mm
    page_height = item_height * total_items

    # EN: Create PDF
    # DE: Erstelle PDF
    c = canvas.Canvas(output_file, pagesize=(page_width, page_height))

    # EN: Current Y position (from bottom to top)
    # DE: Aktuelle Y-Position (von unten nach oben)
    y_position = spacing

    # EN: Determine order of numbers
    # DE: Bestimme Reihenfolge der Nummern
    if descending:
        number_range = range(end_number, start_number - 1, -1)
    else:
        number_range = range(start_number, end_number + 1)

    # EN: Create barcodes with ascending or descending numbers
    # DE: Erstelle Barcodes mit aufsteigenden oder absteigenden Nummern
    for number in number_range:
        # EN: Format number with leading zeros
        # DE: Formatiere Nummer mit führenden Nullen
        num_value = str(number).zfill(leading_zeros)

        # EN: Combine prefix, number and suffix
        # DE: Kombiniere Präfix, Nummer und Suffix
        value = f"{prefix}{num_value}{suffix}"

        # EN: Generate barcode with adjusted height and configurable width
        # DE: Erzeuge Barcode mit angepasster Höhe und konfigurierbarer Breite
        barcode = code128.Code128(value, barHeight=barcode_height, barWidth=bar_width, humanReadable=False)

        # EN: Calculate the exact barcode width and center it
        # DE: Berechne die genaue Barcode-Breite und zentriere ihn
        barcode_width = barcode.width
        barcode_x = (page_width - barcode_width) / 2

        # EN: Draw description text above the barcode
        # DE: Zeichne Beschreibungstext über dem Barcode
        if text_above:
            c.setFont("Helvetica", text_size)
            c.drawString((page_width - c.stringWidth(text_above, "Helvetica", text_size)) / 2,
                         y_position + barcode_height + 1.0 * mm,
                         text_above)

        # EN: Draw barcode
        # DE: Zeichne Barcode
        barcode.drawOn(c, barcode_x, y_position)

        # EN: Draw number below the barcode
        # DE: Zeichne Nummer unter dem Barcode
        c.setFont("Helvetica", text_size)
        c.drawString((page_width - c.stringWidth(value, "Helvetica", text_size)) / 2,
                     y_position - 3 * mm,
                     value)

        # EN: Next position
        # DE: Nächste Position
        y_position += item_height

    # EN: Save PDF
    # DE: Speichere PDF
    c.save()

    # EN: Output success message in the chosen language
    # DE: Erfolgsmeldung in der gewählten Sprache ausgeben
    print(translations[language]["success_msg"].format(total_items, output_file))


if __name__ == "__main__":
    # EN: Use English by default
    # DE: Standardmäßig Englisch verwenden
    default_language = "en"
    t = translations[default_language]

    parser = argparse.ArgumentParser(description=t["desc"])
    parser.add_argument('--output', type=str, default='barcodes.pdf', help=t["output_desc"])
    parser.add_argument('--width', type=float, default=5.0, help=t["width_desc"])
    parser.add_argument('--start', type=int, default=1, help=t["start_desc"])
    parser.add_argument('--end', type=int, default=100, help=t["end_desc"])
    parser.add_argument('--text', type=str, default='', help=t["text_desc"])
    parser.add_argument('--zeros', type=int, default=0, help=t["zeros_desc"])
    parser.add_argument('--barwidth', type=float, default=1.2, help=t["barwidth_desc"])
    parser.add_argument('--prefix', type=str, default='', help=t["prefix_desc"])
    parser.add_argument('--suffix', type=str, default='', help=t["suffix_desc"])
    parser.add_argument('--descending', action='store_true', help=t["descending_desc"])
    parser.add_argument('--lang', type=str, choices=['de', 'en'], default=default_language,
                        help="Sprache/Language (de/en)")

    args = parser.parse_args()

    # EN: Use language from arguments
    # DE: Sprache aus Argumenten verwenden
    language = args.lang

    create_barcode_pdf(args.output, args.width, args.start, args.end, args.text,
                       args.zeros, args.barwidth, args.prefix, args.suffix,
                       args.descending, language)
