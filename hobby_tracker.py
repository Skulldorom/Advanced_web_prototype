import json

def create_empty():
    data = {}
    data['intrest'] = []
    
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
class Intrest:
    def __init__(self,name,note):
        self.id = gen_int_id()
        self.name = name
        self.note = note

    def create_intrest(self,per):
        perlist = []
        for p in per:
            perlist.append(p.per_create())

        with open('data.txt') as json_file:
            data = json.load(json_file)
        data['intrest'].append({
            'id': self.id,
            'name': self.name,
            'note': self.note,
            'info': perlist,
            'array':week_array(perlist)
            })

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)

class per_week():
    def __init__(self,int_id,week_no,act,exp):   
        self.int_id = int_id
        self.week_no = week_no
        self.actual = act
        self.expected = exp
    
    def per_create(self):
        info = {
            'week_no':self.week_no,
            'actual':self.actual,
            'expected':self.expected
        }
        return info


def load_ints():
    with open('data.txt') as json_file:
        data = json.load(json_file)
    return data

def gen_int_id():
    with open('data.txt') as json_file:
        data = json.load(json_file)
    return len(data['intrest'])+1

def week_array(week_list):
    array = []
    for week in week_list:
        array.append([week['week_no']+1,week['actual'],week['expected']])
    return array
    
def test_data():
    First = Intrest("Art","My fav <3")
    weeks = []
    weeks.append(per_week(First.id,0,200,150))
    weeks.append(per_week(First.id,1,360,200))
    weeks.append(per_week(First.id,2,30,150))
    weeks.append(per_week(First.id,3,120,100))
    weeks.append(per_week(First.id,4,500,150))
    weeks.append(per_week(First.id,5,400,200))
    First.create_intrest(weeks)

    Second = Intrest("Piano Practice","Got have another talent right?")
    weeks = []
    weeks.append(per_week(First.id,0,5,200))
    weeks.append(per_week(First.id,1,50,200))
    weeks.append(per_week(First.id,2,60,100))
    weeks.append(per_week(First.id,3,120,100))
    weeks.append(per_week(First.id,4,100,150))
    weeks.append(per_week(First.id,5,50,150))
    Second.create_intrest(weeks)