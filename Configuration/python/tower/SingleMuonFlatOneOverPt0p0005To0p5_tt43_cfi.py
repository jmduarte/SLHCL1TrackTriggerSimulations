import FWCore.ParameterSet.Config as cms

# reference: https://github.com/cms-sw/genproductions/blob/master/python/EightTeV/SingleMuMinusFlatPt0p2To100_cff.py
generator = cms.EDProducer("FlatRandomOneOverPtGunProducer",
    PGunParameters = cms.PSet(
        MaxOneOverPt = cms.double(0.5),
        MinOneOverPt = cms.double(0.0005),
        PartID = cms.vint32(13),
        MaxEta = cms.double(2.2),
        MaxPhi = cms.double(3.14159265359/2),
        MinEta = cms.double(4.4/3),
        MinPhi = cms.double(3.14159265359/4),
        #XFlatSpread = cms.double(1.5),  ## in mm
        #YFlatSpread = cms.double(1.5),  ## in mm
        #ZFlatSpread = cms.double(150.), ## in mm
        RandomCharge = cms.bool(True),
        ReallyFlat = cms.bool(True),
    ),
    Verbosity = cms.untracked.int32(0),
    psethack = cms.string('single muon+/- 1/pt 0.0005 to 0.5 tower 43'),
    AddAntiParticle = cms.bool(False),
    firstRun = cms.untracked.uint32(1)
)
