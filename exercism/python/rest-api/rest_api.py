import json

class RestAPI:
    def __init__(self, database = {"users": []}):
        self.data = database
        
    def get(self, url, payload = None):
        if(url == "/users"):
            if(payload == None):
                return json.dumps(self.data)
            else: 
                tmp = {"users": []}
                names = json.loads(payload)["users"]
                for e in self.data["users"]:
                    if(e["name"] in names): 
                        tmp["users"].append(e)
                return json.dumps(tmp)

    def post(self, url, payload = None):
        if(url == "/add"):
            name = json.loads(payload)["user"]
            d = {"name": name, "owes": {}, "owed_by": {}, "balance": 0.0}
            self.data["users"].append(d)
            return json.dumps(d)

        if(url == "/iou"):
            res = {"users": []}
            d = json.loads(payload)
            lender = json.loads(payload)["lender"]
            borrower = json.loads(payload)["borrower"]
            amount = json.loads(payload)["amount"]

            for e in self.data["users"]:
                if(e["name"] == lender): 
                    if(borrower in e["owes"] and e["owes"][borrower] > amount):
                        e["owes"][borrower] = e["owes"][borrower] - amount
                    elif(borrower in e["owes"] and e["owes"][borrower] == amount):
                        del e["owes"][borrower]
                    elif(borrower in e["owes"] and e["owes"][borrower] < amount):
                        e["owed_by"][borrower] = amount - e["owes"][borrower]
                        del e["owes"][borrower]
                    elif(borrower in e["owed_by"]):
                        e["owed_by"][borrower] = e["owed_by"][borrower] + amount
                    else: 
                        e["owed_by"][borrower] = amount
                        
                    e["balance"] = e["balance"] + amount
                    res["users"].append(e)

                if(e["name"] == borrower):                   
                    if(lender in e["owed_by"] and e["owed_by"][lender] > amount):
                        e["owed_by"][lender] = e["owed_by"][lender] - amount
                    elif(lender in e["owed_by"] and e["owed_by"][lender] == amount):
                        del e["owed_by"][lender]
                    elif(lender in e["owed_by"] and e["owed_by"][lender] < amount):
                        e["owes"][lender] = amount - e["owed_by"][lender]
                        del e["owed_by"][lender]
                    elif(lender in e["owes"]):
                        e["owes"][lender] = e["owes"][lender] + amount
                    else : 
                        e["owes"][lender] = amount

                    e["balance"] = e["balance"] - amount
                    res["users"].append(e)

            return json.dumps(res)