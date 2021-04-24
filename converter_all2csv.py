import jsonlines
import pandas as pd

def read_all_txt():
    business_info = []
    product_info = []
    seller_url = []

    with jsonlines.open('waist_extender_output.jsonl') as myfile:
        for line in myfile.iter():
            product_info.append(line)

    with jsonlines.open('business_info.jsonl') as myfile:
        for line in myfile.iter():
            business_info.append(line)

    with open('business_url.txt','r') as f:
        for line in f:
            seller_url.append(line)

    return product_info, business_info, seller_url

if __name__ == '__main__':
    (product_info, business_info, seller_url) = read_all_txt()

    df = pd.DataFrame()

    for n in range(len(seller_url)):
        if seller_url[n] != 'no data \n':
            df = df.append([[product_info[n]['name'], product_info[n]['images'], product_info[n]['short_description'], seller_url[n], business_info[n]['Business Name'], business_info[n]['Business Address']]])
    
    header = ['Product Name', 'Product Image', 'Product description', 'Seller url', 'Business Name', 'Business Address']
    
    df.columns = header

    df.to_csv('result.csv', index=False, encoding='UTF-8')
    