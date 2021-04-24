import jsonlines

lines = []

with jsonlines.open('revised_search_results_output.jsonl') as myfile:
    for line in myfile.iter():
        lines.append(line)

with open('waist_extender_url.txt','w') as f:
    for line in lines:
        f.write('https://www.amazon.com/' + line['url'] + '\n')