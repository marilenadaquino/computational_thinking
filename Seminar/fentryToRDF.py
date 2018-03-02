from rdflib import Graph, Namespace, URIRef , Namespace , Literal
from rdflib.namespace import RDF, RDFS , OWL , DC
import csv

MYONTO = Namespace("http://example.org/myModelet/") # the URI of my modelet including classes, properties and individuals
MYDATA = Namespace("http://example.org/data/") # the URI of my data
DCTERMS = Namespace("http://purl.org/dc/terms/")
OAD = Namespace("http://lod.xdams.org/reload/oad/")
def getDataAccordingToMyModelet(photoClass, 
								objectTypeClass, 
								folderClass, 
								containerClass, 
								seriesClass, 
								repositoryClass, 
								photoToTypeProperty, 
								photoToIDProperty,
								objectToTitleProperty,
								objectToBroaderProperty
								):
	""" given a list of names of classes and properties 
	this function returns a RDF graph, serialized in n3
	the output graph is saved in myModeletFentry.rdf
	"""

	g = Graph() # create a graph to be filled with triples
	g.bind('myOnto', MYONTO) # bind the prefix of my modelet to the graph
	g.bind('myData', MYDATA)
	with open('fentry.csv') as csvfile: # open the csv file and assign variables to values
		reader = csv.DictReader(csvfile)
		for row in reader:
			photoID = row['photograph ID']
			photoType = row['Object']
			photoTitle = row['Photo title']
			folderHeading = row['Folder heading']
			containerHeading = row['Container heading']
			archiveSeries = row['Archive series']
			repository = row['Repository']
			# classes definition first
			g.add((URIRef(MYDATA+photoID), RDF.type, URIRef(MYONTO+photoClass) ))
			g.add((URIRef(MYDATA+'type/'+photoType), RDF.type, URIRef(MYONTO+objectTypeClass) ))
			g.add((URIRef(MYDATA+'folder'), RDF.type, URIRef(MYONTO+folderClass) ))
			g.add((URIRef(MYDATA+'container'), RDF.type, URIRef(MYONTO+containerClass) ))
			g.add((URIRef(MYDATA+'series'), RDF.type, URIRef(MYONTO+seriesClass) ))
			g.add((URIRef(MYDATA+'repository'), RDF.type, URIRef(MYONTO+repositoryClass) ))
			# hierarchical properties
			g.add((URIRef(MYDATA+photoID), URIRef(MYONTO+objectToBroaderProperty), URIRef(MYDATA+'folder') ))
			g.add((URIRef(MYDATA+'folder'), URIRef(MYONTO+objectToBroaderProperty), URIRef(MYDATA+'container') ))
			g.add((URIRef(MYDATA+'container'), URIRef(MYONTO+objectToBroaderProperty), URIRef(MYDATA+'series') ))
			g.add((URIRef(MYDATA+'series'), URIRef(MYONTO+objectToBroaderProperty), URIRef(MYDATA+'repository') ))
			# titles
			g.add((URIRef(MYDATA+photoID), URIRef(MYONTO+objectToTitleProperty), Literal(photoTitle) ))
			g.add((URIRef(MYDATA+'folder'), URIRef(MYONTO+objectToTitleProperty), Literal(folderHeading) ))
			g.add((URIRef(MYDATA+'container'), URIRef(MYONTO+objectToTitleProperty), Literal(containerHeading) ))
			g.add((URIRef(MYDATA+'series'), URIRef(MYONTO+objectToTitleProperty), Literal(archiveSeries) ))
			g.add((URIRef(MYDATA+'repository'), URIRef(MYONTO+objectToTitleProperty), Literal(repository) ))
			# id and type
			g.add((URIRef(MYDATA+photoID), URIRef(MYONTO+photoToTypeProperty), URIRef(MYDATA+'type/'+photoType) ))
			g.add((URIRef(MYDATA+photoID), URIRef(MYONTO+photoToIDProperty), Literal(photoID) ))

	return g.serialize(destination='myModeletFentry.rdf', format='n3');

# getDataAccordingToMyModelet(* add here classes and properties *)

def getDataAccordingToOtherOntologies(photoClass, 
								objectTypeClass, 
								folderClass, 
								containerClass, 
								seriesClass, 
								repositoryClass, 
								photoToTypeProperty, 
								photoToIDProperty,
								objectToTitleProperty,
								objectToBroaderProperty,
								objectToRepositoryProperty):
	""" given a list of existing classes and properties 
	this function returns a RDF graph, serialized in n3
	the output graph is saved in myModeletFentry.rdf
	"""

	g = Graph() # create a graph to be filled with triples
	g.bind('myOnto', MYONTO) # bind the prefix of my modelet to the graph
	g.bind('oad', OAD)
	g.bind('dcterms', DCTERMS)
	with open('fentry.csv') as csvfile: # open the csv file and assign variables to values
		reader = csv.DictReader(csvfile)
		for row in reader:
			photoID = row['photograph ID']
			photoType = row['Object']
			photoTitle = row['Photo title']
			folderHeading = row['Folder heading']
			containerHeading = row['Container heading']
			archiveSeries = row['Archive series']
			repository = row['Repository']
			# classes definition first
			g.add((URIRef(MYDATA+photoID), RDF.type, URIRef(photoClass) ))
			g.add((URIRef(MYDATA+'type/'+photoType), RDF.type, URIRef(objectTypeClass) ))
			g.add((URIRef(MYDATA+'folder'), RDF.type, URIRef(folderClass) ))
			g.add((URIRef(MYDATA+'container'), RDF.type, URIRef(containerClass) ))
			g.add((URIRef(MYDATA+'series'), RDF.type, URIRef(seriesClass) ))
			g.add((URIRef(MYDATA+'repository'), RDF.type, URIRef(repositoryClass) ))
			# hierarchical properties
			g.add((URIRef(MYDATA+photoID), URIRef(objectToBroaderProperty), URIRef(MYDATA+'folder') ))
			g.add((URIRef(MYDATA+'folder'), URIRef(objectToBroaderProperty), URIRef(MYDATA+'container') ))
			g.add((URIRef(MYDATA+'container'), URIRef(objectToBroaderProperty), URIRef(MYDATA+'series') ))
			g.add((URIRef(MYDATA+'series'), URIRef(objectToRepositoryProperty), URIRef(MYDATA+'repository') ))
			# titles
			g.add((URIRef(MYDATA+photoID), URIRef(objectToTitleProperty), Literal(photoTitle) ))
			g.add((URIRef(MYDATA+'folder'), URIRef(objectToTitleProperty), Literal(folderHeading) ))
			g.add((URIRef(MYDATA+'container'), URIRef(objectToTitleProperty), Literal(containerHeading) ))
			g.add((URIRef(MYDATA+'series'), URIRef(objectToTitleProperty), Literal(archiveSeries) ))
			g.add((URIRef(MYDATA+'repository'), URIRef(objectToTitleProperty), Literal(repository) ))
			# id and type
			g.add((URIRef(MYDATA+photoID), URIRef(photoToTypeProperty), URIRef(MYDATA+'type/'+photoType) ))
			g.add((URIRef(MYDATA+photoID), URIRef(photoToIDProperty), Literal(photoID) ))

	return g.serialize(destination='finalFentry.rdf', format='n3');

#getDataAccordingToOtherOntologies(*add uris here*)
