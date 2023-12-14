import click
import gutenbergpy.textget


@click.command()
@click.argument('book')
@click.argument('outfile', required=False)
def getbook(book, outfile):
  """
    Download a book from project Gutenberg and save it 
    to the specified outfile
    """

  print(f"Downloading Project Gutenberg ID {book}")
  raw_book = gutenbergpy.textget.get_text_by_id(book)
  clean_book = gutenbergpy.textget.strip_headers(raw_book)
  if not outfile:
    outfile = f'{book}.txt'
  print(f"Saving book as {outfile}")
  with open(outfile, 'wb') as file:
    file.write(clean_book)
    file.close()


if __name__ == "__main__":
  getbook()
