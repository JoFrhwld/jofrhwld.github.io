from pyzotero import zotero
from zotero2qmd.zotero2qmd import item2main, main2qmd, filter_pubs
from collections import Counter
import re
import yaml
from pathlib import Path
import click


def make_file_names(all_mains):
    first_aut = [x["author"][0]["name"]["family"] for x in all_mains]
    years = [x["date"].split("-")[0] for x in all_mains]
    keys = [x["params"]["key"] for x in all_mains]

    all_stem = [f"{aut}_{year}_{key}" for aut, year, key in zip(first_aut, years, keys)]

    all_stem = [re.sub(r"_$", "", x) for x in all_stem]
    return all_stem

@click.command()
@click.option(
    '--zotero_key',
    default = ".zotero"
)
def zotero_qmd(
    zotero_key
):
    if zotero_key == ".zotero":
        keypath = Path(".zotero")
        with keypath.open() as keyfile:
            zotero_key = keyfile.readline().strip()

    zot = zotero.Zotero(
        library_id='7642731', 
        library_type='user', 
        api_key=zotero_key
    ) 

    pubs = zot.publications()

    filtered_pubs = filter_pubs(pubs)
    all_mains = [item2main(x) for x in filtered_pubs]
    all_stems = make_file_names(all_mains)
    out_path = Path("research","papers")

    for stem, item in zip(all_stems, all_mains):
        out_file = out_path.joinpath(stem).with_suffix(".qmd")
        if not out_file.exists():
            with out_file.open(mode = "w"):
                qmd_string = "---\n"+yaml.dump(item)+"\n---"
                out_file.write_text(qmd_string)


if __name__ == "__main__":
    zotero_qmd()