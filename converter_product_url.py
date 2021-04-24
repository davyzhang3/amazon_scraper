import jsonlines

lines = []

with jsonlines.open('waist_extender_output.jsonl') as myfile:
    for line in myfile.iter():
        lines.append(line)

with open('business_url.txt','w') as f:
    for line in lines:
        if line['seller_url']:
            f.write('https://www.amazon.com/' + line['seller_url']+ '\n')
        else:
            f.write('no data \n')