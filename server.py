from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import math

app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def start():
    return "<h1>Flask is running </h1>"
   
@app.route('/api/results', methods=["POST"])
def results():
    req_data = request.get_json()
    pi = math.pi   
    # Internal Diameter  (using continuity  equation)
    # L = straightLength = 100
    # Q = flowRate = 300
    # v = velocity = 2.5
    # p = density = 1000
    # u= viscosity =0.001
    # E = roughness = 0.4
    L = straightLength = float(req_data["straightLength"])
    Q = flowRate = float(req_data["flowRate"])
    v = velocity = float(req_data["velocity"]) 
    p = density = float(req_data["density"])
    u= viscosity = float(req_data["viscosity"])
    E = roughness = float(req_data["roughness"])
    docText = req_data['docText']
    Q = Q/3600
    D = internal_diameter = math.sqrt((4*Q)/(v*pi))
    internal_diameter = internal_diameter * 1000
    internal_diameter = 203.2
    schedule40 = []
    A = area = ((pi) * ((internal_diameter/ 2000) ** 2))  * 100
    new_v = Q * A
    area = new_v
    print(new_v, "kkk")
    Re = reynolds_number = ((D * new_v * p) / u) * 10
    f = friction_factor = 0.024
    g = 9.81
    Dp = pressure_drop = f * (L/(10 * internal_diameter)) * (p/g) * ((new_v**2)/2) * 100
   
    #FlowType
    flowType = ""
    if Re < 2000:
        flowType = "LAMINAR"
    if Re > 4000:
        flowType = "TURBULENT"

    if 2000 < Re < 4000:
        flowType = "TRANSIENT"

    #Relative Roughness
    relative_roughness = E / D

    return {
        "internal_diameter": str(round(internal_diameter, 4)),
        "area": str(round(area,4)),
        "reynolds_number": str(round(reynolds_number,4)),
        "flow_type": str(flowType),
        "relative_roughness":str(round(relative_roughness, 4)),
        "pressure_drop": str(round(pressure_drop, 4)),
        "friction_factor": str(round(friction_factor, 4)),
        "docText": docText
        
    }

    
    # return {'ok' :  '200'}        
   

if __name__ == '__main__':
    app.run(debug = True, port = 5000)









# dataDict = json.loads(data2)
# print(dataDict)
# print(data['schedule'])
 # print(request.data)
 
#  from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
# import math

# app = Flask(__name__)
# CORS(app)

# @app.route('/', methods=["GET"])
# def start():
#     return "<h1>Flask is running </h1>"
   
# @app.route('/api/results', methods=["POST"])
# def results():
#     req_data = request.get_json()
#     print(req_data)
#     print((req_data["flowRate"]))
#     # Internal Diameter  (using continuity  equation)
#     Q = flowRate = float(req_data["flowRate"])
#     p = density = float(req_data["density"])
#     u= viscosity = float(req_data["viscosity"])
#     V = pumpDischarge = float(req_data["pumpDischarge"])
#     E = roughness = float(req_data["roughness"])
#     docText = req_data['docText']
#     pi = math.pi

#     #Internal diameter
#     D = internal_diameter = math.sqrt((4 * Q) / (pi * V)) * 1000
#     #get next available diameter and then calculate new V but for now continue
#     # D = 0.2032
#     V = 2.571
#     A = area = ((pi) * ((D / 2) ** 2)) / 1000000
#     Re = reynolds_number = ((D * V * p) / u) /1000
   
#     #FlowType
#     flowType = ""
#     if Re < 2000:
#         flowType = "LAMINAR"
#     if Re > 4000:
#         flowType = "TURBULENT"

#     if 2000 < Re < 4000:
#         flowType = "TRANSIENT"

#     #Relative Roughness
#     relative_roughness = E / D

#     return {
#         "internal_diameter": str(internal_diameter),
#         "area": str(area),
#         "reynolds_number": str(reynolds_number),
#         "flow_type": flowType,
#         "relative_roughness": str(relative_roughness),
#         "docText": docText
        
#     }

    
#     # return {'ok' :  '200'}        
   

# if __name__ == '__main__':
#     app.run(debug = True, port = 5000)









# # dataDict = json.loads(data2)
# # print(dataDict)
# # print(data['schedule'])
#  # print(request.data)
 