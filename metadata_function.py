import json

def get_metadata(data):

    try:
        name = data["metadata"]["name"]
        country = data["metadata"]["country"]
        type = data["metadata"]["company_type"]
        description = data["metadata"]["description"]
        sector = data["metadata"]["sector"]
        industry = data["metadata"]["industry"]
        subindustry = data["metadata"]["subindustry"]
    except:
        name = "NA"
        country = "NA"
        type = "NA"
        description = "NA"
        sector = "NA"
        industry = "NA"
        subindustry = "NA"

    return name, country, type, subindustry, sector, industry, description

if __name__ == "__main__":

    # read in test data
    with open("output.json") as f:
        data = json.load(f)

    #review financials
    get_metadata(data)