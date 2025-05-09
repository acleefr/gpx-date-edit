import xml.etree.ElementTree as ET
from datetime import datetime

def remove_namespace(doc, namespace):
    ns = u'{%s}' % namespace
    nsl = len(ns)
    for elem in doc.iter():
        if elem.tag.startswith(ns):
            elem.tag = elem.tag[nsl:]

def change_gpx_date(input_file, output_file, new_date_str):
    new_date = datetime.strptime(new_date_str, "%Y-%m-%d").date()

    tree = ET.parse(input_file)
    root = tree.getroot()

    # Enlève le namespace pour éviter les <ns0:trkpt> etc.
    remove_namespace(root, "http://www.topografix.com/GPX/1/1")

    for time_elem in root.findall('.//time'):
        original_time = datetime.fromisoformat(time_elem.text.replace('Z', '+00:00'))
        new_datetime = datetime.combine(new_date, original_time.time())
        time_elem.text = new_datetime.isoformat() + "Z"

    # Réécriture propre du fichier
    ET.register_namespace('', "http://www.topografix.com/GPX/1/1")  # Remet le namespace proprement en haut du fichier
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"✅ Nouveau fichier écrit : {output_file}")

# Exemple
change_gpx_date("bzh.gpx", "1804.gpx", "2025-04-18")
