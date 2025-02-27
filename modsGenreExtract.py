import xml.etree.ElementTree as ET

def extract_genre_tags(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()
    
    genres = []
    for genre in root.findall('.//{http://www.loc.gov/mods/v3}genre'):
        if genre.text is not None:
            genres.append(genre.text)
    
    with open(output_file, 'w') as f:
        for genre in genres:
            f.write(genre + '\n')

if __name__ == "__main__":
    input_file = 'VIUonlyCount2.xml'
    output_file = 'dump.txt'
    extract_genre_tags(input_file, output_file)
