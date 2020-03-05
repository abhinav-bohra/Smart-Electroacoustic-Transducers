from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
 
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
 
# Control volume
#volume.SetMasterVolumeLevel(-0.0, None) #max
#volume.SetMasterVolumeLevel(-5.0, None) #72%
volume.SetMasterVolumeLevel(-10.0, None) #51%