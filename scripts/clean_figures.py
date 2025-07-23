import os
import glob

def find_unused_figures(figures_dir, chapters_dir, appendices_dir):
  # Collect all figure file names
  figure_files = set(glob.glob(os.path.join(figures_dir, '**', '*.pdf*'), recursive=True))
  tex_files = set(glob.glob(os.path.join(chapters_dir, '**', '*.tex'), recursive=True))
  tex_files = tex_files | set(glob.glob(os.path.join(appendices_dir, '**', '*.tex'), recursive=True))

  # Search for figure references in .tex files
  used_figures = set()
  for tex_file in tex_files:
    with open(tex_file, 'r') as f:
      content = f.read()
      for figure in figure_files:
        if figure in content:
          used_figures.add(figure)

  # Identify unused figures
  unused_figures = figure_files - used_figures
  return used_figures, unused_figures

if __name__ == "__main__":
  figures_dir = "Figures"  # Adjust path as needed
  chapters_dir = "Chapters"  # Adjust path as needed
  appendices_dir = "Appendices"  # Adjust path as needed

  if not os.path.exists(figures_dir):
    print(f"Figures directory '{figures_dir}' does not exist.")
    exit(1)

  if not os.path.exists(chapters_dir):
    print(f"Chapters directory '{chapters_dir}' does not exist.")
    exit(1)

  used_figures, unused_figures = find_unused_figures(figures_dir, chapters_dir, appendices_dir)
  for unused_figure in unused_figures:
    if os.path.exists(unused_figure):
      os.remove(unused_figure)
      print("Removing unused figure:", unused_figure)
      
  # delete empty directories
  for dirpath, dirnames, filenames in os.walk(figures_dir, topdown=False):
    if not filenames and not dirnames:
      os.rmdir(dirpath)
      print("Removing empty directory:", dirpath)