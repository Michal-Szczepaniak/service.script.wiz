import xbmc
import requests

class XBMCPlayer( xbmc.Player ):

    def __init__(self, *args):
        xbmc.Player.__init__(self)
        xbmc.log('Kodi WiZ __init__')

    def onAVStarted(self):
        xbmc.log('Kodi WiZ onAVStarted')
        requests.post('http://proxy.serv:43201/properties', json={'property': 'playback', 'property_id': 'htpc', 'key': 'state', 'type': 'string', 'value': 'playing'})

    def onPlayBackStarted( self ):
        xbmc.log('Kodi WiZ playbackStarted')
        requests.post('http://proxy.serv:43201/properties', json={'property': 'playback', 'property_id': 'htpc', 'key': 'state', 'type': 'string', 'value': 'playing'})

    def onPlayBackEnded( self ):
        xbmc.log('Kodi WiZ playbackEnded')
        requests.post('http://proxy.serv:43201/properties', json={'property': 'playback', 'property_id': 'htpc', 'key': 'state', 'type': 'string', 'value': 'playing'})

    def onPlayBackStopped( self ):
        xbmc.log('Kodi WiZ playbackStopped')
        requests.post('http://proxy.serv:43201/properties', json={'property': 'playback', 'property_id': 'htpc', 'key': 'state', 'type': 'string', 'value': 'stopped'})

    def onPlayBackPaused(self):
        xbmc.log('Kodi WiZ playbackPaused')
        requests.post('http://proxy.serv:43201/properties', json={'property': 'playback', 'property_id': 'htpc', 'key': 'state', 'type': 'string', 'value': 'paused'})

    def onPlayBackResumed(self):
        xbmc.log('Kodi WiZ playbackResumed')
        requests.post('http://proxy.serv:43201/properties', json={'property': 'playback', 'property_id': 'htpc', 'key': 'state', 'type': 'string', 'value': 'playing'})

player = XBMCPlayer()
monitor = xbmc.Monitor()

monitor.waitForAbort()

del player
