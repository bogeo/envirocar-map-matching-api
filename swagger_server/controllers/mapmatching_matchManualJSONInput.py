import geopandas as gp
import json
from shapely import Point
from .mapmatching_mainmodule import *

from swagger_server.models.track_map_matched import TrackMapMatched  # noqa: E501

def loadTrackFromTxt(trackTxt) -> gp.GeoDataFrame:
    myCarTrackDict = json.loads(trackTxt)
    myCarTrackDictFeatures = myCarTrackDict['features']
    tmp_list = []
    for x in range(0,len(myCarTrackDictFeatures),4):
        #print("")
        #print("feature(",x,") =", myCarTrackDictFeatures[x])
        #print("")
        tmp_list.append({
        'id': myCarTrackDictFeatures[x]['properties']['id'],
        'time': myCarTrackDictFeatures[x]['properties']['time'],
        'phenomenons': myCarTrackDictFeatures[x]['properties']['phenomenons'],
        'geometry': Point(myCarTrackDictFeatures[x]['geometry']['coordinates'])
        })
    subCarTrack = gp.GeoDataFrame(tmp_list)#,crs="EPSG:4326")
    return subCarTrack

def runmapmatchingMatchManualJSONInput(inputJSON):
    radius = 0.0002
    subCarTrack = loadTrackFromTxt(json.dumps(inputJSON))
    minMaxCoords = getBounds(subCarTrack)
    gdfStreets = getStreets(minMaxCoords, radius)
    buffergdf = getBuffer(subCarTrack, radius)
    intersectingStreets, buffergdf = getIntersectingStreets(gdfStreets, buffergdf)
    snappedPointsGdf = getSnappedPoints(intersectingStreets, subCarTrack)
    coordinatesSnappedPts = getCoordinatesOfSnappedPts(snappedPointsGdf)
    snappedPtsGraph = getGraphOfSnappedPts(snappedPointsGdf, buffergdf)
    routingGraph = createProbGraph(coordinatesSnappedPts, snappedPtsGraph)
    distanceGraph = createDistanceGraph(snappedPointsGdf, buffergdf, subCarTrack, routingGraph)
    dijkstraTable = dijkstra(distanceGraph)
    #driveWayPtsGDF = getDriveWayPts(dijkstraTable, coordinatesSnappedPts)
    driveWayGDF, driveWayLine, osmIds = getDriveWay(dijkstraTable, coordinatesSnappedPts)
    #prepare output in trackMapMatched-Format here and respond it as GeoJSON string
    trackMapMatched = TrackMapMatched.from_dict(driveWayGDF.to_json())
    # return as true dict (beautiful JSON web response)
    return json.loads(trackMapMatched)
