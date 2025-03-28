import tests.u as u
import trelby.locationreport as locationreport
import trelby.scenereport as scenereport
import trelby.util as util

# tests location report (just that it runs without exceptions, for now)


def testBasic():
    sp = u.load()
    report = locationreport.LocationReport(scenereport.SceneReport(sp))
    data = report.generate()

    # try to catch cases where generate returns something other than a PDF
    # document
    assert len(data) > 200
    assert data[:8] == util.toLatin1("%PDF-1.5")
