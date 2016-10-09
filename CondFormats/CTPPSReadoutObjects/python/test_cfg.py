import FWCore.ParameterSet.Config as cms

process = cms.Process('test')

# minimum of logs
process.MessageLogger = cms.Service("MessageLogger",
    statistics = cms.untracked.vstring(),
    destinations = cms.untracked.vstring('cerr'),
    cerr = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING')
    )
)

# raw data source
process.source = cms.Source("EmptySource",
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# load a mapping
process.load("CondFormats.CTPPSReadoutObjects.TotemDAQMappingESSourceXML_cfi")
process.TotemDAQMappingESSourceXML.mappingFileNames.append("CondFormats/CTPPSReadoutObjects/xml/ctpps_210_mapping.xml")
#process.TotemDAQMappingESSourceXML.mappingFileNames.append("CondFormats/CTPPSReadoutObjects/xml/ctpps_timing_diamond_215_mapping_new.xml")
  
# print the mapping
process.printTotemDAQMapping = cms.EDAnalyzer("PrintTotemDAQMapping"
)

process.path = cms.Path(
  process.printTotemDAQMapping
)
