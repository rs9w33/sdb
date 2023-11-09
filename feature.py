import geemap, ee
from eepackages.applications import bathymetry

region = 'braamspunt'
df = pd.read_csv(r"guianas-bbox.csv")
bb = df[df.name == region]

xx, XX = bb.minx.values[0],bb.maxx.values[0]
yy, YY = bb.miny.values[0],bb.maxy.values[0]
bounds = ee.Geometry.Rectangle([
    xx, yy, XX, YY])

import geemap
Map = geemap.Map(center=((yy+YY)/2, (xx+XX)/2), zoom=10);
Map.addLayer(bounds); Map

sdb = bathymetry.Bathymetry()

start = '2016-01-01'
stop = '2023-07-01'

i = ee.Date(start)

while i.format('YYYY-MM-dd').getInfo() != te:
    istr = (i.format('YYYY-MM-dd').getInfo())
    print(istr)

    img = sdb.compute_intertidal_depth(
        bounds=bounds,
        start=istr,
        stop=i.advance(6, 'month').format('YYYY-MM-dd').getInfo(),
        scale=10,
        missions=['S2', 'L8', 'L9'],
        filter_masked = True,
        filter_masked_fraction=0.6,
        skip_scene_boundary_fix=False,
        skip_neighborhood_search=False,
        bounds_buffer=0
    )

    mndwi = img.select('mndwi').getDownloadURL({
        'scale': 10,
        'region': bounds, 
        'filePerBand': False,
        'format': 'GEO_TIFF'
        })

    r = request.urlretrieve(
        mndwi, 
        os.path.join(
        r'D:\bathydem\wwf-turtles-guianas\data\sdb-intertidal', # change to location you want to export the images to
        f'{region}-sdb-intertidal-{istr}-mndwi.tiff')
    )

    ndwi = img.select('ndwi').getDownloadURL({
        'scale': 10,
        'region': bounds, 
        'filePerBand': False,
        'format': 'GEO_TIFF'
        })

    r = request.urlretrieve(
        ndwi, 
        os.path.join(
        r'D:\bathydem\wwf-turtles-guianas\data\sdb-intertidal', # change to location you want to export the images to
        f'{region}-sdb-intertidal-{istr}-ndwi.tiff')
    )
    i = i.advance(3, 'month')

