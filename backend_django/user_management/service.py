import os
import requests

FLAGR_URL = os.getenv('FLAGR_URL', 'http://localhost') # in docker, it should http://flagr
API = f'{FLAGR_URL}:18000/api/v1'

def get_all_flags():
    url = f'{API}/flags'
    resp = requests.get(url).json()
    return {x['id']:x['description'] for x in resp if x['enabled']}

def get_variant(context: dict, flags_id: dict):
    url = f'{API}/evaluation/batch'
    data = {
        "entities": [
            {
            "entityContext": context
            }
        ],
        "flagIDs": list( flags_id.keys() )
    }
    return requests.post(url, json=data).json()

def filter_eligible(resp: dict, flags_id: dict, humanized=False):
    eligible = [ x for x in resp['evaluationResults'] if x.get('variantID')]
    if not humanized:
        return data
    else:
        humanize = []
        for data in eligible:
            humanize.append({
                'flagName': flags_id[data['flagID']],
                'flagID': data['flagID'],
                'segmentID': data['segmentID'],
                'variantAttachment': data['variantAttachment'],
                'variantID': data['variantID'],
                'variantKey': data['variantKey']
            })
        return humanize

def all_features(group: str):
    all_flags_id = get_all_flags()
    variants = get_variant({'city':group}, all_flags_id)
    return filter_eligible(variants, all_flags_id, humanized=True)

if __name__ == "__main__":
    print(all_features('surabaya'))