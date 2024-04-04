import bibtexparser
from pathlib import Path
from datetime import datetime
from bibtexparser.bwriter import BibTexWriter

# Function to extract a sortable date from a BibTeX entry
def get_entry_date(entry):
    year = entry.get('year', "0000")
    month = entry.get('month', "01")
    day = "01"  # Default day
    
    try:
        month = datetime.strptime(month, '%B').month
    except ValueError:
        pass
    month = f"{month:02}"
    
    return int(f"{year}{month}{day}")

# Function to sort and write the BibTeX entries
def sort_bibtex_file(input_file, output_file):
    with open(input_file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    
    # Custom sorting function using 'get_entry_date'
    bib_database.entries.sort(key=get_entry_date, reverse=True)

    # Configure the writer
    writer = BibTexWriter()
    writer.indent = '  '  # Two spaces indentation
    writer.order_entries_by = None  # Disable default sorting
    
    # Convert the database to a BibTeX-formatted string
    bibtex_str = bibtexparser.dumps(bib_database, writer)
    
    # Write the sorted database to a file
    with open(output_file, 'w') as bibtex_file:
        bibtex_file.write(bibtex_str)

# Example usage
input_file_path = Path("_bibliography/papers.bib")
output_file_path = Path("_bibliography/papers.bib")

sort_bibtex_file(input_file_path, output_file_path)
