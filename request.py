import requests 
from statistics import mean

url = "https://superheroapi.com/api/2619421814940190/search/"
names_list = ['Hulk', 'Captain America', 'Thanos']

def get_full_info(some_list):
    data = []
    for elem in some_list:
        resp = requests.get(url + elem)
        full_info = resp.json()
        if 'results' in full_info:
            stat_list = full_info['results']
            data.append(stat_list)
    return data

def get_intelligence(some_list):
    res = []
    tmp_list = []
    results = get_full_info(some_list)
    for el in results:
        if(len(el) > 1):
            for elem in el:
                info = elem['powerstats']
                intelligence = info['intelligence']
                tmp_list.append(int(intelligence))
                mind_level = mean(tmp_list)
            res.append(mind_level)
        elif(len(el) == 1):
            for e in el:
                info = e['powerstats']
                mind_level = info['intelligence']
                res.append(int(mind_level))
    return res


def show_results(input_data):
    mind_list = get_intelligence(input_data)
    res_dict = dict(zip(input_data,mind_list))
    max_lvl = max(res_dict.values())
    for k,v in res_dict.items():
        if v == max_lvl:
            print(k + " " + str(v))
            
               
if __name__ == '__main__':
    show_results(names_list)

