import glob

def capitalize(word):
  if "-" in word:
    words = word.split("-")
    capitalized_words = [capitalize(w) for w in words]
    return "-".join(capitalized_words)
  
  letters = list(word)
  letters[0] = letters[0].upper()
  return "".join(letters)

tex_files = glob.glob("**/*.tex", recursive=True)

exclusions = ["a", "an", "the", "in", "on", "at", "for", "to", "with", "and", "or", "but", "is", "are", "was", "were", "of", "by", "from", "as", "that", "which", "this", "it", "its", "they", "their", "them", "he", "she", "his", "her", "pnn", "pnns"]

for f in tex_files:
  with open(f, "r") as file:
    lines = file.read().split("\n")
    
  for i, line in enumerate(lines):
    if "\\caption[" in line:
      title = line.split("[")[1].split("]")[0]
    
      words = title.split()
      capitalized_words = [capitalize(word) if (word.lower() not in exclusions and word[0] not in ["\\", "$"]) else word for word in words]
      capitalized_title = " ".join(capitalized_words)
      lines[i] = line.replace(f"[{title}]", f"[{capitalized_title}]")
      
  with open(f, "w") as file:
    file.write("\n".join(lines))
