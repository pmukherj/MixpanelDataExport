from mixpanel import Mixpanel

class MixpanelData(object):

    def __init__(self, apisecret):
         self.api = Mixpanel(api_secret=apisecret)

    def getSegmentationResult(self, event, from_date, to_date, onProp='',unit='', interval='', where='', limit='', req_type=''):

        request = {}
        request['event'] = event
        request['from_date'] = from_date
        request['to_date'] = to_date

        if (onProp):
            request['on'] = 'properties["' + onProp + '"]'

        if (unit):
            request['unit'] = unit
        elif (interval):
            request['interval'] = interval

        if (limit):
            request['limit'] = limit

        if (where):
            wherestring = ''
            wherestring = '(' + where[0][0] + ' in properties[' + where[0][1] +']) and (defined (properties[' + where[0][1] +']))'
            for dat in where[1:]:
                wherestring = wherestring +  ' and (' + dat[0] + ' in properties[' + dat[1] +']) and (defined (properties[' + dat[1] +']))'
            request['where'] = wherestring

        if (req_type):
            request['type'] = req_type

        data = self.api.request(['segmentation'], request)

        return data
