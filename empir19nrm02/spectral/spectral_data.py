# -*- coding: utf-8 -*-

########################################################################
#
#########################################################################

"""
Module for loading light source (spd) and detector data (res) spectra databases
=============================================================================

 :_SPD_PATH: Path to light source spectra data (SPD's).

 :_RES_PATH: Path to with spectral responsivity data

 :_SPD_BB: Database with BlackBody Data.

 :_SPD_PTLED: Database with Phosphore type white LED Data mainly based on CIE S 025 Data.

 :_SPD_RGBLED: Database with RGB type white LED Data mainly based on CIE S 025 Data.

 :_SPD_PhotoLED: Database with white LEDs from the PhotoLED Project (https://data.dtu.dk/articles/dataset/EMPIR_15SIB07_PhotoLED_-_Database_of_LED_product_spectra/12783389)

 :_RES_VLDetector: Database with VL Detectors mainly based on CIE S 025 Data.

 :_RES_VLNoiseSimulation: Database with ideal VL Detectors with 0.01 noise on a single wavelength

 :_RES_VLShiftSimulation: Database with ideal VL Detecotrs shifted by 0.1nm each.

.. codeauthor:: UK
"""

from luxpy.utils import getdata
import os

#------------------------------------------------------------------------------
# os related utility parameters:
_PKG_PATH = os.path.dirname(__file__);""" Absolute path to package """
_PKG_PATH = _PKG_PATH[:_PKG_PATH.find("spectral")-1]
_SEP = os.sep; """ Operating system separator """

__all__ = ['_PKG_PATH','_SEP']

__all__ += ['_SPD_PATH', '_RES_PATH',
           '_SPD', '_RES',
           '_SPD_BB', '_SPD_PTLED', '_SPD_RGBLED', '_SPD_PHOTOLED', '_SPD_MONOLED', '_SPD_OSRAMLED',
           '_RES_VLDETECTORS', '_RES_VLNOISESIMULATION', '_RES_VLSHIFTSIMULATION']

_SPD_PATH = _PKG_PATH + _SEP + 'data' + _SEP + 'spd' + _SEP  # folder with spd data
_RES_PATH = _PKG_PATH + _SEP + 'data' + _SEP + 'res' + _SEP  # folder with res data

###############################################################################
# spectral power distributions:

# ------------------------------------------------------------------------------

# load BB spd data base:
_SPD_BB = {'S': {'data': getdata(_SPD_PATH + 'SPD_BB.csv', sep=';',kind='np').transpose()}}
#_SPD_BB['S']['info'] = getdata(_SPD_PATH + 'SPD_BBinfo.txt', kind='np', header='infer', verbosity=False)
_SPD_BB_S = _SPD_BB['S']

# load PTLED spd data base:
_SPD_PTLED = {'S': {'data': getdata(_SPD_PATH + 'SPD_PT_LED_White.csv', sep=';',kind='np').transpose()}}
_SPD_PTLED_S = _SPD_PTLED['S']

# load RGB LED spd data base:
_SPD_RGBLED = {'S': {'data': getdata(_SPD_PATH + 'SPD_RGB_LED_White.csv', sep=';',kind='np').transpose()}}
_SPD_RGBLED_S = _SPD_RGBLED['S']

# load RGB LEDs producing White ligth (original collection used in CIE S 025/E:2015; https://cie.co.at/publications/test-method-led-lamps-led-luminaires-and-led-modules ):
_SPD_CIES025_RGBLED = {'S': {'data': getdata(_SPD_PATH + 'CIES025_SPD_RGB_LED_White.csv', sep=';',kind='np').transpose()}}
_SPD_CIES025_RGBLED['S']['info'] = getdata(_SPD_PATH + 'CIES025_SPD_RGB_LED_White_Info.txt', kind='np', header='infer', verbosity=False)
_SPD_CIES025_RGBLED_S = _SPD_CIES025_RGBLED['S']

_SPD_CIES025_PTLED = {'S': {'data': getdata(_SPD_PATH + 'CIES025_SPD_PT_LED_White.csv', sep=';',kind='np').transpose()}}
_SPD_CIES025_PTLED['S']['info'] = getdata(_SPD_PATH + 'CIES025_SPD_PT_LED_White_Info.txt', kind='np', header='infer', verbosity=False)
_SPD_CIES025_PTLED_S = _SPD_CIES025_PTLED['S']

# load PhotoLED LED spd data base:
_SPD_PHOTOLED = {'S': {'data': getdata(_SPD_PATH + 'EMPIR_PhotoLED_SPECTRAL_DATABASE.csv', sep=';',kind='np').transpose()}}
_SPD_PHOTOLED_S = _SPD_PHOTOLED['S']

# load Mono LED spd data base:
_SPD_MONOLED = {'S': {'data': getdata(_SPD_PATH + 'SPD_LED_Mono.csv', sep=';',kind='np').transpose()}}
_SPD_MONOLED_S = _SPD_MONOLED['S']

# load Mono LED spd data base:
_SPD_OSRAMLED = {'S': {'data': ''}}
#_SPD_OSRAMLED = {'S': {'data': getdata(_SPD_PATH + 'SPD_OSRAM.csv', sep=';',kind='np').transpose()}}
#_SPD_OSRAMLED_S = _SPD_OSRAM['S']

# load VL Detectors (current collection):
_RES_VLDETECTORS = {'S': {'data': getdata(_RES_PATH + 'VL_Detectors.csv', sep=';',kind='np').transpose()}}
_RES_VLDETECTORS_S = _RES_VLDETECTORS['S']

# load VL Detectors (original collection used in CIE S 025/E:2015; https://cie.co.at/publications/test-method-led-lamps-led-luminaires-and-led-modules ):
_RES_CIES025_VLDETECTORS = {'S': {'data': getdata(_RES_PATH + 'CIES025_VL_Detectors.csv', sep=';',kind='np').transpose()}}
_RES_CIES025_VLDETECTORS['S']['info'] = getdata(_RES_PATH + 'CIES025_VL_Detectors_Info.txt', kind='np', header='infer', verbosity=False)
_RES_CIES025_VLDETECTORS_S = _RES_CIES025_VLDETECTORS['S']

# load VL Detectors with noise on single wavelegnth posiotions only:
_RES_VLNOISESIMULATION = {'S': {'data': getdata(_RES_PATH + 'VL_DetectorsVLPlusNoise.csv', sep=';',kind='np').transpose()}}
_RES_VLNOISESIMULATION_S = _RES_VLNOISESIMULATION['S']

# load VL Detectors shifted to each other:
_RES_VLSHIFTSIMULATION = {'S': {'data': getdata(_RES_PATH + 'VL_DetectorsVLShift.csv', sep=';',kind='np').transpose()}}
_RES_VLSHIFTSIMULATION_S = _RES_VLSHIFTSIMULATION['S']

# Initialize _SPD :
_SPD = {'BB': _SPD_BB,
        'PTLED': _SPD_PTLED,
        'CIES025_PTLED': _SPD_CIES025_PTLED,
        'RGBLED': _SPD_RGBLED,
        'CIES025_RGBLED': _SPD_CIES025_RGBLED,
        'PHOTOLED': _SPD_PHOTOLED,
        'MONOLED': _SPD_MONOLED,
        'OSRAMLED': None}

# Initialize _SPD :
_RES = {'VLDetectors': _RES_VLDETECTORS,
        'CIES025_VLDetectors': _RES_CIES025_VLDETECTORS,
        'VLSimNoise': _RES_VLNOISESIMULATION,
        'VLSimShift': _RES_VLSHIFTSIMULATION}
