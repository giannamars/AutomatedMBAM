import mbam 
import json

with open('examples/models/ES.json') as data_file:
    my_model = json.load(data_file)

path_to_data = 'examples/data/ES_zeros.h5'

model = mbam.engine.Engine(my_model, path_to_data)
model.run(printing=True)  # runs the geodesic

