import sys

import pergamon


def cnfg_psys_s2nr_lsstwfdsfull_lsstwfds():

    '''
    Explore features of planetary systems (underlying physical features as well as those that can be measured by the 10-year LSST WFD survey) based on signal-to-noise calculation
    '''
    
    pergamon.init( \
                 typeanls='featpsys_s2nr_lsstwfds_lsstwfdsfullm180', \
                 )
        

def cnfg_psys_s2nr_tessffim_tessexm2():
    '''
    Explore features of planetary systems (underlying physical features as well as those that can be measured by 200-sec cadence TESS FFI data in the second extended mission) 
    based on signal-to-noise calculation
    '''
    
    pergamon.init( \
                 typeanls='featpsys_s2nr_tessffim_tessexm2m135', \
                 )
        

def cnfg_psys_s2nr_tess2min_tessnomi2min():
    '''
    Explore features of planetary systems (underlying physical features as well as those that can be measured by 2-min cadence TESS data in the nominal mission)
    based on signal-to-noise calculation
    '''
    
    pergamon.init( \
                 typeanls='featpsys_s2nr_tess2min_tessnomi2min', \
                 )
        

def cnfg_cosc_s2nr_lsst_wfds_lsstdeepfull_lsstdeep():

    '''
    Explore features of COSCs (underlying physical features as well as those that can be measured by the 10-year LSST WFD survey) based on signal-to-noise calculation
    '''
    
    pergamon.init( \
                 typeanls='featcosc_s2nr_lsstwfdsfull_lsstwfds', \
                 )
        

def cnfg_cosc_s2nr_tessffim_tessexm2():
    '''
    Explore features of COSCs (underlying physical features as well as those that can be measured by 2-min cadence TESS data in the nominal mission) based on signal-to-noise calculation
    '''
    
    pergamon.init( \
                 typeanls='featcosc_s2nr_tessffim_tessexm2m135', \
                 )
        

def cnfg_cosc_s2nr_tess2min_tessnomi2min():
    '''
    Explore features of COSCs (underlying physical features as well as those that can be measured by 2-min cadence TESS data in the nominal mission) based on signal-to-noise calculation
    '''
    
    pergamon.init( \
                 typeanls='featcosc_s2nr_tess2min_tessnomi2min', \
                 )
        

def cnfg_supntess():
    '''
    features of supernovae in the TESS FOV
    '''
    
    pergamon.init( \
                  typeanls='featsupntess'
                 )
    

def cnfg_toii():
    '''
    all features in the TOI Catalog with all subpopulations
    '''
    
    pergamon.init( \
                 typeanls='toii'
                 )
    

def cnfg_exar():
    '''
    all features in the NASA Exoplanet Archive with all subpopulations
    '''
    
    pergamon.init( \
                 typeanls='exar'
                 )
    

def cnfg_micc():
    '''
    Merger-induced cora collapse supernovae
    '''
    
    pergamon.init( \
                 typeanls='micc'
                 )
    

def cnfg_multorbt():
    '''
    Kepler dichotomy -- stats of multis
    '''
    
    pergamon.init( \
                 typeanls='toii'
                 )
    

def cnfg_qulpastrfilt_qulp():
    '''
    Population of QLP TCEs that pass Astronet triage and subpopulations of
        TOIs
        FaintStar TOIs PM
        FaintStar TOIs EM1
    '''
    
    pergamon.init( \
                 'qulpastrfilt', 'featqulp'
                 )
        

def cnfg_tceefstr():
    '''
    QLP TCE feature space for
        all TCEs 
        all TOIs
        FaintStar TOIs PM
        FaintStar TOIs EM1
    '''
    
    pergamon.init( \
                 typeanls='tceefstr'
                 )
        

def cnfg_toiiatmo():
    '''
    TOI TSMs binned in equatorial latitude
    '''
    
    pergamon.init( \
                 typeanls='toiiatmo'
                 )
        

def cnfg_obsvjwstexop():
    '''
    features of approved JWST exoplanet programs and their modes
    '''
    
    pergamon.init( \
                 typeanls='featobsvjwstexop'
                 )
        

def cnfg_toiifstr():
    '''
    TOI feature space for
        all TOIs
        FaintStars TOIs (PM)
        FaintStars TOIs (EM1)
        FaintStars TOIs (EM1Ecl)
    '''
    
    pergamon.init( \
                 'toiifstr'
                 )
        

def cnfg_flarspot():
    
    # Figures for XRP
    # Fig 1: stellar type vs. magnitude
    # atmospheric escape rate
    # Fig 2: completeness and recall for flare
    # Spot model:

    pergamon.init( \
                 typeanls='flarmock20scnomi'
                 )
        

# exoplanet metallicity vs mass

globals().get(sys.argv[1])()
