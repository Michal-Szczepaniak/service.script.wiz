import xbmc
import socket

class XBMCPlayer( xbmc.Player ):

    def __init__(self, *args):
        xbmc.Player.__init__(self)
        xbmc.log('Kodi WiZ __init__')

    def onAVStarted(self):
        xbmc.log('Kodi WiZ onAVStarted')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes("{\"method\":\"setPilot\",\"params\":{\"state\":false}}", "utf-8"), ("ip", 38899))

    def onPlayBackStarted( self ):
        xbmc.log('Kodi WiZ playbackStarted')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes("{\"method\":\"setPilot\",\"params\":{\"state\":false}}", "utf-8"), ("ip", 38899))

    def onPlayBackEnded( self ):
        xbmc.log('Kodi WiZ playbackEnded')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes("{\"method\":\"setPilot\",\"params\":{\"state\":true,\"dimming\":10}}", "utf-8"), ("ip", 38899))

    def onPlayBackStopped( self ):
        xbmc.log('Kodi WiZ playbackStopped')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes("{\"method\":\"setPilot\",\"params\":{\"state\":true,\"dimming\":10}}", "utf-8"), ("ip", 38899))

    def onPlayBackPaused(self):
        xbmc.log('Kodi WiZ playbackPaused')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes("{\"method\":\"setPilot\",\"params\":{\"state\":true,\"dimming\":10}}", "utf-8"), ("ip", 38899))

    def onPlayBackResumed(self):
        xbmc.log('Kodi WiZ playbackResumed')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes("{\"method\":\"setPilot\",\"params\":{\"state\":false}}", "utf-8"), ("ip", 38899))

player = XBMCPlayer()
monitor = xbmc.Monitor()

monitor.waitForAbort()

del player
