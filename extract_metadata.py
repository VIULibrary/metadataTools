import xml.etree.ElementTree as ET

def extract_metadata(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    titles = root.findall('.//mods:title', namespaces={'mods': 'http://www.loc.gov/mods/v3'})
    subjects = root.findall('.//mods:subject/mods:topic', namespaces={'mods': 'http://www.loc.gov/mods/v3'})
    genres = root.findall('.//mods:genre', namespaces={'mods': 'http://www.loc.gov/mods/v3'})

    unique_subjects = set(subject.text for subject in subjects if subject.text)
    unique_genres = set(genre.text for genre in genres if genre.text)

    with open(output_file, 'w') as f:
        f.write('###TITLE###\n')
        for title in titles:
            if title.text:
                f.write(title.text + '\n')
        
        f.write('\n###SUBJECT###\n')
        for subject in unique_subjects:
            f.write(subject + '\n')
        
        f.write('\n###GENRE###\n')
        for genre in unique_genres:
            f.write(genre + '\n')

if __name__ == "__main__":
    input_file = 'VIUOnlyCount2.xml'
    output_file = 'outputfile.txt'
    extract_metadata(input_file, output_file)
