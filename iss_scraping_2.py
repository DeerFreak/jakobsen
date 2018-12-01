from time import strftime, localtime
import math as m
import requests

class API(object):
    def __init__(self):
        self.session = requests.Session()
        self.current_pos_me = {'longitude' : 48.0441118, 'latitude' : 11.5321397}

    def _get_data_from_api(self):
        response = self.session.get('http://api.open-notify.org/iss-now.json')
        response.raise_for_status()
        return response.json()


    def get_current_iss_location(self):
        data = self._get_data_from_api()
        iss_position = data['iss_position']
        return iss_position


    def globe_to_kath(self, globe, R):
        x = R * m.cos(m.radians(float(globe['longitude']))) * m.sin(m.radians(float(globe['latitude'])))
        y = R * m.sin(m.radians(float(globe['longitude']))) * m.sin(m.radians(float(globe['latitude'])))
        z = R * m.cos(m.radians(float((globe['latitude']))))
        return (x, y, z)


    def get_vec_me_iss(self, me_ill, iss_ill):
        R = 1
        iss_pos = self.globe_to_kath(iss_ill, R)
        me_pos = self.globe_to_kath(me_ill, R)
        return [x[0]-x[1] for x in zip(iss_pos, me_pos)]


    def get_deg_from_kart(self, kart):
        (x, y, z) = kart[:]
        return (m.degrees(m.atan(y / x)), m.degrees(m.acos(z / m.sqrt(x**2 + y**2 + z**2))))
        

    def get_data(self):        
        current_pos_iss = self.get_current_iss_location()
        kart = self.get_vec_me_iss(current_pos_iss, self.current_pos_me)
        return self.get_deg_from_kart(kart)