import geopandas as gp
import json
from .mapmatching_mainmodule import loadTrack

def loadTrackFromTxt(trackTxt) -> gp.GeoDataFrame:
    myCarTrack = gp.read_file(trackTxt, driver = 'GeoJSON')
    tmp_list = []
    for x in range(0,myCarTrack.shape[0],4):
        tmp_list.append({
        'id': myCarTrack.loc[x,'id'],
        'time': myCarTrack.loc[x,'time'],
        'phenomenons': myCarTrack.loc[x,'phenomenons'],
        'geometry': myCarTrack.loc[x,'geometry']
        })
    subCarTrack = gp.GeoDataFrame(tmp_list)
    return subCarTrack

def run(inputJSON):
    #return loadTrackFromTxt(json.dumps(inputJSON))
    return loadTrack("63948bc3ad53a0015a08780f") #.to_json()