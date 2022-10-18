import json

class JsonReader:
    
    @staticmethod
    def get_json(file):
        
        f = open(file) # Opening JSON file
        
        try:
            data = json.load(f) # JSON object as a dictionary
            
        except:
            raise Exception("Error trying to load JSON file")
        
        finally:
            f.close()  # Closing file
       
        return data