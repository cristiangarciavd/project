import json

class JsonReader:
    
    @staticmethod
    def get_json(file):
        
        # Opening JSON file
        f = open(file)
        
        # JSON object as a dictionary
        data = json.load(f)
        
        # Closing file
        f.close()
       
        return data