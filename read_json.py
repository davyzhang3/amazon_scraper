import jsonlines

lines = []

with jsonlines.open('search_results_output.jsonl') as myfile:
    for line in myfile.iter():
        lines.append(line)

print(lines[0])